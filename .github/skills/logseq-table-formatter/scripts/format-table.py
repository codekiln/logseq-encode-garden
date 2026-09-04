#!/usr/bin/env python3
"""Emit an LFM-aligned markdown table for Logseq pages.

Usage:
  format-table.py --rows 'H1|H2' --rows '---|---' --rows 'a|b'
  echo 'H1|H2' | format-table.py --tabs 2

First --rows line is emitted with "- |"; later lines use "  |" aligned to the first pipe.
"""

from __future__ import annotations

import argparse
import sys
from typing import List, Sequence


def parse_row(line: str) -> List[str]:
    line = line.strip()
    if not line:
        raise ValueError("empty row")
    if "|" in line:
        parts = [p.strip() for p in line.split("|")]
        if parts and parts[0] == "":
            parts = parts[1:]
        if parts and parts[-1] == "":
            parts = parts[:-1]
        return parts
    return [line]


def is_separator_row(cells: Sequence[str]) -> bool:
    return all(set(c) <= {"-"} and c for c in cells)


def column_widths(rows: Sequence[Sequence[str]]) -> List[int]:
    if not rows:
        return []
    n = max(len(r) for r in rows)
    widths = [0] * n
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))
    return widths


def format_row(cells: Sequence[str], widths: Sequence[int], *, separator: bool) -> str:
    padded = []
    for i, w in enumerate(widths):
        cell = cells[i] if i < len(cells) else ""
        if separator:
            padded.append("-" * w)
        else:
            padded.append(cell.ljust(w))
    return "| " + " | ".join(padded) + " |"


def emit_lfm_table(rows: Sequence[Sequence[str]], tabs: int) -> str:
    if len(rows) < 2:
        raise ValueError("need at least header and one body or separator row")

    widths = column_widths(rows)
    indent = "\t" * tabs
    lines: List[str] = []

    for i, row in enumerate(rows):
        sep = is_separator_row(row)
        body = format_row(row, widths, separator=sep)
        if i == 0:
            lines.append(f"{indent}- {body}")
        else:
            lines.append(f"{indent}  {body}")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tabs",
        type=int,
        default=2,
        help="Tab count before the table (default: 2)",
    )
    parser.add_argument(
        "--rows",
        action="append",
        default=[],
        help="Row as pipe-separated cells (repeat per row)",
    )
    args = parser.parse_args()

    raw_rows = args.rows if args.rows else [line.rstrip("\n") for line in sys.stdin]
    if not raw_rows:
        parser.error("provide --rows or stdin")

    rows = [parse_row(r) for r in raw_rows]
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]

    print(emit_lfm_table(rows, args.tabs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
