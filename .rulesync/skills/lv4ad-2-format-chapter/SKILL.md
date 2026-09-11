---
name: lv4ad-2-format-chapter
description: >-
  Reformat an already-scaffolded LV4AD chapter page (from lv4ad-1-import-chapter)
  into house style: nest highlights under the book site's real heading
  hierarchy (with links to each heading's anchor), blockquote the highlight
  text, backtick inline code/commands, and turn each personal annotation into
  its own `[[My Note]]` child bullet in italics. Use when the user asks to
  format, clean up, restructure, or "make it match my style" for an
  [[LV4AD/Ch/...]] page that already has raw/flat highlights. Does not fetch
  new highlights (lv4ad-1-import-chapter) and does not add links to other
  garden entities (lv4ad-3-enrich-links).
targets: ["*"]
codexcli:
  short-description: Format LV4AD chapter highlights into house style
---

# LV4AD 2: Format chapter into house style

Reshapes an existing, already-imported `[[LV4AD/Ch/<NN Title>]]` page.
Preserves every highlight and note verbatim — this is a structure/formatting
pass, not a rewrite.

## Steps

1. **Get the real heading structure.** `web_fetch` the chapter's canonical URL
   (from the page's title bullet) to read the book site's actual section
   numbers, titles, and anchor fragments (e.g. `#_introducing_lazyvim`).
2. **Match each highlight to its section** by re-reading the chapter content
   in reading order, then nest the page's flat highlight bullets under heading
   bullets that mirror the site's own hierarchy and numbering:
   - `- ## 1.1 Why Vim` for a heading with no page anchor on the site.
   - `- ## [1.3 Introducing LazyVim](<chapter-url>#_introducing_lazyvim)` when
     the heading does have one — link text is `<number> <title>` even if the
     site's rendered heading differs slightly in casing/punctuation.
   - Use `###`/`####` etc. to mirror sub-sections exactly as nested on the
     site (see the worked example).
3. **Blockquote every highlight**: `> <highlight text>`, unchanged. Wrap
   inline commands, filenames, and code identifiers already implied by context
   in backticks if the source rendered them as code (don't add emphasis that
   changes meaning).
4. **Reformat each personal note** as its own child bullet directly under the
   highlight it annotates: `[[My Note]] <note text>`, with the note text in
   `*italics*`. One `[[My Note]]` bullet per distinct annotation — don't merge
   or drop any.
5. **Preserve `id::` lines.** If a highlight bullet carries an `id::` (per
   `logseq-block-ids`), keep it attached to that exact bullet through the
   restructuring; grep the graph for `((that-uuid))` before you would ever
   consider dropping one.
6. Leave `readwise-link::` frontmatter and the title bullet untouched.
   Do not add wikilinks to other entities in this pass — that's
   `lv4ad-3-enrich-links`.

## Reference

- [references/format-example.md](./references/format-example.md) — a full
  worked example (Chapter 1) showing the exact target shape.
