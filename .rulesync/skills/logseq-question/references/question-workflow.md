# Question workflow (full procedure)

Authoritative step-by-step for logging a research question in this garden. The **logseq-question** skill centers on this file; **question** entity semantics and shared dedup rules live in skill **logseq-entity** and on **`[[Logseq/Entity/question]]`** (`pages/Logseq___Entity___question.md`).

## Variables

- **Question text** – **Required**: The question as phrased (e.g., "Is it possible to see the compaction text?"). Used for the page title and for deduplication.
- **Topic/namespace** – **Optional**: The domain or tool the question is about (e.g., `Claude Code`, `git`, `LangSmith`, `EdTech/Idea/LearnMark`). If not provided, infer from the question text or ask the user.

## Conventions (from existing question pages)

- **Namespace pattern**: Questions live under a topic namespace, then `/Q/`, then the question text.
  - Link format: `[[Namespace/Q/Question text]]` or `[[Namespace/SubNamespace/Q/Question text]]`
  - File format: `Namespace___Q___Question text.md` (triple underscores; special characters like `?` become `%3F` in filenames)
- **Page content**: Logseq Flavored Markdown (LFM). H1 is the question (often with linked terms). Optional sections: `## Answer`, `## My Notes`. Prefer frontmatter **`see-also::`** for **garden pages** that are “see also” reading—**strongest tie first**—instead of a `## Related` section that only lists internal links. Do **not** use **`see-also::`** to restate **parent namespace** context the title already encodes (see `[[Logseq/Entity]]` and `[[Logseq/Entity/question]]`). Use optional **`via::`** only for **what prompted filing** the page (journal/import/session), not for general related pages.
- **Journal**: Today's journal gets a bullet with the page link: `- [[Namespace/Q/Question text]]`
- **Frontmatter**: Do not add or remove `tags::` on existing pages. On **new** pages, include `logseq-entity:: [[Logseq/Entity/question]]` so the entity type page indexes instances. Optional **`see-also::`** and **`via::`** as above. Other frontmatter (`tags::`, `alias::`) should match patterns on sibling question pages in that namespace when available; do not invent new tag schemes.

## Workflow

### Step 0: Load question entity configuration

- In order, read and apply:
  - `[[Logseq/Entity]]` (registry)
  - `[[Logseq/Entity/question]]` (type SOP for question entities)
  - If either is missing or insufficient, fall back to `.rulesync/config/logseq-entity.md` (section **question**)
- For **deduplication mechanics** and classification outcomes, use skill **logseq-entity**: [entity-search-and-dedup.md](../../logseq-entity/references/entity-search-and-dedup.md) together with the question type rules below.
- If no question-type configuration can be found and conventions cannot be inferred safely, stop and ask the user how to proceed (same spirit as the logseq-entity skill when config is absent).

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
  - Add an entry to **today's journal** (`journals/YYYY_MM_DD.md`) with a link to the existing page, e.g. `- [[Namespace/Q/Existing question text]]`
  - Tell the user the question was already in the garden and that the journal was updated.
  - Stop.
- **If results are ambiguous (similar):** follow the skill reference: present candidates and prefer human judgment before creating a duplicate.
- **Blocked:** if topic namespace or configuration prerequisites are unclear, stop and ask.

### Step 3: Create the question page (new question only)

- **File name**: `pages/Namespace___Q___Question text.md`
  - Use triple underscores for namespace segments. Replace `?` with `%3F` (or equivalent) in the filename if the question contains it.
- **Frontmatter** (new pages only, before the first bullet):
  - Required: `logseq-entity:: [[Logseq/Entity/question]]`
  - Optional: `see-also:: [[Page1]], [[Page2]], ...` (internal **see also** links, **strongest tie first**, no parent-namespace-only entries)
  - Optional: `via:: [[Page1]], ...` only when recording **what put this in the garden** (e.g. today’s journal as provenance is usually enough; use `via::` for a specific stub or source page when that is clearer)
  - Optional: `tags::`, `alias::`, and other keys only when they match established patterns for question pages in this namespace. Never alter **`tags::`** on files that already exist.
  - Place page attributes first (if `tags::` is used, keep project frontmatter order expectations).
- **Content** (LFM):
  - All content as bullets; no blank lines between bullets.
  - H1: the question, with key terms linked to existing pages where appropriate (e.g., `- # Is it possible to see the compaction text in [[Claude Code]]?`).
  - Optionally add placeholder sections: `- ## Answer`, `- ## My Notes` (empty or with a single placeholder bullet). Do not add `## Related` solely for internal page links—use **`see-also::`** instead.
- Follow the logseq-page-naming-reference and logseq-flavored-markdown rules.
- **Non-goal:** Do not bulk-edit older `___Q___` pages to add `logseq-entity::` unless the user explicitly asks (migration is optional).

### Step 4: Add today's journal entry

- Open today's journal file: `journals/YYYY_MM_DD.md`.
- Add a bullet linking to the new question page using forward slashes: `- [[Namespace/Q/Question text]]`
- Place the entry in an appropriate position in the journal (e.g., with other question or topic entries).

### Step 5: Research and answer the question

- After creating the page and journal entry, attempt to answer the question.
- Use available tools (web search, documentation, MCP servers, existing knowledge graph pages) to research the answer.
- Update the `## Answer` section of the newly created question page with the findings.
- **Attribution**: Place the answer under an `[[AI/Response]]` node to attribute it as AI-generated. Example:
  ~~~markdown
  - ## Answer
  	- [[AI/Response]]
  		- The answer content goes here...
  		- [Source](https://example.com)
  ~~~
- **Cite sources**: Put **external** documentation or web URLs in the Answer (markdown links). When the answer points to other **garden pages** as further reading, add or update **`see-also::`** (**strongest tie first**), not a tail `## Related` list. Use **`via::`** only for provenance of **filing**, not for “see also” links.
- Keep the answer concise but informative; use bullet points and proper LFM formatting.
- If the answer cannot be determined or requires user input, note this in the Answer section and inform the user.

## Report

- **If duplicate found**: Report the existing page link and confirm the journal entry was added for today.
- **If new page created**: Report the new page path and link, confirm the journal entry was added, and summarize the answer (or note if the question remains unanswered).

## Related

Use the prefix that matches the type: `rule:` for rules, `command:` for commands, `skill:` for skills.

- skill: `logseq-entity` – Configuration-first entity workflow; shared dedup and config contract
- Type page: `[[Logseq/Entity/question]]` – Canonical SOP for question entities in the graph
- skill: `logseq-question` – This workflow (garden filing + journal + answer pass)
- command: `logseq-question` – Rulesync slash entrypoint; defers to this reference
- rule: `logseq-page-naming-reference` – File naming (`___`), link format (`/`), creating new pages
- rule: `logseq-journal-updates` – Always add a journal entry when creating or updating pages
- rule: `logseq-flavored-markdown` – Bullet structure, headings, LFM syntax
