---
name: logseq-entity
description: >-
  Metaskill for Logseq entity work in the active graph: open [[Logseq/Entity]] and
  [[Logseq/Entity/<Type>]] pages, dedupe, create or update instances per those
  type rules, infer candidates from journals, help initialize entity pages when
  asked, and record graph edits in today's journal (garddiff / Filed / Updated).
  All type-specific rules live in the graph; this skill does not list entity
  types or repo companion skills by name. Other skills in a repo may wrap narrow
  workflows—discover them from the graph, type pages, or the repo's skill layout.
  Use for: entity exists?, similar entities?, new entity page?, add entities from
  today's journal?, define or refresh entity types?
targets: ["*"]
codexcli:
  short-description: Logseq entity registry, dedupe, create, journal extract, garddiff after graph edits
---

# Logseq Entity

Use this skill when the user wants help managing Logseq entities in this garden.

This skill is intentionally general-purpose:

- Deduplicate before creating anything.
- Read garden-specific rules from garden-owned configuration instead of hardcoding them here.
- Work across multiple gardens with different entity types and naming affinities.
- Infer candidates from source material using the active garden config.
- Report what was inferred, what already existed, what was created, and what needs human judgment.

## Progressive Disclosure

This skill is designed to work well in both Claude-style and Rulesync environments:

- Like Claude Code skills, it is directory-based and centers on `SKILL.md`.
- Like Claude Code skills, it uses progressive disclosure: metadata first, then this file, then references only when needed.
- Unlike Claude Code alone, Rulesync treats this as a source artifact that can be generated or simulated across multiple tools, so keep instructions tool-agnostic unless a tool-specific behavior is necessary.

## Configuration First

Before doing entity work, read [references/configuration-contract.md](./references/configuration-contract.md) and [references/logseq-entity-type-pages.md](./references/logseq-entity-type-pages.md), then load:

- `[[Logseq/Entity]]`
- `[[Logseq/Entity/<Type>]]`
- `[[Logseq/Frontmatter]]`
- `[[Logseq/Pref]]` when present (optional encode-wide naming prefs under **`[[Logseq/Pref/Page/Name]]`** and siblings)

Use this fallback when the Logseq entity pages do not exist yet or are incomplete:

- `.rulesync/config/logseq-entity.md`

Treat those garden-owned sources as the source of truth for:

- the general entity model (from `[[Logseq/Entity]]`) — terms, how a page is marked, naming rules; this page does **not** catalog the types
- which entity types this garden models — discover by listing the `Logseq/Entity/<Type>` definition pages (see the one-liner in [references/entity-search-and-dedup.md](./references/entity-search-and-dedup.md)), not from this skill or the model page
- naming and namespace rules
- dedup heuristics
- frontmatter and page-shape expectations
- creation blockers
- reporting expectations

If the Logseq entity pages and fallback config are both missing, inspect the garden for conventions, say that no explicit entity configuration was found, and ask whether to proceed with inferred conventions or create the entity-type pages first.

## Graph edits and today’s journal

When **any graph pages** under `pages/` are **created or materially edited** during entity work—including **imports** that only add `logseq-entity::`, **prerequisite pages required by the active type page or registry**, or **`Logseq/Entity/<Type>`** edits—you are **not done** until **`journals/YYYY_MM_DD.md`** records the change set (**`[[Filed]]`** vs **`[[Updated]]`**, mutual exclusivity, link-first lists). Load **`[[Logseq/Journal]]`** / **`[[Logseq/Journal/Section/Garddiff]]`** when they exist; otherwise follow rule **`logseq-core`** (journal updates).

Procedure: [references/entity-session-journal.md](./references/entity-session-journal.md).

## Polymorphism and other skills in the repo

- **Same skill, different graphs:** Identical `logseq-entity` text may be deployed in multiple gardens; effective behavior follows whatever `[[Logseq/Entity]]` and `[[Logseq/Entity/<Type>]]` pages exist **in the workspace graph**. Do not assume another garden’s entity types.
- **Entity definition pages are authoritative:** Everything on `[[Logseq/Entity/<Type>]]` is binding—not only naming and frontmatter. If an entity definition page defines imports, index updates, checklists, or search patterns, follow it end-to-end.
- **Narrow workflows:** A garden or repo may ship additional skills for routing (for example topic-specific filing). **Do not assume** their names or locations—discover from the graph, from entity definition bullets, or by listing the repo’s skill directories. Those skills should route to Logseq entity definition pages; **do not** duplicate long entity definitions under this skill’s `./references/`.

