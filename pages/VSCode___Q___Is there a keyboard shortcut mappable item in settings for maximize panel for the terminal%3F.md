logseq-entity:: [[Logseq/Entity/Question]], [[Logseq/Entity/Card]]

- # Is there a keyboard shortcut mappable item in settings for maximize panel for the terminal? [[card]]
	- Yes — `workbench.action.toggleMaximizedPanel` (**View: Toggle Maximized Panel** in Command Palette); search for it in **Keyboard Shortcuts** (`Cmd+K Cmd+S`)
	- ## [[AI Answer]]
		- [[AI/Response]]
			- [[Answer/Official]] from [VS Code Key Bindings](https://code.visualstudio.com/docs/getstarted/keybindings)
			- **Short answer:** Yes — the command ID is `workbench.action.toggleMaximizedPanel`, available in **Keyboard Shortcuts** (`Cmd+K Cmd+S` on Mac or `Ctrl+K Ctrl+S` on Windows/Linux).
			- **Steps to bind it:**
				- 1. Open **Keyboard Shortcuts**: `Cmd+K Cmd+S` (Mac) or `Ctrl+K Ctrl+S` (Windows/Linux), or via `F1` → *Preferences: Open Keyboard Shortcuts*
				- 2. Search for `toggleMaximizedPanel` or `Toggle Maximized Panel`
				- 3. Click the `+` icon next to **View: Toggle Maximized Panel** and enter your desired key chord
			- **Command palette name:** `View: Toggle Maximized Panel`
			- **Command ID:** `workbench.action.toggleMaximizedPanel`
			- **JSON snippet** (for `keybindings.json`):
				- ~~~json
				  {
				    "key": "ctrl+shift+m",
				    "command": "workbench.action.toggleMaximizedPanel"
				  }
				  ~~~
			- This toggles the panel (terminal, output, problems, etc.) between its normal docked size and a maximized state covering the editor area. The UI button in the panel toolbar (the corners/expand icon) triggers the same command.
