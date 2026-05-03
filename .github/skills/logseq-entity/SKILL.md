---
name: logseq-entity
description: >-
  Metaskill for Logseq entity work in the active graph: open [[Logseq/Entity]]
  and [[Logseq/Entity/<Type>]] pages, dedupe, create or update instances per
  those type rules, infer candidates from journals, help initialize entity pages
  when asked, and record graph edits in today's journal (garddiff / Filed /
  Updated). All type-specific rules live in the graph; this skill does not list
  entity types or repo companion skills by name. Other skills in a repo may wrap
  narrow workflows—discover them from the graph, type pages, or the repo's skill
  layout. Use for: entity exists?, similar entities?, new entity page?, add
  entities from today's journal?, define or refresh entity types?
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

Use this fallback when the Logseq entity pages do not exist yet or are incomplete:

- `.rulesync/config/logseq-entity.md`

Treat those garden-owned sources as the source of truth for:

- which entity types this garden models (from the registry, not from this skill)
- naming and namespace rules
- dedup heuristics
- frontmatter and page-shape expectations
- creation blockers
- reporting expectations

If the Logseq entity pages and fallback config are both missing, inspect the garden for conventions, say that no explicit entity configuration was found, and ask whether to proceed with inferred conventions or create the entity-type pages first.

## Graph edits and today’s journal

When **any graph pages** under `pages/` are **created or materially edited** during entity work—including **imports** that only add `logseq-entity::`, **prerequisite pages required by the active type page or registry**, or **`Logseq/Entity/<Type>`** edits—you are **not done** until **`journals/YYYY_MM_DD.md`** records the change set (**`[[Filed]]`** vs **`[[Updated]]`**, mutual exclusivity, link-first lists). Load **`[[Logseq/Journal]]`** / **`[[Logseq/Journal/Section/Garddiff]]`** when they exist; otherwise follow rule **`logseq-journal-updates`**.

Procedure: [references/entity-session-journal.md](./references/entity-session-journal.md).

## Polymorphism and other skills in the repo

- **Same skill, different graphs:** Identical `logseq-entity` text may be deployed in multiple gardens; effective behavior follows whatever `[[Logseq/Entity]]` and `[[Logseq/Entity/<Type>]]` pages exist **in the workspace graph**. Do not assume another garden’s entity types.
- **Type pages are full SOPs:** Everything on `[[Logseq/Entity/<Type>]]` is binding—not only naming and frontmatter. If a type page defines imports, index updates, checklists, or search patterns, follow it end-to-end.
- **Narrow workflows:** A garden or repo may ship additional skills for routing (for example topic-specific filing). **Do not assume** their names or locations—discover from the graph, from type-page bullets, or by listing the repo’s skill directories. Those skills should route to Logseq type pages; **do not** duplicate long type SOPs under this skill’s `./references/`.

## Quick Start

### Does this entity already exist?

1. Read [references/configuration-contract.md](./references/configuration-contract.md).
2. Read [references/logseq-entity-type-pages.md](./references/logseq-entity-type-pages.md).
3. Load `[[Logseq/Entity]]` and `[[Logseq/Entity/<Type>]]` when they exist.
4. Fall back to `.rulesync/config/logseq-entity.md` only if needed.
5. Read [references/entity-search-and-dedup.md](./references/entity-search-and-dedup.md).
6. Search according to garden configuration.
7. Report one of:
   - existing canonical entity
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
   - propose the contents of `[[Logseq/Entity]]` and each `[[Logseq/Entity/<Type>]]` page
   - call out whether any dedicated `[[Logseq/Template/Entity/<Type>/Page]]` pages are actually needed
6. Implement:
   - create or update `[[Logseq/Entity]]` and the approved `[[Logseq/Entity/<Type>]]` pages
   - keep registry and instance-template guidance together on the type page by default
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

1. Create or update `[[Logseq/Entity/<Type>]]` as the canonical page for that type.
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
