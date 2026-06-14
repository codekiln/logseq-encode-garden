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

Use this skill when the user wants to **capture a single answerable question** in the knowledge graph using the **`/Q/`** namespace pattern, **log it in today’s journal**, and **research an answer** using the page shape on **`[[Logseq/Entity/Question]]`**.

## Relationship to logseq-entity

A **question** is one **entity type** in this garden. Shared rules apply:

- **Entity definition:** `[[Logseq/Entity/Question]]` (`pages/Logseq___Entity___question.md`).
- **Registry and shared fallback:** `[[Logseq/Entity]]`, then `.rulesync/config/logseq-entity.md` only when graph pages are missing or insufficient (that file is short graph-first fallback text, not per-type sections).
- **Search, dedup, and “existing / similar / new / blocked”:** skill **logseq-entity** — read [references/configuration-contract.md](../logseq-entity/references/configuration-contract.md) and [references/entity-search-and-dedup.md](../logseq-entity/references/entity-search-and-dedup.md) when executing dedup (Step 2 of the workflow).

This skill adds **question-specific** filing steps: namespace/`___Q___` naming, journal bullet, and the research pass. Do not duplicate the entity-type definition; treat **`[[Logseq/Entity/Question]]`** as authoritative for **frontmatter, section headings, page shape, and AI attribution**.

For **non-question** entity work (other types per `[[Logseq/Entity]]`, registry edits, etc.), skill **logseq-entity** owns **garddiff** closeout (**Filed** / **Updated** on today’s journal). Follow that skill’s **Graph edits and today’s journal** section and [references/entity-session-journal.md](../logseq-entity/references/entity-session-journal.md)—journal discipline is **not** exclusive to this question skill.

## Procedure

1. Load type configuration (Step 0): `[[Logseq/Entity]]`, `[[Logseq/Entity/Question]]`, then `.rulesync/config/logseq-entity.md` if needed.
2. Open and follow **[references/question-workflow.md](./references/question-workflow.md)** from top to bottom (variables → conventions → Steps 1–5 → report).

## Progressive disclosure

- **This file** — when to use the skill and how it relates to **logseq-entity** / **`[[Logseq/Entity/Question]]`**.
- **[references/question-workflow.md](./references/question-workflow.md)** — full variables, conventions, numbered steps, reporting, and related rules/commands.
- Answer body LFM (formatting only, not section names): rule **logseq-core** → *Bold and inline code (monospace)* (advanced detail: skill **logseq-lfm**).

## Reference guide

- Full workflow: [references/question-workflow.md](./references/question-workflow.md)
- Entity dedup: [references/entity-search-and-dedup.md](../logseq-entity/references/entity-search-and-dedup.md)
- Entity config contract: [references/configuration-contract.md](../logseq-entity/references/configuration-contract.md)
- Entity sessions and garddiff: [references/entity-session-journal.md](../logseq-entity/references/entity-session-journal.md)
