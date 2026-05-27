logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[mise]], [[mise/ls]], [[mise/ls/--installed]], [[mise/uninstall]], [[mise/Q/How do I remove a mise tool?]], [[mise/Q/What's the difference between mise unuse, mise uninstall, and mise cache clear?]]

- # How do I list installed [[mise]] tools that aren't in any [[mise/Config/mise.toml]] (or other config) file?
	- ## Answer
		- [[AI/Response]]
			- **Short answer:** run `mise ls --installed` and look for rows with **no config path** in the third column, or filter JSON where `source.path` is empty. Those installs are on disk but not pinned in any merged config; remove them with [[mise/uninstall]] (not [[mise/unuse]], which only edits config).
			- **Plain `mise ls`:** With [[mise/ls/--installed]], each line is `TOOL  VERSION  CONFIG_PATH  REQUESTED`. When `CONFIG_PATH` is blank (as with `npm:@anthropic-ai/claude-code` in your example), mise knows the version from the install directory only—it is not listed in `mise.toml`, `config.toml`, or `.tool-versions`. Tools that *are* in config show a path such as `~/.config/mise/config.toml`. [mise ls](https://mise.jdx.dev/cli/ls.html)
			- **Quick filter (text):** `mise ls --installed | awk '$3 !~ /mise\.toml|config\.toml|\.tool-versions/'` drops lines whose third field looks like a config file. Safer when tool names contain spaces: use JSON below.
			- **Reliable filter (JSON + jq):**
				- ~~~
				  mise ls --installed --json | jq -r '
				    to_entries[] | .key as $tool | .value[] |
				    select((.source.path // "") == "") |
				    "\($tool)@\(.version)"
				  '
				  ~~~
				- Each line is a `TOOL@VERSION` reference suitable for [[mise/uninstall]].
			- **Uninstall the listed orphans:** preview with `mise uninstall --dry-run TOOL@VERSION`, then remove one or batch:
				- ~~~
				  mise ls --installed --json | jq -r '
				    to_entries[] | .key as $tool | .value[] |
				    select((.source.path // "") == "") |
				    "\($tool)@\(.version)"
				  ' | xargs mise uninstall
				  ~~~
			- **Related flags (not the same thing):** `mise ls --current` / `-c` shows only versions **specified in config** (the inverse set). `mise ls --prunable` lists old installs mise can drop via `mise prune` because they are no longer the pinned version in **tracked** configs—different from never-having-been-in-config orphans. See [[mise/Q/What's the difference between mise unuse, mise uninstall, and mise cache clear?]].
			- **Why orphans exist:** `mise install <tool@version>` without `mise use` / `mise unuse` leaves binaries under `~/.local/share/mise/installs` without a config entry. Same after you `mise unuse` with `--no-prune` or manually delete a config line but keep the install.
