alias:: [[lazyvim.plugins.extras.lang.json]]
logseq-entity:: [[Logseq/Entity/Software/Plugin/Collection]]

- # [LazyVim extra: lang.json](https://www.lazyvim.org/extras/lang/json)
	- Stock [[LazyVim]] language extra enabled in my nvim dotfiles. A curated *bundle* (not a plugin): LazyVim ships and maintains it; I enable it here, and can still customize it by overriding its plugin specs / LSP settings in my own `plugins/` or via `vim.g` flags. The components below are what to read about when going deeper.
	- ## Components
		- **Neovim plugins** (each a [[Logseq/Entity/Software/Plugin]] under `nvim/Plugin/`):
			- [[nvim/Plugin/SchemaStore.nvim]] — JSON Schema catalog feeding jsonls
		- **LSP** (via [[mason.nvim]]): jsonls (with SchemaStore, format + validate)
		- **Treesitter** added: `json5` (plus base `json` / `jsonc`)
	- ## Where to find these
		- Source: `~/.local/share/nvim/lazy/LazyVim/lua/lazyvim/plugins/extras/lang/json.lua`
		- Docs: https://www.lazyvim.org/extras/lang/json
		- In nvim: `:LazyExtras` · `:Lazy` · `:Mason`
