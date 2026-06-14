alias:: [[lazyvim.plugins.extras.lang.nix]]

- # [LazyVim extra: lang.nix](https://www.lazyvim.org/extras/lang/nix)
	- Stock [[LazyVim]] language extra, enabled in my nvim dotfiles. LazyVim curates and maintains the bundle; the only thing of mine is the choice to enable it.
	- Provides: nil_ls LSP, `nix` treesitter. For [[Nix]] config.
	- Note: mason has no prebuilt `nil` on macOS arm64, so it builds from source via cargo — requires `rust` available (set globally in my mise config).
