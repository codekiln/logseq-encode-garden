logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[LazyVim/Keyshort/LSP/Navigation]]
- # In [[LazyVim]], how can I traverse wiki links in an [[Obsidian]] knowledge garden?
	- ## [[AI Answer]]
		- **Short answer:** the current dotfiles already enable [[LazyVim/plugins/extras/lang/markdown]], which configures the Marksman language server. Open the garden from its root with `nvim .`, place the cursor inside a wiki link, and press `gd`. Use `<C-o>` to return to the previous location and `<C-i>` to move forward again. Press `gr` on a link to list references to its destination.
		- **Why it works:** LazyVim maps `gd` to the attached language server's “go to definition” action and `gr` to “references.” Marksman supports those actions for ordinary Markdown links and wiki links, including links to headings. [[Answer/Official]] from [LazyVim's LSP documentation](https://www.lazyvim.org/plugins/lsp) and the [Marksman README](https://github.com/artempyanykh/marksman).
		- **Setup and checks:**
			- 1. Start Neovim at the vault root: `cd /path/to/vault && nvim .`.
			- 2. Run `:LazyExtras` and check that `lang.markdown` is enabled. The current dotfiles already import this extra, and the installed Marksman reports version `2026-02-08`. [[Answer/Official]] from [LazyVim's Markdown extra](https://www.lazyvim.org/extras/lang/markdown).
			- 3. If `gd` does nothing, use `<leader>cl` to open LazyVim's LSP information and check that Marksman is attached to the Markdown buffer. `:Mason` shows whether the server is installed.
			- 4. If links work only within one file, make the vault a Marksman project by putting an empty `.marksman.toml` at its root or keeping it as a Git repository. This garden is already a Git repository. [[Answer/Official]] from the [Marksman FAQ](https://github.com/artempyanykh/marksman#faq).
		- **Optional Obsidian-specific navigation:** [obsidian.nvim](https://github.com/obsidian-nvim/obsidian.nvim) adds `:Obsidian follow_link`, a smart action that can follow the link under the cursor, a picker for all links in the current note, and actions for moving the cursor to the next or previous valid link. It is useful when Marksman's `gd` and `gr` are too limited for the vault workflow.
