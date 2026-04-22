- [[Keyshort]] [[tmux]] [[tmux/Keyshort]] [[tmux/Keyshort/Pane]]
	- **Rotate Panes** #card
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.36
	  card-next-schedule:: 2026-04-23T04:00:00.000Z
	  card-last-reviewed:: 2026-04-22T08:44:55.116Z
	  card-last-score:: 1
		- Shortcut: `<tmux-prefix> Ctrl+o`
		- Description: Rotate panes within the window, keeping the same visual pane focused (does change which pane is logically focused)
		- [[My Notes]]
			- It's a bit strange; I'm not quite sure what the use case is. Perhaps if you were running some workflow that required a three terminal rotation, and needed to do things subsequently in multiple terminals, you could keep eyes focused on a subset of the screen
			- Easily confused with [[tmux/Keyshort/Pane/Focus Next Pane]] (`Ctrl+b, o`) — if you meant to change focus, release Ctrl before pressing `o`
		-