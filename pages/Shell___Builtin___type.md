- # `type` (shell builtin)
	- ## What it does
		- `type` shows how the shell resolves each command name (alias, function, builtin, or executable path).
	- ## `-a`
		- `-a` shows **all** matches found for each name, in shell resolution order.
		- This is useful for spotting path shadowing (for example, when both [[mise]] and [[nvm]] provide `node`).
	- ## Example
		- Command:
		  ~~~bash
		  type -a node npm codex rulesync claude
		  ~~~
		- Output in this environment:
		  ~~~text
		  node is /Users/pnore/.local/share/mise/installs/node/24.11.1/bin/node
		  node is /Users/pnore/.nvm/versions/node/v12.16.1/bin/node
		  npm is /Users/pnore/.local/share/mise/installs/node/24.11.1/bin/npm
		  npm is /Users/pnore/.local/share/mise/installs/npm/11.6.1/bin/npm
		  npm is /Users/pnore/.nvm/versions/node/v12.16.1/bin/npm
		  codex is /Users/pnore/.local/share/mise/installs/node/24.11.1/bin/codex
		  codex is /Applications/Codex.app/Contents/Resources/codex
		  rulesync is /Users/pnore/.local/share/mise/installs/node/24.11.1/bin/rulesync
		  claude is /Users/pnore/.local/bin/claude
		  ~~~
	- ## POSIX status
		- `type` is **not** required by POSIX `sh`.
		- `type -a` is shell-specific (for example [[Bash]] and [[zsh]]).
		- For POSIX-portable command lookup, prefer `command -v <name>`.
	- ## See also
		- [[Shell/PATH]]
		- [[CLI/Tool]]
		- [[POSIX]]
