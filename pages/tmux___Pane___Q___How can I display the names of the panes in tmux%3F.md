logseq-entity:: [[Logseq/Entity/Question]], [[Logseq/Entity/Card]]

- # How can I display the names of the [[tmux/Pane]]s in tmux? [[card]]
	- ## [[My Answer]]
		- {{embed [[tmux/Option/pane-border-status]]}}
	- ## [[AI Answer]]
		- Short answer: panes don't have a persistent name field the way windows do (`rename-window`); what you set is the pane's **title**, and you make titles visible for every pane by turning on the pane border.
		- Turn on borders with titles for the current session:
			- [[tmux/Option/pane-border-status]]
			- ~~~sh
			  tmux set -g pane-border-status top
			  ~~~
			- `top` or `bottom` both work; this shows a thin border above/below each pane containing `#{pane_index}` and `#{pane_title}` (your default `pane-border-format` already includes both).
		- Set a pane's title (this is the "name" that shows up):
			- ~~~sh
			  tmux select-pane -T "editor"
			  ~~~
			- Run it from inside the target pane, or target another one with `-t`.
		- To make renaming quick, bind a key that prompts for a title, e.g. in `.tmux.conf`:
			- ~~~sh
			  bind-key C-r command-prompt -I "#{pane_title}" "select-pane -T '%%'"
			  ~~~
		-