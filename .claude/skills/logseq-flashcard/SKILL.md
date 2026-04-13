---
name: logseq-flashcard
description: >-
  Create or maintain Logseq SRS flashcards using #card blocks in this garden.
  Use when the user asks to add a flashcard, file a card, audit or fix Keyshort
  flashcards, ensure {{cards}} queries pick up cards, design or debug simple or
  advanced query expressions for card decks, or convert shortcut notes into
  #card format. Covers namespaced pages beyond Keyshort (e.g.
  vim/Keyshort/Inspect/...) as well as Scope/Keyshort/Action pages. Do not use
  for non-Logseq decks (e.g. repeater-only formats).
---
# Logseq flashcard

## Choose a path

1. **Audit or repair Keyshort pages** (`*___Keyshort___*.md`) — read [references/keyshort-audit-and-update.md](./references/keyshort-audit-and-update.md) and run `audit` or `update` as specified there.
2. **New Keyshort page** (canonical `<Scope>/Keyshort/<Action>` with optional subscope) — follow command `.rulesync/commands/logseq-create-shortcut.md` (slash: `logseq-create-shortcut`); it owns naming, ancestry tags, grouped cards, and journal wording.
3. **New flashcard on another namespaced page** (user gives `[[Page/Path/Title]]` and content) — read [references/create-flashcard-page.md](./references/create-flashcard-page.md), then implement: dedup → LFM page → parent ancestry for the right `{{cards [[...]] }}` root → `#card` + children → journal entry.
4. **Design or debug `{{cards …}}` / simple vs advanced queries** — read [references/cards-macro-and-query-language.md](./references/cards-macro-and-query-language.md) for how card lookup relates to Logseq’s **simple query** language, combinators, filter constraints, and when to use **advanced queries**.

## Always

- Rules: `logseq-flavored-markdown`, `logseq-page-naming-reference`, `journal-updates` (link new pages under `[[Filed]]`, edits under `[[Updated]]`, default link-only).
- Use `#card` only; avoid `Question :: Answer` and “Flashcard Questions” sections on Keyshort pages.

## Reference index

- [references/keyshort-audit-and-update.md](./references/keyshort-audit-and-update.md) — discover Keyshort files, check ancestry, fix missing `#card`, report (replaces ad-hoc runs of `logseq-manage-shortcut-flashcards`).
- [references/create-flashcard-page.md](./references/create-flashcard-page.md) — general `#card` page creation (vim-style nested Keyshort, dedup, SRS lines, journal).
- [references/cards-macro-and-query-language.md](./references/cards-macro-and-query-language.md) — `{{cards}}` vs `{{query}}`, simple-query operators, page vs block filter rules, advanced-query relationship, official doc links.

## Related commands

- `logseq-create-shortcut` — create/update Keyshort pages with `#card`.
- `logseq-manage-shortcut-flashcards` — legacy command name; behavior lives in this skill’s Keyshort reference.
