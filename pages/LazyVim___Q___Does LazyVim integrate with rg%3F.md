logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[LazyVim/Keyshort/Search]], [[nvim/Plugin/snacks.nvim/Picker]]

- # Does [[LazyVim]] integrate with [[rg]]?
	- ## [[AI Answer]]
		- **Short answer:** Yes, deeply. [[rg]] is one of LazyVim's listed external requirements, and it is the search engine behind `:grep`, the file and grep pickers, search-and-replace, and TODO search. Nothing needs configuring — install `rg` on `$PATH` and every search path uses it.
		- **Health check:** `:checkhealth lazyvim` verifies `rg` alongside `git`, `fd`, `lazygit`, `fzf`, and `curl` ([lua/lazyvim/health.lua](https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/health.lua)). A missing `rg` is reported as an error, not a warning.
		- **Vim's own grep:** LazyVim sets `grepprg` to `rg --vimgrep` with a matching `grepformat` of `%f:%l:%c:%m` ([lua/lazyvim/config/options.lua](https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua)), so plain `:grep pattern` runs ripgrep and fills the quickfix list.
		- **The default picker:** [[nvim/Plugin/snacks.nvim]]'s grep source builds its command as `rg` with `--color=never --no-heading --with-filename --line-number --column --smart-case --max-columns=500` plus `--glob=!.git`; `hidden`, `ignored`, `follow`, and `ft` picker options map onto `--hidden`, `--no-ignore`, `-L`, and `-t`. Its file source auto-detects `fd` first, then `rg --files`, then `find`. Snacks' own health check errors out if `rg` is absent, because `Snacks.picker.grep()` has no fallback.
		- **The keys this shows up on** (see [[LazyVim/Keyshort/Search]]): `<leader>/` and `<leader>sg` are live grep over the root, `<leader>sw` greps the word under the cursor — all ripgrep processes streaming into the picker.
		- **Search and replace:** `<leader>sr` opens [[nvim/Plugin/grug-far.nvim]], whose default engine is `ripgrep` (alternatives are `astgrep` and `astgrep-rules`); the `filesFilter` field passes globs straight through to `rg`.
		- **TODO search:** `<leader>st` uses [[nvim/Plugin/todo-comments.nvim]], which sets `command = "rg"` for its project-wide keyword scan.
		- **With editor extras enabled:** the [[nvim/Plugin/telescope.nvim]] extra prefers `rg --files --color never -g !.git` for its file finder and falls back to `fd`/`find` only if ripgrep is missing; the [[nvim/Plugin/fzf-lua]] extra likewise drives `rg` for grep. So the answer holds whichever picker is in use.
