logseq-entity:: [[Logseq/Entity/CLI/Command]]
tags:: [[mise/Commands]]

- # [mise unuse](https://mise.jdx.dev/cli/unuse.html)
	- **Usage**: `mise unuse [FLAGS] <INSTALLED_TOOL@VERSION>…`
	- **Aliases**: `rm`, `remove`
	- **Source code**: [`src/cli/unuse.rs`](https://github.com/jdx/mise/blob/main/src/cli/unuse.rs)
	- Removes installed tool versions from mise.toml
	- By default, this will use the `mise.toml` file that has the tool defined. If multiple config files exist (e.g., both `mise.toml` and `mise.local.toml`), the lowest precedence file (`mise.toml`) will be used. See [https://mise.en.dev/configuration.html#target-file-for-write-operations](https://mise.en.dev/configuration.html#target-file-for-write-operations)
	- In the following order:
		- If  [[mise/unuse/--global]] is set, it will use the [[mise/Config/mise.toml/Global]].
		- If `--path` is set, it will use the config file at the given path.
		- If `--env` is set, it will use `mise.<env>.toml`.
		- If `MISE_DEFAULT_CONFIG_FILENAME` is set, it will use that instead.
		- If `MISE_OVERRIDE_CONFIG_FILENAMES` is set, it will the first from that list.
	- Otherwise just "mise.toml" or global config if cwd is home directory.
	- Will also prune the installed version if no other configurations are using it.