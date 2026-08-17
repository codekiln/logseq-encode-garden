- # Pane border
	- In [[tmux]], pane borders are the lines that separate the [[tmux/Pane]]s in a window. Border options control their characters, appearance, active-pane indicators, and optional status text.
	- The options below are window options. Use `set-option -g` to set the inherited global value or `set-option -w` to set the value for one window.
	- ## Options
		- {{embed [[tmux/Option/pane-active-border-style]]}}
		- {{embed [[tmux/Option/pane-border-format]]}}
		- {{embed [[tmux/Option/pane-border-indicators]]}}
		- {{embed [[tmux/Option/pane-border-lines]]}}
		- {{embed [[tmux/Option/pane-border-status]]}}
		- {{embed [[tmux/Option/pane-border-style]]}}
	- ## Example configuration
		- ~~~sh
		  set-option -g pane-border-lines heavy
		  set-option -g pane-border-style fg=colour238
		  set-option -g pane-active-border-style fg=colour46
		  set-option -g pane-border-indicators arrows
		  set-option -g pane-border-status top
		  set-option -g pane-border-format ' #{pane_index}: #{pane_title} '
		  ~~~
	- ## Related
		- [[tmux/Pane/Q/How can I display the names of the panes in tmux?]]
		- [[tmux/Q/How can I put a thick border around the focused pane?]]
