tags:: [[Claude Code]], [[Diataxis/How To]]
see-also:: [[Claude Code/Settings]], [[Claude Code/--enable-auto-mode]], [[Claude Code/Docs/IDE Integrations]], [[Claude Code/Devcontainer]], [[GitHub/Codespace]], [[Person/Simon Willison/25/10/Living Dangerously with Claude Code]]
alias:: [[Anthropic/App/Claude Code/How To/Enable bypassPermissions in the VS Code Extension]]

- # How To Enable bypassPermissions in the VS Code Extension
	- ## Overview
		- Enables **bypassPermissions** in the Claude Code VS Code extension—the UI equivalent of legacy YOLO mode and the CLI flag `--dangerously-skip-permissions`. [^1]
		- For developers who want unattended tool runs without answering every prompt, using extension settings instead of manually launching `claude --dangerously-skip-permissions` from a terminal.
	- ## Prerequisites
		- [Claude Code VS Code extension](https://marketplace.visualstudio.com/items?itemName=Anthropic.claude-code) installed
		- A recent extension build that exposes permission modes (older builds required the CLI flag instead)
		- A risk posture that accepts skipping permission prompts for tool use in this environment
	- ## Steps
		- ### 1. Install or update the extension
			- Install from the VS Code Marketplace or update to the latest Claude Code extension.
		- ### 2. Open VS Code settings
			- Open **Settings** (Command Palette → **Preferences: Open Settings**, or **Code → Settings → Settings**).
		- ### 3. Allow dangerously skip permissions
			- Search for **Claude Code: Allow Dangerously Skip Permissions** and enable the toggle.
		- ### 4. Set the initial permission mode (optional)
			- Search for **Claude Code: Initial Permission Mode** and set the value to `bypassPermissions` so new sessions start in bypass mode. [^1]
		- ### 5. Start or reload a Claude Code session
			- Open Claude Code in the integrated panel; confirm the session mode is **bypassPermissions**, or cycle modes with **Shift+Tab** if another mode is active.
	- ## Devcontainer and Codespaces pattern
		- A common pattern: run VS Code and Claude Code inside the devcontainer or Codespace, keep secrets out of the workspace mount, and use bypass mode only inside that constrained environment. [^4]
		- See [[Claude Code/Devcontainer]] and [[GitHub/Codespace]].
	- ## Troubleshooting
		- **Extension lacks bypass settings** — update the extension; earlier releases did not expose bypass cleanly and required `claude --dangerously-skip-permissions` from a terminal. [^2]
		- **bypassPermissions unavailable** — check `disableBypassPermissionsMode` and managed policy settings on [[Claude Code/Settings]].
		- **Want fewer prompts without full bypass** — use auto mode per [[Claude Code/--enable-auto-mode]], or set `defaultMode` to `auto` in settings; auto classifies safe vs dangerous actions. [^3]
		- **Permission mode names** — `default`, `acceptEdits`, `plan`, `auto`, and `bypassPermissions` (equivalent to legacy dangerous-skip). [^1]
	- ## Footnotes
		- [^1]: https://code.claude.com/docs/en/permission-modes
		- [^2]: https://github.com/anthropics/claude-code/issues/8539
		- [^3]: https://www.anthropic.com/engineering/claude-code-auto-mode
		- [^4]: https://dev.to/trekhleb/run-claude-codes-dangerously-skip-permissions-safely-with-docker-514d
