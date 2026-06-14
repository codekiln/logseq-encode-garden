alias:: [[lazyvim.plugins.extras.lang.sql]]
logseq-entity:: [[Logseq/Entity/Software/Plugin/Collection]]

- # [LazyVim extra: lang.sql](https://www.lazyvim.org/extras/lang/sql)
	- Stock [[LazyVim]] language extra enabled in my nvim dotfiles. A curated *bundle* (not a plugin): LazyVim ships and maintains it; I enable it here, and can still customize it by overriding its plugin specs / LSP settings in my own `plugins/` or via `vim.g` flags. The components below are what to read about when going deeper.
	- ## Components
		- **Neovim plugins** (each a [[Logseq/Entity/Software/Plugin]] under `nvim/Plugin/`):
			- [[nvim/Plugin/vim-dadbod]] — database interface; `:DB`
			- [[nvim/Plugin/vim-dadbod-ui]] — DB explorer UI; `<leader>D`
			- [[nvim/Plugin/vim-dadbod-completion]] — SQL completion source
		- **No LSP server** by default — this extra is the dadbod stack + linting, not a language server.
		- **Formatter / linter** (via [[mason.nvim]]): sqlfluff (`--dialect=ansi`)
		- **Treesitter** added: `sql`
		- Filetypes: `sql`, `mysql`, `plsql`. Connections via `vim.g.dbs` (keep `.lazy.lua` secrets out of git).
	- ## Where to find these
		- Source: `~/.local/share/nvim/lazy/LazyVim/lua/lazyvim/plugins/extras/lang/sql.lua`
		- Docs: https://www.lazyvim.org/extras/lang/sql
		- In nvim: `:LazyExtras` · `:Lazy` · `:Mason`
