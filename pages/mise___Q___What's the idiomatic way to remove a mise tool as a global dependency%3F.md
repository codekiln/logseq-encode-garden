logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[mise]], [[mise/use/--global]], [[mise/Config/Global]], [[mise/unset]]

- # What's the idiomatic way to remove a [[mise]] tool as a global dependency?
- ## Answer
	- [[AI/Response]]
		- **Short answer:** use `mise unuse -g <tool[@version]>`. That is the dedicated command for removing a tool entry from the global `mise` config.
		- **Why this is the idiomatic command:** `mise unuse` is purpose-built for removing tool versions from config, and `-g` targets the global config file at `~/.config/mise/config.toml`.
		- **What happens to installed files:** `mise unuse` also prunes the installed version if no other config still uses it. Add `--no-prune` if you want to remove the global dependency but keep the installed tool around.
		- **What not to use for this:** `mise uninstall` only removes the installed version from disk and does **not** modify config, while [[mise/unset]] is for environment variables rather than tool dependencies.
		- **Related alternative:** `mise use --remove -g <tool>` exists, but `mise unuse -g <tool>` is the clearer, purpose-specific form.
		- [mise unuse](https://mise.jdx.dev/cli/unuse.html)
		- [mise uninstall](https://mise.jdx.dev/cli/uninstall.html)
		- [mise use](https://mise.jdx.dev/cli/use.html)
