logseq-entity:: [[Logseq/Entity/Definition]]

- # Software Option
	- In this garden, **Software Option** pages model one named configuration option exposed by a software project.
	- ## What counts as a Software Option
		- A setting with a stable name, documented behavior, and a set of accepted values or value shape defined by its software project.
		- Command-line invocation switches are [[Logseq/Entity/CLI/Flag]] instances; invocable subcommands are [[Logseq/Entity/CLI/Command]] instances.
	- ## Naming and identity
		- Instances use the owning software's namespace in the shape `{software}/Option/{option-name}`.
		- The owning software and exact option name together identify an instance.
	- ## Frontmatter and page shape
		- `logseq-entity:: [[Logseq/Entity/Software/Option]]` marks an instance.
		- The page describes the option's behavior, scope, accepted values, and commands or configuration syntax for setting and inspecting it.
		- Shared frontmatter conventions live on [[Logseq/Frontmatter]].
	- ## Examples in this garden
		- [[tmux/Option/pane-border-status]], [[tmux/Option/mode-keys]], and [[tmux/Option/status-keys]].
