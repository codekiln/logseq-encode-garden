# Entity-Type Initialization

Use this reference when the user wants to bootstrap or refresh the garden's entity ontology, such as:

- `initialize entity types for this garden`
- `help me figure out which entity types this garden should cover`
- `set up [[Logseq/Entity]] and the related type pages`

Read [configuration-contract.md](./configuration-contract.md) and [logseq-entity-type-pages.md](./logseq-entity-type-pages.md) first.

## Preserve The Hybrid Model

The primary source of truth should be:

- `[[Logseq/Entity]]`
- `[[Logseq/Entity/<Type>]]`

The fallback/bootstrap source should remain:

- `.rulesync/config/logseq-entity.md`

Do not invert that relationship. The fallback config can seed or support initialization, but the Logseq-native pages should remain authoritative once they exist.

## RPI Workflow

Prefer an explicit research / plan / implement flow.

### Research

Inspect the garden before proposing entity types.

Look for:

- existing `[[Logseq/Entity]]` or `[[Logseq/Entity/<Type>]]` pages
- `.rulesync/config/logseq-entity.md` as bootstrap guidance
- repeated page patterns, namespaces, aliases, and frontmatter conventions
- journal entries and reference pages that repeatedly mention the same kinds of entities
- existing template pages related to entity creation

Research outputs should include:

- candidate entity types the garden appears to model
- evidence for each type
- naming and dedup patterns already present in the garden
- any gaps or contradictions that need human judgment

### Plan

Propose the smallest useful initial ontology.

The plan should usually include:

- a draft `[[Logseq/Entity]]` registry
- the initial set of `[[Logseq/Entity/<Type>]]` pages to create or update
- what guidance belongs on each type page:
  - what counts as the type
  - naming and alias rules
  - dedup keys
  - frontmatter expectations
  - page shape
  - creation blockers
  - example entities
  - instance-template guidance
- whether any dedicated `[[Logseq/Template/Entity/<Type>/Page]]` pages are truly needed

Prefer starting with a small number of well-supported types instead of enumerating every possible type in the garden.

Pause after the plan when:

- the evidence is ambiguous
- multiple ontology shapes seem reasonable
- the garden has conflicting naming conventions

### Implement

Once the direction is clear:

1. Create or update `[[Logseq/Entity]]` as the registry.
2. Create or update the approved `[[Logseq/Entity/<Type>]]` pages.
3. Keep ontology and instance-template guidance on the type page by default.
4. Create a dedicated `[[Logseq/Template/Entity/<Type>/Page]]` page only when the type page should point to a separately instantiable or significantly larger template.
5. Keep `.rulesync/config/logseq-entity.md` as fallback/bootstrap support if it still adds value.

## Reporting

After initialization work, report:

- researched signals and candidate types
- the proposed ontology shape
- pages created or updated
- fallback/bootstrap config that remains in effect
- open questions or deferred types
