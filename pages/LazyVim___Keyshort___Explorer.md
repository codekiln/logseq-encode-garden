- [[Keyshort]] [[LazyVim]] [[LazyVim/Keyshort]]
	- **Open the File Explorer at the Project Root** [[Card]]
	  card-last-interval:: 3.94
	  card-repeats:: 1
	  card-ease-factor:: 2.36
	  card-next-schedule:: 2026-09-10T08:16:05.102Z
	  card-last-reviewed:: 2026-09-06T10:16:05.103Z
	  card-last-score:: 3
		- Shortcut: `<leader>e`
		- Description: Opens the [[nvim/Plugin/snacks.nvim]] explorer sidebar rooted at the detected project root.
	- **Open the File Explorer at the Working Directory** [[Card]]
	  card-last-interval:: 3.94
	  card-repeats:: 1
	  card-ease-factor:: 2.36
	  card-next-schedule:: 2026-09-10T08:57:56.021Z
	  card-last-reviewed:: 2026-09-06T10:57:56.021Z
	  card-last-score:: 3
		- Shortcut: `<leader>E`
		- Description: opens the [[nvim/Plugin/snacks.nvim]] explorer, rooted at the current working directory rather than the project root
	- **Close the File Explorer** [[Card]]
		- Shortcut: `q`
		- Description: Cancels the [[nvim/Plugin/snacks.nvim]] explorer picker and closes the sidebar. The explorer opens focused on its list window, where both `q` and `<Esc>` are bound to cancel. From the input box, `<Esc>` first leaves insert mode, so it takes a second press to close.
	- [[My Note]]
		- `<leader>fe` and `<leader>fE` are aliases of these two keys.
		- The snacks explorer is a picker in a sidebar, so the picker's own search and filter keys work inside it.
		- `<leader>e` does not toggle. Pressing it again while the sidebar is open reopens and refocuses it rather than closing it.
		- `<C-c>` does not cancel here. The explorer rebinds it to `tcd`, which changes the tab's working directory to the selected entry.