tags:: [[Claude/Code]], [[mise]], [[Q]]
alias:: [[Claude/Code/Q/Why do I have multiple installations when using mise]]
logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[mise/Task]], [[dotfiles]]
date-created:: [[2026/06/02]]
title:: Claude/Code/Q/Why do I have multiple installations when using mise?

- # Why does Claude Code warn about multiple installations when managed via mise?
	- ## Symptom
		- Claude Code shows this warning at startup:
		  ```
		  ⚠ Multiple installations found
		  ├ npm-global at ~/.local/bin/claude
		  └ native at ~/.local/bin/claude
		  ```
		- Both entries point to the **same symlink** — so only one Claude Code is actually running.
	- ## Root cause
		- The warning is triggered by an **orphaned mise install directory** left behind when switching from the npm mise backend to the native mise backend.
		- **Before** (npm backend in `~/.config/mise/config.toml`):
		  ```toml
		  "npm:@anthropic-ai/claude-code" = "latest"
		  ```
		- **After** (native backend):
		  ```toml
		  claude-code = "latest"
		  ```
		- Changing the tool entry installs the native version but does **not** uninstall the old npm version. The orphaned directory remains at:
		  ```
		  ~/.local/share/mise/installs/npm-anthropic-ai-claude-code/
		  ```
		- Claude Code scans mise's installs directory and finds both, triggering the warning.
	- ## Fix
		- ### Option A — mise task (if your dotfiles include `tool:missing:uninstall`)
			- Preview orphans first:
			  ```sh
			  mise run tool:missing:ls
			  ```
			- Remove them:
			  ```sh
			  mise run tool:missing:uninstall
			  ```
			- This task finds all installed tools with no config source (`source == null`) and uninstalls them.
		- ### Option B — direct removal
			- `mise uninstall npm:@anthropic-ai/claude-code` will return "no versions found" because the tool is no longer in any config.
			- Remove the orphaned directory manually:
			  ```sh
			  rm -rf ~/.local/share/mise/installs/npm-anthropic-ai-claude-code
			  ```
	- ## How to verify
		- Run `claude --version` — should start without the multiple-installations warning.
