#### [Sessions, windows and panes](https://github.com/tmux/tmux/wiki/Getting-Started#sessions-windows-and-panes)
	- ![tmux pane diagram](https://github.com/tmux/tmux/wiki/images/tmux_pane_diagram.png)
		- [[tmux/Status Line]] is at the bottom and displays the [[tmux/session/Name]], the [[tmux/Window]]s
		- [[tmux/Pane]] is one of the rectangular sections
		- Each pane is separated from the panes around it by a line, this is called the [[tmux/Pane/Border]].
		- There is one pane in each window called the [[tmux/Pane/Active]], this is where any text typed is sent and is the default pane used for [[tmux/Command]]s that target the window.
			- [[tmux/Pane/Active/Border]] - the active pane's border is a different color, green by default.
			- The pane border of the active pane is marked in **green**, or if there are only two panes then the top, bottom, left or right half of the border is green.
	-