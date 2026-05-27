logseq-entity:: [[Logseq/Entity/CLI/Command]]

- # [mise use | mise-en-place](https://mise.jdx.dev/cli/use.html)
	- **Usage**: `mise use [FLAGS] [TOOL@VERSION]…`
	- **Aliases**: `u`
	- **Source code**: [`src/cli/use.rs`](https://github.com/jdx/mise/blob/main/src/cli/use.rs)
	- Does the equivalent of calling [[mise/install]] to install a [[mise/Tool]] **and** adds the version to [[mise/Config/mise.toml]].
		- By default, installs it in a [[mise/Config/mise.toml/local]].
		- {{embed [[mise/use/--global]]}}
	- {{embed [[mise/use/Card/vs Install]]}}