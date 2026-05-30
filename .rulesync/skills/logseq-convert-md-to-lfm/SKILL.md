---
name: logseq-convert-md-to-lfm
description: >-
  Convert standard Markdown (especially pasted from ChatGPT or similar) into
  Logseq-Flavored Markdown: nest code blocks inside bullets, fix heading-to-indent
  levels, drop horizontal rules, convert wide tables to label-value bullets,
  fix footnotes to URL-only, and replace generic link text. Use when the user
  pastes non-LFM markdown to import, asks to "convert to LFM", or to clean up an
  AI-generated dump. For table column alignment use logseq-table-formatter; for
  baseline LFM rules see logseq-core / logseq-lfm.
targets: ["*"]
codexcli:
  short-description: Convert standard Markdown into Logseq-Flavored Markdown
---

# Convert Markdown → LFM

Apply the conversion checklist when importing standard markdown into the garden. Baseline LFM rules live in `logseq-core`; this skill covers the exceptional fixes that pasted/AI markdown typically needs.

## Checklist (work top to bottom)

1. **Links** — replace generic text like `[github.com](url)` with the destination's real title.
2. **Code blocks** — nest fenced blocks *inside* a bullet, not as sibling bullets; use `~~~` inside outer ``` ``` ``` blocks.
3. **Horizontal rules** — delete `---` separators; use heading hierarchy/indentation instead.
4. **Tables** — convert >2-column tables to label-value bullets; a 2-column table may stay if wrapped in a `-` bullet. (For aligning a table you keep, use the `logseq-table-formatter` skill.)
5. **Heading levels** — `#` at root, `##` at one TAB, `###` at two TABs.
6. **Footnotes** — `Footnotes` section (not "References"); `[^1]: url` (URL-only, no link text); separate adjacent refs with spaces (`[^4] [^5]`).

Read [references/conversion-checklist.md](./references/conversion-checklist.md) for full examples, common pitfalls, and before/after conversions.
