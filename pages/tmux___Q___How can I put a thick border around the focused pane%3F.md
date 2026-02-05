# How can I put a thick border around the focused pane in [[tmux]]?
	- It's difficult to figure out which pane has focus.
	- ## Answer
		- Use the `pane-border-lines` option set to `heavy`:
			- ~~~
			  set -g pane-border-lines heavy
			  ~~~
		- This uses thick UTF-8 box-drawing characters for all pane borders.
		- To make the **active pane** stand out even more, combine with `pane-active-border-style`:
			- ~~~
			  set -g pane-border-lines heavy
			  set -g pane-active-border-style fg=green
			  set -g pane-border-style fg=colour238
			  ~~~
		- ### Available `pane-border-lines` values
			- `single` - single lines using ACS or UTF-8 characters (default)
			- `double` - double lines using UTF-8 characters
			- `heavy` - heavy/thick lines using UTF-8 characters
			- `simple` - simple ASCII characters
			- `number` - displays the pane number
			- `spaces` - space characters (no visible border)
		- ### Additional options for indicating the active pane
			- `pane-border-indicators` can highlight the active pane in different ways:
				- `off` - no special indication
				- `colour` - color only half the border in 2-pane windows
				- `arrows` - display arrow markers pointing to active pane
				- `both` - use both color and arrows
			- Example:
				- ~~~
				  set -g pane-border-indicators arrows
				  ~~~
		- ### Requirements
			- `heavy` and `double` border styles require UTF-8 support in your terminal
			- If UTF-8 is not supported, tmux falls back to standard ACS line drawing
	- ## My Notes
		- Add to `~/.tmux.conf` and reload with `tmux source-file ~/.tmux.conf`
		- Or test live with `prefix + :` then type the set command
	- ## Related
		- [[tmux/setw]]