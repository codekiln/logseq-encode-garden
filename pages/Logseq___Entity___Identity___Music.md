logseq-entity:: [[Logseq/Entity/Definition]]
logseq-entity-hierarchy-type:: [[Logseq/Entity/Hierarchy/Frontmatter/Type/extends]]
- # Music Identity
	- In this garden, **Music Identity** pages model the public artist or project names under which music is released or performed.
	- ## Inherited rules
		- Naming, person relationships, deduplication and marking follow [[Logseq/Entity/Identity]]. A Music Identity is an identity, not a biographical musician.
	- ## Attribution and placement
		- A recording's [[Logseq/Frontmatter/created-by-identities]] lists the identities credited on the release, in published order.
		- Place releases under the first credited identity as `<Identity>/Music/Recording/<Title>`, following [[Logseq/Entity/Music/Recording]]. A joint release has one page and lists every credited identity.
		- Place a separately represented composition under its primary credited identity as `<Identity>/Music/Work/<Title>`, following [[Logseq/Entity/Music/Work]]. A recording's artist credit does not establish the composition's authorship.
		- Personal credits still link the people who actually wrote, produced or performed the music, following [[Logseq/Entity/Person/Maker]].
	- ## Examples
		- [[Bibio]] and [[Dorian Concept]] are solo music identities, each linked to a separate person hub.
		- [[Bibio/Music/Recording/Answers]] credits both identities without creating a separate identity for their collaboration.
	- ## Child entities
		- [[Logseq/Entity/Identity/Music/Band]]
