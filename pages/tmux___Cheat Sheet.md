tags:: [[Keyshorts]]

- # tmux Cheat Sheet
	- ## Prefix key
		- Default: `Ctrl+b`
	- ## Session management
		- | Command                     | Action                                   |
		  |-----------------------------|------------------------------------------|
		  | `tmux`                      | Start a new session                      |
		  | `tmux new -s <name>`        | Start a new session with name            |
		  | `tmux ls`                   | List all sessions                        |
		  | `tmux attach` / `tmux a`    | Attach to the most recent session        |
		  | `tmux attach -t <name>`     | Attach to a specific session             |
		  | `tmux kill-session -t <name>`| Terminate a specific session            |
		  | `tmux kill-session -a`      | Kill all sessions except current         |
		  | `tmux kill-server`          | Terminate all sessions and the server    |
	- ## Window management (within a session)
		- default prefix is `ctrl+b`
		- | Shortcut (after prefix)     | Action                                   |
		  |-----------------------------|------------------------------------------|
		  | `c`                         | Create a new window                      |
		  | `,`                         | Rename current window                    |
		  | `&`                         | Kill current window                      |
		  | `n`                         | Next window                              |
		  | `p`                         | Previous window                          |
		  | `w`                         | List windows                             |
		  | `0..9`                      | Select window by number                  |
		  | `$`                         | Rename session (interactive)             |
	- ## Pane management
		- | Shortcut (after prefix)     | Action                                   |
		  |-----------------------------|------------------------------------------|
		  | `%`                         | Split pane **vertically**   (there will be a line going from top to bottom with terminals at left and right)             |
		  | `"`                         | Split pane **horizontally**   (there will be a line going from left to right with terminals above and below)           |
		  | `x`                         | Kill current pane                        |
		  | `o`                         | Switch to next pane                      |
		  | `;`                         | Toggle last active pane                  |
		  | `{` / `}`                   | Move pane left / right                   |
		  | `z`                         | Toggle zoom/focus on current pane        |
		  | `<Arrow keys>` (with prefix+Ctrl) | Resize pane in direction           |
	- ## Copy mode & scrolling
		- ==NOTE - tmux intercepts mouse wheel by default==
			- if you need to pass mouse wheel through to an application like [[Claude Code]], use one of these two:
				- 1 - config approach
					- add to `~/.tmux.conf`
					  collapsed:: true
						- ```tmux
						  set -g mouse on
						  ```
					- reload conf:
						- `Ctrl-b : source-file ~/.tmux.conf`
				- 2 - immediate application
					- `ctrl-b : set -g mouse on`
				-
		- | Shortcut                     | Action                                  |
		  |-----------------------------|------------------------------------------|
		  | `[`                          | Enter copy mode                           |
		  | `]`                          | Paste buffer                              |
		  | `Space` (in copy mode)       | Begin text selection                      |
		  | `Enter` (in copy mode)       | Copy selection                            |
		  | `q`                          | Exit copy mode                            |
		  | Movement in copy mode        | `h/j/k/l`, `w`, `b`, `PgUp/PgDn` etc.    |
	- ## Configuration (via `~/.tmux.conf`)
		- Change prefix key: `unbind C-b` then `set-option -g prefix C-a`
		- [[tmux/setw]] - note, you have to enter the prefix and then colon before entering these commands, e.g. `ctrl+b :` then type the words
			- Rename windows by default: `set-option -g base-index 1` / `setw -g pane-base-index 1`
			- Enable vi-keys in copy mode: `setw -g mode-keys vi`
			- Enable mouse support: `setw -g mouse on`
	- ## Quick reference terms
		- **Session**: A container of windows.
		- **Window**: Like a tab; contains one or more panes.
		- **Pane**: A split region within a window (runs a shell/program).
		- **Client**: A terminal attached to a session.
		- **Server**: Background process managing sessions.