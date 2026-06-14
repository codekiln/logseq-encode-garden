logseq-entity:: [[Logseq/Entity/Question]]

- # In [[yazi]], if nvim is my `$EDITOR`, is there a key which can open it up in my editor in read-only mode?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** No built-in default key exists for this. Add a custom `shell` binding that calls `nvim -R` with the `%h` placeholder (hovered file path).
			- **Why there's no default key:** Yazi's default opener for text files runs `${EDITOR:-vi} %s` (writable). The default keymap binds `o` / `<Enter>` to `open` (which triggers that opener), and `O` / `<S-Enter>` to `open --interactive`. Neither has a read-only variant out of the box.
			- **Checking the default `[mgr]` keymap:** `e` is not mapped; `r` is mapped to `rename`. So `e` alone is a clean, free key in `[mgr]`.
			- **Add a key binding** in `~/.config/yazi/keymap.toml`:
			- ~~~toml
			  [[mgr.prepend_keymap]]
			  on   = "e"
			  run  = "shell 'nvim -R %h' --block"
			  desc = "Open hovered file in nvim read-only"
			  ~~~
			- `%h` expands to the hovered file's path (shell-quoted automatically). `--block` suspends yazi until nvim exits.
			- **Chord alternative:** `on = [ "e", "r" ]` is a single chord binding (press `e` then `r` in sequence, like `[ "g", "g" ]`). It does not conflict with standalone `r → rename` since yazi only enters chord mode after the first key.
			- **Alternative — use `view`:** nvim ships a `view` alias that is identical to `nvim -R`:
			- ~~~toml
			  [[mgr.prepend_keymap]]
			  on   = [ "e", "r" ]
			  run  = "shell 'view %h' --block"
			  desc = "Open hovered file in view (nvim read-only)"
			  ~~~
			- Docs: [keymap — shell](https://yazi-rs.github.io/docs/configuration/keymap/#mgr.shell), [yazi-default.toml opener.edit](https://github.com/sxyazi/yazi/blob/shipped/yazi-config/preset/yazi-default.toml)
