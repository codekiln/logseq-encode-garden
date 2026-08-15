logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Lazygit/Keyshort/Undo and Redo]]

- # Why does it make sense for [[Lazygit]] to use the [[git/reflog]] for undo and redo?
	- ## [[AI Answer]]
		- **Short answer:** what gets undone is a ref pointer, and the reflog is git's own record of every position those pointers have held.
		- **Undo here means something different than it does in an editor**
			- A text editor keeps a private undo stack because the document has no memory of itself: overwrite a character and the previous one is gone unless the editor saved a copy first.
			- Git splits the content from the position. Commits are objects that stay on disk once written; `HEAD` and the branch tips are small mutable pointers into that set of objects. A reset, a checkout, a rebase mostly changes which commit a pointer names.
			- So undo means putting the pointers back where they were before the last command. The old commits are still sitting in the object store, so getting back to them requires nothing to be rebuilt.
		- **The reflog is that record, and git keeps it already**
			- Git writes an entry in `.git/logs/` every time a ref changes — commit, checkout, merge, reset, cherry-pick, each step of a rebase — whether the command came from lazygit's TUI or from the shell. Lazygit reads a log git was maintaining anyway instead of keeping a second one.
			- Walking it backward, lazygit translates each entry into the action that reverses it: a checkout entry sends you back to the branch you left, an applied commit sends you back to the commit before it, an interactive rebase sends you back to where you stood when the rebase began.
			- The reflog only ever appends, so the entry you undo stays on record and redo is a step forward through the same log. Lazygit writes its own undos and redos as reflog entries, which is how its position survives quitting and reopening the app.
			- The same property lets it undo commands you ran in the shell before opening lazygit for the first time.
		- **What the reflog covers sets what undo covers**
			- The reflog records ref positions, so that is how far `z` reaches. Working-tree edits and the stash sit outside it, and a discarded hunk stays gone. Creating a branch leaves no entry. A push has already left the machine.
			- Mid-rebase the reflog says too little about what happened inside, so the way back out is aborting the rebase (`m`).
		- [[Answer/Official]] from [Undo/Redo in lazygit](https://github.com/jesseduffield/lazygit/blob/master/docs/Undoing.md)
