# Logseq Entity Type Pages

This skill should prefer Logseq-native entity-type pages as the primary source of truth.

## Canonical Structure

Use these pages when they exist:

- `[[Logseq/Entity]]` as the registry of entity types in the garden
- `[[Logseq/Entity/<Type>]]` as the canonical page for a specific entity type

`<Type>` is **whatever page titles exist** under the `Logseq/Entity/` namespace in **this** garden (for example a page titled `Logseq/Entity/software-project`—the exact spelling and depth are garden-defined).

## Default Interpretation

Treat `[[Logseq/Entity/<Type>]]` as the canonical reference point for that type in the current garden.

That page should ideally describe:

- what counts as the entity type
- what does not count
- canonical naming rules
- aliases or namespace rules
- identity and dedup keys
- frontmatter expectations
- creation blockers
- inference policy
- example entities
- page template guidance
- operational workflows that belong in the garden (imports, hub or index updates, discovery or search patterns, CLI notes)—not in Rulesync skill `references/`

## Narrow Rulesync skills (repo-specific)

A repository may add **small** skills whose only job is to route agents to heavy workflows. Conventions:

- The narrow skill’s `description` targets task routing; its body should **point at** the relevant `[[Logseq/Entity/<Type>]]` pages (and any linked Logseq SOP notes).
- **Authoritative detail stays in Logseq** on the type page (and linked pages). Do not mirror long checklists in `./references/` for domain-specific procedures.
- Not every type needs a narrow skill—only where extra discovery helps.
- The type page may list a companion skill name in a short bullet for humans and agents.

## Template Guidance

By default, the entity-type page should contain the template guidance for creating an instance of that type.

That keeps the type definition and the operational template together in one intuitive place for both humans and LLMs.

## Dedicated Template Pages

If the instance template becomes large or needs to be instantiated directly through Logseq's template UI, the entity-type page may point to a dedicated template page such as:

- `[[Logseq/Template/Entity/<Type>/Page]]`

When both exist:

- `[[Logseq/Entity/<Type>]]` is the conceptual authority
- `[[Logseq/Template/Entity/<Type>/Page]]` is the operational template artifact

## Skill Behavior

When working with an entity type:

1. Read `[[Logseq/Entity]]` if it exists to discover the garden's entity types.
2. Read `[[Logseq/Entity/<Type>]]` for the type-specific rules.
3. If that page points to a dedicated template page, read that too.
4. Only fall back to `.rulesync/config/logseq-entity.md` when the Logseq entity pages do not yet exist or are incomplete.

## Initializing entity pages in the graph

When the garden does not yet have complete Logseq-native entity pages:

1. Research the garden's existing entity-like patterns and current conventions.
2. Use `.rulesync/config/logseq-entity.md` for shared fallback text (resolution order, reporting) when present—not for a full per-type rule dump.
3. Create or update `[[Logseq/Entity]]` as the registry.
4. Create or update `[[Logseq/Entity/<Type>]]` for the initial supported types.
5. Keep template guidance on the type page by default.
6. Keep the repo config file short; per-type rules belong on the graph pages above.
