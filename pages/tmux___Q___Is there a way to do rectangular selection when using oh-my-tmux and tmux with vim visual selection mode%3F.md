tags:: [[Question]] 
see-also:: [[tmux/Q/What is a conceptual overview of how copy paste works in oh-my-tmux with nvim?]]

- # Is there a way to do rectangular selection when using [[tmux/oh-my-tmux]] and [[tmux]] with vim visual selection mode?
	- ## [[My Notes]]
		- I haven't done this successfully yet. I find it difficult to quickly determine what to edit at which layer - of configuration; there's tmux itself, then there's oh-my-tmux, then there are my configurations layered on top in the [[.tmux.conf.local]]. Could use some [[CLI/Coach]]ing.
	- ## Answer
		- [[AI/Response]]
			- **Yes.** tmux copy mode with vi keys supports rectangular (block) selection. Behavior depends on your bindings.
			- ### Default / toggle-based (no config) [[AI/Need/Confirmation]]
				- Enter copy mode: `Prefix+[`
				- Press `v` to toggle rectangle mode on/off (in default vi copy mode, `v` is bound to `rectangle-toggle`)
				- **Press Space** to start the selection (required)
				- Move with `h`/`j`/`k`/`l` to define the block
				- Press `Enter` (or `y` if bound) to copy; paste with `Prefix+]`
			- ### Vim-like bindings (recommended)
				- If [[tmux/oh-my-tmux]] has already bound `v` to `begin-selection`, rectangle mode can be unavailable unless you add explicit bindings. In `.tmux.conf.local` (oh-my-tmux's user override - [[.tmux.conf.local]]), you can make it behave like vim:
				- `v` = character-wise selection, `C-v` = rectangular selection, `y` = yank. No need to press Space after `C-v`:
				- ~~~text
				  bind -T copy-mode-vi v   send -X rectangle-off \; send -X begin-selection
				  bind -T copy-mode-vi C-v send -X rectangle-on \; send -X begin-selection
				  bind -T copy-mode-vi y   send -X copy-selection-and-cancel
				  ~~~
				- Use `rectangle-on` / `rectangle-off` rather than `rectangle-toggle` so `v` and `C-v` don't flip state in confusing ways.
			- ### tmux version
				- Syntax is for tmux **2.4+** (key table `copy-mode-vi`, `send -X`). For older tmux, use the `vi-copy` table and `bind-key -t vi-copy ...` (see sources).
			- ### Sources
				- [tmux copy mode - select text block (Super User)](https://superuser.com/questions/395158/tmux-copy-mode-select-text-block)
				- [tmux PR #2546 — rectangle-on/rectangle-off](https://github.com/tmux/tmux/pull/2546)