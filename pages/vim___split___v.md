alias:: [[vim/vsplit]], [[vsplit]]

- # `:vsplit` — vertical split
	- Opens a new vertical split pane in [[vim]] / [[nvim]], placing two windows side by side.
	- ## Usage
		- `:vsplit` or `:vsp` — split the current buffer into two side-by-side panes
		- `:vsplit {file}` — open `{file}` in the new split
		- `:vsplit | terminal {cmd}` — open a terminal buffer in the split (renders [[ANSI]] output via [[PTY]])
	- ## Window management after splitting
		- `<C-w>h` / `<C-w>l` — move focus left / right between splits
		- `<C-w>c` — close the current split
