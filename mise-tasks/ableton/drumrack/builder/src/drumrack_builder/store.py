"""SQLite storage: curation decisions in one database, the disposable analysis cache in another."""

from __future__ import annotations

import json
import sqlite3
import threading
import time
from contextlib import contextmanager
from pathlib import Path

from . import compare

CURATION_SCHEMA = """
CREATE TABLE IF NOT EXISTS samples (
  id INTEGER PRIMARY KEY,
  path TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  folder TEXT NOT NULL,
  ext TEXT NOT NULL,
  size INTEGER NOT NULL DEFAULT 0,
  mtime REAL NOT NULL DEFAULT 0,
  in_folder INTEGER NOT NULL DEFAULT 0,
  in_rack INTEGER NOT NULL DEFAULT 0,
  missing INTEGER NOT NULL DEFAULT 0,
  excluded INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS rack_usage (
  sample_id INTEGER NOT NULL REFERENCES samples(id) ON DELETE CASCADE,
  rack_path TEXT NOT NULL,
  note INTEGER NOT NULL,
  PRIMARY KEY (sample_id, rack_path, note)
);
CREATE TABLE IF NOT EXISTS racks (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  base_path TEXT,
  created_at REAL NOT NULL,
  updated_at REAL NOT NULL,
  last_export TEXT
);
-- One row per pad the rack will have. keep=1 leaves the base rack's pad exactly as it was.
CREATE TABLE IF NOT EXISTS pads (
  rack_id INTEGER NOT NULL REFERENCES racks(id) ON DELETE CASCADE,
  note INTEGER NOT NULL CHECK (note BETWEEN 0 AND 127),
  name TEXT NOT NULL DEFAULT '',
  sample_id INTEGER REFERENCES samples(id),
  keep INTEGER NOT NULL DEFAULT 0,
  -- The base rack pad whose devices and mixer this pad starts from; NULL starts from the template.
  source_note INTEGER,
  base_label TEXT NOT NULL DEFAULT '',
  PRIMARY KEY (rack_id, note)
);
CREATE TABLE IF NOT EXISTS shortlists (
  id INTEGER PRIMARY KEY,
  rack_id INTEGER NOT NULL REFERENCES racks(id) ON DELETE CASCADE,
  note INTEGER NOT NULL,
  name TEXT NOT NULL,
  created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS shortlist_items (
  shortlist_id INTEGER NOT NULL REFERENCES shortlists(id) ON DELETE CASCADE,
  sample_id INTEGER NOT NULL REFERENCES samples(id),
  position INTEGER NOT NULL,
  PRIMARY KEY (shortlist_id, sample_id)
);
CREATE TABLE IF NOT EXISTS votes (
  id INTEGER PRIMARY KEY,
  shortlist_id INTEGER NOT NULL REFERENCES shortlists(id) ON DELETE CASCADE,
  winner_id INTEGER NOT NULL,
  loser_id INTEGER NOT NULL,
  created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS brackets (
  id INTEGER PRIMARY KEY,
  shortlist_id INTEGER NOT NULL REFERENCES shortlists(id) ON DELETE CASCADE,
  state TEXT NOT NULL,
  created_at REAL NOT NULL
);
"""

ANALYSIS_SCHEMA = """
CREATE TABLE IF NOT EXISTS analysis (
  path TEXT PRIMARY KEY,
  size INTEGER NOT NULL,
  mtime REAL NOT NULL,
  duration REAL, frames INTEGER, sample_rate INTEGER, channels INTEGER,
  peak_db REAL, rms_db REAL, lufs REAL,
  pitch_hz REAL, pitch_midi REAL, pitch_confidence REAL, centroid_hz REAL,
  error TEXT,
  analyzed_at REAL NOT NULL
);
"""

ANALYSIS_FIELDS = (
    "duration",
    "frames",
    "sample_rate",
    "channels",
    "peak_db",
    "rms_db",
    "lufs",
    "pitch_hz",
    "pitch_midi",
    "pitch_confidence",
    "centroid_hz",
)

SORTS = {
    "name": "s.name COLLATE NOCASE",
    "folder": "s.folder COLLATE NOCASE, s.name COLLATE NOCASE",
    "duration": "a.duration IS NULL, a.duration",
    "pitch": "a.pitch_midi IS NULL, a.pitch_midi",
    "loudness": "COALESCE(a.lufs, a.rms_db) IS NULL, COALESCE(a.lufs, a.rms_db) DESC",
    "brightness": "a.centroid_hz IS NULL, a.centroid_hz",
}


class StoreError(ValueError):
    pass


