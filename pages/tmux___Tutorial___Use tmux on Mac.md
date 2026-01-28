tags:: [[tmux]], [[macOS]], [[Diataxis/Tutorial]]
- # Tutorial: Use tmux on Mac
	- ## What You'll Create
		- A named tmux session with multiple windows and panes
		- A workflow for detaching, reattaching, and navigating quickly
	- ## Prerequisites
		- macOS with Terminal (or iTerm2)
		- Homebrew installed
	- ## Learning Goals
		- Start and attach to sessions
		- Create, rename, and close windows
		- Split panes, move between them, and resize
		- Use copy mode and scrollback
		- Save basic settings in a tmux config
	- ## Steps
		- ### 1. Install tmux with Homebrew
			- Run:
				~~~
				brew install tmux
				~~~
			- You should see Homebrew install tmux successfully.
		- ### 2. Start your first session
			- Create a session named "work":
				~~~
				tmux new -s work
				~~~
			- Notice the status bar at the bottom showing the session name.
		- ### 3. Detach and reattach
			- Detach with the tmux prefix, then `d`:
				- Press `Ctrl-b`, then `d`
			- Reattach later:
				~~~
				tmux attach -t work
				~~~
			- You should return to the same terminal state.
		- ### 4. Create and manage windows
			- Create a new window:
				- Press `Ctrl-b`, then `c`
			- Rename the current window:
				- Press `Ctrl-b`, then `,`
			- Move between windows:
				- Press `Ctrl-b`, then `n` for next or `p` for previous
				- Press `Ctrl-b`, then a number `0-9` to jump
			- Close a window when done:
				- Press `Ctrl-b`, then `&`
			- You should see window names update in the status bar.
		- ### 5. Split panes and navigate
			- Split vertically (left/right):
				- Press `Ctrl-b`, then `%`
			- Split horizontally (top/bottom):
				- Press `Ctrl-b`, then `"`
			- Move between panes:
				- Press `Ctrl-b`, then arrow keys
			- Resize panes:
				- Press `Ctrl-b`, then hold `Option` and press arrow keys
			- You should have multiple shells visible at once.
		- ### 6. Use copy mode and scrollback
			- Enter copy mode:
				- Press `Ctrl-b`, then `[`
			- Scroll with arrow keys or `Page Up`/`Page Down`
			- Start selection with `Space`, then move the cursor
			- Copy selection with `Enter`
			- Paste in tmux with:
				- Press `Ctrl-b`, then `]`
			- You should be able to scroll and paste text without leaving tmux.
		- ### 7. Save a minimal config
			- Create or edit `~/.tmux.conf`:
				~~~
				set -g mouse on
				setw -g mode-keys vi
				set -g history-limit 50000
				~~~
			- Reload the config:
				~~~
				tmux source-file ~/.tmux.conf
				~~~
			- You should now be able to scroll with the mouse and use vi keys in copy mode.
	- ## What You've Learned
		- How to start, detach, and reattach tmux sessions
		- How to manage windows and panes
		- How to use copy mode and paste buffer
		- How to add a basic tmux configuration on macOS
	- ## Related
		- [[tmux/Cheat Sheet]]
		- [[tmux/setw]]
		- [[tmux/Tutorial/Kanban for Agentic Coding]]
