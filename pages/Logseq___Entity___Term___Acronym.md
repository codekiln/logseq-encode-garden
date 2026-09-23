logseq-entity:: [[Logseq/Entity/Definition]]
see-also:: [[Logseq/Entity/Abbreviation]]

- # Acronym
	- In this garden, **Acronym** pages model term pages whose name is an acronym, with the expanded phrase carried as an alias.
	- ## Examples in this garden
		- [[TAM]] — Total Addressable Market
	- ## An add-on to a term page
		- Acronym is declared after the type that shapes the page, on a page that is already a term of some kind: [[Logseq/Entity/Term]] for a glossary entry, or [[Logseq/Entity/Concept]] when the acronym gets a full explanation, as [[TAM]] does.
	- ## What counts as an Acronym
		- The page name is the acronym or initialism itself, and readers look up the letters: TAM, SOTA, PEBCAK.
		- `alias::` carries the fully expanded phrase: `alias:: [[Total Addressable Market]]`.
		- A page named by the full phrase is a Term or Concept; the short form can be one of its aliases. A clipped word such as [[Keyshort]] is an [[Logseq/Entity/Abbreviation]].
	- ## Naming
		- The page name is the acronym, and nothing else about the name is fixed. The page sits wherever its topic puts it: at the root like [[TAM]] and [[SOTA]], or inside a namespace like [[EdTech/OER]] and [[xAPI/LRS]].
	- ## Frontmatter
		- `logseq-entity::` — the primary type first, then this page: `logseq-entity:: [[Logseq/Entity/Term]], [[Logseq/Entity/Term/Acronym]]`, or `logseq-entity:: [[Logseq/Entity/Concept]], [[Logseq/Entity/Term/Acronym]]`.
		- `alias::` — the expanded phrase.
		- Legacy acronym pages carry `tags:: [[Term]], [[Acronym]]`, and that tagging stays as it is.
		- Shared frontmatter conventions live on [[Logseq/Frontmatter]].
	- ## Page shape
		- The primary type sets the shape. The H1 gives the expansion with the acronym in parentheses, `- # Total Addressable Market (TAM)`, so the letters and the phrase appear together at the top.
	- ## Relationship to Abbreviation
		- [[Logseq/Entity/Abbreviation]] is a primary type for every shortened form, contractions included. Acronym is the add-on for the subset whose page name is an acronym, declared after Term or Concept.
	- ## Finding and deduplicating
		- Search the letters as a page name, the expanded phrase as a title or alias, and pages tagged `[[Acronym]]` that lack `logseq-entity::`. The legacy tag marks candidates; add the entity when a page is revised, and leave a bulk backfill for when the author asks for one.
