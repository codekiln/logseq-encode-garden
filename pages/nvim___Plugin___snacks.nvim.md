logseq-entity:: [[Logseq/Entity/Software/Plugin]]
created-by:: [[Person/Folke Lemaitre]]

- # [snacks.nvim](https://github.com/folke/snacks.nvim)
	- ## Key features
		- [[nvim/Plugin/snacks.nvim/Picker]] — a fuzzy finder over files, buffers, grep, LSP results, keymaps, and more; stands in for [[Telescope]] or fzf-lua. [[LazyVim]] falls back to this picker when neither of those extras is enabled.
		- [[nvim/Plugin/snacks.nvim/Notifier]] — replaces `nvim-notify` for UI notifications.
		- [[nvim/Plugin/snacks.nvim/Dashboard]] — configurable start screen shown on launch.
		- Other modules, each toggleable independently: [[nvim/Plugin/snacks.nvim/Indent]], [[nvim/Plugin/snacks.nvim/Zen]], [[nvim/Plugin/snacks.nvim/Scratch]], [[nvim/Plugin/snacks.nvim/Terminal]], [[nvim/Plugin/snacks.nvim/Git Browse]], and more.
	- ## My Setup
		- No `snacks.nvim` overrides exist in my dotfiles — every module below is switched on (or off) purely by [[LazyVim]]'s own default plugin spec, which my config imports unmodified.
		- ### Enabled
			- [[nvim/Plugin/snacks.nvim/Picker]], [[nvim/Plugin/snacks.nvim/Notifier]], [[nvim/Plugin/snacks.nvim/Dashboard]], [[nvim/Plugin/snacks.nvim/Indent]], [[nvim/Plugin/snacks.nvim/Zen]], [[nvim/Plugin/snacks.nvim/Scratch]], [[nvim/Plugin/snacks.nvim/Terminal]], [[nvim/Plugin/snacks.nvim/Git Browse]], [[nvim/Plugin/snacks.nvim/Explorer]]
			- Also wired up, with no page of their own yet: bufdelete, toggle (the `<leader>u*` UI toggles), rename (rename-on-file-rename), words (LSP reference highlighting), scope, scroll, input, bigfile, quickfile, animate, dim, debug, and profiler.
		- ### Not enabled
			- [Statuscolumn](https://github.com/folke/snacks.nvim/blob/main/docs/statuscolumn.md) — explicitly turned off; [[LazyVim]] sets the statuscolumn itself instead.
			- [GitHub](https://github.com/folke/snacks.nvim/blob/main/docs/gh.md) — issue/PR browser; nothing in my config wires it up.
			- [Image](https://github.com/folke/snacks.nvim/blob/main/docs/image.md) — inline image/markdown preview; likewise unused.