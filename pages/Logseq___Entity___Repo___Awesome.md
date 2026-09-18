logseq-entity:: [[Logseq/Entity/Definition]]

- # Repo Awesome
	- In this garden, **Repo Awesome** pages model a specialization of [[Logseq/Entity/Repo]]: a **curated awesome-list repository** — usually `awesome-<topic>` on GitHub — that aggregates links to other projects, tools, or resources in a maintained Markdown index.
	- ## Relationship to [[Logseq/Entity/Collection]]
		- Same spirit as the Collection pattern (curated, typed members, intentional selection), but members are usually **external** repos or sites linked from the list rather than garden entity pages for every row. The awesome repo page is the collection entity; individual list entries become garden pages only when filed separately.
	- ## Examples in this garden
		- [[Person/Dave Lage/GitHub/awesome-neovim]] — curated [[nvim]] plugins; cited in [[LV4AD/Ch/05 Plugin Basics]].
		- [[Person/Stephen Akinyemi/GitHub/awesome-mcp-servers]] — curated [[MCP]] servers.
		- [[GitHub/unixorn/awesome-zsh-plugins]] — curated [[zsh]] plugins and frameworks (filed under `GitHub/<owner>/` rather than `Person/…/GitHub/`).
	- ## When a page might be this type
		- Strong signals: repo name or README follows the awesome-list convention; primary value is link curation and pruning, not shipping a library or app; community treats it as the canonical index for a topic.
		- Not this type: a normal library or app repo (use [[Logseq/Entity/Software/Project]]); a host-specific plugin bundle (use [[Logseq/Entity/Software/Plugin/Collection]]).
	- ## Frontmatter
		- `logseq-entity:: [[Logseq/Entity/Repo/Awesome]]`.
		- `created-by::` — list maintainer when known.
		- `date-created::` — repository creation date on the host, not the import date.
	- ## Page shape
		- Same as [[Logseq/Entity/Repo]]: linked H1 to the repo, [[GitHub/Star]] when available, short bullets on topic and why the list matters in this graph.
