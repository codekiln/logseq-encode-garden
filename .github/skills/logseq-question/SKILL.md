---
name: logseq-question
description: >-
  Log a research question in the Logseq garden under Topic/Q/..., deduplicate
  against existing ___Q___ pages, add today's journal link, and research an
  answer (with AI attribution). Use when the user invokes /logseq-question or
  asks to file, record, or capture a scoped question page. Do not use for non-Q
  pages, general notes, or entity types other than question—use skill
  logseq-entity and the relevant [[Logseq/Entity/<Type>]] page instead.
---
# Logseq question

Capture a single answerable question in the graph under the **`/Q/`** namespace, log it in today's journal, and research an answer.

## Read this first

**[[Logseq/Entity/Question]]** (`pages/Logseq___Entity___Question.md`) is the sole authority for question pages: the `/Q/` naming and `___Q___` file mapping, dedup search order, frontmatter, section order and the `[[AI Answer]]` shape, how to pick a topic namespace, how to answer, and how legacy pages differ. Read it before filing anything; this skill does not restate it.

A question is one **entity type**, so the shared machinery is the **logseq-entity** skill's, not this one's:

- **Dedup mechanics** and the *existing / similar / new / blocked* outcomes → [entity-search-and-dedup.md](../logseq-entity/references/entity-search-and-dedup.md)
- **Config resolution order** when graph pages are missing → [configuration-contract.md](../logseq-entity/references/configuration-contract.md)
- **`[[Filed]]` / `[[Updated]]` closeout** on today's journal → [entity-session-journal.md](../logseq-entity/references/entity-session-journal.md) and [[Logseq/Journal]]

## Procedure

1. Read `[[Logseq/Entity]]`, then `[[Logseq/Entity/Question]]`. Fall back to `.rulesync/config/logseq-entity.md` only if a graph page is missing.
2. Settle the question text and its topic namespace per the type page's **Creating an instance**.
3. Dedup with the logseq-entity references above plus the type page's **Finding and deduplicating**. An **existing** match stops the run — say so and journal it rather than filing a second page; **similar** or **blocked** stops for human judgment.
4. Create the page in the shape the type page gives, and record it under `[[Filed]]`.
5. Research and write the answer per the type page's **Answering an instance**. Pages edited along the way go under `[[Updated]]`; never list one page under both the same day.
6. Report the page link, its journal placement, and the answer — or say plainly that the question is still open.

## Progressive disclosure

- **[[Logseq/Entity/Question]]** — what a question page is: naming, dedup, frontmatter, shape, answering.
- **This file** — when to reach for it, and the order of the pass.
- **skill logseq-entity** — dedup, config contract, journal closeout shared by every entity type.
- Answer body LFM: rule **logseq-core** → *Bold and inline code (monospace)* (advanced detail: skill **logseq-lfm**).
