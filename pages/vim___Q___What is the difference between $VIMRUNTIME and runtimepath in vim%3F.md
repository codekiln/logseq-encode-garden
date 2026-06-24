logseq-entity:: [[Logseq/Entity/Question]]

- # What is the difference between `$VIMRUNTIME` and `runtimepath` in [[vim]]?
	- ## [[AI Answer]]
		- **Short answer:** `$VIMRUNTIME` is a single directory pointing to vim's built-in files; `runtimepath` is the full ordered list of directories vim searches for all runtime content, with `$VIMRUNTIME` as one entry in that list.
		- `$VIMRUNTIME` is set automatically by vim to the directory containing its **core installation files** — syntax definitions, help docs, filetype plugins, color schemes that ship with vim (e.g. `/usr/share/vim/vim91`). It is a single, fixed path.
		- `runtimepath` (abbreviated `rtp`) is a **comma-separated list** of directories vim scans in order when loading plugins, autoload files, syntax files, ftplugins, and more. The list typically looks like:
			- `~/.vim` (or `~/.config/nvim`) first — your personal config
			- Plugin manager paths (e.g. `~/.vim/plugged/...`) next
			- `$VIMRUNTIME` somewhere in the middle — vim's own built-ins
			- System-wide plugin dirs last
		- So `:echo $VIMRUNTIME` returns **one** path (where vim itself lives), while `:set runtimepath?` returns **many** paths — the full load order reflecting your plugins and configuration.
		- **Practical implication:** if you want to know where vim's built-in `syntax/python.vim` lives, `$VIMRUNTIME` tells you directly. If you want to know *which* `syntax/python.vim` vim will actually load (yours vs the built-in), you need `runtimepath` — vim picks the first match it finds walking the list left to right.
