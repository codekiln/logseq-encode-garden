- [[Keyshort]] [[tmux]] [[tmux/Keyshort]] [[tmux/Keyshort/Pane]]
	- **Resize Pane (Directional)** #card
	  card-last-interval:: 4
	  card-repeats:: 2
	  card-ease-factor:: 2.22
	  card-next-schedule:: 2026-04-26T08:59:18.924Z
	  card-last-reviewed:: 2026-04-22T08:59:18.924Z
	  card-last-score:: 3
		- Shortcut:
			- `<prefix> Alt-Up` resize pane up
			- `<prefix> Alt-Down` resize pane down
			- `<prefix> Alt-Left` resize pane left
			- `<prefix> Alt-Right` resize pane right
		- Description: Adjusts the current pane size incrementally in the arrow direction in [[tmux/oh-my-tmux]]
		- [[My Notes]]
			- if you have a sub-pane of a sub-pane, it doesn't work. Basically, the underlying tmux commands that are mapped here only work for the "top level" renames
				- [[tmux/Q/Why doesn't prefix Alt-Left or Alt-Right resize the inner horizontal split in a nested tmux layout (outer top-bottom split and lower left-right split), while Alt-Up or Alt-Down still move the outer boundary?]]