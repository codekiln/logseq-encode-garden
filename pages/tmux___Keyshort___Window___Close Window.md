alias:: [[tmux/Keyshort/Window/Kill Window]]

- [[Keyshort]] [[tmux]] [[tmux/Keyshort]] [[tmux/Keyshort/Window]]
	- **Close / Kill Window** [[card]]
	  card-last-interval:: 4.14
	  card-repeats:: 2
	  card-ease-factor:: 2.7
	  card-next-schedule:: 2026-04-19T10:39:42.309Z
	  card-last-reviewed:: 2026-04-15T07:39:42.310Z
	  card-last-score:: 5
		- Shortcut: `<prefix> &` (e.g. Ctrl+b then &), then type `y` at the prompt to confirm.
		- Description: Closes / kills the current tmux window. Tmux prompts for confirmation before closing.
		- From the command line:
			- Close current window: `tmux kill-window`
			- Close a specific window: `tmux kill-window -t 1` or `tmux kill-window -t my-window-name`
		- Mouse: Right-click the window name in the status bar → choose **Kill** (or the X option) in the menu. See [[tmux/Window/Right Click]].