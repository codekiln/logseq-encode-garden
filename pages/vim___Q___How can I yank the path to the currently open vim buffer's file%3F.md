logseq-entity:: [[Logseq/Entity/question]]
via:: [[2026-04-01 Wed]]

- # How can I yank the path to the currently open [[vim]] buffer's file?
	- ## My Notes
		- Added `yp` to yank the absolute path to a file in the [[Clipboard]] in [[Beads]] for [[dotfiles]]
		- ```
		  ○ dotfiles-han · nvf: map yp to yank current buffer absolute path to system clipboard   [● P2 · OPEN]
		  Owner: codekiln · Type: feature
		  Created: 2026-04-01 · Updated: 2026-04-01
		  
		  DESCRIPTION
		  Add a normal-mode mapping yp in the Home Manager nvf setup (nix/home/nvf.nix) that copies the
		  absolute filesystem path of the current buffer to the system clipboard (and the default register),
		  similar to Vim's :let @+=expand('%:p') / nvim_buf_get_name(0) workflow.
		  
		  Acceptance: yp in a normal file buffer puts the full path on the OS clipboard; behavior for unnamed
		  or special buffers is defined (message, no-op, or fallback) and documented in code comments if non-
		  obvious.
		  
		  
		  ACCEPTANCE CRITERIA
		  yp copies expand('%:p') (or equivalent) to + register / clipboard on macOS/Linux builds
		  
		  
		  LABELS: neovim, nvf
		  
		  
		  ```
	- ## Answer
		- [[AI/Response]]
			- **Registers:** The read-only **`%`** register holds the **current buffer’s file name** (as stored by Vim), not a full path unless the buffer was opened with one. See [`:help quote_%`](https://vimhelp.org/change.html#quote_%25).
			- **Full path into a register or clipboard (Ex):** Use **`expand()`** so you control modifiers (`:p` absolute, `:h` directory, `:t` tail). Examples (press Enter after each):
				- `:let @+ = expand('%:p')` — full path into the **`+`** register (system clipboard when `+clipboard` is available).
				- `:let @" = expand('%:p')` — full path into the **unnamed** register; then paste with `p` / `P`.
				- `:call setreg('+', expand('%:p'))` — same idea, works in Vim and [[nvim]].
			- **Insert / command line without a mapping:** In **Insert mode** or **Command-line mode**, **`Ctrl-r %`** inserts the contents of the **`%`** register (the file name as Vim knows it). For a full path you still want **`Ctrl-r =expand('%:p')`** then Enter (expression register).
			- **[[nvim]] Lua (optional):** `vim.fn.setreg('+', vim.fn.expand('%:p'))` or `vim.api.nvim_buf_get_name(0)` for the buffer’s path string inside scripts.
			- **Handy mapping pattern:** `nnoremap <leader>yp :let @+ = expand('%:p')<CR>:echo 'Copied: ' . @+<CR>` (adjust `<leader>` as you like).
			- **Caveats:** **`%`** for a **new, unsaved buffer** may be empty or not what you expect; **`expand('%:p')`** follows Vim’s usual name rules. For paths with spaces, the copied string is still one line of plain text.
			- [Vim help: `quote_%` (filename register)](https://vimhelp.org/change.html#quote_%25)
			- [Vim help: `expand()`](https://vimhelp.org/builtin.html#expand())
	- ## Related
		- [[nvim/Q/What does " mean in nvim?]] — register overview including **`%`**