# Question workflow (full procedure)

Authoritative step-by-step for logging a research question in this garden. The **logseq-question** skill centers on this file; **question** entity semantics and shared dedup rules live in skill **logseq-entity** and on **`[[Logseq/Entity/Question]]`** (`pages/Logseq___Entity___question.md`).

## Variables

- **Question text** – **Required**: The question as phrased (e.g., "Is it possible to see the compaction text?"). Used for the page title and for deduplication.
- **Topic/namespace** – **Optional**: The domain or tool the question is about (e.g., `Claude Code`, `git`, `LangSmith`, `EdTech/Idea/LearnMark`). If not provided, infer from the question text or ask the user.

## Conventions (question filing only)

This file defines **namespace, dedup, journal, and research** steps. It does **not** define question page body shape, section headings, or frontmatter keys—those come from **`[[Logseq/Entity/Question]]`** (read in Step 0 before Steps 3 and 5).

- **Namespace pattern**: Questions live under a topic namespace, then `/Q/`, then the question text.
  - Link format: `[[Namespace/Q/Question text]]` or `[[Namespace/SubNamespace/Q/Question text]]`
  - File format: `Namespace___Q___Question text.md` (triple underscores; special characters like `?` become `%3F` in filenames)
- **Journal**: Record the filing in **`journals/YYYY_MM_DD.md`**. When **`[[Logseq/Journal/Section/Garddiff]]`** (or your day’s **Gard/Diff** block) defines **`[[Filed]]`** / **`[[Updated]]`**, put **new** question pages under **`[[Filed]]`** as a link-only line: `- [[Namespace/Q/Question text]]`. If the day file has **no** garddiff block, add the same link where topical bullets live. Follow rule **`logseq-core`** (journal updates) and skill **logseq-entity** → [entity-session-journal.md](../../logseq-entity/references/entity-session-journal.md) for mutual exclusivity and “no boilerplate” rules.

## Workflow

### Step 0: Load question entity configuration

- In order, read and apply:
  - `[[Logseq/Entity]]` (registry)
  - `[[Logseq/Entity/Question]]` (`pages/Logseq___Entity___question.md`) — **authoritative for page shape, frontmatter, section headings, and AI attribution**
  - If either is missing or insufficient, fall back to `.rulesync/config/logseq-entity.md` for shared fallback text (resolution order, reporting)—per-type rules still belong on `[[Logseq/Entity/Question]]` once you create it
- From the type page, apply at minimum:
  - **Frontmatter** (required `logseq-entity::`, optional keys, `tags::` discipline)
  - **Page shape (canonical)** — H1, section order, which sections to omit when empty, `[[AI/Response]]` placement, and “do not use `## Related` for internal links”
  - **Legacy instances** — how to treat older pages that differ from canonical shape (do not bulk-migrate unless asked)
- For **deduplication mechanics** and classification outcomes, use skill **logseq-entity**: [entity-search-and-dedup.md](../../logseq-entity/references/entity-search-and-dedup.md) together with the **Finding and deduplicating** section on the type page.
- If no question-type configuration can be found and conventions cannot be inferred safely, stop and ask the user how to proceed (same spirit as the logseq-entity skill when config is absent).
- **Do not** invent section titles or frontmatter keys from this workflow file or from memory when the type page is available.

### Step 1: Normalize and clarify inputs

- Treat the user's input as the question text. Strip or normalize trailing punctuation (e.g., `?`) for search only; keep the canonical form for the page title.
- If topic/namespace was not given, infer a plausible namespace from the question (e.g., "compaction text in Claude Code" → `Claude Code`) or ask the user.

### Step 2: Search for existing question pages (deduplication)

- Treat the incoming question as a **question** entity candidate. Apply the dedup process in `.rulesync/skills/logseq-entity/references/entity-search-and-dedup.md` together with the question type rules (search order, classify **existing** / **similar** / **new** / **blocked**).
- Practical search (align with that reference):
  - Grep for the question text (normalized, key phrases) in `pages/**___Q___*.md`
  - Search by namespace + `Q` (e.g., `Claude Code___Q___*`, `git___Q___*`)
  - Check page titles and first-level headings; consider rephrasings and minor wording differences
- **If a matching or near-duplicate question page exists (existing):**
  - Do **not** create a new page.
  - Add a **narrative** journal note **outside** the garddiff **`[[Filed]]` / `[[Updated]]`** link lists when those lists are reserved for **`pages/`** graph edits only; link `- [[Namespace/Q/Existing question text]]`. **Unless** you also **edited** that question page—then log that page under **`[[Updated]]`** per **`[[Logseq/Journal/Section/Garddiff]]`** / rule **`logseq-core`** (journal updates).
  - Tell the user the question was already in the garden and that the journal was updated.
  - Stop.
