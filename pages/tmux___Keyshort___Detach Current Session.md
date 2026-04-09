- [[Keyshort]] [[tmux]] [[tmux/Keyshort]]
	- **Detach Current Session** #card
	  card-last-interval:: 10.36
	  card-repeats:: 3
	  card-ease-factor:: 2.7
	  card-next-schedule:: 2026-04-19T15:50:09.741Z
	  card-last-reviewed:: 2026-04-09T07:50:09.741Z
	  card-last-score:: 5
		- Shortcut: `<prefix> d` [[Keyshort/Default]]
		- Description: Detaches the current client from the tmux session while leaving the session and its running programs intact.
		- [[My Notes]]
			- Reattach later with `tmux attach -t <session-name>`
			- this is a default tmux keybinding. quoting [[tmux/man]]:
				- > A session may be detached using ‘C-b d’ (or by an external event such as ssh(1)
				     disconnection) and reattached with:
				       `$tmux attach-session`