- [[Keyshort]] [[tmux]] [[tmux/Keyshort]] [[tmux/Keyshort/Pane]]
	- **Rotate Panes** #card
	  card-last-interval:: 4
	  card-repeats:: 2
	  card-ease-factor:: 2.22
	  card-next-schedule:: 2026-06-16T07:01:28.668Z
	  card-last-reviewed:: 2026-06-12T07:01:28.668Z
	  card-last-score:: 3
		- Shortcut: `<tmux-prefix> Ctrl+o`
		- Description: Rotate panes within the window, keeping the same visual pane focused (does change which pane is logically focused)
		- [[My Notes]]
			- [[Mnemonic]]
				- [[tmux/Keyshort/Pane/Focus Next Pane]] is (`Ctrl+b, o`), this is like that, but it's rotate to next pane instead of shifting focus. Different way to do the same thing, kind of
			- It's a bit strange; I'm not quite sure what the use case is. Perhaps if you were running some workflow that required a three terminal rotation, and needed to do things subsequently in multiple terminals, you could keep eyes focused on a subset of the screen
			- Easily confused with [[tmux/Keyshort/Pane/Focus Next Pane]] (`Ctrl+b, o`) — if you meant to change focus, release Ctrl before pressing `o`