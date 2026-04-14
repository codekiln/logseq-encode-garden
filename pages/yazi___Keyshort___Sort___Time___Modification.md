- [[Keyshort]] [[yazi]] [[yazi/Keyshort]]
	- **Sort by modification time (normal order)** #card
	  card-last-interval:: 5.08
	  card-repeats:: 2
	  card-ease-factor:: 2.6
	  card-next-schedule:: 2026-04-19T08:52:28.799Z
	  card-last-reviewed:: 2026-04-14T07:52:28.799Z
	  card-last-score:: 5
		- Shortcut: `,` `m` (comma, then lowercase `m`)
		- Context: File list / manager pane (default keymap)
		- Description: Runs `sort mtime --reverse=no` and sets **linemode** to `mtime` so each row shows last modified time. Pair with `,` `M` for reversed order. See [keymap — mgr.sort](https://yazi-rs.github.io/docs/configuration/keymap/#mgrsort) and [preset keymap-default.toml](https://github.com/sxyazi/yazi/blob/shipped/yazi-config/preset/keymap-default.toml).
		- [[My Notes]]
			- `,` is the sorting leader in yazi - brings up a panel pop up [[Modal]] at the bottom of the screen which has 13 options for sorting.
	- **Sort by modification time (reverse order)** #card
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-04-03T04:00:00.000Z
	  card-last-reviewed:: 2026-04-02T06:27:18.387Z
	  card-last-score:: 1
		- Shortcut: `,` `M` (comma, then uppercase `M` / Shift+m)
		- Context: File list / manager pane (default keymap)
		- Description: Runs `sort mtime --reverse=yes` and sets **linemode** to `mtime`. Use when you want the opposite mtime ordering from `,` `m`. See [preset keymap-default.toml](https://github.com/sxyazi/yazi/blob/shipped/yazi-config/preset/keymap-default.toml).