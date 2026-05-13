- [[Keyshort]] [[yazi]] [[yazi/Keyshort]]
	- **Sort by birth time (normal order)** #card
	  card-last-interval:: 31.36
	  card-repeats:: 4
	  card-ease-factor:: 2.8
	  card-next-schedule:: 2026-06-13T16:40:18.575Z
	  card-last-reviewed:: 2026-05-13T08:40:18.576Z
	  card-last-score:: 5
		- Shortcut: `,` `b` (comma, then lowercase `b`)
		- Context: File list / manager pane (default keymap)
		- Description: Runs `sort btime --reverse=no` and sets **linemode** to `btime`. Pair with `,` `B` for reversed order. Birth time availability depends on the filesystem. See [keymap — mgr.sort](https://yazi-rs.github.io/docs/configuration/keymap/#mgrsort) and [preset keymap-default.toml](https://github.com/sxyazi/yazi/blob/shipped/yazi-config/preset/keymap-default.toml).
		- [[My Notes]] it seems a bit funny to call it "birth" time, when most programs call it "creation" time
	- **Sort by birth time (reverse order)** #card
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.22
	  card-next-schedule:: 2026-05-14T04:00:00.000Z
	  card-last-reviewed:: 2026-05-13T08:39:24.472Z
	  card-last-score:: 1
		- Shortcut: `,` `B` (comma, then uppercase `B` / Shift+b)
		- Context: File list / manager pane (default keymap)
		- Description: Runs `sort btime --reverse=yes` and sets **linemode** to `btime`. See [preset keymap-default.toml](https://github.com/sxyazi/yazi/blob/shipped/yazi-config/preset/keymap-default.toml).