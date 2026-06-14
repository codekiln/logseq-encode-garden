logseq-entity:: [[Logseq/Entity/Question]]

- # Is there a quick keyboard shortcut to toggle displaying warnings in [[LazyVim/plugins/extras/lang/markdown]]?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** `<leader>ud` enables/disables diagnostics (including [[markdownlint]] warnings). In [[LazyVim]], `<leader>` is `Space` by default.
			- Found under `<leader>u` (`+ui` group). The [[which-key]] label is state-dependent: shows **Enable Diagnostics** when off, **Disable Diagnostics** when on.
			- Defined in LazyVim's core keymaps as `Snacks.toggle.diagnostics():map("<leader>ud")` — applies globally (not markdown-only), useful when linting noise is distracting mid-edit.
			- **Other relevant shortcuts:**
				- `[w` / `]w` — jump to previous / next warning
				- `<leader>cd` — open a floating window with diagnostics for the current line
				- `<leader>um` — toggle [[nvim/Plugin/render-markdown.nvim]] rendering (visual rendering, not warnings)
