alias:: [[lazyvim.plugins.extras.lang.markdown]]
logseq-entity:: [[Logseq/Entity/Software/Plugin/Collection]]

- # [LazyVim extra: lang.markdown](https://www.lazyvim.org/extras/lang/markdown)
	- Stock [[LazyVim]] language extra enabled in my nvim dotfiles. A curated *bundle* (not a plugin): LazyVim ships and maintains it; I enable it here, and can still customize it by overriding its plugin specs / LSP settings in my own `plugins/` or via `vim.g` flags. The components below are what to read about when going deeper.
	- ## Components
		- **Neovim plugins** (each a [[Logseq/Entity/Software/Plugin]] under `nvim/Plugin/`):
			- [[nvim/Plugin/render-markdown.nvim]] — in-buffer rendering; toggle `<leader>um`
			- [[nvim/Plugin/markdown-preview.nvim]] — browser preview; `<leader>cp`
		- **LSP** (standalone binary via [[mason.nvim]]): marksman
		- **Formatters / linters** (via [[mason.nvim]] + conform/nvim-lint/none-ls): markdownlint-cli2, markdown-toc, prettier
		- **Treesitter**: `markdown`, `markdown_inline`
		- Also registers the `.mdx` filetype as `markdown.mdx`.
	- ## Where to find these
		- Source: `~/.local/share/nvim/lazy/LazyVim/lua/lazyvim/plugins/extras/lang/markdown.lua`
		- Docs: https://www.lazyvim.org/extras/lang/markdown
		- In nvim: `:LazyExtras` (enabled extras) · `:Lazy` (plugins) · `:Mason` (tools)
