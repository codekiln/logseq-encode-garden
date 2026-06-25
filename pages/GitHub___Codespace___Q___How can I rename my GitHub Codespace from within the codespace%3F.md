logseq-entity:: [[Logseq/Entity/Question]]

- # How can I rename my GitHub Codespace from within the codespace?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Renaming a codespace - GitHub Docs](https://docs.github.com/en/codespaces/customizing-your-codespace/renaming-a-codespace)
		- **Short answer:** Use the `gh` CLI (pre-installed and pre-authenticated in every codespace) to change the display name from a terminal inside the codespace.
		- **Command:**
			- ~~~bash
			  gh codespace edit -c $CODESPACE_NAME -d 'New Display Name'
			  ~~~
		- **How it works:**
			- `$CODESPACE_NAME` is an environment variable automatically set inside every [[GitHub/Codespace]] to its permanent machine name (e.g. `literate-space-parakeet-w5vg5ww5p793g7g9`).
			- The `-d` / `--display-name` flag sets the human-readable label shown in the GitHub UI and `gh codespace list`.
			- Only the **display name** can be changed; the permanent name is fixed at creation time.
		- **Steps:**
			- 1. Open a terminal inside the codespace.
			- 2. Optionally confirm the permanent name: `echo $CODESPACE_NAME`
			- 3. Run: `gh codespace edit -c $CODESPACE_NAME -d 'My New Name'`
		- **Shorter alias:** `gh cs edit -c $CODESPACE_NAME -d 'My New Name'`
		- **Alternative (outside the codespace):** rename via [github.com/codespaces](https://github.com/codespaces) → kebab menu → **Rename**, or with `gh codespace list` to find the permanent name and then `gh codespace edit`.
