logseq-entity:: [[Logseq/Entity/Question]]

- # What is the easiest way to get to the [[GitHub]] repository side if I'm in a [[GitHub/Codespace]]?
	- ## [[AI Answer]]
		- **Short answer:** Run `gh repo view --web` in the Codespace terminal, or use the VS Code Command Palette → **"Go to Repository on GitHub"**.
		- ### Two main paths
			- #### 1. [[GitHub CLI]] (fastest from terminal)
				- `gh repo view --web` — opens the repository's [[GitHub]] page in a new browser tab. The [[GitHub CLI]] (`gh`) is pre-installed in all GitHub Codespaces.
			- #### 2. VS Code Command Palette
				- Press `F1` (or `Ctrl+Shift+P` / `Cmd+Shift+P`), type **"Go to Repository on GitHub"** and select it. This is the GUI equivalent.
		- ### Other quick routes
			- **Status bar shortcut**: Click the branch name in the VS Code bottom status bar → there is often a "Go to Repository" link in the resulting menu.
			- **URL edit**: The Codespace browser URL is `https://<name>.github.dev/`. Swap `<name>.github.dev` for `github.com/<owner>/<repo>` to land on the repo home.
