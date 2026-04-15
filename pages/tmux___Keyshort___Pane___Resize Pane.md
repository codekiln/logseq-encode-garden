- [[Keyshort]] [[tmux]] [[tmux/Keyshort]] [[tmux/Keyshort/Pane]]
	- **Resize Pane (Directional)** #card
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.36
	  card-next-schedule:: 2026-04-16T04:00:00.000Z
	  card-last-reviewed:: 2026-04-15T07:37:27.581Z
	  card-last-score:: 1
		- Shortcut:
			- `<prefix> Alt-Up` resize pane up
			- `<prefix> Alt-Down` resize pane down
			- `<prefix> Alt-Left` resize pane left
			- `<prefix> Alt-Right` resize pane right
		- Description: Adjusts the current pane size incrementally in the arrow direction in [[tmux/oh-my-tmux]]
		- [[My Notes]]
			- doesn't work on all panes;
				- I can't find it right now, but I definitely asked a [[tmux/Q]] at one time about how if you have a sub-pane of a sub-pane, it doesn't work. Basically, the underlying tmux commands that are mapped here only work for the "top level" renames