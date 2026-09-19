logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tmux/Q/Is there a way to fuzzy find through the directories that are open in my tmux panes?]]

- # What's the easiest way to get the CWD of a [[tmux/Pane]]?
	- ## [[AI Answer]]
		- **Short answer:** run `tmux display-message -p '#{pane_current_path}'` from inside the pane.
		- ~~~sh
		  tmux display-message -p '#{pane_current_path}'
		  ~~~
		- To check a pane other than the active one, add `-t` with a `window.pane` target:
			- ~~~sh
			  tmux display-message -p -t 1.2 '#{pane_current_path}'
			  ~~~
		- `-p` prints the formatted message to stdout instead of the status line, and `#{pane_current_path}` is the format variable holding the pane's current working directory — so this works from a script or from another pane, not only from inside the target pane itself.
		- ### Sources
			- [tmux(1) man page — display-message, FORMATS](https://man.openbsd.org/tmux.1)
