alias:: [[lazyvim.plugins.extras.lang.rust]]
logseq-entity:: [[Logseq/Entity/Software/Plugin/Collection]]

- # [LazyVim extra: lang.rust](https://www.lazyvim.org/extras/lang/rust)
	- Stock [[LazyVim]] language extra enabled in my nvim dotfiles. A curated *bundle* (not a plugin): LazyVim ships and maintains it; I enable it here, and can still customize it by overriding its plugin specs / LSP settings in my own `plugins/` or via `vim.g` flags. The components below are what to read about when going deeper.
	- ## Components
		- **Neovim plugins** (each a [[Logseq/Entity/Software/Plugin]] under `nvim/Plugin/`):
			- [[nvim/Plugin/rustaceanvim]] — drives rust-analyzer (`RustLsp` commands, debuggables). Configures the LSP directly, not through nvim-lspconfig.
			- [[nvim/Plugin/crates.nvim]] — `Cargo.toml` completion + LSP actions
		- **LSP**: rust-analyzer — **expected on `$PATH`** (rustaceanvim errors if missing); not installed by mason here. `bacon-ls` optional for diagnostics.
		- **DAP** (via [[mason.nvim]]): codelldb
		- **Treesitter** added: `rust`, `ron`
	- ## Where to find these
		- Source: `~/.local/share/nvim/lazy/LazyVim/lua/lazyvim/plugins/extras/lang/rust.lua`
		- Docs: https://www.lazyvim.org/extras/lang/rust
		- In nvim: `:LazyExtras` · `:Lazy` · `:Mason`
