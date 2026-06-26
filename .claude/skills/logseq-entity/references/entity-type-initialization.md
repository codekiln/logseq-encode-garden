# Entity-Type Initialization

Use this reference when the user wants to bootstrap or refresh the garden's entity model in Logseq, such as:

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

Do not invert that relationship. The repo file can seed shared process text and support initialization, but **per-type rules** should live on the Logseq type pages once they exist.

## RPI Workflow

Prefer an explicit research / plan / implement flow.

### Research

Inspect the garden before proposing entity types.

Look for:

- existing `[[Logseq/Entity]]` or `[[Logseq/Entity/<Type>]]` pages
- `.rulesync/config/logseq-entity.md` for shared fallback text when present
- repeated page patterns, namespaces, aliases, and frontmatter conventions
- journal entries and reference pages that repeatedly mention the same kinds of entities
- existing template pages related to entity creation

Research outputs should include:

- candidate entity types the garden appears to model
- evidence for each type
- naming and dedup patterns already present in the garden
- any gaps or contradictions that need human judgment

### Plan

Propose the smallest useful initial model.

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
- multiple shapes for the registry seem reasonable
- the garden has conflicting naming conventions

### Implement

Once the direction is clear:

1. Create or update `[[Logseq/Entity]]` as the registry.
2. Ensure `[[Logseq/Entity/Definition]]` (the meta type codifying the type-page shape) exists; mark every type page with `logseq-entity:: [[Logseq/Entity/Definition]]` so the set of types is queryable via its backlinks.
3. Create or update the approved `[[Logseq/Entity/<Type>]]` pages, following the canonical shape on `[[Logseq/Entity/Definition]]`.
4. Keep type definition and instance-template guidance on the type page by default.
5. Create a dedicated `[[Logseq/Template/Entity/<Type>/Page]]` page only when the type page should point to a separately instantiable or significantly larger template.
6. Keep `.rulesync/config/logseq-entity.md` short—shared fallback only; do not recreate per-type catalogs in the repo file.

## Reporting

After initialization work, report:

- researched signals and candidate types
- the proposed registry and type-page set
- pages created or updated
- what remains in the repo fallback file (if anything beyond shared text)
- open questions or deferred types
