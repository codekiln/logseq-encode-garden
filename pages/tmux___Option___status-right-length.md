logseq-entity:: [[Logseq/Entity/Software/Option]]
see-also:: [[tmux/Option/status-right]]

- ### [`status-right-length`](https://man.openbsd.org/tmux#status-right-length)
	- A [[tmux]] session option setting the maximum width, in columns, of the right component of the [[tmux/Status Line]]. The default is `40`.
	- Like [[tmux/Option/status-left-length]] it caps rather than reserves, and it keeps the first N characters — so lowering it below what [[tmux/Option/status-right]] expands to removes the trailing date and time before it touches the pane title sitting in front of them. Shorten the `#{=21:pane_title}` cell first, then bring this cap down to match.
	- ## Usage
		- ~~~sh
		  tmux show-options -gv status-right-length
		  tmux set-option -g status-right-length 30
		  ~~~
		- Measure what `status-right` wants before choosing a cap:
			- ~~~sh
			  tmux display-message -p '#{w:#{T:status-right}}'
			  ~~~
