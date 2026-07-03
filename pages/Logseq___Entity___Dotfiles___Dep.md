alias:: [[Logseq/Entity/Dotfiles/Dependency]]
logseq-entity:: [[Logseq/Entity/Definition]]

- # Dotfiles Dependency
	- In this garden, **Dotfiles Dependency** pages model a tool, config, agent skill, or MCP server considered for — or installed into — the personal dotfiles, tracked through an intake pipeline from first idea to selection. The process behind the pipeline is [[My/Dotfiles/Process/Adding a New Global Dependency/Idea]].
	- ## What counts as an instance
		- A specific dependency evaluated for the dotfiles: a [[CLI Tool]], a global [[AI/Coding/Config]], an agent skill, an [[MCP]] server, or similar.
		- Not an instance: a software project with no bearing on the dotfiles (model it as [[Logseq/Entity/Software/Project]] alone); a [[My/Pref]] or [[My/Principle]] page.
	- ## Frontmatter
		- On instances, set `logseq-entity:: [[Logseq/Entity/Dotfiles/Dep]]`.
		- `dotfiles-dep-stage::` records the intake stage; its permitted values are defined by [[Logseq/Entity/Dotfiles/Dep/Frontmatter/dotfiles-dep-stage]].
		- Shared frontmatter conventions live on [[Logseq/Frontmatter]].
	- ## Relationships to other types
		- [[Logseq/Entity/Software/Project]] — a dependency that is also a shipping project may declare both, primary entity first.
		- [[OpenSpec]] — once a dependency reaches the selected stage, it advances into a dotfiles openspec change.
	- ## Page shape (body)
		- Logseq Flavored Markdown. Suggested: upstream link, what it provides, why it is being considered, and the current stage.
