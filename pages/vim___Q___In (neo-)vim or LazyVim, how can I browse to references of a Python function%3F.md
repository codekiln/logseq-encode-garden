logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[LazyVim/Keyshort/LSP/Navigation]], [[vim/Neovim/Report/Find Usages and Copy Python Dotted Path - Deep Research]]

- # In (neo-)vim or LazyVim, how can I browse to references of a [[Python]] function?
	- ## [[AI Answer]]
		- Short answer: put the cursor on the function name and press `gr` — this is [[LazyVim]]'s default keymap for "Go to References", backed by the attached [[LSP]] (`pyright`/`basedpyright` for [[Python]]).
		- [[Answer/Official]] from [LazyVim Keymaps](https://www.lazyvim.org/keymaps):
			- `gr` — References (normal mode)
			- Related navigation: `gd` Go to Definition, `gD` Go to Declaration, `gI` Go to Implementation, `gy` Go to Type Definition
			- `]]` / `<a-n>` and `[[` / `<a-p>` step to the next/previous reference once a references list is open
		- Steps:
			- 1. Confirm a Python LSP is attached with `:LspInfo` (install `pyright` or `basedpyright` via `:Mason` if missing).
			- 2. Put the cursor on the function name.
			- 3. Press `gr` — this opens a picker (Telescope or Snacks, depending on your LazyVim version/config) listing every call site.
			- 4. `<CR>` on an entry jumps there; `<C-o>` jumps back.
		- In plain [[nvim]] without a distro, the equivalent is the built-in `vim.lsp.buf.references()`, which you'd bind to a keymap yourself.
		- For a deeper comparison of plugin stacks and a PyCharm-style "copy dotted reference path" workflow, see [[vim/Neovim/Report/Find Usages and Copy Python Dotted Path - Deep Research]].
