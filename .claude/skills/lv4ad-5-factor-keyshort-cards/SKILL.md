---
name: lv4ad-5-factor-keyshort-cards
description: >-
  Factor inline [[card]] keyshort flashcards from an LV4AD section subpage (e.g.
  [[LV4AD/Ch/04 Opening Files/01 Introducing File Pickers]]) into first-class
  Card entity pages as siblings under that section (no /Card/ namespace
  segment), replace each inline block with a page embed on the section page, and
  add a matching embed on the chapter page at the highlight where the keyshort
  is taught. Use when applying the LV4AD section + card embed model after
  lv4ad-2-format-chapter (and optional section subpages). Follows
  [[Logseq/Entity/Card]] naming. Does not import Readwise highlights (lv4ad-1)
  or create section pages from scratch.
---
# LV4AD 5: Factor keyshort cards

Optional study layer on top of a formatted `[[LV4AD/Ch/<NN Title>]]` chapter.
Section subpages hold section-local card decks; each card becomes its own page
at `[[LV4AD/Ch/<NN Title>/<SS Section>/<Short Title>]]` (section page is the
**source page** per `[[Logseq/Entity/Card]]` — no `/Card/` namespace segment).
Each card is surfaced twice via page embeds:

1. **Section page** — deck index (embed replaces the former inline `[[card]]` block).
2. **Chapter page** — provenance embed as a child of the highlight that teaches the keyshort.

Load **logseq-flashcard** (`card-entity-and-factor-out.md`) and
`[[Logseq/Entity/Card]]` for Card entity conventions; this skill adds the
LV4AD section subpage as source page and dual-embed placement.

## Prerequisites

- Chapter page exists and is formatted (**lv4ad-2-format-chapter**; **lv4ad-3-enrich-links** optional).
- A **section subpage** exists at `[[LV4AD/Ch/<NN Title>/<SS Section Title>]]`
  (e.g. `01 Introducing File Pickers` under `04 Opening Files`).
- Section page may already link the book heading and list inline `[[card]]` blocks
  (legacy marker) to factor out.
- Chapter section heading may already cross-link the section page, e.g.
  `(My Notes: [[LV4AD/Ch/04 Opening Files/01 Introducing File Pickers]])`.

## Steps

1. **Open the section page** (`pages/LV4AD___Ch___<NN>___<SS>….md`). Find every
   reviewable block marked `[[card]]` (usually a `###` question about
   `[[Keyshort]]` / `[[LazyVim/…]]` with answer children and optional SRS
   lines: `card-last-interval::`, `card-repeats::`, etc.).
2. **Dedup** per `logseq-link-hygiene`: grep for an existing
   `…/<SS Section>/<Short Title>` page or the same prompt text before
   creating a file. Do **not** use a `/Card/` path segment — that shape is
   deprecated per `[[Logseq/Entity/Card]]`.
3. **Choose `Short Title`** — concise, title-case, no leading numbers from the
   prompt (e.g. `Fastest Way to Close LazyVim`, not `What is the fastest…`).
4. **Create the card page** at
   `pages/LV4AD___Ch___<NN Title>___<SS Section>___<Short Title>.md`
   → `[[LV4AD/Ch/<NN Title>/<SS Section>/<Short Title>]]`:
   - Frontmatter: `logseq-entity:: [[Logseq/Entity/Card]], [[Logseq/Entity/Keyshort]]`
   - Move the **entire** inline card block verbatim (question `###`, `[[card]]`
     marker, all `card-*::` SRS lines, answer children). Preserve `id::` if present.
   - Do not add agent commentary or duplicate the prompt elsewhere on the page.
5. **Section page** — replace the inline card block with:
   `- {{embed [[LV4AD/Ch/<NN Title>/<SS Section>/<Short Title>]]}}`
   at the same list position (reading order).
6. **Chapter page** — locate the **provenance highlight**: the `- > …` blockquote
   on `[[LV4AD/Ch/<NN Title>]]` that teaches the keyshort(s) the card tests
   (match on key names in backticks, `:commands`, or `<leader>` sequences from
   the card answers). Add the embed as a **child bullet** under that highlight
   (sibling to `[[My Note]]` / `[[AI Notes]]` children):
   `- {{embed [[LV4AD/Ch/<NN Title>/<SS Section>/<Short Title>]]}}`
   - If no single highlight is a clear match, prefer the highlight that first
     introduces the primary answer keyshort; if still ambiguous, embed on the
     section page only and note the gap in chat — do not guess a wrong highlight.
   - Skip a second chapter embed if one is already present for that card.
7. **Journal** per `[[Logseq/Journal]]`: new card pages under `[[Filed]]`
   (group e.g. `lv4ad keyshort cards`); touched section and chapter pages under
   `[[Updated]]`.

## Multi-answer cards

When a card tests **two distinct answers** (two keyshorts, two scopes, or a
keyshort plus a command name), frame the prompt and answers with matching
**1.** / **2.** numbering:

- **Prompt** — use `### 1. …, and 2. …? [[card]]` (or `1. …, 2. …, and 3. …`
  for three parts). Do not ask "what two keyshorts…" without numbering the parts.
- **Answers** — one child bullet per part, each prefixed `1.` / `2.` (or
  `3.`), and each stating what that part does **differently** (scope, target,
  or command name) — not a single line listing both keys.

<CORRECT_✅>
- ### 1. What [[Keyshort]] opens [[nvim/Plugin/mini.files]] at the directory of the current file, and 2. what [[Keyshort]] opens it at the current working directory? [[card]]
	- 1. `<leader>fm` — opens at the directory containing the file in the active buffer
	- 2. `<leader>fM` — opens at Neovim's current working directory (cwd)
</CORRECT_✅>

<CORRECT_✅>
- ### 1. What are two [[Keyshort]]s for activating the [[LazyVim/Picker/File]], 2. what is the command called? [[card]]
	- 1. `<leader> Space` (aka `Space Space`) or `<leader>ff` — both open the same picker
	- 2. `Find Files (Root Directory)`
</CORRECT_✅>

Apply when **drafting** new inline cards on a section page. The "do not
rewrite" guardrail below still applies when **moving** an existing card block
verbatim during factor-out — unless the user asks to fix prompt shape.

## Worked example

See [references/worked-example.md](./references/worked-example.md) (Chapter 4,
section 4.1, card *Fastest Way to Close LazyVim*).

## Guardrails

- **Naming** — use `[[LV4AD/Ch/<NN>/<SS>/<Short Title>]]` only. Never insert a
  `/Card/` namespace segment; that shape is deprecated (`[[Logseq/Entity/Card]]`,
  logseq-flashcard `card-entity-and-factor-out.md`).
- Never modify protected `tags::` on any page.
- Do not rewrite highlight, note, or card prompt/answer text when moving blocks.
- Do not add `prev::` / `next::` to section or card pages (**lv4ad-4-chapter-nav**).
- Do not remove the section subpage link from the chapter heading when adding
  provenance embeds.
- One card page per inline `[[card]]` block; multi-part numbered questions stay
  on a single card page.

## Pipeline position

Run after **lv4ad-2-format-chapter** (and **lv4ad-3-enrich-links** if linking).
Requires a section subpage (human- or agent-scaffolded). Safe before or after
**lv4ad-4-chapter-nav**. Independent of **lv4ad-1-import-chapter** re-runs —
re-import does not restore factored cards; merge manually if highlights change.
