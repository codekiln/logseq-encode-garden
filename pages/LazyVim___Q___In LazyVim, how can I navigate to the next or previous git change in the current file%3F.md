logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[LazyVim/Keyshort/Git]]

- # In LazyVim, how can I navigate to the next or previous git change in the current file?
	- ## [[AI Answer]]
		- **Short answer:** `]h` jumps to the next git hunk in the current buffer and `[h` jumps to the previous one. Hunks are the changed blocks that [[nvim/Plugin/gitsigns.nvim]] marks in the sign column against the git index.
		- ### Keys
			- `]h` — next hunk
			- `[h` — previous hunk
			- `]H` — last hunk in the file
			- `[H` — first hunk in the file
		- ### Where the keys come from
			- [[LazyVim]] binds these in the gitsigns `on_attach` hook, so they exist in any buffer that sits inside a git repository. [[Answer/Official]] from [LazyVim gitsigns keymaps](https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/plugins/editor.lua).
			- The Ex form is `:Gitsigns next_hunk` and `:Gitsigns prev_hunk`.
		- ### Inside a diff
			- When the buffer is in diff mode (for example after `:Gitsigns diffthis main`), `]h` and `[h` fall through to Vim's built-in `]c` and `[c` change jumps instead.
		- ### Acting on the hunk you land on
			- `<leader>ghp` — preview the hunk inline
			- `<leader>ghs` — stage the hunk
			- `<leader>ghr` — reset the hunk
			- `<leader>ghb` — blame the line
			- These sit in the same `<leader>gh` group that [[LazyVim/Keyshort/Git]] points to for hunk-level work.
