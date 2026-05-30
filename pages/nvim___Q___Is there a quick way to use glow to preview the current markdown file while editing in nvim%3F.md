logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[glow]], [[vim/Q/How can I get a VS Code-style split Markdown preview in (neo-)vim that renders in the terminal (e.g. glow)?]]

- # Is there a quick way to use [[glow]] to preview the current [[Markdown]] file while editing in [[nvim]]? [[card]]
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** yes — `:!glow %` or `:vsplit | terminal glow -p %` both work with zero config.
			- ### Quickest one-liners
				- **`:!glow %`** — runs `glow` on the current file in the shell, shows the rendered output, then returns to nvim. Simple, no split.
				- **`:vsplit | terminal glow -p %`** — opens a vertical split and pipes the file through `glow` in a terminal buffer (paged). Closer to a side-by-side view.
			- ### Add a keybind for repeat use
				- Add to your `init.lua` (or an ftplugin for markdown):
					- ~~~lua
					  vim.keymap.set('n', '<leader>mg', ':vsplit | terminal glow -p %<CR>',
					    { desc = 'Glow markdown preview' })
					  ~~~
				- After pressing `<leader>mg`, press `q` to quit the glow pager, then close the split with `<C-w>c`.
			- ### tmux split (zero Lua)
				- In a tmux session, open a second pane and run `glow -p path/to/file.md` (or use `watchexec`/`entr` to auto-refresh on save). Nothing to configure in nvim.
			- ### Richer in-buffer rendering (no glow process)
				- **[render-markdown.nvim](https://github.com/MeanderingProgrammer/render-markdown.nvim)** renders Markdown decorations inline using Neovim's virtual-text UI — no external CLI needed, and it updates as you type.
			- ### Sources
				- [Haylin Moore — nvim keybind for rendering markdown in glow](https://hayl.in/posts/nvim-glow/)
				- [MeanderingProgrammer/render-markdown.nvim](https://github.com/MeanderingProgrammer/render-markdown.nvim)
