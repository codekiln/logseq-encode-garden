logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[nvim/Distro/LazyVim]]

- # Is **lazy.nvim** the same thing as [[nvim/Distro/LazyVim]]?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** No — **lazy.nvim** is a plugin manager; **[[nvim/Distro/LazyVim]]** is a full Neovim distribution built on top of it.
			- **lazy.nvim** — a standalone plugin manager for [[nvim]] (by Folke Lemaitre). Handles plugin installation, lazy-loading on events/filetypes/keymaps, caching, and bytecode compilation. Can be dropped into any config.
			- **[[nvim/Distro/LazyVim]]** — an opinionated Neovim distribution (also by Folke) built on top of **lazy.nvim**. Ships pre-wired with LSP, Treesitter, formatters, and keymaps so it works on first launch.
			- The naming is a frequent source of confusion: both projects are by the same author and the distro name is a play on the plugin manager name.
			- Sources: [lazy.nvim on GitHub](https://github.com/folke/lazy.nvim) · [LazyVim docs](https://www.lazyvim.org/) · [Hacker News thread on the distinction](https://news.ycombinator.com/item?id=38153783)
