## use [[tmux/Command/set-option/-g]] to make [[tmux/Pane]] borders more pronounced
	- activate [[tmux/Option/pane-border-status]]
		- `tmux set-option -g pane-border-status top`
	- use a double border [[tmux/Option/pane-border-lines]]
		- `tmux set-option -g pane-border-lines double`
	- make pane borders have arrows and numbers [[tmux/Option/pane-border-indicators]]
		- `tmux set-option -g pane-border-indicators both`
	- make pane borders yellow and **bold** [[tmux/Option/pane-active-border-style]]
		- `tmux set-option -g pane-active-border-style fg=colour226,bold`