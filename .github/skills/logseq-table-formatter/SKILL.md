---
name: logseq-table-formatter
description: >-
  Format markdown tables inside Logseq Flavored Markdown (LFM) pages and
  journals: bullet-wrapped first row, continuation rows with aligned pipe
  columns, padded cells for readable plain text, and [[wikilinks]] for graph
  commands or pages when they exist. Use when adding or fixing tables in
  pages/*.md or journals/*.md, when the user asks for column alignment, or after
  editing comparison tables. Do not use to convert wide tables to bullets (skill
  logseq-convert-md-to-lfm) or for non-Logseq markdown.
---
# Logseq table formatter

Use when a table lives **inside** an LFM bullet tree (`pages/`, `journals/`) and must render in Logseq **and** read cleanly in the raw file.

## Default path

1. Confirm the table should stay a table (not a bullet label/value list). If more than two columns and the content is not a compact comparison, consider bullets per skill **logseq-convert-md-to-lfm**.
2. Build row data (header + separator + body). Prefer **short** cell text; put detail in child bullets under the table.
3. Use **wikilinks** in cells when a canonical page exists (`[[mise/unuse]]`, not `` `mise unuse` ``). Run skill **logseq-link-hygiene** when unsure a page exists.
4. Format with aligned columns:
   - First row: `- | col1 | col2 | … |` at the correct tab depth.
   - Following rows: same tab depth, **two spaces** instead of `- `, then `| … |` so every `|` shares the same column as row 1.
   - Pad cell text with spaces so pipes line up across all rows (verify in plain text).
5. Prefer the formatter script for padding; hand-edit only small tables.

## Script

From repo root:

```sh
python3 .rulesync/skills/logseq-table-formatter/scripts/format-table.py \
  --tabs 2 \
  --rows='Command|Primary effect|Cache' \
  --rows='----|----|----' \
  --rows='[[mise/unuse]]|remove config and binary|✓'
```

- `--tabs N` — tab count before the table (default `2`).
- `--rows='a|b|c'` — one row per flag (use `=` so separator rows like `----|----` are not parsed as CLI flags). First row is emitted with `- |`, rest with aligned `  |`.
- Or pipe one row per line on stdin: `printf '%s\n' 'H|H' '---|---' 'a|b' | python3 …/format-table.py --tabs 2`

Trust script output for column widths; fix wikilinks and wording before running.

## When to read references

- [references/lfm-table-layout.md](./references/lfm-table-layout.md) — LFM nesting, garden examples, wikilink vs backticks, checkmarks, edge cases.

## Related

- rule: **logseq-core** — bullets, tabs, no blank lines between blocks (advanced detail: skill **logseq-lfm**).
- skill: **logseq-convert-md-to-lfm** — when **not** to keep a table.
- skill: **logseq-link-hygiene** — resolve `[[wikilinks]]` before filing.
