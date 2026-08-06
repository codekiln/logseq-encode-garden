#!/usr/bin/env python3
"""Restore ChatGPT Deep Research citations using links embedded in the PDF.

The script reads a Deep Research Markdown export containing markers like
`cite turn...` and a matching PDF. It extracts clickable citation anchors from
the PDF with Poppler's `pdftohtml -xml`, replaces web citation markers in
Markdown order with Logseq-compatible footnote references, strips local
`filecite` markers, and appends URL-only Markdown footnotes.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


CITE_RE = re.compile(r"cite[^]+")
FILECITE_RE = re.compile(r"\s*filecite[^]+")
ANCHOR_RE = re.compile(r'<text[^>]*><a href="([^"]+)">(\d+)</a></text>')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Restore Deep Research citations from PDF links."
    )
    parser.add_argument("--pdf", required=True, help="Path to Deep Research PDF")
    parser.add_argument(
        "--markdown", required=True, help="Path to Deep Research Markdown export"
    )
    parser.add_argument(
        "--output",
        help="Write transformed Markdown here. Defaults to stdout.",
    )
    parser.add_argument(
        "--allow-no-citations",
        action="store_true",
        help="Allow Markdown with no web citation markers.",
    )
    return parser.parse_args()


def extract_pdf_anchors(pdf: Path) -> list[tuple[str, int]]:
    try:
        result = subprocess.run(
            ["pdftohtml", "-xml", "-stdout", str(pdf)],
            check=True,
            text=True,
            capture_output=True,
        )
    except FileNotFoundError:
        raise SystemExit("pdftohtml is required; install Poppler or load its runtime.")
    except subprocess.CalledProcessError as exc:
        raise SystemExit(exc.stderr or f"pdftohtml failed with {exc.returncode}")

    anchors = [(url, int(num)) for url, num in ANCHOR_RE.findall(result.stdout)]
    if not anchors:
        raise SystemExit("No clickable citation anchors found in PDF.")
    return anchors


def restore(markdown: str, anchors: list[tuple[str, int]], allow_empty: bool) -> str:
    cite_groups = list(CITE_RE.finditer(markdown))
    if not cite_groups and not allow_empty:
        raise SystemExit("No Deep Research web citation markers found in Markdown.")
    if len(anchors) < len(cite_groups):
        raise SystemExit(
            f"PDF has {len(anchors)} anchors but Markdown has "
            f"{len(cite_groups)} citation groups."
        )

    url_min_number: dict[str, int] = {}
    for url, number in anchors:
        url_min_number[url] = min(number, url_min_number.get(url, number))

    used_numbers: set[int] = set()
    body_anchors = iter(anchors[: len(cite_groups)])

    def replace_cite(_: re.Match[str]) -> str:
        url, _number = next(body_anchors)
        footnote_number = url_min_number[url]
        used_numbers.add(footnote_number)
        return f" [^{footnote_number}]"

    transformed = CITE_RE.sub(replace_cite, markdown)
    filecite_count = len(FILECITE_RE.findall(transformed))
    transformed = FILECITE_RE.sub("", transformed)
    transformed = re.sub(r"\s+([.,;:])", r"\1", transformed)
    transformed = re.sub(r"(\[\^\d+\])(?=\[\^\d+\])", r"\1 ", transformed)

    if "" in transformed or "filecite" in transformed:
        raise SystemExit("Unresolved Deep Research citation markers remain.")

    if used_numbers:
        number_to_url = {
            number: url for url, number in url_min_number.items() if number in used_numbers
        }
        footnotes = ["", "## Footnotes"]
        for number in sorted(used_numbers):
            footnotes.append(f"[^{number}]: {number_to_url[number]}")
        transformed = transformed.rstrip() + "\n" + "\n".join(footnotes) + "\n"

    print(
        f"Restored {len(cite_groups)} citation groups to "
        f"{len(used_numbers)} unique URL footnotes; stripped "
        f"{filecite_count} local file citation markers.",
        file=sys.stderr,
    )
    return transformed


def main() -> int:
    args = parse_args()
    pdf = Path(args.pdf)
    markdown_path = Path(args.markdown)
    if not pdf.exists():
        raise SystemExit(f"PDF not found: {pdf}")
    if not markdown_path.exists():
        raise SystemExit(f"Markdown not found: {markdown_path}")

    anchors = extract_pdf_anchors(pdf)
    transformed = restore(
        markdown_path.read_text(), anchors, allow_empty=args.allow_no_citations
    )

    if args.output:
        Path(args.output).write_text(transformed)
    else:
        sys.stdout.write(transformed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
