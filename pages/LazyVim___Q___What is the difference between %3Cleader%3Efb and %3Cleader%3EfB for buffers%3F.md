logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[LazyVim/Keyshort/Buffer]]

- # What is the difference between `<leader>fb` and `<leader>fB` for buffers?
	- ## [[AI Answer]]
		- **Short answer:** `<leader>fb` shows the files you have open. `<leader>fB` shows those plus everything else vim is holding on the side — help pages, plugin panels, the startup screen.
		- **Why there are two lists**
			- When you open a file, vim loads the text into memory and keeps it there after you switch away. That copy in memory is a buffer.
			- Vim uses buffers for things that are not your files as well. A `:help` page is a buffer, a plugin's sidebar is a buffer, the startup screen is a buffer. A popup that listed every one of those would bury the files you are actually working on.
			- So vim marks each buffer two ways, and the ordinary list uses the marks to skip the clutter:
				- whether the buffer belongs in your working set of files — on when you open a file, off for help pages and plugin windows
				- whether a real file sits behind the text — the startup screen and most plugin panels have none
			- `<leader>fb` shows the buffers that pass both marks. `<leader>fB` ignores both marks and shows everything, which is what the menu means by `Buffers (all)`.
		- **In the [[nvim/Plugin/snacks.nvim]] picker, the one a stock install uses**
			- ~~~lua
			  { "<leader>fb", function() Snacks.picker.buffers() end, desc = "Buffers" },
			  { "<leader>fB", function() Snacks.picker.buffers({ hidden = true, nofile = true }) end, desc = "Buffers (all)" },
			  ~~~
			- `hidden = true` skips the check on the first mark, `nofile = true` skips the check on the second. Both start off, so `<leader>fb` is the same picker with nothing waived. The marks are vim's `'buflisted'` and `'buftype'` settings, under `:help buflisted` and `:help buftype`.
			- Both keys behave the same in three other ways: they include the file you are currently in, they include files vim has unloaded from memory but still remembers, and they sort by what you touched most recently.
			- `<leader>,` opens the same list as `<leader>fb` — two keystrokes instead of three.
		- **Other search popups split the pair differently**
			- With `fzf-lua`, both keys list the same buffers and only the sort order differs.
			- With telescope, `<leader>fb` leaves out the file you are currently in, so there `<leader>fB` is mainly how you get back to it.
			- The `(all)` label describes what snacks does, which is what runs unless a picker was swapped in.
		- **When to reach for `<leader>fB`:** something you know is open fails to appear under `<leader>fb` — you were reading `:help`, or it belongs to a plugin panel.
		- [[Answer/Official]] from [LazyVim Keymaps](https://www.lazyvim.org/keymaps), read against `lua/lazyvim/plugins/extras/editor/snacks_picker.lua` and `lua/snacks/picker/source/buffers.lua` in the installed plugins.
