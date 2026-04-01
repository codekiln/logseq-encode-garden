logseq-entity:: [[Logseq/Entity/question]]
via:: [[2026-03-28 Sat]]

- # How can I view file modification times in [[yazi]]?
	- ## Answer
		- [[AI/Response]]
			- Use **line mode** so each row in the file list shows metadata on the right. Set **`[mgr] linemode = "mtime"`** in `~/.config/yazi/yazi.toml` to show **last modified time** for files.
			- Other built-in values include **`"none"`**, **`"size"`**, **`"btime"`** (birth time), **`"permissions"`**, and **`"owner"`** (Unix), per [yazi.toml | Yazi — mgr.linemode](https://yazi-rs.github.io/docs/configuration/yazi/#mgrlinemode).
			- **Interactive / keymap:** the **`linemode`** action accepts the same mode names (e.g. `linemode mtime`). Bind it in `keymap.toml` if you want to cycle modes without editing config ([keymap — mgr.linemode](https://yazi-rs.github.io/docs/configuration/keymap/#mgrlinemode)).
			- **Sorting by mtime:** that is separate from display — use **`[mgr] sort_by = "mtime"`** (or the **`sort`** action) if you want the listing ordered by modification time.
			- [[yazi/Plugin/spotter]] **Spotter:** **`spot`** (default **Tab** in the preset map) opens the file-information spotter for more detail on the hovered file.
	- ## My Notes
		- *placeholder*