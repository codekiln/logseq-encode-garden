logseq-entity:: [[Logseq/Entity/Question]]

- # How do I activate [[Key/Meta]] 1 through [[Key/Meta]] 7 to select a [[tmux/Pane]] layout?
	- ## [[AI Answer]]
		- **Short answer:** `M-` means **Meta** = `Alt`/`Option` (not `Cmd`). After pressing your prefix, press `Option+1` through `Option+7`.
		- ### Why `Cmd` doesn't work
			- In [[tmux]] binding notation, `M-` is the **Meta** modifier, which maps to `Alt` (or `Option` on macOS) — not `Command`. `Prefix Cmd+1` sends a key tmux does not recognize for these bindings.
		- ### Default layout bindings (`-T prefix`)
			- These are bound in the `prefix` key table, so the sequence is: press `<prefix>`, release, then press the key.
			- | Key | Layout |
			  |-----|--------|
			  | `<prefix>` `Option+1` | `even-horizontal` |
			  | `<prefix>` `Option+2` | `even-vertical` |
			  | `<prefix>` `Option+3` | `main-horizontal` |
			  | `<prefix>` `Option+4` | `main-vertical` |
			  | `<prefix>` `Option+5` | `tiled` |
			  | `<prefix>` `Option+6` | `main-horizontal-mirrored` |
			  | `<prefix>` `Option+7` | `main-vertical-mirrored` |
		- ### macOS terminal requirement
			- The terminal emulator must forward `Option` as a Meta keypress. In **iTerm2**: Preferences → Profiles → Keys → set `Left Option key` to **Esc+** (or `Meta`). In **Terminal.app**: Use Option as Meta key is not supported natively — consider switching to iTerm2.
		- ### Verify the binding is active
			- ~~~sh
			  tmux list-keys -T prefix | grep "M-[1-7]"
			  ~~~
			- If the output is empty, the bindings are not loaded. Source your config:
			- ~~~sh
			  tmux source-file ~/.tmux.conf
			  ~~~
		- ### Sources
			- [tmux(1) man page — KEY BINDINGS](https://man.openbsd.org/tmux.1)
			- [iTerm2 docs — Meta key](https://iterm2.com/documentation-preferences-profiles-keys.html)
