logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[mise]], [[mise/Task/File]], [[mise/Task/File/Group]], [[mise/Config/Global]], [[mise/tasks]], [[mise/Q/How do I list installed mise tools that aren't in any config file?]]

- # If I place an executable [[mise/Task/File]] at `~/.config/mise/tasks/myscript`, will `mise run myscript` work without extra configuration?
	- ## [[AI Answer]]
		- **Short answer:** Yes, with normal global [[mise/Config/Global]]—no `[task_config]` or TOML task entry required. Put an **executable** script at `~/.config/mise/tasks/myscript` (or a grouped path like `~/.config/mise/tasks/foo/bar` → task name `foo:bar`). Run `mise run myscript` from any directory once global config loads.
		- **Why it works:** `.config/mise/tasks` is one of mise's default file-task directories, searched relative to each config scope's `config_root`. For `~/.config/mise/config.toml`, that root is `~/.config/mise`, so `~/.config/mise/tasks/` is discovered automatically. Global configs load independently; defaults apply unless `task_config.includes` replaces them.
		- **Requirements (not optional "configuration"):**
			- **Executable bit:** `chmod +x ~/.config/mise/tasks/myscript` — mise skips non-executable files.
			- **Shebang (recommended):** e.g. `#!/usr/bin/env bash` so mise picks the interpreter; optional `#MISE description="…"` for `mise tasks` / help.
			- **Global config present:** standard `~/.config/mise/config.toml` (or another global file mise merges) — you already need this for global tools; file tasks piggyback on the same scope.
		- **Caveats:**
			- If `[task_config].includes` is set in global config **without** listing `.config/mise/tasks`, default directories are **replaced** and your script will not appear until you add that path back.
			- Default task **cwd** is the config root (`~/.config/mise`), not your shell cwd. Use `#MISE dir="{{cwd}}"` in the script header when the task should run where you invoked `mise run`.
			- Subdirectories add `:` prefixes ([[mise/Task/File/Group]]); a flat file `tasks/myscript` is task `myscript`, not `tasks:myscript`.
		- **Verified on this machine:** `tool:missing:ls` and `tool:missing:uninstall` under `~/.config/mise/tasks/tool/missing/` run via `mise run` with no `task_config.includes` in global config.
		- [File tasks](https://mise.jdx.dev/tasks/file-tasks.html)
		- [Task configuration — `task_config.includes`](https://mise.jdx.dev/tasks/task-configuration.html#task-config-includes)
