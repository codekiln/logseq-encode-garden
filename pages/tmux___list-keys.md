logseq-entity:: [[Logseq/Entity/CLI/Command]]

- # [tmux list-keys](https://man.openbsd.org/tmux.1#list-keys)
	- **Usage**: `list-keys [-1aN] [-P prefix-string] [-T key-table] [key]`
	- **Aliases**: `lsk`
	- List key bindings. Two forms:
		- Default: lists all bindings as `bind-key` commands (suitable for `.tmux.conf`). All key tables are shown unless `-T key-table` is given.
		- `-N`: shows only bindings with attached notes; only root and prefix tables by default. This is what `prefix ?` (`C-b ?`) runs internally.
	- **Flags**
		- `-T key-table` — restrict output to a single table (e.g. `prefix`, `root`, `copy-mode`, `copy-mode-vi`).
		- `-N` — show only noted bindings; output is `key   note` format.
		- `-a` — with `-N`, include bindings that lack a note (shows command instead of skipping).
		- `-1` — print only the first matching key.
		- `-P prefix-string` — prepend a string before each key in the output.
