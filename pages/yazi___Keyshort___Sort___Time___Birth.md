- [[Keyshort]] [[yazi]] [[yazi/Keyshort]]
	- **Sort by birth time (normal order)** #card
	  card-last-interval:: 10.36
	  card-repeats:: 3
	  card-ease-factor:: 2.7
	  card-next-schedule:: 2026-05-02T16:40:51.280Z
	  card-last-reviewed:: 2026-04-22T08:40:51.280Z
	  card-last-score:: 5
		- Shortcut: `,` `b` (comma, then lowercase `b`)
		- Context: File list / manager pane (default keymap)
		- Description: Runs `sort btime --reverse=no` and sets **linemode** to `btime`. Pair with `,` `B` for reversed order. Birth time availability depends on the filesystem. See [keymap — mgr.sort](https://yazi-rs.github.io/docs/configuration/keymap/#mgrsort) and [preset keymap-default.toml](https://github.com/sxyazi/yazi/blob/shipped/yazi-config/preset/keymap-default.toml).
		- [[My Notes]] it seems a bit funny to call it "birth" time, when most programs call it "creation" time
	- **Sort by birth time (reverse order)** #card
	  card-last-interval:: 8.88
	  card-repeats:: 3
	  card-ease-factor:: 2.22
	  card-next-schedule:: 2026-04-24T04:25:49.680Z
	  card-last-reviewed:: 2026-04-15T07:25:49.680Z
	  card-last-score:: 3
		- Shortcut: `,` `B` (comma, then uppercase `B` / Shift+b)
		- Context: File list / manager pane (default keymap)
		- Description: Runs `sort btime --reverse=yes` and sets **linemode** to `btime`. See [preset keymap-default.toml](https://github.com/sxyazi/yazi/blob/shipped/yazi-config/preset/keymap-default.toml).