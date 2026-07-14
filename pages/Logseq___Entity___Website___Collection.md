logseq-entity:: [[Logseq/Entity/Definition]]

- # Website Collection
	- In this garden, **Website Collection** pages model a specialization of the [[Logseq/Entity/Collection]] pattern: a **curated collection of websites** gathered around a theme or standard. Members are [[Logseq/Entity/Website]] instances.
	- ## Examples in this garden
		- [[Design/Good/Web]] — a curated gallery of exemplary web design, sitting under the broader [[Design/Good]] hub.
	- ## When a page might be modeling a website collection
		- Strong signals: a named, intentional selection of sites chosen for a shared quality (great design, a genre, a reference set); the page's job is the curation itself, and each member is a [[Logseq/Entity/Website]].
		- Not this type: a single site (use [[Logseq/Entity/Website]]); a heterogeneous design hub whose members are not all websites (keep as a plain hub page, e.g. [[Design/Good]], per [[Logseq/Entity/Collection]] on typed members).
	- ## How to name instance pages
		- Name the collection for its curating theme, nesting under an existing hub where one fits, e.g. [[Design/Good/Web]]. The reserved trailing `/Collection` marker is not required on instance names when the theme already reads as a collection; see [[Logseq/Entity/Collection]].
	- ## Frontmatter
		- `logseq-entity:: [[Logseq/Entity/Website/Collection]]`. Additive — list comma-separated with any other entities, primary first (see [[Logseq/Entity]]).
		- Shared frontmatter conventions live on [[Logseq/Frontmatter]].
	- ## Page shape
		- Lean: a line on what the collection curates and by what criterion, then a member list where each [[Logseq/Entity/Website]] gets a one-line note on why it belongs.