class Store:
    """One connection guarded by a lock; FastAPI runs sync endpoints on worker threads."""

    def __init__(self, curation: Path, analysis: Path):
        curation.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(curation, check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys = ON")
        self.db.execute("PRAGMA journal_mode = WAL")
        self.db.executescript(CURATION_SCHEMA)
        self.db.execute("ATTACH DATABASE ? AS cache", (str(analysis),))
        self.db.executescript(ANALYSIS_SCHEMA.replace("EXISTS analysis", "EXISTS cache.analysis"))
        self.lock = threading.RLock()

    @contextmanager
    def tx(self):
        with self.lock:
            try:
                yield self.db
                self.db.commit()
            except BaseException:
                self.db.rollback()
                raise

    def close(self) -> None:
        self.db.close()

    # ------------------------------------------------------------------ samples

    def upsert_sample(self, path: Path, *, in_folder: bool = False, in_rack: bool = False) -> int:
        exists = path.is_file()
        stat = path.stat() if exists else None
        with self.tx() as db:
            db.execute(
                """INSERT INTO samples (path, name, folder, ext, size, mtime, in_folder, in_rack, missing)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                   ON CONFLICT(path) DO UPDATE SET size = excluded.size, mtime = excluded.mtime,
                     missing = excluded.missing,
                     in_folder = MAX(samples.in_folder, excluded.in_folder),
                     in_rack = MAX(samples.in_rack, excluded.in_rack)""",
                (
                    str(path),
                    path.stem,
                    str(path.parent),
                    path.suffix.lower().lstrip("."),
                    stat.st_size if stat else 0,
                    stat.st_mtime if stat else 0,
                    int(in_folder),
                    int(in_rack),
                    int(not exists),
                ),
            )
            return db.execute("SELECT id FROM samples WHERE path = ?", (str(path),)).fetchone()["id"]

    def mark_folder_scan(self, seen: set[str], roots: list[Path]) -> int:
        """Samples under scanned roots that were not seen this time are marked missing."""
        missing = 0
        with self.tx() as db:
            for row in db.execute("SELECT id, path FROM samples WHERE in_folder = 1").fetchall():
                under = any(Path(row["path"]).is_relative_to(r) for r in roots)
                if under and row["path"] not in seen and not Path(row["path"]).is_file():
                    db.execute("UPDATE samples SET missing = 1 WHERE id = ?", (row["id"],))
                    missing += 1
        return missing

    def record_rack_usage(self, sample_id: int, rack_path: Path, note: int) -> None:
        with self.tx() as db:
            db.execute("INSERT OR IGNORE INTO rack_usage VALUES (?, ?, ?)", (sample_id, str(rack_path), note))

    def sample(self, sample_id: int) -> dict:
        row = self.db.execute(
            f"SELECT s.*, {', '.join('a.' + f for f in ANALYSIS_FIELDS)}, a.error AS analysis_error "
            "FROM samples s LEFT JOIN cache.analysis a ON a.path = s.path AND a.size = s.size "
            "AND a.mtime = s.mtime WHERE s.id = ?",
            (sample_id,),
        ).fetchone()
        if row is None:
            raise StoreError(f"no sample {sample_id}")
        return dict(row)

    def samples(
        self,
        *,
        query: str = "",
        folder: str = "",
        include_excluded: bool = False,
        only_excluded: bool = False,
        rack_path: str = "",
        sort: str = "name",
        limit: int = 500,
        offset: int = 0,
    ) -> tuple[int, list[dict]]:
        where, params = ["s.missing = 0"], []
        for word in query.split():
            where.append("(s.name LIKE ? ESCAPE '\\' OR s.folder LIKE ? ESCAPE '\\')")
            pattern = "%" + word.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_") + "%"
            params += [pattern, pattern]
        if folder:
            where.append("(s.folder = ? OR s.folder LIKE ?)")
            params += [folder, folder.rstrip("/") + "/%"]
        if only_excluded:
            where.append("s.excluded = 1")
        elif not include_excluded:
            where.append("s.excluded = 0")
        if rack_path:
            where.append("s.id IN (SELECT sample_id FROM rack_usage WHERE rack_path = ?)")
            params.append(rack_path)
        order = SORTS.get(sort)
        if order is None:
            raise StoreError(f"unknown sort {sort!r}")
        clause = " AND ".join(where)
        join = "LEFT JOIN cache.analysis a ON a.path = s.path AND a.size = s.size AND a.mtime = s.mtime"
        total = self.db.execute(f"SELECT COUNT(*) FROM samples s WHERE {clause}", params).fetchone()[0]
        rows = self.db.execute(
            f"SELECT s.*, {', '.join('a.' + f for f in ANALYSIS_FIELDS)}, a.error AS analysis_error "
            f"FROM samples s {join} WHERE {clause} ORDER BY {order}, s.id LIMIT ? OFFSET ?",
            [*params, limit, offset],
        ).fetchall()
        return total, [dict(r) for r in rows]

    def folders(self) -> list[dict]:
        rows = self.db.execute(
            "SELECT folder, COUNT(*) AS n FROM samples WHERE missing = 0 GROUP BY folder ORDER BY folder COLLATE NOCASE"
        ).fetchall()
        return [dict(r) for r in rows]

    def set_excluded(self, sample_id: int, excluded: bool) -> None:
        with self.tx() as db:
            if db.execute("UPDATE samples SET excluded = ? WHERE id = ?", (int(excluded), sample_id)).rowcount == 0:
                raise StoreError(f"no sample {sample_id}")

    # ------------------------------------------------------------------ analysis cache

    def unanalyzed(self, limit: int = 50) -> list[dict]:
        rows = self.db.execute(
            "SELECT s.id, s.path, s.size, s.mtime FROM samples s LEFT JOIN cache.analysis a "
            "ON a.path = s.path AND a.size = s.size AND a.mtime = s.mtime "
            "WHERE a.path IS NULL AND s.missing = 0 ORDER BY s.excluded, s.id LIMIT ?",
            (limit,),
        ).fetchall()
        return [dict(r) for r in rows]

    def save_analysis(self, path: str, size: int, mtime: float, result: dict | None, error: str | None) -> None:
        values = [None if result is None else result.get(f) for f in ANALYSIS_FIELDS]
        with self.tx() as db:
            db.execute(
                f"INSERT OR REPLACE INTO cache.analysis (path, size, mtime, {', '.join(ANALYSIS_FIELDS)}, error, "
                f"analyzed_at) VALUES (?, ?, ?, {', '.join('?' * len(ANALYSIS_FIELDS))}, ?, ?)",
                (path, size, mtime, *values, error, time.time()),
            )

    def counts(self) -> dict:
        row = self.db.execute(
            "SELECT COUNT(*) AS samples, SUM(s.excluded) AS excluded, "
            "SUM(CASE WHEN a.path IS NOT NULL THEN 1 ELSE 0 END) AS analyzed FROM samples s "
            "LEFT JOIN cache.analysis a ON a.path = s.path AND a.size = s.size AND a.mtime = s.mtime "
            "WHERE s.missing = 0"
        ).fetchone()
        return {k: row[k] or 0 for k in ("samples", "excluded", "analyzed")}

    # ------------------------------------------------------------------ racks

    def create_rack(self, name: str, base_path: str | None = None) -> int:
        name = name.strip()
        if not name:
            raise StoreError("a rack needs a name")
        now = time.time()
        with self.tx() as db:
            return db.execute(
                "INSERT INTO racks (name, base_path, created_at, updated_at) VALUES (?, ?, ?, ?)",
                (name, base_path, now, now),
            ).lastrowid

    def racks(self) -> list[dict]:
        rows = self.db.execute(
            "SELECT r.*, (SELECT COUNT(*) FROM pads p WHERE p.rack_id = r.id) AS pad_count "
            "FROM racks r ORDER BY r.updated_at DESC"
        ).fetchall()
        return [dict(r) for r in rows]

    def rack(self, rack_id: int) -> dict:
        row = self.db.execute("SELECT * FROM racks WHERE id = ?", (rack_id,)).fetchone()
        if row is None:
            raise StoreError(f"no rack {rack_id}")
        return dict(row)

    def update_rack(self, rack_id: int, **fields: object) -> None:
        allowed = {k: v for k, v in fields.items() if k in ("name", "last_export")}
        if "name" in allowed and not str(allowed["name"]).strip():
            raise StoreError("a rack needs a name")
        self.rack(rack_id)
        with self.tx() as db:
            for key, item in allowed.items():
                db.execute(f"UPDATE racks SET {key} = ? WHERE id = ?", (item, rack_id))
            db.execute("UPDATE racks SET updated_at = ? WHERE id = ?", (time.time(), rack_id))

    def delete_rack(self, rack_id: int) -> None:
        with self.tx() as db:
            db.execute("DELETE FROM racks WHERE id = ?", (rack_id,))

    def pads(self, rack_id: int) -> list[dict]:
        rows = self.db.execute(
            "SELECT p.*, s.name AS sample_name, s.path AS sample_path, s.missing AS sample_missing "
            "FROM pads p LEFT JOIN samples s ON s.id = p.sample_id WHERE p.rack_id = ? ORDER BY p.note",
            (rack_id,),
        ).fetchall()
        return [dict(r) for r in rows]

    def set_pad(
        self,
        rack_id: int,
        note: int,
        *,
        sample_id: int | None,
        name: str | None = None,
        keep: bool = False,
        source_note: int | None = None,
        base_label: str = "",
    ) -> None:
        """Assign a sample to a pad. A pad imported from the base rack keeps its source note."""
        if not 0 <= note <= 127:
            raise StoreError(f"pad note {note} is outside 0-127")
        self.rack(rack_id)
        if sample_id is not None:
            self.sample(sample_id)
        with self.tx() as db:
            current = db.execute(
                "SELECT name, source_note, base_label FROM pads WHERE rack_id = ? AND note = ?", (rack_id, note)
            ).fetchone()
            label = name if name is not None else (current["name"] if current else "")
            if current is not None and source_note is None:
                source_note, base_label = current["source_note"], current["base_label"]
            if keep and source_note is None:
                raise StoreError("only a pad from the base rack can keep its sample")
            db.execute(
                """INSERT INTO pads (rack_id, note, name, sample_id, keep, source_note, base_label)
                   VALUES (?, ?, ?, ?, ?, ?, ?)
                   ON CONFLICT(rack_id, note) DO UPDATE SET name = excluded.name, sample_id = excluded.sample_id,
                   keep = excluded.keep, source_note = excluded.source_note, base_label = excluded.base_label""",
                (rack_id, note, label, sample_id, int(keep), source_note, base_label),
            )
            db.execute("UPDATE racks SET updated_at = ? WHERE id = ?", (time.time(), rack_id))

    def rename_pad(self, rack_id: int, note: int, name: str) -> None:
        with self.tx() as db:
            if (
                db.execute(
                    "UPDATE pads SET name = ? WHERE rack_id = ? AND note = ?", (name.strip(), rack_id, note)
                ).rowcount
                == 0
            ):
                raise StoreError(f"rack {rack_id} has no pad {note}")

    def move_pad(self, rack_id: int, note: int, target: int) -> None:
        """Move a pad, swapping with whatever sits on the target note. Shortlists move with their pad."""
        if not 0 <= target <= 127:
            raise StoreError(f"pad note {target} is outside 0-127")
        with self.tx() as db:
            db.execute("UPDATE pads SET note = -1 WHERE rack_id = ? AND note = ?", (rack_id, target))
            db.execute("UPDATE pads SET note = ? WHERE rack_id = ? AND note = ?", (target, rack_id, note))
            db.execute("UPDATE pads SET note = ? WHERE rack_id = ? AND note = -1", (note, rack_id))
            db.execute("UPDATE shortlists SET note = -1 WHERE rack_id = ? AND note = ?", (rack_id, target))
            db.execute("UPDATE shortlists SET note = ? WHERE rack_id = ? AND note = ?", (target, rack_id, note))
            db.execute("UPDATE shortlists SET note = ? WHERE rack_id = ? AND note = -1", (note, rack_id))

    def remove_pad(self, rack_id: int, note: int) -> None:
        with self.tx() as db:
            db.execute("DELETE FROM pads WHERE rack_id = ? AND note = ?", (rack_id, note))

    # ------------------------------------------------------------------ shortlists

    def create_shortlist(self, rack_id: int, note: int, name: str) -> int:
        self.rack(rack_id)
        if not name.strip():
            raise StoreError("a shortlist needs a name")
        with self.tx() as db:
            return db.execute(
                "INSERT INTO shortlists (rack_id, note, name, created_at) VALUES (?, ?, ?, ?)",
                (rack_id, note, name.strip(), time.time()),
            ).lastrowid

    def shortlist(self, shortlist_id: int) -> dict:
        row = self.db.execute("SELECT * FROM shortlists WHERE id = ?", (shortlist_id,)).fetchone()
        if row is None:
            raise StoreError(f"no shortlist {shortlist_id}")
        result = dict(row)
        result["items"] = [
            dict(r)
            for r in self.db.execute(
                "SELECT i.sample_id, i.position, s.name, s.path, s.excluded FROM shortlist_items i "
                "JOIN samples s ON s.id = i.sample_id WHERE i.shortlist_id = ? ORDER BY i.position",
                (shortlist_id,),
            ).fetchall()
        ]
        return result

    def shortlists(self, rack_id: int) -> list[dict]:
        ids = [
            r["id"]
            for r in self.db.execute(
                "SELECT id FROM shortlists WHERE rack_id = ? ORDER BY note, id", (rack_id,)
            ).fetchall()
        ]
        return [self.shortlist(i) for i in ids]

    def rename_shortlist(self, shortlist_id: int, name: str) -> None:
        if not name.strip():
            raise StoreError("a shortlist needs a name")
        with self.tx() as db:
            db.execute("UPDATE shortlists SET name = ? WHERE id = ?", (name.strip(), shortlist_id))

    def delete_shortlist(self, shortlist_id: int) -> None:
        with self.tx() as db:
            db.execute("DELETE FROM shortlists WHERE id = ?", (shortlist_id,))

    def add_candidate(self, shortlist_id: int, sample_id: int) -> None:
        self.shortlist(shortlist_id)
        self.sample(sample_id)
        with self.tx() as db:
            position = db.execute(
                "SELECT COALESCE(MAX(position), -1) + 1 FROM shortlist_items WHERE shortlist_id = ?", (shortlist_id,)
            ).fetchone()[0]
            db.execute("INSERT OR IGNORE INTO shortlist_items VALUES (?, ?, ?)", (shortlist_id, sample_id, position))

    def remove_candidate(self, shortlist_id: int, sample_id: int) -> None:
        with self.tx() as db:
            db.execute(
                "DELETE FROM shortlist_items WHERE shortlist_id = ? AND sample_id = ?", (shortlist_id, sample_id)
            )

    def candidates(self, shortlist_id: int) -> list[int]:
        return [i["sample_id"] for i in self.shortlist(shortlist_id)["items"]]

    # ------------------------------------------------------------------ comparisons

    def votes(self, shortlist_id: int) -> list[tuple[int, int]]:
        return [
            (r[0], r[1])
            for r in self.db.execute(
                "SELECT winner_id, loser_id FROM votes WHERE shortlist_id = ? ORDER BY id", (shortlist_id,)
            ).fetchall()
        ]

    def vote(self, shortlist_id: int, winner: int, loser: int) -> None:
        candidates = self.candidates(shortlist_id)
        if winner == loser or winner not in candidates or loser not in candidates:
            raise StoreError("both samples must be different candidates on this shortlist")
        with self.tx() as db:
            db.execute(
                "INSERT INTO votes (shortlist_id, winner_id, loser_id, created_at) VALUES (?, ?, ?, ?)",
                (shortlist_id, winner, loser, time.time()),
            )

    def undo_vote(self, shortlist_id: int) -> None:
        with self.tx() as db:
            db.execute(
                "DELETE FROM votes WHERE id = (SELECT MAX(id) FROM votes WHERE shortlist_id = ?)", (shortlist_id,)
            )

    def pairwise(self, shortlist_id: int) -> dict:
        candidates = self.candidates(shortlist_id)
        votes = self.votes(shortlist_id)
        return {
            "pair": compare.next_pair(candidates, votes),
            "ranking": compare.ranking(candidates, votes),
            "votes": len(votes),
        }

    def start_bracket(self, shortlist_id: int) -> int:
        """Seed by the pairwise ranking so earlier votes count."""
        seeds = [r["sample_id"] for r in self.pairwise(shortlist_id)["ranking"]]
        bracket = compare.Bracket.create(seeds)
        with self.tx() as db:
            return db.execute(
                "INSERT INTO brackets (shortlist_id, state, created_at) VALUES (?, ?, ?)",
                (shortlist_id, json.dumps(bracket.to_dict()), time.time()),
            ).lastrowid

    def bracket(self, shortlist_id: int) -> tuple[int, compare.Bracket] | None:
        row = self.db.execute(
            "SELECT id, state FROM brackets WHERE shortlist_id = ? ORDER BY id DESC LIMIT 1", (shortlist_id,)
        ).fetchone()
        if row is None:
            return None
        return row["id"], compare.Bracket.from_dict(json.loads(row["state"]))

    def pick(self, shortlist_id: int, winner: int) -> compare.Bracket:
        found = self.bracket(shortlist_id)
        if found is None:
            raise StoreError("start a bracket first")
        bracket_id, bracket = found
        current = bracket.current()
        try:
            bracket.pick(winner)
        except ValueError as error:
            raise StoreError(str(error)) from error
        assert current is not None
        _, _, match = current
        loser = match.b if winner == match.a else match.a
        with self.tx() as db:
            db.execute("UPDATE brackets SET state = ? WHERE id = ?", (json.dumps(bracket.to_dict()), bracket_id))
            # A bracket decision is also a pairwise vote, so the ranking learns from it.
            db.execute(
                "INSERT INTO votes (shortlist_id, winner_id, loser_id, created_at) VALUES (?, ?, ?, ?)",
                (shortlist_id, winner, loser, time.time()),
            )
        return bracket
