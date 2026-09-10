logseq-entity:: [[Logseq/Entity/Software/Plugin]]
created-by:: [[Person/Max Shen]]
date-created:: [[2023/04/24]]

- # [hardtime.nvim](https://github.com/m4xshen/hardtime.nvim)
	- An [[nvim]] plugin that breaks bad motion habits: it blocks repeated `hjkl` / arrow keys, hints faster Vim motions, and reports the habits you repeat most. Scope is core Vim movement coaching — pedagogical UI for motions, not LazyVim-wide learning.
	- Relates to [[My/Principle/Make the Right Thing Easy and the Wrong Thing Hard]]: raise friction on inefficient keys until better motions win.
	- ## Key features
		- Blocks (or hints on) repeated restricted keys within a short window
		- Hint messages that suggest shorter motions (`w`/`f`/`t`, relative jumps, operators + text objects, etc.)
		- `:Hardtime enable` / `disable` / `toggle`, plus `:Hardtime report` for the most common hints
		- Depends on `nui.nvim` for the report popup
