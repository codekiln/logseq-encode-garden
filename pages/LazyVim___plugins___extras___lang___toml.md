alias:: [[lazyvim.plugins.extras.lang.toml]]
logseq-entity:: [[Logseq/Entity/Software/Plugin/Collection]]

- # [LazyVim extra: lang.toml](https://www.lazyvim.org/extras/lang/toml)
	- Stock [[LazyVim]] language extra enabled in my nvim dotfiles. A curated *bundle* (not a plugin): LazyVim ships and maintains it; I enable it here, and can still customize it by overriding its plugin specs / LSP settings in my own `plugins/` or via `vim.g` flags. The components below are what to read about when going deeper.
	- ## Components
		- **LSP** (via [[mason.nvim]]): taplo. Covers [[TOML]] config (mise, cargo, pyproject).
		- **Treesitter**: base `toml`
		- (This extra adds no extra Neovim plugin — it just wires the taplo server.)
	- ## Where to find these
		- Source: `~/.local/share/nvim/lazy/LazyVim/lua/lazyvim/plugins/extras/lang/toml.lua`
		- Docs: https://www.lazyvim.org/extras/lang/toml
		- In nvim: `:LazyExtras` · `:Lazy` · `:Mason`
