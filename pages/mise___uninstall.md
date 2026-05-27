logseq-entity:: [[Logseq/Entity/CLI/Command]]
tags:: [[mise/Commands]]
see-also:: [[mise/install]], [[mise/unuse]], [[mise/unset]], [[mise/cache/clear]]

- # [mise uninstall](https://mise.jdx.dev/cli/uninstall.html)
	- **Usage**: `mise uninstall [FLAGS] [INSTALLED_TOOL@VERSION]…`
	- **Source code**: [`src/cli/uninstall.rs`](https://github.com/jdx/mise/blob/main/src/cli/uninstall.rs)
	- Removes installed tool versions from disk. Does **not** modify `mise.toml` or other config files.
