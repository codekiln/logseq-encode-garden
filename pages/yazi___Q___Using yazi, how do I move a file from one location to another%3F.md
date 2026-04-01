logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[yazi/Keyshort]]

- # Using [[yazi]], how do I move a file from one location to another?
	- ## Answer
		- [[AI/Response]]
			- *Yazzi* is almost certainly [[yazi]] (the Rust terminal file manager).
			- **Move to another folder:** select the entry (**Space**, or use visual mode **v**), press **x** to **yank (cut)**, navigate to the target directory (**h** / **j** / **k** / **l** or arrows), then **p** to **paste**. That moves the file or directory from the source path to the destination.
			- **Copy instead of move:** **y** (copy yank), move the cursor to the destination, **p** to paste.
			- **If a same-named file already exists:** **P** (shift+p) pastes with **overwrite**; plain **p** avoids overwriting by renaming (suffix such as `_1`) per default behavior.
			- **Rename without changing folder:** **r** renames the selection in the **current** directory only.
			- **Cancel the pending yank:** **Y** or **X** clears cut/copy state.
			- [Quick Start | Yazi — File operations](https://yazi-rs.github.io/docs/quick-start)
			- [Default `keymap-default.toml` (preset)](https://github.com/sxyazi/yazi/blob/shipped/yazi-config/preset/keymap-default.toml)
	- ## My Notes
		- *placeholder*
