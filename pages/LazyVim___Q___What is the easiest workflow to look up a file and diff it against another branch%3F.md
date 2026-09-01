logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[LazyVim/Keyshort/Git]], [[Lazygit/Q/Can an agent open lazygit on one file in one commit for me to review?]]

- # What is the easiest workflow to look up a file and diff it against another branch?
	- ## [[AI Answer]]
		- **Short answer:** Find the file with `<leader>ff` (or `<leader><space>`), then run `:Gitsigns diffthis <branch>` for a side-by-side vimdiff of the open buffer against that branch's version of the same path. That is the shortest stock [[LazyVim]] path that stays in the editor and targets one file.
		- ### Recommended workflow
			- 1. `<leader>ff` (or `<leader><space>`) — fuzzy file picker at the project root; open the file. Same picker as on [[LazyVim/Keyshort/Search]].
			- 2. `:Gitsigns diffthis main` — replace `main` with any ref (`origin/main`, a feature branch, a SHA). Opens a vertical vimdiff: left is the revision, right is the working-tree buffer. Close the revision window with `:q` when done.
			- 3. Navigate hunks with `]h` / `[h` while the diff is open (same keys as the [[nvim/Plugin/gitsigns.nvim]] hunk maps LazyVim binds under `<leader>gh`).
		- ### Why this wins for "one file vs another branch"
			- [[LazyVim]] already ships [[nvim/Plugin/gitsigns.nvim]]. Its stock maps cover `<leader>ghd` (diff vs index) and `<leader>ghD` (diff vs `~`), but not an arbitrary branch — so the Ex form `:Gitsigns diffthis <branch>` is the intended escape hatch. [[Answer/Official]] from [gitsigns `:Gitsigns diffthis`](https://github.com/lewis6991/gitsigns.nvim/blob/main/doc/gitsigns.txt) and [LazyVim's gitsigns `on_attach`](https://www.lazyvim.org/plugins/editor).
			- It scopes to the current buffer automatically. No path typing after the file is open, and no whole-tree picker to filter down.
		- ### Good alternatives in the same stack
			- **PR-style, many files, filter to one:** `<leader>gD` opens [[nvim/Plugin/snacks.nvim]]'s `git_diff` against the merge-base with `origin` (`group = true`). Type part of the path in the picker to narrow to one file. For a named base instead of `origin`: `:lua Snacks.picker.git_diff({ base = "main", group = true })`. This answers "what changed on this branch since it diverged," which is merge-base semantics, not always tip-to-tip. [[Answer/Official]] from [LazyVim snacks picker keymaps](https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/plugins/extras/editor/snacks_picker.lua) and [snacks `git_diff` `base`](https://github.com/folke/snacks.nvim/blob/main/docs/picker.md).
			- **Branch-to-branch in [[Lazygit]]:** `<leader>gg` → Local Branches → cursor on the other branch → `W` (diffing options) → select / enter the other ref → land in the diff files view → `/` to filter by path. Best when the question is "everything this branch changed," then drill into one file. [[Answer/Official]] from [lazygit keybindings — View diffing options](https://github.com/jesseduffield/lazygit/blob/master/docs/keybindings/Keybindings_en.md).
			- **Patch in a pager, no split:** with the file open, `:!git diff <branch> -- %` or a floating terminal via `<leader>ft` and the same command. Fastest for a quick read; worse for navigating hunks side by side.
			- **Historical contents only (not a diff):** `git show <branch>:<path>` — see [[git/show]].
		- ### What not to reach for first
			- `diffview.nvim` (`:DiffviewOpen main -- %`) is excellent for this job, but it is not stock [[LazyVim]] — enable it only if it is already installed.
			- Opening [[Lazygit]] with `--filter` on the current file (as in [[Lazygit/Q/Can an agent open lazygit on one file in one commit for me to review?]]) is great for commit history of one path; it does not by itself start a compare against another branch tip.
