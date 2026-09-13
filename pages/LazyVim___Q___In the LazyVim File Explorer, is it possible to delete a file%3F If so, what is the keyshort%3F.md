logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[nvim/Plugin/snacks.nvim]]

- # In the [[LazyVim]] File Explorer, is it possible to delete a file? If so, what is the keyshort?
	- ## [[AI Answer]]
		- Short answer: yes. In the [[nvim/Plugin/snacks.nvim]] explorer sidebar (`<leader>e`), press `d` to delete the file (or files) under the cursor / current selection.
		- `d` runs the `explorer_del` action, which prompts for confirmation (`Delete <path>?`) before acting, then moves the item to the system trash rather than permanently deleting it, and closes any open buffer for that file.
		- Related explorer keys on the same list: `a` add, `r` rename, `c` copy, `m` move, `y` / `p` yank / paste.
		- Confirmed by reading the plugin source directly (no official doc page lists this): `lua/snacks/picker/config/sources.lua` binds `["d"] = "explorer_del"` for the `explorer` source's `win.list.keys`; `lua/snacks/explorer/actions.lua` (`M.actions.explorer_del`) confirms via `Snacks.picker.util.confirm`, calls `M.trash(path)`, and force-deletes the buffer with `Snacks.bufdelete`.
