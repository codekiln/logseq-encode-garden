alias:: [[lazyvim.plugins.extras.lang.typescript]]
logseq-entity:: [[Logseq/Entity/Software/Plugin/Collection]]

- # [LazyVim extra: lang.typescript](https://www.lazyvim.org/extras/lang/typescript)
	- Stock [[LazyVim]] language extra enabled in my nvim dotfiles. A curated *bundle* (not a plugin): LazyVim ships and maintains it; I enable it here, and can still customize it by overriding its plugin specs / LSP settings in my own `plugins/` or via `vim.g` flags. The components below are what to read about when going deeper.
	- Note: this extra is a **directory module** (`typescript/init.lua` + `vtsls.lua` / `oxc.lua` / `biome.lua` / `tsgo.lua`); enabling it transitively imports the LSP sub-extra (`lang.typescript.vtsls` by default).
	- ## Components
		- **Neovim plugins** (each a [[Logseq/Entity/Software/Plugin]] under `nvim/Plugin/`):
			- [[nvim/Plugin/mini.icons]] — JS/TS filetype glyphs (extends the base plugin)
		- **LSP** (via [[mason.nvim]]): vtsls (default). Switch to `tsgo` via `vim.g.lazyvim_ts_lsp` or the `tsgo` extra.
		- **DAP** (via [[mason.nvim]]): js-debug-adapter (node/chrome/msedge)
		- **Filetypes**: javascript, javascriptreact, typescript, typescriptreact (+ `.jsx`/`.tsx`)
	- ## Where to find these
		- Source: `~/.local/share/nvim/lazy/LazyVim/lua/lazyvim/plugins/extras/lang/typescript/`
		- Docs: https://www.lazyvim.org/extras/lang/typescript
		- In nvim: `:LazyExtras` · `:Lazy` · `:Mason`
