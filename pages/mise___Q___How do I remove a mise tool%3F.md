logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[mise]], [[mise/use/--global]], [[mise/Config/Global]], [[mise/unset]]

- # How do I remove a [[mise/Tool]]? [[card]]
	- ## [[My Answer]]
		- [[tldr]]
			- filter [[mise/ls]] with [[rg]] to find `<TOOL_REFERENCE>` then call [[mise/unuse]] `<TOOL_REFERENCE>`
		- ### Step 1 - find the tool reference with [[mise/ls]]
			- basic
				- `mise ls | rg claude`
					- `npm:@anthropic-ai/claude-code  2.1.150           ~/.config/mise/config.toml                      latest`
					- here, the tool reference is `npm:@anthropic-ai/claude-code`
			- notes
				- by default `mise ls` returns versions that are in [[mise/Config/mise.toml]] even if they aren't installed. use [[mise/ls/--installed]] to instead only return installed versions.
				- if you want to search only for globally installed tools, use [[mise/ls/--global]].
		- ### Step 2 - remove with [[mise/unuse]]
			- `mise unuse npm:@anthropic-ai/claude-code`
	- ## [[My Notes]]
		- The *easiest* way is a bit fake: edit the [[mise/Config/mise.toml]] manually to remove it. This is fake because it still leaves the underlying tool on your machine.
		- If the [[mise/Tool]] you are uninstalling is available in a few different config files, you might want to use a flag to specify the location you want to install it from.
			- [[mise/unuse/--global]] ==is unnecessary== if there's no ambiguity about where the tool is defined
			- use [[mise/ls/--global]] and [[mise/ls/--installed]] to find the globally installed [[mise/Tool]]s, then use [[rg]] or [[grep]] to filter it down to the one you want
				- ```
				  mise ls --global --installed | rg claude
				  npm:@anthropic-ai/claude-code  2.1.150           ~/.config/mise/config.toml  latest
				  ```
				- from this we know that the tool reference is `npm:@anthropic-ai/claude-code`
	- ## [[AI/Response]]
		- **Short answer:** use `mise unuse -g <tool[@version]>`. That is the dedicated command for removing a tool entry from the global `mise` config.
		- **Why this is the idiomatic command:** `mise unuse` is purpose-built for removing tool versions from config, and `-g` targets the global config file at `~/.config/mise/config.toml`.
		- **What happens to installed files:** `mise unuse` also prunes the installed version if no other config still uses it. Add `--no-prune` if you want to remove the global dependency but keep the installed tool around.
		- **What not to use for this:** `mise uninstall` only removes the installed version from disk and does **not** modify config, while [[mise/unset]] is for environment variables rather than tool dependencies.
		- **Related alternative:** `mise use --remove -g <tool>` exists, but `mise unuse -g <tool>` is the clearer, purpose-specific form.
		- [mise unuse](https://mise.jdx.dev/cli/unuse.html)
		- [mise uninstall](https://mise.jdx.dev/cli/uninstall.html)
		- [mise use](https://mise.jdx.dev/cli/use.html)