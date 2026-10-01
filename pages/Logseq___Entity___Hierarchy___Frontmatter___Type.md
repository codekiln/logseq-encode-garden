logseq-entity:: [[Logseq/Entity/Frontmatter/Definition]]
alias:: [[logseq-entity-hierarchy-type]]

- # `logseq-entity-hierarchy-type::` — how a child entity relates to its parent
	- Set on a child [[Logseq/Entity/Definition]] page, one whose name nests under a parent definition page, such as [[Logseq/Entity/Article/Blog]] under [[Logseq/Entity/Article]]. The value says whether the child entity is a kind of its parent or a part of it, for example `logseq-entity-hierarchy-type:: [[Logseq/Entity/Hierarchy/Frontmatter/Type/extends]]`.
	- ## Permitted values
		- [[Logseq/Entity/Hierarchy/Frontmatter/Type/extends]]
		- [[Logseq/Entity/Hierarchy/Frontmatter/Type/part-of]]
	- ## Notes
		- A child segment that is only a namespace, because the parent has no definition page, takes no value. [[Logseq/Entity/AI/Model]] is one.
		- [[Logseq/Entity/Hierarchy/Discussion]] holds the dated discussion of how child and parent entities relate, including which markers one page may carry together.
