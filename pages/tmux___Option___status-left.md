logseq-entity:: [[Logseq/Entity/Software/Option]]
see-also:: [[tmux/Option/status-left-length]]

- ### [`status-left`](https://man.openbsd.org/tmux#status-left)
	- A [[tmux]] session option holding the format string drawn at the left end of the [[tmux/Status Line]]. The default is `[#{session_name}] `, which is how the [[tmux/session/Name]] comes to sit there.
	- The string is expanded as a format and passed through `strftime(3)`, so date and time specifiers work inside it.
	- Its width is bounded by [[tmux/Option/status-left-length]].
	- ## Usage
		- Show the raw format string:
			- ~~~sh
			  tmux show-options -gv status-left
			  ~~~
		- Expand it uncapped, and measure the columns it wants:
			- ~~~sh
			  tmux display-message -p '#{T:status-left}'
			  tmux display-message -p '#{w:#{T:status-left}}'
			  ~~~
		- Spend every column on the name by dropping the brackets:
			- ~~~sh
			  set -g status-left '#{session_name} '
			  ~~~
	- ## Per-cell width inside the format
		- A `=N:` limit written inside the format string bounds a single cell on its own, independent of `status-left-length`: `#{=20:session_name}` shows at most twenty characters of the name however high the length cap goes. Raising the length cap while such a limit is in place changes nothing.
		- The stock `status-left` carries no per-cell limit, so `status-left-length` is the only bound on the session name. [[tmux/Option/status-right]] is the contrasting case — its default does cap a cell this way.
