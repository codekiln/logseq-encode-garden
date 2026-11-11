"""Index sample folders and existing Drum Racks, and run sample analysis in the background."""

from __future__ import annotations

import hashlib
import logging
import os
import threading
from dataclasses import dataclass, field
from pathlib import Path

from . import adg
from .analysis import LiveOnlyError, analyze
from .config import Config
from .store import Store

log = logging.getLogger(__name__)


@dataclass
class SourceRack:
    id: str
    path: Path
    name: str
    creator: str
    pads: list[adg.Pad]
    origin: str = "library"


def rack_id(path: Path) -> str:
    return hashlib.sha1(str(path).encode()).hexdigest()[:12]


def walk_audio(roots: list[Path], extensions: list[str]):
    suffixes = {"." + e for e in extensions}
    for root in roots:
        if not root.is_dir():
            log.warning("sample folder %s does not exist", root)
            continue
        for directory, dirnames, filenames in os.walk(root):
            # Live's analysis files and hidden folders are not samples.
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            for filename in filenames:
                if not filename.startswith(".") and Path(filename).suffix.lower() in suffixes:
                    yield Path(directory) / filename


def find_racks(roots: list[Path]) -> list[Path]:
    found = []
    for root in roots:
        if root.is_dir():
            found += [p for p in root.rglob("*.adg") if not p.name.startswith(".")]
    return sorted(found)


@dataclass
class Library:
    config: Config
    store: Store
    source_racks: dict[str, SourceRack] = field(default_factory=dict)
    status: dict = field(default_factory=lambda: {"scanning": False, "analyzing": False, "message": ""})
    _wake: threading.Event = field(default_factory=threading.Event)
    _stop: threading.Event = field(default_factory=threading.Event)
    _scan_lock: threading.Lock = field(default_factory=threading.Lock)

    def scan(self) -> dict:
        """Index sample folders and racks. Safe to repeat; existing curation is kept."""
        if not self._scan_lock.acquire(blocking=False):
            return {"started": False}
        try:
            self.status.update(scanning=True, message="scanning sample folders")
            seen = set()
            for path in walk_audio(self.config.sample_folders, self.config.extensions):
                self.store.upsert_sample(path, in_folder=True)
                seen.add(str(path))
            missing = self.store.mark_folder_scan(seen, self.config.sample_folders)
            self.status.update(message="reading Drum Racks")
            racks = self.scan_racks()
            self.status.update(
                scanning=False,
                message=f"indexed {len(seen)} samples and {len(racks)} racks"
                + (f"; {missing} samples no longer found" if missing else ""),
            )
            self._wake.set()
            return {"started": True, "samples": len(seen), "racks": len(racks), "missing": missing}
        finally:
            self.status["scanning"] = False
            self._scan_lock.release()

    def scan_racks(self) -> dict[str, SourceRack]:
        racks: dict[str, SourceRack] = {}
        for path in find_racks(self.config.rack_folders):
            if path.resolve().is_relative_to(self.config.output_folder):
                origin = "builder"
            else:
                origin = "library"
            try:
                rack = adg.read_rack(path)
            except adg.RackError as error:
                # Instrument and effect racks share the extension; only Drum Racks are listed.
                log.debug("skipping %s: %s", path, error)
                continue
            source = SourceRack(
                id=rack_id(path), path=path, name=path.stem, creator=rack.creator, pads=rack.pads, origin=origin
            )
            for pad in rack.pads:
                for sample in pad.samples:
                    sample_id = self.store.upsert_sample(Path(sample), in_rack=True)
                    self.store.record_rack_usage(sample_id, path, pad.note)
            racks[source.id] = source
        self.source_racks = racks
        return racks

    def source_rack(self, rack_key: str) -> SourceRack:
        rack = self.source_racks.get(rack_key)
        if rack is None:
            raise KeyError(f"no source rack {rack_key}")
        return rack

    def protected_paths(self) -> list[Path]:
        return [r.path for r in self.source_racks.values()]

    # ------------------------------------------------------------------ analysis

    def analyze_pending(self, batch: int = 25) -> int:
        done = 0
        for row in self.store.unanalyzed(batch):
            if self._stop.is_set():
                break
            try:
                result, error = analyze(Path(row["path"])).as_dict(), None
            except LiveOnlyError as exc:
                result, error = None, str(exc)
            except Exception as exc:  # a damaged or unsupported file must not stop the worker
                result, error = None, f"{type(exc).__name__}: {exc}"
            self.store.save_analysis(row["path"], row["size"], row["mtime"], result, error)
            done += 1
        return done

    def analysis_worker(self) -> None:
        while not self._stop.is_set():
            self.status["analyzing"] = True
            if self.analyze_pending() == 0:
                self.status["analyzing"] = False
                self._wake.wait(timeout=30)
                self._wake.clear()

    def start(self) -> None:
        threading.Thread(target=self.scan, name="scan", daemon=True).start()
        threading.Thread(target=self.analysis_worker, name="analysis", daemon=True).start()

    def stop(self) -> None:
        self._stop.set()
        self._wake.set()
