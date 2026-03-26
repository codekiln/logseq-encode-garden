- # Does [[yazi]] have a way to show files or folders that begin with a dot or period, aka hidden files and folders?
- ## Answer
	- [[AI/Response]]
		- Yes. [[yazi]] treats dot-prefixed names as **hidden** and lets you show or hide them interactively and via config.
		- **Toggle in the UI:** Press **`.`** (period) to toggle visibility of hidden files in the current directory listing. Documented under *File operations* in the [Quick Start](https://yazi-rs.github.io/docs/quick-start) (same binding as in the [default keymap preset](https://github.com/sxyazi/yazi/blob/shipped/yazi-config/preset/keymap-default.toml)).
		- **Show hidden by default:** In `~/.config/yazi/yazi.toml`, set `[mgr] show_hidden = true`. The `show_hidden` option under `[mgr]` is documented in [yazi.toml | Yazi](https://yazi-rs.github.io/docs/configuration/yazi/) (`true` = show, `false` = do not show).
		- Example minimal snippet:
			- ~~~
			  [mgr]
			  show_hidden = true
			  ~~~
		- To change the key, override the manager `hidden` action in `keymap.toml` per [keymap docs](https://yazi-rs.github.io/docs/configuration/keymap/).
- ## My Notes
	- *placeholder*
- ## Related
	- [[yazi/Keyshort/Toggle hidden files]]
	- [[yazi/How To/cd to a directory on yazi exit]]
