logseq-entity:: [[Logseq/Entity/Question]]

- # Is `<leader>gL`'s current working directory the internal `:pwd`, or the directory [[LazyVim]] was started in?
	- ## [[AI Answer]]
		- Short answer: it's Neovim's live internal cwd (`:pwd`, `getcwd()`), not the launch directory.
		- The [[nvim/Plugin/snacks.nvim]] [[git]] log picker (which [[LazyVim]] uses for `<leader>gL`) reads `(vim.uv or vim.loop).cwd()` at invocation time, so it reflects whatever `:cd`/`:lcd`, autochdir, or root-detection has last set — which can diverge from the directory Neovim was started in.
