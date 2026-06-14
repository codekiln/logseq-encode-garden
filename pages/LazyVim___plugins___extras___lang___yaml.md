alias:: [[lazyvim.plugins.extras.lang.yaml]]
logseq-entity:: [[Logseq/Entity/Software/Plugin/Collection]]

- # [LazyVim extra: lang.yaml](https://www.lazyvim.org/extras/lang/yaml)
	- Stock [[LazyVim]] language extra enabled in my nvim dotfiles. A curated *bundle* (not a plugin): LazyVim ships and maintains it; I enable it here, and can still customize it by overriding its plugin specs / LSP settings in my own `plugins/` or via `vim.g` flags. The components below are what to read about when going deeper.
	- ## Components
		- **Neovim plugins** (each a [[Logseq/Entity/Software/Plugin]] under `nvim/Plugin/`):
			- [[nvim/Plugin/SchemaStore.nvim]] — YAML Schema catalog feeding yamlls
		- **LSP** (via [[mason.nvim]]): yamlls (SchemaStore, line-folding capability, format + validate)
		- **Treesitter**: base `yaml`
	- ## Where to find these
		- Source: `~/.local/share/nvim/lazy/LazyVim/lua/lazyvim/plugins/extras/lang/yaml.lua`
		- Docs: https://www.lazyvim.org/extras/lang/yaml
		- In nvim: `:LazyExtras` · `:Lazy` · `:Mason`
