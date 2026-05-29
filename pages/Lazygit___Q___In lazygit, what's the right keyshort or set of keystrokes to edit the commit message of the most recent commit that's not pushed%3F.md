logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Lazygit/Keyshort]]

- # In [[Lazygit]], what's the right keyshort or set of keystrokes to edit the commit message of the most recent commit that's not pushed?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** navigate to the **Commits** panel, select the top commit, and press `r` (inline reword) or `R` (open in external editor).
			- **Step by step:**
				- 1. Open the **Commits** panel — press `4` or Tab/Shift-Tab to cycle through panels until the commits list is focused.
				- 2. The most recent commit is at the top; it is selected by default if you just committed.
				- 3. Press `r` to **reword** inline — lazygit opens a small text input directly in the UI where you can retype the message and confirm with Enter.
				- 4. Alternatively press `R` (uppercase) to reword in your configured `$EDITOR` (e.g. vim, nano), which gives you the full editor experience including multi-line body editing.
			- Both `r` and `R` work on any unpushed commit, not only the HEAD; select any commit in the list and use the same keys.
			- Source: [lazygit keybindings reference — Commits panel](https://github.com/jesseduffield/lazygit/blob/master/docs/keybindings/Keybindings_en.md)
