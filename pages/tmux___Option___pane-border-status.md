logseq-entity:: [[Logseq/Entity/Software/Option]]

- ### [`pane-border-status`](https://man.openbsd.org/tmux#pane-border-status)
	- A [[tmux]] window option that controls whether pane-border status lines are shown and where they appear.
	- ## Values
		- `off` — hide pane-border status lines.
		- `top` — show a status line along the top border of each pane.
		- `bottom` — show a status line along the bottom border of each pane.
		- `top-floating` — show a top status line only on floating panes.
		- `bottom-floating` — show a bottom status line only on floating panes.
	- ## Usage
		- Set it globally for all windows that inherit the global value:
			- ~~~sh
			  tmux set-option -g pane-border-status top
			  ~~~
		- Set it for the current window:
			- ~~~sh
			  tmux set-option -w pane-border-status top
			  ~~~
		- Show the global value:
			- ~~~sh
			  tmux show-options -gv pane-border-status
			  ~~~
		- Turn it off globally:
			- ~~~sh
			  tmux set-option -g pane-border-status off
			  ~~~
	- ## Displayed text
		- `pane-border-format` controls the text in the border status line.
		- Pane titles can be set with `select-pane -T "name"` and displayed through the `#{pane_title}` format.
	- ## Related
		- [[tmux/Keyshort/Pane/Show Pane Titles]]
