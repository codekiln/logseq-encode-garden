- [[Keyshort]] [[yazi]] [[yazi/Keyshort]]
	- **Sort by modification time (normal order)** #card
	  card-last-interval:: 90.49
	  card-repeats:: 5
	  card-ease-factor:: 2.9
	  card-next-schedule:: 2026-09-22T18:17:14.100Z
	  card-last-reviewed:: 2026-06-24T07:17:14.100Z
	  card-last-score:: 5
		- Shortcut: `,` `m` (comma, then lowercase `m`)
		- Context: File list / manager pane (default keymap)
		- Description: Runs `sort mtime --reverse=no` and sets **linemode** to `mtime` so each row shows last modified time. Pair with `,` `M` for reversed order. See [keymap — mgr.sort](https://yazi-rs.github.io/docs/configuration/keymap/#mgrsort) and [preset keymap-default.toml](https://github.com/sxyazi/yazi/blob/shipped/yazi-config/preset/keymap-default.toml).
		- [[My Notes]]
			- `,` is the sorting leader in yazi - brings up a panel pop up [[Modal]] at the bottom of the screen which has 13 options for sorting.
	- **Sort by modification time (reverse order)** #card
	  card-last-interval:: 90.49
	  card-repeats:: 5
	  card-ease-factor:: 2.9
	  card-next-schedule:: 2026-09-22T18:17:17.648Z
	  card-last-reviewed:: 2026-06-24T07:17:17.649Z
	  card-last-score:: 5
		- Shortcut: `,` `M` (comma, then uppercase `M` / Shift+m)
		- Context: File list / manager pane (default keymap)
		- Description: Runs `sort mtime --reverse=yes` and sets **linemode** to `mtime`. Use when you want the opposite mtime ordering from `,` `m`. See [preset keymap-default.toml](https://github.com/sxyazi/yazi/blob/shipped/yazi-config/preset/keymap-default.toml).