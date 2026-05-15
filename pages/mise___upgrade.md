tags:: [[mise/Commands]]

- # [mise upgrade | mise-en-place](https://mise.jdx.dev/cli/upgrade.html)
	- **Usage**: `mise upgrade [FLAGS] [INSTALLED_TOOL@VERSION]…`
	- **Aliases**: `up`
	- **Source code**: [`src/cli/upgrade.rs`](https://github.com/jdx/mise/blob/main/src/cli/upgrade.rs)
	- Upgrades outdated tools
	- By default, this keeps the range specified in mise.toml. So if you have node@20 set, it will upgrade to the latest 20.x.x version available. See the `--bump` flag to use the latest version and bump the version in mise.toml.
	- This will update mise.lock if it is enabled, see [https://mise.en.dev/configuration/settings.html#lockfile](https://mise.en.dev/configuration/settings.html#lockfile)