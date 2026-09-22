logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[gh-dash]], [[nvim/Plugin/snacks.nvim/Picker]]

- # In [[LazyVim]], is there a way to quickly see what PRs are open for the repo at my [[pwd]], without leaving vim?
	- ## [[AI Answer]]
		- **Short answer:** yes — `Snacks.picker.gh_pr()`. It ships inside [[nvim/Plugin/snacks.nvim]], which this [[LazyVim]] setup already installs and uses as its picker engine, so it needs **no new plugin**, only a keymap. It shells out to the same authenticated `gh` CLI session [[gh-dash]] already uses.
		- ### Recommended setup
			- 1. Add a keymap, e.g. in `keymaps.lua`: `vim.keymap.set("n", "<leader>gp", function() Snacks.picker.gh_pr() end, { desc = "GitHub PRs (open)" })`. `<leader>gp` / `<leader>gP` are free — stock [[LazyVim]] only binds `<leader>gg` `<leader>gG` `<leader>gL` `<leader>gb` `<leader>gf` `<leader>gl` `<leader>gB` `<leader>gY` under `<leader>g`, and the local dotfiles only add `<leader>gR` (tuicr) on top.
			- 2. Trigger it from any buffer in the repo — no keymap needed first, `:lua Snacks.picker.gh_pr()` works ad hoc — and it lists that repo's open PRs, resolved from `pwd`.
			- 3. `<cr>` on a result opens the actions menu: view diff, checkout the branch, merge, review, or open in the browser, all inside nvim.
			- [[Answer/Official]] from [snacks.nvim `docs/gh.md`](https://github.com/folke/snacks.nvim/blob/main/docs/gh.md) — confirmed against the exact commit pinned in dotfiles' `lazy-lock.json` (`882c996`, 2026-05-25), which already ships this picker source.
		- ### Why this over the other options
			- `octo.nvim` — the deepest GitHub PR/issue plugin, but **not installed** here, and its [[LazyVim]] extra pulls in [[Telescope]] as a second picker framework alongside [[nvim/Plugin/snacks.nvim]] just to get PR listing.
			- `fzf-lua` — also **not installed**; a third picker framework for the same result `Snacks.picker.gh_pr()` already gives for free.
			- `diffview.nvim` — **not installed**, and it answers "what changed on this branch," not "what PRs are open" — it isn't a PR-listing tool regardless of install state.
			- `:terminal gh pr list` (or `gh pr list --json ...`) — zero-plugin and always works, but it's a plain terminal buffer: no fuzzy filter, no in-picker actions. `Snacks.picker.gh_pr()` gives the same data with both.
		- ### What it doesn't replace
			- [[gh-dash]]'s persistent multi-repo dashboard (My PRs / Needs My Review / Involved) and its wired [[tuicr]] handoff (`T` → `tuicr pr {{.RepoName}}#{{.PrNumber}}`, see [[gh-dash/Keyshort/Open selected PR in tuicr]]) stay the better fit for triage across many repos at once, and for jumping straight into a full review. `Snacks.picker.gh_pr()` answers the narrower "I'm already in vim at a git root, just show me this repo's open PRs" — it does not itself open a PR in [[tuicr]].
