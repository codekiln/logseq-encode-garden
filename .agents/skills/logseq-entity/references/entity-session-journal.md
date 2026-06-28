# Entity workflows and today’s journal (garden diff)

## When this applies

Whenever an agent **creates** a new file under `pages/` or **materially edits** an existing graph page while doing **logseq-entity** work—new or updated entity instances, prerequisite pages **when the active type page or registry requires them**, `Logseq/Entity/<Type>` or registry edits, imports that add `logseq-entity::` / `created-by::` / `alias::`, etc.—the task is **not finished** until today’s journal records those graph moves.

This is independent of whether the user asked for a journal note; it is **repo policy** when `[[Logseq/Journal]]` / rule **`logseq-core`** (journal updates) apply.

## Configuration order

1. If the graph defines **`[[Logseq/Journal]]`** and **`[[Logseq/Journal/Section/Garddiff]]`**, read them first for section labels, nesting, **Filed** vs **Updated** naming, and mutual-exclusivity rules.
2. Otherwise use Rulesync rule **`logseq-core`** (journal updates; when present in the workspace).

## What to write

- **`[[Filed]]`** (or the garden’s equivalent): **link-only** bullets for pages that **first appeared today** in the graph.
- **`[[Updated]]`** (or equivalent): **link-only** bullets for pages that **already existed** and were edited in this session.
- Each **`[[Page]]` at most once** across Filed vs Updated for that calendar day; if both created and edited same day, keep it under **Filed** only.
- Avoid repetitive boilerplate (`Created …`, `Imported …`) on those lines unless the garddiff page explicitly allows a single short child sentence.
- **Grouping (interactive):** When several entries cluster naturally, propose labels to the human and confirm before finalizing. Labels are plain-text (bare word or short phrase, not a `[[wikilink]]`), alphabetically sorted once confirmed.

## Placement

Merge into the existing **garddiff** / **Gard/Diff** (or equivalent) block for **`journals/YYYY_MM_DD.md`**; do not invent a parallel change log for the same day.

## Agent report

End-of-task summary should **confirm** which journal links were added (or state that no graph pages changed).

## Related

- rule: `logseq-core` — default journal-updates checklist when garddiff pages are missing.
- command: `logseq-format-journal` — load **`[[Logseq/Journal]]`** before editing `journals/*.md`.
