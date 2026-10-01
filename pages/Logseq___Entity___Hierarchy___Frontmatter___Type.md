logseq-entity:: [[Logseq/Entity/Frontmatter/Definition]]
alias:: [[logseq-entity-hierarchy-type]]

- # `logseq-entity-hierarchy-type::` — how a child entity relates to its parent
	- Set on a child [[Logseq/Entity/Definition]] page, one whose name nests under a parent definition page, such as [[Logseq/Entity/Article/Blog]] under [[Logseq/Entity/Article]]. The value says whether the child entity is a kind of its parent or a part of it, for example `logseq-entity-hierarchy-type:: [[Logseq/Entity/Hierarchy/Frontmatter/Type/extends]]`.
	- ## Permitted values
		- [[Logseq/Entity/Hierarchy/Frontmatter/Type/extends]]
		- [[Logseq/Entity/Hierarchy/Frontmatter/Type/part-of]]
	- ## Notes
		- Leave the property off a definition page whose parent has no definition page. [[Logseq/Entity/AI/Model]] carries none, because `Logseq/Entity/AI` is only a namespace.
		- [[Logseq/Entity/Hierarchy/Discussion]] holds the dated discussion of how child and parent entities relate, including which markers one page may carry together.
