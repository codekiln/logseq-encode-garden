---
name: logseq-flashcard-favorite
description: >-
  Generate and keep in sync the [[Logseq/Flashcard/Review/Favorite]] deck tree
  from the graph's :favorites (logseq/config.edn). Use when the user asks to
  build, refresh, or reconcile favorite-driven flashcard decks: an aggregate
  {{cards (or …)}} deck, a negated background {{cards (not (or …))}} deck, and
  one scoped {{cards [[Favorite]]}} subpage per favorite. Runs idempotently via
  the mise file task and preserves the review-history children Logseq appends to
  {{cards}} blocks. Do not use for ad-hoc card authoring (logseq-flashcard) or
  non-favorite decks.
targets: ["*"]
codexcli:
  short-description: Sync Logseq favorite flashcard decks from config.edn :favorites
---

# Logseq flashcard favorite decks

Reconciles the `Logseq/Flashcard/Review/Favorite` page tree with the graph's
`:favorites` (`logseq/config.edn`). The engine is the `nbb-logseq` ClojureScript
script `scripts/generate-favorite-decks.cljs`, run through a **mise file task**
(per `[[My/Pref/Dev/mise/Tasks]]` — file tasks + usageCLI). It does **not** touch
the hand-curated `[[Logseq/Flashcard/Review]]` page.

## Run it

~~~sh
# preview (default; writes nothing)
mise run logseq:flashcard-favorite
# apply
mise run logseq:flashcard-favorite --write
# apply and delete subpages for favorites removed from config
mise run logseq:flashcard-favorite --write --prune
~~~

If `nbb-logseq` is missing, the task self-declares it (`#MISE tools=…`); run
`mise install`, or `mise use -g npm:@logseq/nbb-logseq@latest` (see
`.rulesync/skills/logseq-link-hygiene/references/nbb-logseq.md`).

## What it produces

- Aggregate page `[[Logseq/Flashcard/Review/Favorite]]`: an **All Favorite
  Flashcards** deck `{{cards (or …)}}`, a collapsed **Background / Non-Favorite**
  deck `{{cards (not (or …))}}` (`query-properties:: [:block]`), and a **By
  Favorite** link list.
- One subpage per favorite, full namespace nested (e.g. `Lightroom/Classic` →
  `[[Logseq/Flashcard/Review/Favorite/Lightroom/Classic]]`), each with
  `{{cards [[Favorite]]}}`.
- Self-referential / meta favorites under `Logseq/Flashcard/*` are skipped.

## Idempotency contract (why re-runs are safe)

The script **merges**, never overwrites. It locates managed decks by their
`favorite-deck::` anchor property and rewrites only the `{{cards …}}` expression
when the favorite *set* drifts (whitespace/order/case-insensitive) — so the
`Summary / Remembered / Forgotten` children Logseq appends after a review are
preserved. A second `--write` run on an unchanged graph changes no files.

Full merge/template/anchor details: `references/algorithm.md`.

## Always

- Rules: `logseq-core` (LFM + naming; protected `tags::`), `logseq-link-hygiene`.
- After `--write`, add today's journal entries: new pages under `[[Filed]]`,
  refreshed pages under `[[Updated]]` (link-only; mutually exclusive).
- Stale subpages are reported by default and deleted only with `--prune` (this
  preserves SRS review history unless deletion is explicitly requested).
- For `{{cards}}` / simple-query semantics, defer to skill `logseq-flashcard`
  (`references/cards-macro-and-query-language.md`).

## Editing this skill

Edit only the `.rulesync/` source (this `SKILL.md`, `scripts/`, `references/`),
then run `npx rulesync generate` and commit source + generated outputs together.
The mise task at `mise-tasks/logseq/flashcard-favorite` points at the `.rulesync`
engine path; keep that path in sync if the script moves.
