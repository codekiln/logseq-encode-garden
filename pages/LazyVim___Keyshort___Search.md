- [[Keyshort]] [[LazyVim]] [[LazyVim/Keyshort]]
	- **Find Files in the Project Root** [[Card]]
		- Shortcut: `<leader>ff`
		- Description: Fuzzy file picker scoped to the detected root. `<leader>fF` searches the current working directory instead, and `<leader>fg` restricts it to git-tracked files.
	- **Grep the Project Root** [[Card]]
		- Shortcut: `<leader>/`
		- Description: Live grep across the root directory, backed by [[ripgrep]]. `<leader>sg` is the same picker on a mnemonic chord; `<leader>sG` greps the current working directory.
		- [[LazyVim/Tutorial/Search for a Phrase Across Files]] walks through phrase matching, literal punctuation, both directory scopes, and hidden or ignored files.
	- **Search the Word Under the Cursor** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-04T04:00:00.000Z
	  card-last-reviewed:: 2026-09-03T10:39:36.853Z
	  card-last-score:: 1
		- Shortcut - for the **word** under the **cursor** or the **visual selection**, grep for the word
			- `<leader>sw` - grep is scoped to files from the git root
				- [[Mnemonic]]
					- ==s==earch ==w==ord - sw
			- `<leader>sW` - grep scoped to files in the current working directory
				- [[Mnemonic]]
					- ==s==earch word ==W==orking directory - `sW`
	- **Search and Replace Across Files** [[Card]]
		- Shortcut: `<leader>sr`
		- Description: Opens [[nvim/Plugin/grug-far.nvim]], a buffer-based find-and-replace over the project with a live preview of every hit before anything is written.
	- **Find a Config File** [[Card]]
		- Shortcut: `<leader>fc`
		- Description: File picker rooted at the Neovim config directory — the fast way into `lua/config/keymaps.lua` or `lua/plugins/extras.lua`.
	- **Search All Keymaps** [[Card]]
		- Shortcut: `<leader>sk`
		- Description: Picker over every active mapping with its description. The way to answer "what is this key bound to" without leaving the editor.
	- **Search Command History** [[Card]]
		- Shortcut: `<leader>sc`
		- Description: Picker over previously run Ex commands. `<leader>s/` does the same for search history.
	- **View All Marks** [[Card]]
		- Shortcut: `<leader>sm`
		- Description: Picker listing every set mark with its file and line, so marks stay usable without memorising which letter went where.
	- **Search TODO and FIXME Comments** [[Card]]
		- Shortcut: `<leader>st`
		- Description: Picker over comment keywords found by [[nvim/Plugin/todo-comments.nvim]]. `<leader>sT` narrows to `TODO,FIX,FIXME`; `]t` / `[t` step between them in the buffer.
	- [[My Note]]
		- Every picker here is [[nvim/Plugin/snacks.nvim]]'s, not [[Telescope]] or fzf-lua — no editor extra is enabled, so LazyVim falls back to its built-in snacks picker. Cheat sheets written against the Telescope or fzf-lua extras list `<leader>ss` for symbol search; that mapping does not exist here (see [[LazyVim/Keyshort/Code Action]] for `<leader>cs`).
		- `<leader>sR` resumes the last picker with its query intact.
