logseq-entity:: [[Logseq/Entity/Question]]

- # What exactly are vim marks, and what are they good for?
	- ## [[AI Answer]]
		- Short answer: a **mark** is a name bound to a specific line and column in a specific file, set once and revisited on demand — a manual bookmark, as opposed to the automatic jump list that records everywhere you've *been*.
		- **Kinds of marks:**
			- Lowercase `a`–`z` — buffer-local; only resolve within the buffer where they were set.
			- Uppercase `A`–`Z` — global (file marks); jumping to one switches buffers/files if needed, since the mark carries its file with it.
			- `0`–`9` — automatically maintained: where the cursor was on the last few `:wq` exits across sessions.
			- Special automatic marks: `` ` ``` `` (position before the last jump), `` `. `` (last change), `` `^ `` (last insert), `` `[ `` / `` `] `` (start/end of last changed or yanked text).
		- **What they're good for:** returning to a precise spot — the top of a function, a config block, the far end of a long diff — without scrolling or re-searching, and (with uppercase marks) jumping straight back across files during a multi-file edit or refactor.
		- Set with `m{letter}`; jump with `` `{letter} `` for the exact position or `'{letter}` for the first non-blank of that line; clear with `:delmarks`. See [[vim/Keyshort/Mark]] for the shortcut reference, and [[LazyVim/Keyshort/Search]] for `<leader>sm`, the picker that lists every set mark with its file and line.