## Graph Page Hygiene

When creating or editing `[[Logseq/Entity]]`, `[[Logseq/Entity/<Type>]]`, `[[Logseq/Frontmatter]]`, or other graph entity definition pages:

- Keep graph pages self-contained and graph-native. Do **not** add Rulesync, skill, slash-command, generated-file, repo-path, or agent-workflow references to Logseq pages.
- Do **not** add agent-only reminders such as journal bookkeeping or source-block handling to entity type pages. Those operational duties live in Rulesync rules/skills and journal guidance.
- Keep actual Logseq links clickable. Do **not** wrap `[[Page]]` links in backticks; use backticks only for non-link path shapes, filenames, globs, or property syntax.
- Use declarative garden voice instead of second-person instructions.
- Put shared frontmatter conventions on `[[Logseq/Frontmatter]]`; type pages should mention only entity-specific frontmatter plus a short reference to that page.
- Entity type page names follow **`[[Logseq/Entity]]`**: multi-word types prefer nested Title Case segments (for example **`Software/Project`**); deferred legacy paths stay listed on the registry until migrated.

## Quick Start

### Does this entity already exist?

1. Read [references/configuration-contract.md](./references/configuration-contract.md).
2. Read [references/logseq-entity-type-pages.md](./references/logseq-entity-type-pages.md).
3. Load `[[Logseq/Entity]]` and `[[Logseq/Entity/<Type>]]` when they exist.
4. Fall back to `.rulesync/config/logseq-entity.md` only if needed.
5. Read [references/entity-search-and-dedup.md](./references/entity-search-and-dedup.md).
6. Search according to garden configuration.
7. Report one of:
   - existing entity
   - similar entities that need human judgment
   - no matching entity found
   - blocked because config or prerequisites are missing

### Search for similar entities

1. Read [references/configuration-contract.md](./references/configuration-contract.md).
2. Read [references/logseq-entity-type-pages.md](./references/logseq-entity-type-pages.md).
3. Load `[[Logseq/Entity]]` and `[[Logseq/Entity/<Type>]]` when they exist.
4. Fall back to `.rulesync/config/logseq-entity.md` only if needed.
5. Read [references/entity-search-and-dedup.md](./references/entity-search-and-dedup.md).
6. Return likely candidates ordered from strongest to weakest match.
7. Call out why each candidate might be the same entity or a different one.

### Create a new entity page

1. Read [references/configuration-contract.md](./references/configuration-contract.md).
2. Read [references/logseq-entity-type-pages.md](./references/logseq-entity-type-pages.md).
3. Load `[[Logseq/Entity]]` and `[[Logseq/Entity/<Type>]]` when they exist.
4. Fall back to `.rulesync/config/logseq-entity.md` only if needed.
5. Confirm it does not already exist using [references/entity-search-and-dedup.md](./references/entity-search-and-dedup.md).
6. Create the page using the configured page shape, frontmatter, naming rules, and template guidance.
7. If configuration-defined prerequisites are missing, stop and present recommended choices to the user.
8. Complete **Graph edits and today’s journal** (section above): update `journals/YYYY_MM_DD.md` for every new or changed graph page from this workflow.

### Initialize entity types for this garden

When the user says something like `initialize entity types for this garden`:

1. Read [references/configuration-contract.md](./references/configuration-contract.md).
2. Read [references/logseq-entity-type-pages.md](./references/logseq-entity-type-pages.md).
3. Read [references/entity-type-initialization.md](./references/entity-type-initialization.md).
4. Research:
   - inspect existing `[[Logseq/Entity]]` pages if they already exist
   - inspect `.rulesync/config/logseq-entity.md` as shared fallback text when present
   - inspect representative garden pages and journals to infer repeated entity kinds, naming conventions, and page-shape expectations
5. Plan:
   - propose a small initial set of entity types the garden appears to cover
   - `[[Logseq/Entity]]` is the shared, garden-agnostic conceptual model: reuse it as-is (copy from another garden) rather than authoring a per-garden version; the garden-specific work is the `[[Logseq/Entity/<Type>]]` pages
   - propose the contents of each `[[Logseq/Entity/<Type>]]` page
   - call out whether any dedicated `[[Logseq/Template/Entity/<Type>/Page]]` pages are actually needed
