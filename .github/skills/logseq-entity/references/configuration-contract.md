# Configuration Contract

This skill is intentionally general-purpose.

Do not hardcode garden-specific entity rules into the skill. Instead, load them from garden-owned configuration sources.

Prefer Logseq-native entity pages first. Use file-based config as fallback.

## Default Config Location

Look for configuration in this order:

- `[[Logseq/Entity]]`
- `[[Logseq/Entity/<Type>]]`
- `.rulesync/config/logseq-entity.md`

If none of these exist, the skill should:

1. inspect the garden for obvious existing entity conventions
2. state that no explicit `logseq-entity` config was found
3. ask the user whether to proceed with inferred conventions or create config first

## Bootstrap And Initialization

When the user wants to initialize entity types for a garden:

- use `.rulesync/config/logseq-entity.md` as bootstrap guidance when it exists
- create or update `[[Logseq/Entity]]` and `[[Logseq/Entity/<Type>]]` as the primary source of truth
- keep the file-based config as fallback/bootstrap support instead of replacing the Logseq-native ontology pages

## What Belongs In Garden Configuration

Store garden-specific policy there, including:

- which entity types this garden actively models
- how to recognize those entity types
- canonical naming preferences
- allowed or preferred namespaces
- alias strategy
- frontmatter expectations by entity type
- minimum page shape by entity type
- creation blockers
- whether to infer aggressively or conservatively
- whether source blocks should remain in place, be copied, or be moved
- required follow-up actions such as journaling or backlink insertion

## What Stays In The Skill

The skill should keep only reusable process:

- read garden configuration first
- extract candidate entities from source material
- deduplicate against the garden
- classify candidates as existing, similar, new, or blocked
- create or update entities according to config
- report what happened and what needs human judgment

## Suggested Config Shape

The configuration can stay in Markdown as long as it is explicit and machine-readable enough for an AI agent.

Preferred Logseq-native shape:

- `[[Logseq/Entity]]` as the registry
- `[[Logseq/Entity/<Type>]]` as the canonical type page

Fallback file-based shape:

- `.rulesync/config/logseq-entity.md`

Recommended sections:

- purpose and scope of this garden
- enabled entity types
- per-entity-type rules
- search and dedup preferences
- page templates or minimum shape
- creation blockers and escalation rules
- examples

The skill should treat the garden-owned configuration as the source of truth for entity behavior in that garden.
