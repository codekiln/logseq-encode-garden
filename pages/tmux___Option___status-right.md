logseq-entity:: [[Logseq/Entity/Software/Option]]
see-also:: [[tmux/Option/status-right-length]]

- ### [`status-right`](https://man.openbsd.org/tmux#status-right)
	- A [[tmux]] session option holding the format string drawn at the right end of the [[tmux/Status Line]]. The default shows the [[tmux/Pane/Title]] in double quotes, then the time and the date:
		- ~~~
		  #{?window_bigger,[#{window_offset_x}#,#{window_offset_y}] ,}"#{=21:pane_title}" %H:%M %d-%b-%y
		  ~~~
	- The `#{=21:pane_title}` cell caps the pane title at twenty-one characters inside the format string, independent of [[tmux/Option/status-right-length]]. Shortening that number is what narrows the right end; lowering the length cap on its own takes the date and time away instead.
	- Once a pane title is long enough to reach the cell cap, the whole expansion is 39 columns wide — near enough the default `status-right-length` of `40` that the right end runs at full width all the time.
	- ## Usage
		- Show it, and measure what it currently wants:
			- ~~~sh
			  tmux show-options -gv status-right
			  tmux display-message -p '#{w:#{T:status-right}}'
			  ~~~
		- Return eleven columns to the window list by shortening the title cell — 39 columns become 28:
			- ~~~sh
			  set -g status-right '"#{=10:pane_title}" %H:%M %d-%b-%y'
			  set -g status-right-length 30
			  ~~~
