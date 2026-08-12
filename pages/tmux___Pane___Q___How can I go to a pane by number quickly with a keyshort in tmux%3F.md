logseq-entity:: [[Logseq/Entity/Question]]

- # How can I go to a [[tmux/Pane]] by number quickly with a [[Keyshort]] in [[tmux]]?
	- ## [[AI Answer]]
		- **Short answer:** press [[tmux/Prefix]] then `q` — tmux overlays each pane's number, and pressing that digit while the overlay is shown jumps straight to it.
		- ### How it works
			- `<prefix> q` runs tmux's `display-panes` command, which briefly shows each pane's number and temporarily binds digits `0`–`9` to `select-pane`. Press the digit before the overlay disappears (default `display-panes-time` is `1000` ms) to switch to that pane.
			- ~~~sh
			  tmux display-panes
			  ~~~
		- ### Sources
			- [[Answer/Official]] from [tmux(1) man page](https://man.openbsd.org/tmux.1)
