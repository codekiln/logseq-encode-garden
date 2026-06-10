# Logseq Entity Type Pages

This skill should prefer Logseq-native entity-type pages as the primary source of truth.

## Canonical Structure

Use these pages when they exist:

- `[[Logseq/Entity]]` as the registry of entity types in the garden
- `[[Logseq/Entity/<Type>]]` as the canonical page for a specific entity type
- `[[Logseq/Frontmatter]]` as the shared convention page for page-level attributes

Documentation uses `[[Logseq/Entity/<Type>]]` as shorthand: substitute the **actual** type path from **`[[Logseq/Entity]]`** in the workspace graph. In this encode garden, multi-word types prefer **nested Title Case segments**—for example **`[[Logseq/Entity/Software/Project]]`**, **`[[Logseq/Entity/Article]]`**, or **`[[Logseq/Entity/Game/Type]]`**—not a single **kebab-case** segment. **`[[Logseq/Entity]]`** lists each canonical title (including types awaiting rename).

## Default Interpretation

Treat `[[Logseq/Entity/<Type>]]` as the canonical reference point for that type in the current garden.

Nested entity-type pages may represent narrower taxonomic scopes under a broader type. For example, a garden may use `[[Logseq/Entity/Game]]` for individual game instances and `[[Logseq/Entity/Game/Type]]` for game genres or mechanics. Treat that relationship as implicit unless the graph explicitly defines a property or workflow for it; do not add `extends::` or similar fields on behalf of the garden.

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
- type-specific workflows that are part of the entity model itself, such as required index updates or discovery/search patterns

Prefer references to garden-wide rules over copying shared conventions into every type page. Type pages should focus on what is specific to recognizing, deduplicating, and shaping that entity type.

## Graph Page Hygiene

Entity type pages are graph documentation, not agent documentation:

- Do not write Rulesync, skill, slash-command, generated-file, repo-path, or agent workflow references into Logseq entity pages.
- Do not add `Agents`, `garddiff`, journal-update, or source-block sections to entity type pages. Those are garden-wide operational rules handled outside the type page.
- Do not wrap actual `[[Page]]` wikilinks in backticks. Keep them clickable in graph pages.
- Use declarative garden voice, not second-person voice.
- Keep shared frontmatter semantics on `[[Logseq/Frontmatter]]`; type pages should state only the entity marker and any type-specific frontmatter.
- Follow garden naming conventions for new entity type page names: singular where natural; **nested Title Case segments** for multi-word types; plural or contextual forms through `alias::` when needed (see **`[[Logseq/Pref/Page/Name]]`** when it exists).

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
3. Read `[[Logseq/Frontmatter]]` when it exists for shared page-level attributes.
4. Skim `[[Logseq/Pref]]` (and linked preference pages such as **`[[Logseq/Pref/Page/Name]]`**) when present for encode-wide naming defaults.
5. If the type page points to a dedicated template page, read that too.
6. Only fall back to `.rulesync/config/logseq-entity.md` when the Logseq entity pages do not yet exist or are incomplete.

## Initializing entity pages in the graph

When the garden does not yet have complete Logseq-native entity pages:

1. Research the garden's existing entity-like patterns and current conventions.
2. Use `.rulesync/config/logseq-entity.md` for shared fallback text (resolution order, reporting) when present—not for a full per-type rule dump.
3. Create or update `[[Logseq/Entity]]` as the registry.
4. Create or update `[[Logseq/Entity/<Type>]]` for the initial supported types.
5. Create or update `[[Logseq/Frontmatter]]` when shared page-level conventions are needed.
6. Keep template guidance on the type page by default.
7. Keep the repo config file short; per-type rules belong on the graph pages above.
