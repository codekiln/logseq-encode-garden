# Entity Inference From Journal

Use this reference when reading a journal or page to discover candidate entities.

Read [configuration-contract.md](./configuration-contract.md) and [logseq-entity-type-pages.md](./logseq-entity-type-pages.md) first, then load the garden's entity rules from `[[Logseq/Entity]]` and `[[Logseq/Entity/<Type>]]`, falling back to `.rulesync/config/logseq-entity.md` only if needed.

## Goal

Extract entities from Logseq-flavored markdown, then separate high-confidence candidates from aggressive inferences that should be reported back to the user.

## Direct Candidate Signals

Treat these as strong candidates when the active entity-type config says they are relevant:

- direct source links
- official homepages
- clear entity names in H1, H2, or H3 bullets
- markdown reference text that names an entity directly

Examples from a software-oriented journal:

- `[WhiskeyJack96/logseqlsp: ...](https://github.com/WhiskeyJack96/logseqlsp)`
- `[Feel-ix-343/markdown-oxide: ...](https://github.com/Feel-ix-343/markdown-oxide)`
- `[neovide/neovide: ...](https://github.com/neovide/neovide)`
- `[rsvim/rsvim: ...](https://github.com/rsvim/rsvim)`

## Aggressive Inference Signals

This skill may infer aggressively when the garden configuration allows it, but it must always report what it inferred.

Infer an entity even without a first-party source link when the surrounding context strongly suggests one specific entity, such as:

- a discussion of a named entity kind supported by the config
- a secondary article whose title clearly names the entity
- nearby notes that describe the entity as a concrete thing rather than as a general concept

Example:

- a Hacker News link titled `Helix: A Neovim inspired editor, written in Rust`

For example, in a software-focused garden this is enough to infer `[[Helix]]`, but the final report should say that the inference came from indirect context rather than a canonical project link.

## Extraction Workflow

1. Read the entire journal page and list candidate entity mentions relevant to the active config.
2. Normalize names:
   - preserve intended capitalization for human-facing output
   - derive the likely canonical name for the page title
   - keep source-identity information needed for search and alias decisions
3. Classify each candidate:
   - direct source-link candidate
   - indirect but strong inference
   - too weak, ambiguous, or probably not an in-scope entity
4. Deduplicate every candidate using [entity-search-and-dedup.md](./entity-search-and-dedup.md).
5. Create only the entities that are both missing and in scope according to config.

## Reporting Back To The User

After scanning a journal page, summarize:

- `found`: all in-scope candidates found
- `created`: new pages created
- `already existed`: entities that were already in the garden
- `inferred aggressively`: items created or proposed from indirect context
- `needs decision`: cases blocked by missing prerequisite entities, missing config, or unresolved duplicates

If the user asked only to scan, do not create pages. If the user asked to add entities, create the safe missing pages and then report the result.
