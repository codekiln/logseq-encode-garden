logseq-entity:: [[Logseq/Entity/Question]]
tags:: [[Question]]
see-also:: [[tmux/Q/Is there a way to do rectangular selection when using oh-my-tmux and tmux with vim visual selection mode?]]

- # Are there two different modes of visual selection in [[tmux]]?
  - ## [[My Answer]]
    - 1 - `SPACE` - starts selection 
    - 2 - `v` toggles between visual and rectangular selection
    - 3 - `V` selects lines
    - 4 - `o` - go to the other end of the selection
    - 5 - `ESCAPE` - drop selection but stay in copy mode
	- ## [[AI Answer]]
		- **Short answer:** Yes. Stock tmux `copy-mode-vi` has two selection shapes you toggle between: **character-wise** (normal, started with `Space`) and **rectangle/block** (toggled with `v`). There is no "word-based" mode — word motions (`w`, `b`, `e`) just move the cursor within either shape.
		- ### Stock `copy-mode-vi` selection bindings (no config, no [[oh-my-tmux]])
			- | Key | Command | Effect |
			  |-----|---------|--------|
			  | `Space` | `begin-selection` | Start character-wise (linear) selection |
			  | `v` | `rectangle-toggle` | Toggle rectangle/block mode on the active selection |
			  | `V` | `select-line` | Select entire lines |
			  | `o` | `other-end` | Swap cursor to other end of selection |
			  | `Escape` | `clear-selection` | Drop selection without leaving copy mode |
		- ### How the two shapes work
			- 1. **Character-wise** — press `Space` to start. Highlights linearly from mark to cursor, wrapping across lines. Use `h`/`j`/`k`/`l` or word motions (`w`, `W`, `b`, `e`) to extend.
			- 2. **Rectangle (block)** — press `v` after starting a selection to toggle rectangle mode. The highlight becomes a column-aligned block between mark and cursor, regardless of line content. Press `v` again to toggle back. Equivalent to vim's `Ctrl-v` visual block.
		- ### oh-my-tmux remaps these
			- [[oh-my-tmux]] rebinds `v` to `begin-selection` and `C-v` to `rectangle-toggle`, matching vim conventions — so if your `v` starts a selection rather than toggling rectangles, you are using those remapped bindings, not stock tmux defaults.
		- ### "Word-based" clarification
			- `select-word` exists as a tmux command but has no default key binding in `copy-mode-vi`. The word-like feeling comes from navigating the cursor with `w`/`b`/`e` inside an existing character-wise selection. In mouse mode, double-clicking selects the word under the cursor.
		- ### Verify your session
			- Run `tmux list-keys -T copy-mode-vi | grep -E 'begin-selection|rectangle'` to see what your current config has bound.
		- ### Sources
			- [tmux(1) man page — copy-mode commands](https://man.openbsd.org/tmux.1) (`begin-selection`, `rectangle-toggle`, `select-line`, `select-word`)
			- [Superuser: tmux copy mode select text block](https://superuser.com/questions/395158/tmux-copy-mode-select-text-block)
