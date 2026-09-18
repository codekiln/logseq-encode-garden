---
name: lv4ad-4-chapter-nav
description: >-
  Wire serial prev:: / next:: frontmatter on top-level [[LV4AD/Ch/<NN Title>]]
  chapter pages so the book reads in order in Logseq. Use when filing a new
  LV4AD chapter, backfilling spine navigation on existing chapters, or after
  reordering the [[LV4AD]] hub list. Updates neighbor chapters too. Does not
  touch highlight bodies (lv4ad-2-format-chapter) or entity wikilinks
  (lv4ad-3-enrich-links). Subpages such as [[LV4AD/Ch/04 Opening Files/01 …]] do
  not get prev/next.
metadata:
  short-description: Add prev/next chapter nav to LV4AD chapter pages
---
# LV4AD 4: Chapter spine navigation

Adds `prev::` and `next::` page attributes on **top-level** chapter pages only
(`pages/LV4AD___Ch___<NN Title>.md` → `[[LV4AD/Ch/<NN Title>]]`). Subpages
under a chapter (e.g. `LV4AD___Ch___04 Opening Files___01 …`) never carry spine
nav.

## Steps

1. **Read the canonical order** from `[[LV4AD]]` (`pages/LV4AD.md`): hub bullets
   under the book title, in reading order. Grep `pages/LV4AD___Ch___*.md` to
   confirm each linked chapter has a file (logical-only pages are fine to link
   but this skill only writes files that exist).
2. **For each top-level chapter page**, set frontmatter **before** the first
   list bullet (after any other page attributes such as `readwise-link::`):
   - `prev:: [[LV4AD/Ch/<previous>]]` — omit on chapter 1.
   - `next:: [[LV4AD/Ch/<next>]]` — omit on the last chapter in the hub list.
   - Order when multiple attributes exist: `readwise-link::` (if present),
     then `prev::`, then `next::`, then a blank line, then the title bullet.
3. **Update neighbors** whenever a chapter is newly filed or inserted mid-spine:
   the previous chapter's `next::` and the next chapter's `prev::` must match.
4. **Journal it**: add an `[[Updated]]` entry for today per `[[Logseq/Journal]]`
   (e.g. grouping `lv4ad chapter nav` with links to every chapter touched).

## Worked example

`[[LV4AD/Ch/04 Opening Files]]` (hub page with embeds, no `readwise-link::`):

```
prev:: [[LV4AD/Ch/03 Getting Around]]
next:: [[LV4AD/Ch/05 Plugin Basics]]

- # [Chapter 4: Opening Files - LazyVim for Ambitious Developers](…)
```

A middle chapter with Readwise metadata (`[[LV4AD/Ch/03 Getting Around]]`):

```
readwise-link:: https://read.readwise.io/read/…
prev:: [[LV4AD/Ch/02 Modal Editing]]
next:: [[LV4AD/Ch/04 Opening Files]]

- # [Chapter 3: Getting Around - LazyVim for Ambitious Developers](…)
```

## Guardrails

- Never add `prev::` / `next::` to subpages or to `[[LV4AD]]` itself.
- Never link a chapter to itself; skip `prev::` / `next::` rather than guess
  when the hub order is ambiguous.
- Do not modify protected `tags::` or rewrite highlight/note bodies — only
  page-level frontmatter for spine nav.
- Later LV4AD passes must preserve existing `prev::` / `next::` lines unchanged
  (same as `readwise-link::`).

## Pipeline position

Run after **lv4ad-1-import-chapter** (page exists and is on the hub). Safe to
run before or after **lv4ad-2-format-chapter** and **lv4ad-3-enrich-links**; it
only touches frontmatter.
