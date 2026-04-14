#!/usr/bin/env python3
"""
One-off migration for person entity conventions:
1. Strip [[People/...]] targets from alias:: frontmatter on all pages/Person___*.md
2. Add logseq-entity:: [[Logseq/Entity/person]] only to person *hub* files (Person___<Name>.md with no extra ___)

Never modifies tags:: lines. Idempotent for logseq-entity::.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"
PERSON_FM_LINE = re.compile(r"^[^\n]+::")
BRACKET_LINKS = re.compile(r"\[\[([^\]]+)\]\]")
PERSON_ENTITY_MARKER = "[[Logseq/Entity/person]]"


def is_person_hub(path: Path) -> bool:
    name = path.name
    if not name.startswith("Person___") or not name.endswith(".md"):
        return False
    middle = name[len("Person___") : -len(".md")]
    return "___" not in middle


def split_frontmatter(lines: list[str]) -> tuple[list[str], list[str]]:
    """Leading frontmatter: consecutive key:: lines (blank lines between keys are skipped)."""
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    fm: list[str] = []
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if PERSON_FM_LINE.match(line):
            fm.append(line)
            i += 1
            continue
        break
    return fm, lines[i:]


def strip_people_from_alias_line(line: str) -> str | None:
    """Return updated line, or None to remove the line entirely."""
    stripped = line.strip()
    if not stripped.startswith("alias::"):
        return line
    rest = stripped.split("alias::", 1)[1].strip()
    vals = BRACKET_LINKS.findall(rest)
    kept = [v for v in vals if not v.startswith("People/")]
    if not kept:
        return None
    new_body = ", ".join(f"[[{v}]]" for v in kept)
    return f"alias:: {new_body}\n"


def process_file(path: Path, dry_run: bool) -> tuple[bool, bool]:
    """Returns (alias_changed, entity_added)."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    fm, body = split_frontmatter(lines)

    alias_changed = False
    new_fm: list[str] = []
    for ln in fm:
        if ln.strip().startswith("alias::"):
            upd = strip_people_from_alias_line(ln)
            if upd is None:
                alias_changed = True
                continue
            if upd.rstrip("\n") != ln.rstrip("\n"):
                alias_changed = True
            new_fm.append(upd)
        else:
            new_fm.append(ln)

    has_person_entity = any(
        "logseq-entity::" in x and PERSON_ENTITY_MARKER in x for x in new_fm
    )
    entity_added = False
    if is_person_hub(path) and not has_person_entity:
        insert = f"logseq-entity:: {PERSON_ENTITY_MARKER}\n"
        new_fm.append(insert)
        entity_added = True

    if not alias_changed and not entity_added:
        return False, False

    new_text = "".join(new_fm + body)
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return alias_changed, entity_added


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    paths = sorted(PAGES.glob("Person___*.md"))
    a_count = e_count = 0
    for p in paths:
        a, e = process_file(p, dry_run)
        if a:
            a_count += 1
        if e:
            e_count += 1
    mode = "dry-run" if dry_run else "applied"
    print(f"{mode}: alias touched {a_count} files, logseq-entity added {e_count} hub files (total scanned {len(paths)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
