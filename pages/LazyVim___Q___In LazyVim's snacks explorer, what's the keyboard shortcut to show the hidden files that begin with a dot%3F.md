logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[nvim/Plugin/snacks.nvim/Explorer]]

- # In [[LazyVim]]'s snacks explorer, what's the [[Keyshort]] to show the hidden files that begin with a dot? [[Card]]
	- ## [[My Answer]]
		- `H` toggles hidden files
		- `I` toggles gitignored files
		- at the top of the explorer, `i` and `h` will appear
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Explorer | snacks.nvim](https://github.com/folke/snacks.nvim/blob/main/docs/explorer.md)
		- **Short answer:** Press **`H`** while focused in the [[nvim/Plugin/snacks.nvim/Explorer]] sidebar to toggle hidden (dotfile) visibility.
		- The explorer docs list it under *Navigation*: `H` → Toggle hidden files, alongside `I` → Toggle ignored files (from gitignore).
		- This is the default keymap shipped by [[nvim/Plugin/snacks.nvim]] (`lua/snacks/picker/config/sources.lua`, explorer actions table: `["H"] = "toggle_hidden"`). No override was found in this operator's dotfiles nvim config, so the default applies.
	- [[My Note]]
		- Hidden state does not persist across sessions by default; each new explorer instance starts with hidden files off unless configured otherwise via the `hidden` option.
