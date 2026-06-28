---
root: false
targets:
  - '*'
description: 'Always-on Logseq guardrails for every page/journal edit (protected tags, LFM basics, naming, no-agent-taint, journal updates, block-ref safety)'
globs: ['{journals,pages}/**/*.md']
---
# Logseq core guardrails

These guardrails apply to every edit of a page or journal in this garden. Deeper how-to detail lives in skills (see the Skills index in the `overview` rule); load those when a task calls for them. This file itself is plain Markdown, not LFM.

## Protected `tags::` (most important)

- **NEVER modify, add, or remove the `tags::` frontmatter** in any document. The user has a specific tagging system; changing it disrupts their categorization.
- Preserve existing frontmatter tags exactly. Even if a tag looks missing or wrong, do not touch it.
- This applies ONLY to the `tags::` item — not to inline `#tags` in the body, and not to other page-level attributes (those may change when explicitly instructed).

## LFM basics

- Every line is prefixed with a bullet (`-`), including headings: `- # Heading Text`.
- TAB indentation determines parent/child nesting. Headings nest: H2 under H1, H3 under H2, etc.
- No blank lines anywhere — every line has content, at minimum a `-`.
- No ordered lists; use numbers inside unordered items: `- 1. First item` (TAB-indent before the `-`).
- Code blocks use `~~~` fences, nested inside a bullet. When a code block sits inside an outer ``` ``` ``` example, use `~~~` for the inner block.

<CORRECT_✅>
~~~markdown
- # Main Topic
  - ## Overview
    - ### Basic Idea
      - Sub-detail A
- # Next Topic
  - First point
~~~
</CORRECT_✅>

## Frontmatter shape

- Page-level attributes (Logseq frontmatter) MUST be the first lines of the file, before any unordered list item.
- Use kebab-case keys; separate key and value with `:: ` (e.g. `tags:: [[Q]], [[nvm]]`, `other-attr:: value`).
- `date-created::` records when the **entity** (post, book, software, video, event) was created/published — not when the page was added to the garden. Do not use the import date when the real date is known.

## Namespaces and naming

- Links use `/`: `[[Project/Tasks]]`. On disk that is `Project___Tasks.md` (triple underscore). Never create real folders for namespaces; never use `___` inside a `[[link]]`.
- Page names are **singular**; plural or contextual forms belong in `alias::`, not in the page name (`[[Project]]` + `alias:: [[Projects]]`, not `[[Projects]]`). Do not add `alias::` values speculatively — aliases are human-curated. If an alias seems useful, suggest it in the chat response; do not write it to the page without explicit instruction.
- Do not invent namespaces or link to pages that don't already exist (use the `logseq-link-hygiene` skill if unsure).
- Do not link a page to itself (no `[[This Page]]` in its own body).

## No agent taint

Do not copy AI-agent rationale, the user's request/instructions, task constraints, or process commentary into graph pages unless the user explicitly asks to record it as knowledge-garden content. Before writing a prose block, ask: would a human still write this on the page later, without the AI task context? Operational caveats ("I preserved tags", "I used an iframe", "I could not run the checker") go in the chat response, not the page.

Before finishing a graph edit, scan added lines for high-risk agent-taint signs and remove process commentary: *intentionally*, *because the user asked*, *I*, *we*, *this edit*, *snapshot*, *agent*, *instruction*, *request*. (Not always wrong, but always worth a second look.)

## Journal updates (record graph edits)

When creating or modifying graph pages, record the change in today's journal (`journals/YYYY_MM_DD.md`). Follow `[[Logseq/Journal]]` for the format — `[[Filed]]` / `[[Updated]]`, grouping, mutual exclusivity, link-only style, and section conventions all live there.

## Block-reference safety

- Never wrap a live `((uuid))` block ref or a `[[Page]]` link in backticks — that renders it as literal text. Reserve backticks for code tokens and for abstract path shapes (e.g. `Person/Name/GitHub/Project`).
- Keep an `id::` line attached to its block when moving/copying (refs resolve graph-wide). Before removing an `id::`, grep the graph for `((that-uuid))`; preserve it if any refs exist. (Full procedures: `logseq-block-ids` skill.)

## Logical vs on-disk pages

Absence of a `.md` file does **not** mean the page is absent — a `[[Namespace/Page]]` referenced anywhere exists as a logical page. To check existence, `grep -r "Namespace/Page" pages/ journals/`, don't just `ls` the file. Linking `[[Namespace/Page]]` is complete on its own; only create a `.md` file when you have real content for it.
