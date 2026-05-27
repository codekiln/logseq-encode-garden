tags:: [[mise/Commands]]
see-also:: [[mise/unuse]], [[mise/uninstall]]

- # [mise cache clear](https://mise.jdx.dev/cli/cache/clear.html)
	- **Usage**: `mise cache clear [PLUGIN]…`
	- **Aliases**: `c`
	- **Source code**: [`src/cli/cache/clear.rs`](https://github.com/jdx/mise/blob/main/src/cli/cache/clear.rs)
	- Deletes all cache files in mise. Pass tool names (e.g. `node`, `python`) to clear only those plugins; omit arguments to clear everything.