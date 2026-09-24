---
name: logseq-question
description: >-
  Log a research question in the Logseq garden under Topic/Q/..., deduplicate
  against existing ___Q___ pages, add today's journal link, and research an
  answer (with AI attribution). Use when the user invokes /logseq-question or
  asks to file, record, or capture a scoped question page. Do not use for non-Q
  pages, general notes, or entity types other than question—use skill
  logseq-entity and the relevant [[Logseq/Entity/<Type>]] page instead.
metadata:
  short-description: 'File a garden question under /Q/, journal it, and answer it'
---
# Logseq question

Capture a single answerable question in the graph, log it in today's journal, and research an answer.

**`[[Logseq/Entity/Question]]` is the format authority.** It defines the `/Q/` namespace pattern, the `___Q___` filename shape, how the topic namespace is chosen, the search order and the **existing** / **similar** / **new** / **blocked** outcomes, frontmatter, and the page shape including `## [[My Answer]]`, `## [[My Notes]]`, `## [[AI Answer]]`, and the card-backed variant. Follow it end to end; do not invent section titles or frontmatter keys from memory.

This skill adds the filing pass around it: journal bookkeeping and the research step. Shared entity behavior — configuration order and dedup mechanics — comes from skill **logseq-entity**.

## Procedure

1. Load `[[Logseq/Entity]]` and `[[Logseq/Entity/Question]]`. Fall back to `.rulesync/config/logseq-entity.md` only when those pages are missing or incomplete; if no question configuration can be found at all, stop and ask.
2. Deduplicate per the type page's **Finding and deduplicating** section, using the mechanics in [references/entity-search-and-dedup.md](../logseq-entity/references/entity-search-and-dedup.md).
   - **existing** — do not create a page. Log it in today's journal (under **`[[Updated]]`** if you edit that page, otherwise as a narrative line), tell the user the question is already in the garden, and stop.
   - **similar** — present the candidates and let the user choose before writing.
   - **blocked** — stop and ask.
3. **new** — create the page per `[[Logseq/Entity/Question]]`. LFM mechanics come from rule **logseq-core** (detail: skill **logseq-lfm**).
4. Append a link-only line under today's **`[[Filed]]`** list in `journals/YYYY_MM_DD.md`: `- [[Namespace/Q/Question text]]`. Follow **`[[Logseq/Journal]]`** and [references/entity-session-journal.md](../logseq-entity/references/entity-session-journal.md) for mutual exclusivity and section conventions.
5. Research the answer with the tools available — web search, official documentation, MCP servers, existing graph pages — and write it into the page per the type page. Pages you create while researching go under **`[[Filed]]`**; pages you edit go under **`[[Updated]]`**.
6. Leave older `___Q___` pages alone unless the user asks for a migration.

## Report

- **Duplicate** — the existing page link and the journal line added for today.
- **New page** — the page path and link, its **`[[Filed]]`** placement, and a summary of the answer or a note that the question is still open.

## Reference guide

- Type page: `[[Logseq/Entity/Question]]` — the entity definition for question entities
- skill: `logseq-entity` — configuration order, dedup, Filed / Updated after graph edits
- rule: `logseq-core` — LFM, `___` file naming, `/` link format, journal updates
