---
name: logseq-flashcard
description: >-
  Create or maintain Logseq SRS flashcards and first-class Card entity pages in
  this garden. Use when the user asks to add a flashcard, factor out cards,
  create or audit Card pages, audit or fix Keyshort flashcards, ensure {{cards}}
  queries pick up cards, design or debug simple or advanced query expressions
  for card decks, or convert shortcut notes into review cards. New generic card
  work uses [[Card]] and [[Logseq/Entity/Card]]; legacy Keyshort audits may
  still encounter #card / [[card]]. Do not use for non-Logseq decks (e.g.
  repeater-only formats).
---
# Logseq flashcard

## Choose a path

1. **Factor out or create a first-class Card entity page** (`[[Source/Page/Card/Title]]`) — read [references/card-entity-and-factor-out.md](./references/card-entity-and-factor-out.md), then load `[[Logseq/Entity]]` and `[[Logseq/Entity/Card]]` before editing graph pages.
2. **Audit or repair Keyshort pages** (`*___Keyshort___*.md`) — read [references/keyshort-audit-and-update.md](./references/keyshort-audit-and-update.md) and run `audit` or `update` as specified there.
3. **New Keyshort page** (canonical `<Scope>/Keyshort/<Action>` with optional subscope) — follow command `.rulesync/commands/logseq-create-shortcut.md` (slash: `logseq-create-shortcut`); it owns naming, ancestry tags, grouped cards, and journal wording.
4. **New legacy flashcard on another namespaced page** (user gives `[[Page/Path/Title]]` and content but does not want a `/Card/` entity page) — read [references/create-flashcard-page.md](./references/create-flashcard-page.md), then implement: dedup → LFM page → parent ancestry for the right `{{cards [[...]] }}` root → `[[Card]]` + children → journal entry.
5. **Design or debug `{{cards …}}` / simple vs advanced queries** — read [references/cards-macro-and-query-language.md](./references/cards-macro-and-query-language.md) for how card lookup relates to Logseq’s **simple query** language, combinators, filter constraints, and when to use **advanced queries**.

## Always

- Rules: `logseq-flavored-markdown`, `logseq-page-naming-reference`, `logseq-link-hygiene`, `journal-updates` (link new pages under `[[Filed]]`, edits under `[[Updated]]`, default link-only).
- For new card work, use `[[Card]]` as the Logseq review marker and `logseq-entity:: [[Logseq/Entity/Card]]` for first-class card pages. Treat `#card` and `[[card]]` as legacy forms to preserve or migrate intentionally.
- Avoid `Question :: Answer` and “Flashcard Questions” sections on Keyshort pages.

## Reference index

- [references/card-entity-and-factor-out.md](./references/card-entity-and-factor-out.md) — first-class `/Card/` entity pages, `[[Logseq/Entity/Card]]`, `[[Card]]` marker, and page embed replacement.
- [references/keyshort-audit-and-update.md](./references/keyshort-audit-and-update.md) — discover Keyshort files, check ancestry, fix missing review markers, report (replaces ad-hoc runs of `logseq-manage-shortcut-flashcards`).
- [references/create-flashcard-page.md](./references/create-flashcard-page.md) — legacy general card page creation (vim-style nested Keyshort, dedup, SRS lines, journal).
- [references/cards-macro-and-query-language.md](./references/cards-macro-and-query-language.md) — `{{cards}}` vs `{{query}}`, simple-query operators, page vs block filter rules, advanced-query relationship, official doc links.

## Related commands

- `logseq-create-shortcut` — create/update Keyshort pages with review cards.
- `logseq-manage-shortcut-flashcards` — legacy command name; behavior lives in this skill’s Keyshort reference.
