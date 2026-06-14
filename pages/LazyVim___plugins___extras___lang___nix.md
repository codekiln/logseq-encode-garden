alias:: [[lazyvim.plugins.extras.lang.nix]]
logseq-entity:: [[Logseq/Entity/Software/Plugin/Collection]]

- # [LazyVim extra: lang.nix](https://www.lazyvim.org/extras/lang/nix)
	- Stock [[LazyVim]] language extra enabled in my nvim dotfiles. A curated *bundle* (not a plugin): LazyVim ships and maintains it; I enable it here, and can still customize it by overriding its plugin specs / LSP settings in my own `plugins/` or via `vim.g` flags. The components below are what to read about when going deeper.
	- ## Components
		- **LSP** (via [[mason.nvim]]): nil_ls. For [[Nix]] config.
		- **Formatter** (conform, optional): nixfmt
		- **Linter** (nvim-lint, optional): statix
		- **Treesitter** added: `nix`
		- (This extra adds no extra Neovim plugin — it wires the nil_ls server + formatter/linter.)
	- ## Where to find these
		- Source: `~/.local/share/nvim/lazy/LazyVim/lua/lazyvim/plugins/extras/lang/nix.lua`
		- Docs: https://www.lazyvim.org/extras/lang/nix
		- In nvim: `:LazyExtras` · `:Lazy` · `:Mason`
	- ## Install note
		- mason has no prebuilt `nil` on macOS arm64, so it builds from source via `cargo` — requires `rust` available (set globally in my mise config).
