logseq-entity:: [[Logseq/Entity/question]], [[Logseq/Entity/Card]]
see-also:: [[glow]], [[vim/Q/How can I get a VS Code-style split Markdown preview in (neo-)vim that renders in the terminal (e.g. glow)?]]

- # Is there a quick way to use [[glow]] to preview the current [[Markdown]] file while editing in [[nvim]]? [[card]]
	- ## [[My Answer]]
		- ### Haven't found a good answer to this yet
			- I'm looking for something in vim that displays markdown as well as glow for flipping between reading mode and editing mode.
		- ### Current Workaround - vsplit
			- `:vsplit | terminal glow -p %` opens a vertical split using [[nvim]]'s built-in terminal buffer, which renders [[glow]]'s [[ANSI]] output properly.
			- ### Extra
				- To map it to `<leader>mg`, add to `init.lua`:
					- ~~~lua
					  vim.keymap.set('n', '<leader>mg', ':vsplit | terminal glow -p %<CR>',
					    { desc = 'Glow markdown preview' })
					  ~~~
				- Press `q` to quit the [[glow]] pager, then `<C-w>c` to close the split.
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** `:vsplit | terminal glow -p %` — opens a vertical split and pipes the file through [[glow]] in [[nvim]]'s terminal buffer, which renders [[ANSI]] output properly. `:!glow %` runs [[glow]] outside the [[nvim]] UI and produces no visible output inside the editor.
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
				- [[nvim/Plugin/render-markdown.nvim]] renders Markdown decorations inline using Neovim's virtual-text UI — no external CLI needed, and it updates as you type.
			- ### Sources
				- [Haylin Moore — nvim keybind for rendering markdown in glow](https://hayl.in/posts/nvim-glow/)
				- [[nvim/Plugin/render-markdown.nvim]]