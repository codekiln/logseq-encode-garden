# LFM table layout (reference)

## Nesting pattern

Tables sit **under** a parent bullet (often a `##` heading bullet). Only the **first** row carries the list marker.

```markdown
	- ## [[My Answer]]
		- | Command              | Primary effect           | Cache |
		  | -------------------- | ------------------------ | ----- |
		  | [[mise/unuse]]       | remove config and binary | ✓     |
```

- **Row 1:** `{tabs}- | cell | cell |`
- **Row 2+:** `{tabs}  | cell | cell |` — replace `- ` with two spaces so the leading `|` aligns with row 1’s first `|`.

Garden examples: `pages/nvim___Q___What does %22 mean in nvim%3F.md`, `pages/mise___Q___What's the difference between mise unuse, mise uninstall, and mise cache clear%3F.md`, `pages/brew___file.md`.

## Column alignment

- Compute each column width as the maximum **visible** character length of cells in that column (header, separator dashes, body).
- Left-pad cell content with spaces inside `| … |` so pipes form vertical columns in a monospace view.
- Separator row: dashes only (`-` repeated to column width), no extra spaces required beyond padding.
- After editing, verify all pipe positions match on every row (script or a quick column check).

## Cell content

| Use | When |
|-----|------|
| `[[Page/Name]]` | Target page exists or is created in the same edit |
| Plain text | Labels, ✓/✗, short phrases |
| `` `command` `` | Ephemeral shell tokens with no graph page; flags like `` `--no-prune` `` |

Do not wrap wikilinks in `**…**` (see rule **logseq-core** → *Bold and inline code*; advanced detail: skill **logseq-lfm**).

## Two-column vs wide tables

- **Two columns**, compact comparisons: table is fine inside a bullet.
- **Many columns** or long prose per cell: prefer nested bullets (label → value) per skill **logseq-convert-md-to-lfm**.

## Footnotes under the table

Place caveats as a **sibling** bullet under the same parent, not inside the table:

```markdown
		- | … table … |
		- Optional note with [[mise/install]] if needed.
```

## Common mistakes

- Putting `- ` on every table row (breaks LFM list semantics and misaligns pipes).
- Unpadded columns (hard to scan in git diffs and plain-text review).
- Backtick command names when a CLI stub page exists (`[[mise/unuse]]`).
