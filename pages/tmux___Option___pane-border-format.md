logseq-entity:: [[Logseq/Entity/Software/Option]]
see-also:: [[tmux/Option/pane-border-status]], [[tmux/Pane/Border]]

- ### [`pane-border-format`](https://man.openbsd.org/tmux#pane-border-format)
	- Sets the format text shown in pane-border status lines. It accepts tmux formats such as `#{pane_index}`, `#{pane_title}`, and `#{pane_active}`.
	- The text appears when [[tmux/Option/pane-border-status]] is set to a visible position.
	- Example: `tmux set-option -g pane-border-format ' #{pane_index}: #{pane_title} '`
	- ## The stock value already renders the pane title
		- The manual states no default for this option, so the value has to be read off a server started with no config on the build in use rather than looked up. On [[tmux/v/3.7b]], measured [[2026/08/24]]:
			- ~~~sh
			  tmux -L stock -f /dev/null new-session -d
			  tmux -L stock show-options -gv pane-border-format
			  # #{?pane_active,#[reverse],}#{pane_index}#[default] "#{pane_title}"#{?#{mouse},…}
			  tmux -L stock kill-server
			  ~~~
		- The `"#{pane_title}"` in there is why naming panes with `select-pane -T` needs no format of its own: turning [[tmux/Option/pane-border-status]] on is the whole of it. This is the reason [[My/Dotfiles]] change `track-tmux-pane-border-status` is one line — the running server's value was identical to stock, character for character, so tracking it would have been upkeep that changed no behavior.
		- Read what a given pane's border line will say, with the format expanded in that pane's context:
			- ~~~sh
			  tmux display-message -p -t '<session>:<window>.1' '#{E:pane-border-format}'
			  ~~~