6. Implement:
   - ensure `[[Logseq/Entity]]` (the general model) is present, then create or update the approved `[[Logseq/Entity/<Type>]]` pages
   - keep type definition and instance-template guidance together on the type page by default
   - do **not** add a catalog of types back onto `[[Logseq/Entity]]`; the set of type pages is the list
   - keep `.rulesync/config/logseq-entity.md` limited to shared fallback material (resolution order, reporting)—**not** a duplicate catalog of per-type rules
   - after any new or changed graph pages: complete **Graph edits and today’s journal** (section above)
7. Report:
   - what the skill inferred during research
   - which types were proposed
   - which pages were created or updated
   - what was intentionally deferred for human judgment

Prefer an explicit RPI flow:

- `research`: inspect the garden and gather evidence
- `plan`: propose the initial entity-type model and pause when ambiguity is material
- `implement`: write the `Logseq/Entity` pages once the direction is clear

### Create or update an entity type page

When the user wants to define a new entity type for the garden:

1. Create or update `[[Logseq/Entity/<Type>]]` as the definition page for that type.
2. Put both type definition and instance-template guidance on that page by default.
3. Only create a dedicated `[[Logseq/Template/Entity/<Type>/Page]]` page when the template needs to be instantiated directly through Logseq or grows too large for the type page.
4. If the garden is still being bootstrapped, keep `.rulesync/config/logseq-entity.md` as a short shared fallback (see that file’s headings)—do not grow it back into per-type duplication.
5. Complete **Graph edits and today’s journal** (section above) for every graph page touched.

### Add entities from today's journal page

When the user says something like `add entities from today's journal page`:

1. Read today's journal page.
2. Read [references/configuration-contract.md](./references/configuration-contract.md).
3. Read [references/logseq-entity-type-pages.md](./references/logseq-entity-type-pages.md).
4. Load `[[Logseq/Entity]]` and the relevant `[[Logseq/Entity/<Type>]]` pages when they exist.
5. Fall back to `.rulesync/config/logseq-entity.md` only if needed.
6. Read [references/entity-inference-from-journal.md](./references/entity-inference-from-journal.md).
7. Extract in-scope entity candidates from direct links and strong indirect context.
8. Deduplicate each candidate using [references/entity-search-and-dedup.md](./references/entity-search-and-dedup.md).
9. For each missing entity, create a page using the active garden configuration.
10. Complete **Graph edits and today’s journal** (section above) for all new or changed graph pages from step 9 (and any prerequisite pages).
11. Summarize:
   - entities found
   - entities already present
   - entities created
   - aggressive inferences that may need correction
   - blocked cases that require a human choice
   - journal: which `[[Filed]]` / `[[Updated]]` links were added (or that none applied)

## Reference Guide

- **Another skill invoked for the same task:** follow that skill’s scope and steps; this skill still supplies **shared** entity behavior (configuration order, dedup references, **garddiff** / **Filed** / **Updated** when `pages/` change) unless the other skill explicitly documents a different journal contract for the same edit.
- Polymorphism and narrow repo skills: see **Polymorphism and other skills in the repo** above and [references/logseq-entity-type-pages.md](./references/logseq-entity-type-pages.md)
- Configuration contract: [references/configuration-contract.md](./references/configuration-contract.md)
- Logseq entity-type pages: [references/logseq-entity-type-pages.md](./references/logseq-entity-type-pages.md)
- Entity-type initialization: [references/entity-type-initialization.md](./references/entity-type-initialization.md)
- Search and dedup rules: [references/entity-search-and-dedup.md](./references/entity-search-and-dedup.md)
- Journal extraction and aggressive inference: [references/entity-inference-from-journal.md](./references/entity-inference-from-journal.md)
- After graph edits (garddiff / Filed / Updated): [references/entity-session-journal.md](./references/entity-session-journal.md)
- `date-created::` (entity creation/publication date, not import date): [references/date-created-frontmatter.md](./references/date-created-frontmatter.md)
- External entity pages (H1 link, no duplicate URL/macros): [references/external-entity-page.md](./references/external-entity-page.md)
