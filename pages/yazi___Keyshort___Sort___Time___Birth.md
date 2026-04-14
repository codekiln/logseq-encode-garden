- [[Keyshort]] [[yazi]] [[yazi/Keyshort]]
	- **Sort by birth time (normal order)** #card
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-04-03T04:00:00.000Z
	  card-last-reviewed:: 2026-04-02T06:29:04.019Z
	  card-last-score:: 1
		- Shortcut: `,` `b` (comma, then lowercase `b`)
		- Context: File list / manager pane (default keymap)
		- Description: Runs `sort btime --reverse=no` and sets **linemode** to `btime`. Pair with `,` `B` for reversed order. Birth time availability depends on the filesystem. See [keymap — mgr.sort](https://yazi-rs.github.io/docs/configuration/keymap/#mgrsort) and [preset keymap-default.toml](https://github.com/sxyazi/yazi/blob/shipped/yazi-config/preset/keymap-default.toml).
	- **Sort by birth time (reverse order)** #card
	  card-last-interval:: 4
	  card-repeats:: 2
	  card-ease-factor:: 2.36
	  card-next-schedule:: 2026-04-18T07:51:08.691Z
	  card-last-reviewed:: 2026-04-14T07:51:08.691Z
	  card-last-score:: 3
		- Shortcut: `,` `B` (comma, then uppercase `B` / Shift+b)
		- Context: File list / manager pane (default keymap)
		- Description: Runs `sort btime --reverse=yes` and sets **linemode** to `btime`. See [preset keymap-default.toml](https://github.com/sxyazi/yazi/blob/shipped/yazi-config/preset/keymap-default.toml).