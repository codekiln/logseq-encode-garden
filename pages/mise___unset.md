tags:: [[mise/Commands]]
see-also:: [[mise/Environment]]

- [mise unset | mise-en-place](https://mise.jdx.dev/cli/unset.html)
	- **Usage**: `mise unset [-f --file <FILE>] [-g --global] [ENV_KEY]…`
	- **Source code**: [`src/cli/unset.rs`](https://github.com/jdx/mise/blob/main/src/cli/unset.rs)
	- Remove environment variable(s) from the config file.
	- By default, this command modifies `mise.toml` in the current directory.