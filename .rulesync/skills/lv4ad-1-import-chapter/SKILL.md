---
name: lv4ad-1-import-chapter
description: >-
  Scaffold a new chapter page for "LazyVim for Ambitious Developers" (LV4AD)
  from raw Readwise highlights via the readwise CLI. Use when the user asks to
  import, pull in, or file LV4AD chapter highlights from Readwise, names a
  chapter number/title of that book, or pastes a readwise export for it. Creates
  the [[LV4AD/Ch/<NN Title>]] page with readwise-link:: frontmatter, a title
  bullet linking the book site's chapter, and raw un-formatted highlight/note
  bullets; links it from the [[LV4AD]] book hub. Formatting the highlights into
  house style is a separate step (lv4ad-2-format-chapter); spine prev/next nav
  is lv4ad-4-chapter-nav; do not do those here.
targets: ["*"]
codexcli:
  short-description: Scaffold an LV4AD chapter page from Readwise highlights
---

# LV4AD 1: Import chapter highlights

Scaffold-only step. Pull one chapter's highlights from Readwise and lay them
out as a new page; leave formatting/linking to the follow-on skills
**lv4ad-2-format-chapter**, **lv4ad-3-enrich-links**, and **lv4ad-4-chapter-nav**.

## Steps

1. **Find the book hub.** Grep for `LV4AD` across `pages/` and `journals/`
   (per `logseq-link-hygiene`) to find or confirm the existing `[[LV4AD]]` hub
   page (`pages/LV4AD.md`). It is the entity page for the whole book
   (`logseq-entity:: [[Logseq/Entity/Book]]`, `created-by:: [[Person/Dusty Phillips]]`).
   Do not invent a different hub name.
2. **Fetch the chapter's highlights.** Use skill `readwise-cli`. Resolve the
   Reader document id from the chapter's `readwise-link::` permalink
   (`…/read/<id>`) or search:
   `readwise reader-search-documents --query "LazyVim for Ambitious Developers chapter <N>"`.
   Pull highlights:
   `readwise reader-get-document-highlights --document-id <id> --json`
   Capture the Readwise **permalink** for this chapter — it becomes
   `readwise-link::`.
   - See [references/readwise-highlight-notes.md](./references/readwise-highlight-notes.md)
     for how user notes, Readwise AI answers, and stray book text share one
     `notes` field.
3. **Resolve the canonical chapter URL** on the free book site
   (`https://lazyvim-ambitious-devs.phillips.codes/course/chapter-<N>/`) via
   `web_fetch` so the title bullet links to the real source, not Readwise.
4. **Create the page** at `pages/LV4AD___Ch___<NN Title>.md` (e.g.
   `LV4AD___Ch___01 Intro and Install.md` → `[[LV4AD/Ch/01 Intro and Install]]`):
   - Frontmatter: `readwise-link:: <readwise permalink>`
   - `- # [Chapter <N>: <Title> - LazyVim for Ambitious Developers](<chapter url>)`
   - One bullet per highlight, in reading order, **flat** (no heading nesting
     yet): `- > <exact content field>`.
   - When a highlight's `notes` field is non-null, add **plain child bullets**
     directly under that highlight:
     - Split `notes` on `\n---\n` into segments (trim each); one child bullet
       per segment, in order.
     - Preserve segment text verbatim — do not add `[[My Note]]`,
       `[[AI Notes]]`, or italics yet.
     - Do not invent or paraphrase notes/highlights not present in the export.
   - The user may add more notes later in Logseq; those are preserved by
     re-import only if they also exist in Readwise.
5. **Link it from the hub**: add a bullet under `[[LV4AD]]`'s body pointing to
   the new chapter page (mirror the existing single-line style already used
   there for other chapters).
6. **Journal it**: add a `[[Filed]]` entry for today per `[[Logseq/Journal]]`
   (e.g. "lv4ad chapter import" grouping with links to the chapter and any new
   entity stubs).

## Guardrails

- This skill only scaffolds; it must not reorder highlights under headings,
  label notes (`[[My Note]]` / `[[AI Notes]]`), italicize notes, classify AI
  vs user prose, or add entity wikilinks — that's `lv4ad-2-format-chapter` and
  `lv4ad-3-enrich-links`.
- Never fabricate highlights, notes, or URLs. If the chapter URL can't be
  confirmed, leave the title bullet linking to the book home
  (`https://lazyvim-ambitious-devs.phillips.codes/`) instead of guessing an anchor.
- Follow `logseq-core` (protected `tags::`, LFM bullets/indentation, no blank lines).
