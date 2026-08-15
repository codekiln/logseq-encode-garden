- [[Keyshort]] [[Lazygit]] [[Lazygit/Keyshort]]
	- **Undo the Last Git Command** [[Card]]
		- Shortcut: `z`
		- Description: Reads [[git/reflog]] to work out which git command ran last and what would reverse it, then prompts before running it.
	- **Redo the Undone Command** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-08-16T04:00:00.000Z
	  card-last-reviewed:: 2026-08-15T07:06:27.709Z
	  card-last-score:: 1
		- Shortcut: `Z`
		- Description: Uppercase `Z`, also driven by the [[git/reflog]]. **Not** `<C-z>` — that suspends lazygit to the shell, which is what several cheat sheets get wrong.
		  id:: 6a7a211b-0c2f-4e75-9013-1f1ac7311015
	- [[My Note]]
		- Only commits are considered. Working-tree changes are outside the reflog, so an undo will not bring back a discarded hunk — that is what [[Lazygit/Keyshort/Discard Change]] warns about.
		- The reflog basis is the same mechanism that made a rewritten commit recoverable in [[Lazygit/26/04/24 Fri Issues with git merge conflict resolution]]; `4]` browses it directly (see [[Lazygit/Keyshort/Show Reflog]]).