- [[Keyshort]] [[Lazygit]] [[Lazygit/Keyshort]]
	- **Stage or Unstage the Selected File** [[Card]]
		- Shortcut: `<space>`
		- Description: Toggles staged status for the file under the cursor in the Files panel. One key for both directions — pressing it on a staged file unstages it.
	- **Stage or Unstage Everything** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-04T04:00:00.000Z
	  card-last-reviewed:: 2026-09-03T10:34:51.419Z
	  card-last-score:: 1
		- Shortcut: `a`
		- Description: Toggles staged/unstaged for every file in the working tree at once.
	- **Stage Individual Lines or Hunks** [[Card]]
		- Shortcut: `<enter>` on a file, then `<space>`
		- Description: Enters the staging view for that file, where `<space>` stages the selected hunk and `v` starts a line-wise selection to stage part of a hunk. The reason to reach for lazygit over `git add` when a file holds two unrelated changes.
	- [[My Note]]
		- This is the piece that keeps commits honest: [[git]] staging by hunk means an incidental fix does not have to ride along with the change it was found next to. Pairs with the targeted-`git add` habit in this garden's commit conventions.