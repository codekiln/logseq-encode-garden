logseq-entity:: [[Logseq/Entity/Question]]
- # How do we know that [[rg]] is used for search in [[LazyVim]]?
	- ## [[AI Answer]]
		- [[LazyVim]] maps `<leader>/` to `LazyVim.pick("grep")`. This setup registers [[nvim/Plugin/snacks.nvim/Picker]] as LazyVim's picker, and that picker's grep source builds the search command with `cmd = "rg"`.
		- Run `:checkhealth lazyvim` inside Neovim to verify that `rg` is installed and available. [[LazyVim/Q/Does LazyVim integrate with rg?]] links to the source and describes the other searches backed by `rg`.
