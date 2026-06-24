logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[mise/Q/How can I run mise commands to update pinned global dev tools using aqua and a mise Task]]

- # Will calling [[mise/upgrade]] in a directory that has a local [[mise/Config/mise.toml]] upgrade global [[mise/Tool]]s?
	- ## [[AI Answer]]
		- **Short answer:** Yes. `mise upgrade` without flags operates on the merged config stack, so global tools are upgraded regardless of whether the CWD has a local `mise.toml`.
		- [[Answer/Official]] from [mise upgrade docs](https://mise.jdx.dev/cli/upgrade.html)
			- mise merges all config sources in order (global `~/.config/mise/config.toml`, then local `.mise.toml` / `mise.toml`, etc.). Running `mise upgrade` resolves tools from that full merged config, which includes tools defined only in global config.
			- To restrict upgrades to the project-local config only — skipping tools that appear exclusively in global config — pass `--local` (see [`src/cli/upgrade.rs`](https://github.com/jdx/mise/blob/main/src/cli/upgrade.rs)).
			- To target only globally-configured tools, run `mise upgrade` from a directory that has **no** local `mise.toml` (e.g. `~`), or name the tools explicitly: `mise upgrade <tool>`.
