---
name: lv4ad-2-format-chapter
description: >-
  Reformat an already-scaffolded LV4AD chapter page (from
  lv4ad-1-import-chapter) into house style: nest highlights under the book
  site's real heading hierarchy (with links to each heading's anchor),
  blockquote the highlight text, backtick inline code/commands, and turn each
  personal annotation into its own `[[My Note]]` or `[[AI Notes]]` child bullet
  in italics with properly nested follow-on bullets. Use when the user asks to
  format, clean up, restructure, or "make it match my style" for an
  [[LV4AD/Ch/...]] page that already has raw/flat highlights. Does not fetch new
  highlights (lv4ad-1-import-chapter) and does not add links to other garden
  entities (lv4ad-3-enrich-links).
metadata:
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
3. **Blockquote every highlight**: `- > <highlight text>`, unchanged. Wrap
   inline commands, filenames, and code identifiers already implied by context
   in backticks if the source rendered them as code (don't add emphasis that
   changes meaning).
   - **One paragraph per blockquote bullet.** When a highlight spans multiple
     paragraphs, split it into sibling `- >` bullets — do **not** use
     continuation lines (`  > `) to glue paragraphs together.
   - **Recover misplaced book text.** If highlight prose ended up nested
     inside a `[[My Note]]` or `[[AI Notes]]` block (common when Readwise
     drops a figure or code block), promote it back to a sibling blockquote
     bullet at the correct section level.
4. **Label and reformat each note segment** as its own child bullet directly
   under the highlight it annotates, with the note text in `*italics*`:
   - Notes come from Readwise (`notes` on each highlight — user prose,
     Readwise's built-in AI answers, and sometimes stray book text) **and** from
     notes the user adds later in Logseq. See
     [references/readwise-note-labels.md](./references/readwise-note-labels.md)
     for classification rules.
   - `[[My Note]]` — the reader's own reflection, question, or missing-text
     reconstruction.
   - `[[AI Notes]]` — Readwise AI answers (e.g. *The document identifies…*,
     *The document does not explicitly define…*) or other AI expansions.
   - If a segment is already labeled, keep it — only fix nesting/italics.
   - If import split Readwise `notes` on `\n---\n`, label each segment
     separately; post-`---` book prose after a *Missing text* note gets
     **promoted** to a sibling blockquote instead of a note.
   - One note bullet per distinct annotation — don't merge or drop any.
   - **Nest follow-on content under the note bullet** (extra indent), not as
     siblings at the highlight level: bullet lists, sub-headings, code fences,
     and continuation paragraphs all belong as children of the note.
5. **Shape note interiors** when a note reconstructs missing book content or
   expands on a highlight:
   - Sub-sections inside a note use `### [[Entity/Page]]` headings with the
     primary subject as a wikilink (e.g. `### [[nvim/Plugin/mini.files]]`),
     not plain-text titles like `### Mini.files`.
   - Under each `###`, keep the recovered prose in **one bullet per paragraph**
     — don't split a single sentence across multiple bullets.
   - Code snippets inside a note use a fenced block (triple backticks) nested
     under the note, not one bullet per source line.
6. **Preserve `id::` lines.** If a highlight bullet carries an `id::` (per
   `logseq-block-ids`), keep it attached to that exact bullet through the
   restructuring; grep the graph for `((that-uuid))` before you would ever
   consider dropping one.
7. Leave `readwise-link::`, `prev::`, `next::` frontmatter and the title bullet
   untouched. Do not add wikilinks to other entities in this pass — that's
   `lv4ad-3-enrich-links`. Spine nav is **lv4ad-4-chapter-nav**.

## Reference

- [references/format-example.md](./references/format-example.md) — worked
  examples (Chapters 1 and 5) showing the exact target shape.
- [references/readwise-note-labels.md](./references/readwise-note-labels.md) —
  `[[My Note]]` vs `[[AI Notes]]` classification from Readwise `notes` segments.