- **If results are ambiguous (similar):** follow the skill reference: present candidates and prefer human judgment before creating a duplicate.
- **Blocked:** if topic namespace or configuration prerequisites are unclear, stop and ask.

### Step 3: Create the question page (new question only)

- **File name**: `pages/Namespace___Q___Question text.md`
  - Use triple underscores for namespace segments. Replace `?` with `%3F` (or equivalent) in the filename if the question contains it.
- **Frontmatter and body**: Implement **`[[Logseq/Entity/Question]]`** → **Frontmatter** and **Page shape (canonical)** from Step 0. For `tags::` / `alias::` on new pages, match sibling question pages in the same namespace when the type page allows it.
- **LFM mechanics** (not section names): rule **logseq-core** — bullets, tab indentation, no blank lines between bullets (advanced detail: skill **logseq-lfm**); rule **logseq-core** for links vs filenames (detail: skill **logseq-lfm**).
- **Non-goal:** Do not bulk-edit older `___Q___` pages unless the user explicitly asks (see **Legacy instances** on the type page).

### Step 4: Add today's journal entry (garddiff + narrative)

- Open today's journal file: `journals/YYYY_MM_DD.md`.
- **New question page (after Step 3):** Under the day’s **garddiff** / **Gard/Diff** block, append a **link-only** line under **`[[Filed]]`**: `- [[Namespace/Q/Question text]]` (forward slashes in the link). That page is **new in `pages/`** today—this satisfies rule **`logseq-core`** (journal updates) without duplicating the same link under **`[[Updated]]`**.
- **Optional narrative:** If your journal style uses a topical block (questions, friction, etc.), you may add a short child or sibling bullet for context—keep it one sentence max per **`[[Logseq/Journal/Section/Garddiff]]`** optional-context rules.
- **While answering (Step 5):** If you **edit** other existing **`pages/**/*.md`** files, add each under **`[[Updated]]`** (link-only). New files created during research → **`[[Filed]]`**. Never list the same **`[[Page]]`** under both **Filed** and **Updated** the same day.
- If the graph has **no** garddiff convention yet, fall back to a single topical bullet with `- [[Namespace/Q/Question text]]` and still follow rule **`logseq-core`** (journal updates).

### Step 5: Research and answer the question

- After creating the page and journal entry, attempt to answer the question.
- Use available tools (web search, documentation, MCP servers, existing knowledge graph pages) to research the answer.
- Add findings under the **AI answer section** defined on **`[[Logseq/Entity/Question]]`** → **Page shape (canonical)** (section heading, `[[AI/Response]]` child, and any “Short answer” / formatting bullets there). Do not assume legacy section titles on older `___Q___` pages unless you are editing one of those pages as-is.
- **Cite sources** per the type page: external URLs in the answer body; garden “see also” pages in **`see-also::`** when the type page says so—not a tail `## Related` list.
- Keep the answer concise but informative; use bullet points and LFM per rule **logseq-core** (advanced detail: skill **logseq-lfm**; including *Bold and inline code* in answer bodies).
- If the answer cannot be determined or requires user input, note that in the appropriate section per the type page and inform the user.

## Report

- **If duplicate found**: Report the existing page link and confirm the journal entry was added for today (narrative or **`[[Updated]]`** per Step 2).
- **If new page created**: Report the new page path and link, confirm **`[[Filed]]`** / garddiff (or fallback journal) per Step 4, and summarize the answer (or note if the question remains unanswered).

## Related

Use the prefix that matches the type: `rule:` for rules, `command:` for commands, `skill:` for skills.

- skill: `logseq-entity` – Configuration-first entity workflow; shared dedup and config contract
- Type page: `[[Logseq/Entity/Question]]` – Canonical entity definition for question entities in the graph
- skill: `logseq-question` – This workflow (garden filing + journal + answer pass)
- command: `logseq-question` – Rulesync slash entrypoint; defers to this reference
- rule: `logseq-core` – File naming (`___`), link format (`/`), creating new pages (detail: skill `logseq-lfm`)
- rule: `logseq-core` – Always add a journal entry when creating or updating pages (journal updates)
- rule: `logseq-core` – Bullet structure, headings, LFM syntax (advanced detail: skill `logseq-lfm`)
