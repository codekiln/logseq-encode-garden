logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[vim/Keyshort/Indent]], [[Logseq/Flavored Markdown]]

- # Does [[LazyVim]] support indenting with tabs the way [[Logseq]] expects? If so, how do I indent and de-indent with tabs in markdown?
	- ## [[AI Answer]]
		- **Short answer:** Not out of the box. [[Logseq]] writes one literal tab per nesting level, but [[LazyVim]] opens markdown with `expandtab` on and `shiftwidth=2`, so `>>` inserts two spaces. Drop an `.editorconfig` with `indent_style = tab` at the graph root and the same keys — `>>` / `<<`, visual `>` / `<`, insert-mode `Ctrl-T` / `Ctrl-D` — start writing real tabs.
		- ### Why the default is spaces
			- Neovim's own `ftplugin/markdown.vim` would force `setlocal expandtab tabstop=4 softtabstop=4 shiftwidth=4`, but only when `g:markdown_recommended_style` is truthy.
			- [[LazyVim]] sets `vim.g.markdown_recommended_style = 0` in `lua/lazyvim/config/options.lua`, so markdown buffers skip that block and simply inherit LazyVim's globals from the same file: `expandtab = true`, `shiftwidth = 2`, `tabstop = 2`, `smartindent = true`.
			- Net effect in a markdown buffer: `expandtab` on, `shiftwidth=2`, `tabstop=2`, `softtabstop=0` — two spaces per level. `:verbose set expandtab?` reports `ftplugin.vim` as the last setter.
		- ### Switching the graph to tabs
			- [[Answer/Official]] from [`:help editorconfig`](https://neovim.io/doc/user/editorconfig.html): "after running ftplugins and FileType autocommands, the EditorConfig feature searches all parent directories of that file for `.editorconfig` files, parses them, and applies their properties." Running last is what makes it win over both the runtime ftplugin and the LazyVim globals. An `.editorconfig` at the graph root scopes the change to the graph and carries to other editors:
				- ~~~ini
				  [*.md]
				  indent_style = tab
				  ~~~
			- With that in place `>>` on a bullet writes a literal `\t`, and `:verbose set expandtab?` names `editorconfig.lua` as the setter.
			- **Per-machine alternative** — `~/.config/nvim/after/ftplugin/markdown.lua` with `vim.opt_local.expandtab = false`. Simpler, but it applies to *every* markdown file, not just the graph.
			- Keep `shiftwidth` equal to `tabstop` and leave `softtabstop=0`, so one indent level is exactly one tab and Vim never pads a level with a mix of tabs and spaces.
		- ### Indenting and de-indenting
			- **Normal mode:** `>>` indents the line one level, `<<` outdents. Take a count or a motion for more: `3>>` for three lines, `>ip` for the paragraph. See [[vim/Keyshort/Indent]].
			- **Visual mode:** `V` to select whole lines, then `>` / `<`. [[LazyVim]] remaps these to `>gv` / `<gv` in `lua/lazyvim/config/keymaps.lua`, so the selection survives the shift — `>>>` walks a whole subtree out three levels without reselecting.
			- **Insert mode:** `Ctrl-T` indents and `Ctrl-D` outdents the current line. This is the closest analogue to Logseq's Tab / Shift-Tab, and it beats `<Tab>` in practice because it works from anywhere in the line rather than only at column 1. Neither key is remapped by [[LazyVim]].
			- **Insert-mode `<Tab>`** at the start of a line does insert one indent level, but `blink.cmp` claims `<Tab>` first for completion accept and snippet jumps and only falls through to a literal tab when no menu is open — so it is the least predictable of the three.
			- `>` and `<` shift the entire line including the `-` bullet marker, which is exactly the nesting move Logseq performs.
			- `:set list` renders tabs as visible glyphs, useful for confirming a page really uses tabs rather than spaces.
