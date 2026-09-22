logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[LazyVim/Q/What is the keyshort to see the error log after a notification message disappears?]], [[LazyVim/Tutorial/Search for a Phrase Across Files/Q/Why does cd pages show a Messages notification but pwd shows nothing visible?]]
- # How can I see recent messages in LazyVim without the path getting cut off, like with `:pwd`?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [LazyVim Keymaps](https://www.lazyvim.org/keymaps)
		- **Short answer:** use `<leader>snh` — noice.nvim's "Noice History" — which opens the full plain-text message log in a normal buffer instead of a width-limited popup, so a long `:pwd` path is never truncated.
		- codekiln's LazyVim setup runs noice.nvim and [[nvim/Plugin/snacks.nvim]] with no local overrides (`chezmoi/dot_config/nvim/lua/plugins/` only customizes `marksman.lua`, `extras.lua`, `colorscheme.lua`), so LazyVim's [stock keymaps](https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/plugins/ui.lua) apply as shipped: `<leader>snl` last message, `<leader>snh` full history, `<leader>sna` all messages, `<leader>snd` dismiss all.
		- `<leader>n` ([[nvim/Plugin/snacks.nvim/Notifier]] "Notification History") works too for `:pwd` specifically, since noice routes plain `msg_show` messages through the same `{ "snacks", "notify" }` backend as other notifications — its history/[[nvim/Plugin/snacks.nvim/Picker]] view isn't clipped to the small popup's width either.
		- `<leader>snt` ("Noice Picker") is listed in LazyVim's defaults but requires Telescope or fzf-lua; neither is installed here (only `snacks.nvim` appears in `lazy-lock.json`), so it won't do anything useful in this setup — `<leader>snh` or `<leader>n` are the reliable options.
