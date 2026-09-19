logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[LazyVim/Q/In LazyVim's snacks explorer, what's the keyboard shortcut to show the hidden files that begin with a dot?]]

- # In [[LazyVim]]'s [[LazyVim/Picker/File]] (`<leader><space>` / `<leader>ff`), are dotfiles hidden by default, and what's the keyboard shortcut to show hidden or ignored files?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Picker | snacks.nvim](https://github.com/folke/snacks.nvim/blob/main/docs/picker.md)
		- **Short answer:** Yes. The `Files` picker defaults to `hidden = false` and `ignored = false`, so dotfiles and gitignored files are excluded until toggled on. Press **`<A-h>`** (Alt-h) to toggle hidden files and **`<A-i>`** (Alt-i) to toggle ignored files — works from the input or the results list, in normal or insert mode.
		- These are the same `toggle_hidden` / `toggle_ignored` actions the [[nvim/Plugin/snacks.nvim/Explorer]] sidebar uses, but Explorer's own keymap table binds capital `H` / `I` instead of `<A-h>` / `<A-i>` — different default bindings for the same underlying toggle (source: `lua/snacks/picker/config/sources.lua` and `lua/snacks/picker/config/defaults.lua` in [[nvim/Plugin/snacks.nvim]]).
		- No override for these keymaps was found in this operator's dotfiles nvim config, so the shipped defaults apply.
