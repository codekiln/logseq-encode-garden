# Entity Search And Dedup

Use this reference before creating or renaming any entity.

Read [configuration-contract.md](./configuration-contract.md) and [logseq-entity-type-pages.md](./logseq-entity-type-pages.md) first, then load the garden's entity rules from `[[Logseq/Entity]]` and `[[Logseq/Entity/<Type>]]`, falling back to `.rulesync/config/logseq-entity.md` only if needed.

## Goal

Decide whether a candidate is:

- an existing canonical entity
- a likely duplicate or near-match that needs human review
- a genuinely new entity page
- blocked by missing configuration or missing prerequisite entities

## Search Order

Search in the config-defined order and stop early only when the match is clearly canonical.

If the config does not specify an order, use this default:

1. Exact canonical page name
   - Check the expected page shape based on config.
   - Also check obvious case and punctuation variants.
2. Exact alias match
   - Search frontmatter `alias::` values for configured aliases and known source identities.
3. Partial title matches
   - Search page filenames and H1 blocks for short-name and long-name variants.
   - Search both with and without namespace, owner, or context prefixes.
4. Source identity fields
   - Search for configured source identities such as repo owner/name, domain, title, handle, ISBN, DOI, or other identifiers relevant to the entity type.
5. Page-body mentions
   - Search page bodies for distinctive URLs, labels, or descriptions.

Prefer `rg` for all searches.

## Match Outcomes

Treat a result as **existing** when one or more of these is true:

- the canonical filename matches the intended entity
- an alias clearly resolves the candidate to an existing canonical page
- the page body makes clear that the page is the same entity

Treat a result as **similar** when one or more of these is true:

- only a partial-name match was found
- the same source identifier appears under a different owner or context
- the candidate could be a subtype, fork, edition, plugin, adaptation, or adjacent entity
- the page title is close but the underlying source identity differs

Treat a result as **new** only when:

- no canonical page exists
- no alias resolves to the same entity
- no existing page body or source identity strongly indicates it is already covered

Treat a result as **blocked** when:

- no garden-owned entity configuration exists and conventions cannot be inferred safely
- the config requires prerequisite entities that do not yet exist
- the config requires a human decision before page creation

## Canonical Name Preference

Take canonical naming rules from config.

The skill may infer likely conventions from existing pages, but the garden-owned configuration is the source of truth.

## Dedup Reporting

When reporting results, use this structure:

- `existing`: canonical entities already present
- `similar`: near-matches that may need human review
- `new`: entities that appear safe to create
- `blocked`: cases that need configuration or human choice

For each item, briefly state why it landed in that bucket.
