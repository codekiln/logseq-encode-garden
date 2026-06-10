# Favorite-deck generation algorithm

Engine: `scripts/generate-favorite-decks.cljs` (run via `nbb-logseq` from the
graph root). The mise task `mise-tasks/logseq/flashcard-favorite` forwards
`--write` / `--prune` and `cd`s to `MISE_PROJECT_ROOT`.

## Pipeline

1. **Read favorites** — regex-extract the single-line `:favorites [ … ]` vector
   from `logseq/config.edn` (plain quoted strings, order preserved). No full EDN
   parse, so unrelated config syntax can't break it.
2. **Canonicalize casing** — build `normalized → {casing → frequency}` from every
   `[[link]]` across `pages/` + `journals/`, then map each favorite to its most
   frequent real casing (`zoxide` → `Zoxide`, `devcontainer` → `DevContainer`).
   Falls back to the config string when no link exists. (Logseq refs are
   case-insensitive, so this is for readability, not correctness.)
3. **Filter meta** — drop favorites whose canonical title starts with
   `Logseq/Flashcard` (e.g. the self-referential `logseq/flashcard/review`).
4. **Reconcile** the aggregate page, each subpage, and stale subpages (below).

## Anchors

Managed `{{cards}}` blocks carry a `favorite-deck::` property used to find them
on re-runs:

- aggregate positive deck → `favorite-deck:: aggregate`
- negated background deck → `favorite-deck:: background`
- per-favorite subpage deck → `favorite-deck:: [[Favorite]]`

`macro-line-idx` finds the property line, then walks upward to the nearest
`{{cards` line. Subpages fall back to the first `{{cards}}` line if the anchor
property is absent (e.g. hand-created pages).

## Drift comparison (`expr-sig`)

A cards expression is reduced to `[negated? #{normalized-links}]`. Comparison is
therefore insensitive to whitespace, link order, and casing — the cosmetic edits
Logseq makes (`( or` vs `(or`, trailing spaces) never trigger a rewrite. Only a
real change to the favorite *set* (or negation) rewrites the macro line, via
`replace-macro` (`\{\{cards…\}\}` on that single line). All other lines —
including `Summary / Remembered / Forgotten` review-history children and block
properties — are left byte-for-byte intact.

## Page templates (used only on *create*)

Aggregate `pages/Logseq___Flashcard___Review___Favorite.md`:

~~~
- # Favorite Flashcards
	- foregrounds flashcard scopes for my [[Logseq/Favorite]]s ([[Logseq/Queries]]).
	- ## All Favorite Flashcards
		- {{cards (or [[mise]] [[Lightroom/Classic]] …) }}
		  favorite-deck:: aggregate
	- ## Background / Non-Favorite
	  collapsed:: true
		- {{cards (not (or [[mise]] [[Lightroom/Classic]] …)) }}
		  favorite-deck:: background
		  query-properties:: [:block]
	- ## By Favorite
		- [[Logseq/Flashcard/Review/Favorite/mise]]
		- …
~~~

Subpage `pages/Logseq___Flashcard___Review___Favorite___vim.md`:

~~~
- # Favorite Flashcards: [[vim]]
	- {{cards [[vim]] }}
	  favorite-deck:: [[vim]]
~~~

Namespaced favorites nest the full path: `Lightroom/Classic` →
`Logseq/Flashcard/Review/Favorite/Lightroom/Classic` →
`Logseq___Flashcard___Review___Favorite___Lightroom___Classic.md`.

## By-Favorite list

`ensure-by-favorite` finds the `## By Favorite` heading, scans its section until
the next `#`/`##` heading, and **appends** a link for any favorite not already
present (matched by normalized page name). It never reorders or removes existing
links.

## Stale handling

Files matching `pages/Logseq___Flashcard___Review___Favorite___*.md` whose
favorite is no longer in `:favorites` are reported as `[stale]`. With `--prune`
(and `--write`) they are deleted; otherwise they are kept so SRS review history
is never silently lost. The aggregate page itself (no `___` suffix) is never
treated as stale.

## Modes

- default: **dry-run** — prints a `create / update / unchanged / stale / skip`
  report; writes nothing.
- `--write`: applies creates and in-place macro/link refreshes.
- `--prune`: with `--write`, deletes stale subpages.
