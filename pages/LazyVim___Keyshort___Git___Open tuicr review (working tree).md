logseq-entity:: [[Logseq/Entity/Keyshort]], [[Logseq/Entity/Card]]
see-also:: [[LazyVim/Keyshort/Git]], [[tuicr]], [[My/Pref/Dev/mise/Tasks]]

- [[Keyshort]] [[LazyVim]] [[LazyVim/Keyshort]] [[LazyVim/Keyshort/Git]]
	- **Open tuicr Review for the Working Tree** [[Card]]
		- Shortcut: `<leader>gR`
		- Description:
			- Opens a split terminal in LazyVim and runs a global mise tuicr review task for the current directory.
			- Uses `tuicr:review-herdr` when inside Herdr and `tuicr:review-tmux` when inside tmux.
			- This shortcut is wired in dotfiles at `chezmoi/dot_config/nvim/lua/config/keymaps.lua`.
		- [[Mnemonic]]
			- ==g==it ==R==eview
			- `<leader>gR`
