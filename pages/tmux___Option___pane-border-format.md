logseq-entity:: [[Logseq/Entity/Software/Option]]

- ### [`pane-border-format`](https://man.openbsd.org/tmux#pane-border-format)
	- Sets the format text shown in pane-border status lines. It accepts tmux formats such as `#{pane_index}`, `#{pane_title}`, and `#{pane_active}`.
	- The text appears when [[tmux/Option/pane-border-status]] is set to a visible position.
	- Example: `tmux set-option -g pane-border-format ' #{pane_index}: #{pane_title} '`
