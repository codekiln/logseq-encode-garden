---
description: >-
  Create or update a Logseq Term page with deduplication, minimal default
  structure, and a journal entry
trigger: /logseq-term
turbo: true
---
# Workflow: /logseq-term

# Create or Update a Logseq Term Page

This command creates or updates a `[[Term]]` page in the Logseq knowledge garden. It follows the existing house style inferred from current `tags:: [[Term]]` pages: start minimal, use aliases when helpful, and only expand into a fuller explanation structure when the concept actually needs it.

## Variables

- **Term name** – **Required**: The canonical term to add, such as `Headless Browser`, `Context Window`, or `Fingerspitzengefühl`.
- **Namespace/context** – **Optional**: A namespace if the term clearly belongs under an existing hierarchy, such as `AI`, `Programming/Language`, or `EdTech`. If omitted, prefer a non-namespaced page when that matches existing garden patterns.
- **Aliases** – **Optional**: Common alternate names, abbreviations, or singular/plural variants to include in `alias::`.
- **Depth** – **Optional**: Either a minimal definition page or a fuller explanation-style page. Default to minimal unless the user asks for a deeper explainer or the concept clearly warrants one.

## Conventions

- **Tags**: New term pages should include `tags:: [[Term]]` as frontmatter.
- **Aliases**: Add `alias::` only when it helps deduplication, discovery, or matches existing usage.
- **No baked-in Related section**: Do **not** add a `## Related` section by default. Logseq backrefs already provide this and explicit related links tend to duplicate them. Only add a related section if the user explicitly asks.
- **Page style**:
  - Minimal pages are preferred by default: one heading or top block plus a concise definition.
  - Expanded pages may use sections such as `## Overview`, `## Context`, `## Key Principles`, `## Mechanism`, `## Examples`, or `## Misconceptions` when needed.
- **Journal**: Record the creation or update in today's journal using the `[[Filed]]` / `[[Updated]]` conventions.

## Workflow

### Step 1: Determine the canonical page name

- Normalize the requested term.
- If a namespace/context was provided and it matches existing garden conventions, use it.
- Otherwise prefer the simplest canonical page name that fits the existing garden.
- Use Logseq naming conventions:
  - Link form: `[[Namespace/Subnamespace/Term Name]]`
  - File form: `pages/Namespace___Subnamespace___Term Name.md`

### Step 2: Search for existing pages (deduplication)

- Search `pages/*.md` for:
  - existing pages tagged `[[Term]]`
  - filename matches for the term
  - `alias::` matches for alternate spellings, abbreviations, and singular/plural variants
- Read likely matches before creating anything.
- **If an existing matching page is found:**
  - Do **not** create a duplicate.
  - Update the existing page instead.
  - Use the canonical page name of the existing file for all new references.

### Step 3: Create or update the page

- Preserve any existing `tags::` exactly as written on existing pages.
- For a **new** page, create frontmatter as needed:
  - `tags:: [[Term]]`
  - optional `alias:: ...`
- Default body for a new minimal page:

~~~markdown
tags:: [[Term]]
alias:: [[Alternate Name]]
- # Term Name
	- Concise definition in one or two sentences.
~~~

- A slightly more compact variant is also acceptable when it matches nearby pages:

~~~markdown
tags:: [[Term]]
alias:: [[Alternate Name]]
- Term Name
	- Concise definition in one or two sentences.
~~~

- Only expand beyond the minimal structure when one of these is true:
  - the user asked for a fuller explainer
  - the topic is complex enough that a single definition would be too thin
  - there is already an existing expanded term page pattern nearby that should be preserved
- If expanding, use explanation-style sections selectively rather than mechanically. Do not force every section.
- Do **not** add a `## Related` section unless the user explicitly requests it.

### Step 4: Add or update today's journal entry

- Open today's journal in `journals/YYYY_MM_DD.md`.
- If the page is **new**, add the page link under `[[Filed]]`.
- If the page was **updated**, add the page link under `[[Updated]]`.
- Keep the page in only one of those sections for the day.
- Default journal entry format is link-only:
  - `[[Term Name]]`
  - `[[Namespace/Term Name]]`

### Step 5: Report

- If a duplicate was found, report which existing page was updated.
- If a new page was created, report the canonical page link and file path.
- Mention whether aliases were added and whether the journal was updated.

## Related

Use the prefix that matches the type: `rule:` for rules, `command:` for commands, `skill:` for skills.

- rule: `logseq-flavored-markdown` – Logseq bullet structure and frontmatter rules
- rule: `logseq-page-naming-reference` – File naming and link naming conventions
- rule: `logseq-journal-updates` – Record creations and updates in today's journal

// turbo
