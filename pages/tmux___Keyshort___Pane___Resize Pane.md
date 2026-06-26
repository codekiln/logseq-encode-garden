- [[Keyshort]] [[tmux]] [[tmux/Keyshort]] [[tmux/Keyshort/Pane]]
	- **Resize Pane (Directional)** #card
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.22
	  card-next-schedule:: 2026-06-27T04:00:00.000Z
	  card-last-reviewed:: 2026-06-26T07:32:46.508Z
	  card-last-score:: 1
		- Shortcut:
			- `<prefix> Alt-Up` resize pane up
			- `<prefix> Alt-Down` resize pane down
			- `<prefix> Alt-Left` resize pane left
			- `<prefix> Alt-Right` resize pane right
		- Description: Adjusts the current pane size incrementally in the arrow direction.
		- [[My Notes]]
			- on [[macOS]] with [[Ghostty]], `<prefix> Alt-Left` and `<prefix> Alt-Right` do not work
				- [[Ghostty]]'s built-in defaults bind `alt+arrow_left=esc:b` and `alt+arrow_right=esc:f` (readline word-jump). These ship regardless of `macos-option-as-alt` and take priority over Option-as-Meta. tmux's `M-Left`/`M-Right` expect xterm sequences `\033[1;3D`/`\033[1;3C` — not `ESC b`/`ESC f` — so they never fire.
				- `Alt-Up` and `Alt-Down` still work because Ghostty has no built-in default for those directions, so they fall through as proper xterm modifier sequences (`\033[1;3A`/`\033[1;3B`).
				- The fix (overriding Ghostty's defaults with `keybind = alt+arrow_left=esc:[1;3D`) breaks word navigation at the terminal, which is more valuable. Accepted limitation on macOS.
				- see [[tmux/Q/Why doesn't prefix Alt-Left or Alt-Right resize the inner horizontal split in a nested tmux layout (outer top-bottom split and lower left-right split), while Alt-Up or Alt-Down still move the outer boundary?]]