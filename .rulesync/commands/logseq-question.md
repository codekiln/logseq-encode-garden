---
targets:
  - '*'
description: Log a question in the knowledge garden under a logical namespace and record it in today's journal, avoiding duplicates
argument-hint: Question text (required); optional topic/namespace (e.g., Claude Code, git, LangSmith)
---
# Log a Question in the Knowledge Garden

This command records a question in a logical place in the Logseq knowledge garden and documents that the question was asked in today's journal. It follows existing question-page patterns and attempts to avoid duplicate question pages.

## Variables

- **Question text** – **Required**: The question as phrased (e.g., "Is it possible to see the compaction text?"). Used for the page title and for deduplication.
- **Topic/namespace** – **Optional**: The domain or tool the question is about (e.g., `Claude Code`, `git`, `LangSmith`, `EdTech/Idea/LearnMark`). If not provided, infer from the question text or ask the user.

## Conventions (from existing question pages)

- **Namespace pattern**: Questions live under a topic namespace, then `/Q/`, then the question text.
  - Link format: `[[Namespace/Q/Question text]]` or `[[Namespace/SubNamespace/Q/Question text]]`
  - File format: `Namespace___Q___Question text.md` (triple underscores; special characters like `?` become `%3F` in filenames)
- **Page content**: Logseq Flavored Markdown (LFM). H1 is the question (often with linked terms). Optional sections: `## Answer`, `## My Notes`, `## Related`.
- **Journal**: Today's journal gets a bullet with the page link: `- [[Namespace/Q/Question text]]`
- **Frontmatter**: Do not add or remove `tags::` on existing pages. When creating a new page, do not invent new tags; follow patterns only if the user has specified tag conventions for question pages.

## Workflow

### Step 1: Normalize and clarify inputs

- Treat the user's input as the question text. Strip or normalize trailing punctuation (e.g., `?`) for search only; keep the canonical form for the page title.
- If topic/namespace was not given, infer a plausible namespace from the question (e.g., "compaction text in Claude Code" → `Claude Code`) or ask the user.

### Step 2: Search for existing question pages (deduplication)

- Search for pages that may already represent the same question:
  - Grep for the question text (normalized, key phrases) in `pages/**___Q___*.md`
  - Search by namespace + "Q" (e.g., `Claude Code___Q___*`, `git___Q___*`)
  - Check page titles and first-level headings; consider rephrasings and minor wording differences
- **If a matching or near-duplicate question page exists:**
  - Do **not** create a new page.
  - Add an entry to **today's journal** (`journals/YYYY_MM_DD.md`) with a link to the existing page, e.g. `- [[Namespace/Q/Existing question text]]`
  - Tell the user the question was already in the garden and that the journal was updated.
  - Stop.

### Step 3: Create the question page (new question only)

- **File name**: `pages/Namespace___Q___Question text.md`
  - Use triple underscores for namespace segments. Replace `?` with `%3F` (or equivalent) in the filename if the question contains it.
- **Content** (LFM):
  - All content as bullets; no blank lines between bullets.
  - H1: the question, with key terms linked to existing pages where appropriate (e.g., `- # Is it possible to see the compaction text in [[Claude Code]]?`).
  - Optionally add placeholder sections: `- ## Answer`, `- ## My Notes`, `- ## Related` (empty or with a single placeholder bullet).
- Follow the logseq-page-naming-reference and logseq-flavored-markdown rules. Do not add or remove `tags::` unless the user has specified tag conventions for new question pages.

### Step 4: Add today's journal entry

- Open today's journal file: `journals/YYYY_MM_DD.md`.
- Add a bullet linking to the new question page using forward slashes: `- [[Namespace/Q/Question text]]`
- Place the entry in an appropriate position in the journal (e.g., with other question or topic entries).

## Report

- **If duplicate found**: Report the existing page link and confirm the journal entry was added for today.
- **If new page created**: Report the new page path and link, and confirm the journal entry was added for today.

## Related

Use the prefix that matches the type: `rule:` for rules, `command:` for commands, `skill:` for skills.

- rule: `logseq-page-naming-reference` – File naming (`___`), link format (`/`), creating new pages
- rule: `logseq-journal-updates` – Always add a journal entry when creating or updating pages
- rule: `logseq-flavored-markdown` – Bullet structure, headings, LFM syntax
