alias:: [[lazyvim.plugins.extras.lang.python]]
logseq-entity:: [[Logseq/Entity/Software/Plugin/Collection]]

- # [LazyVim extra: lang.python](https://www.lazyvim.org/extras/lang/python)
	- Stock [[LazyVim]] language extra enabled in my nvim dotfiles. A curated *bundle* (not a plugin): LazyVim ships and maintains it; I enable it here, and can still customize it by overriding its plugin specs / LSP settings in my own `plugins/` or via `vim.g` flags. The components below are what to read about when going deeper.
	- ## Components
		- **Neovim plugins** (each a [[Logseq/Entity/Software/Plugin]] under `nvim/Plugin/`):
			- [[nvim/Plugin/venv-selector.nvim]] — virtualenv picker; `<leader>cv`
			- [[nvim/Plugin/neotest-python]] — pytest/unittest adapter (via neotest)
			- [[nvim/Plugin/nvim-dap-python]] — debugging (via nvim-dap)
		- **LSP** (via [[mason.nvim]]): pyright (default) + [[Ruff]]. Switch to basedpyright via `vim.g.lazyvim_python_lsp`.
		- **DAP** (via [[mason.nvim]]): debugpy
		- **Treesitter** added: `ninja`, `rst` (plus base `python`)
	- ## Where to find these
		- Source: `~/.local/share/nvim/lazy/LazyVim/lua/lazyvim/plugins/extras/lang/python.lua`
		- Docs: https://www.lazyvim.org/extras/lang/python
		- In nvim: `:LazyExtras` · `:Lazy` · `:Mason`
