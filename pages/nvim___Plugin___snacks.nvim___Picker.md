- # [Picker](https://github.com/folke/snacks.nvim/blob/main/docs/picker.md)
	- Fuzzy-finder module of [[nvim/Plugin/snacks.nvim]] — over 40 built-in sources (files, buffers, grep, LSP, git, and more), with a fast matcher that supports [fzf](https://junegunn.github.io/fzf/search-syntax/) search syntax.
	- It stands in for [[Telescope]] or fzf-lua in this [[LazyVim]] setup. Most sources appear in a floating [[Modal]]-style layout; [[nvim/Plugin/snacks.nvim/Explorer]] uses the same picker engine in a sidebar.
	- ## Mental Model
		- A picker combines three things:
			- A **source** supplies candidates and actions: file paths for `Files`, matching lines for `Grep`, or a directory tree for `Explorer`.
			- A **matcher** narrows or ranks those candidates from the text in the input.
			- A **layout** arranges the input, results, and optional preview. The source can choose a different layout without becoming a different picker system.
	- ## Anatomy of a Picker Dialog
		- This conceptual stack names the stable parts; an actual layout may place the preview beside or below the input and results.
		- ~~~text
		  +--------------------------------------------------+
		  | [1] Title: Grep    [2] Flag: R                   |
		  +--------------------------------------------------+
		  | [3] > search text              [4] 12/4915       |
		  +--------------------------------------------------+
		  | [5] > selected result                            |
		  |       another result                             |
		  |       another result                             |
		  +--------------------------------------------------+
		  | [6] Preview: selected file or matching line      |
		  +--------------------------------------------------+
		  ~~~
		- 1. **Title** — names the active source. `Files`, `Grep`, and `Explorer` are different jobs performed by the same picker framework.
		- 2. **Flags** — show noteworthy option states. They appear beside the title only when their configured state is active.
		- 3. **Input** — type the file-name pattern, search expression, or Explorer filter here.
		- 4. **Count** — `12/4915` means that 12 displayed candidates remain from 4,915 candidates supplied by the source.
		- 5. **Results list** — move the selection with `<C-j>` and `<C-k>` or the arrow keys; Enter performs the source's default action.
		- 6. **Preview** — shows the selected item when the current source and layout enable it. It is optional.
	- ## Why `R` Appears in `Grep`
		- The `Grep` source starts with `regex = true`. In that default state, no `R` appears.
		- `<Alt-r>` toggles `regex` to `false`. The picker defines its regex flag as `{ icon = "R", value = false }`, so it displays `R` precisely when regular-expression interpretation is **off** and the grep pattern is treated as fixed text.
		- `R` identifies the **regex option**; its presence marks that option's non-default, disabled state. It does not mean “read only.” A useful reading is **`R` visible → read the pattern literally**.
		- Press `<Alt-r>` again to restore `regex = true`; the `R` disappears.
	- ## Is `Explorer` Related?
		- **Yes.** [[nvim/Plugin/snacks.nvim/Explorer]] is a specialized picker source, not a separate fuzzy-finder implementation.
		- Its `Explorer` title, `>` input, candidate count, and file-tree result list correspond to the same picker concepts shown in the diagram. What changes is the source and layout.
		- Explorer defaults to the `sidebar` layout, focuses the results list, keeps the tree open after selecting files, and disables the picker preview. The editor beside the sidebar is the main Neovim window, not an Explorer preview pane.
		- Press `/` from the Explorer list to focus its input and search the tree. Pressing `<leader>/` while Explorer is focused launches the separate `Grep` picker rooted at the directory of the selected Explorer entry.
	- ## Learn It by Comparing Three Sources
		- 1. Press `<leader><space>` or `<leader>ff` and notice the `Files` title. The input fuzzy-matches file paths.
		- 2. Press `<leader>/` and notice the `Grep` title. The input searches file contents through [[rg]]; press `<Alt-r>` and watch the `R` flag appear or disappear.
		- 3. Press `<leader>e` and notice the `Explorer` title. The same input, count, and results concepts now live in a persistent tree sidebar.
		- Treat the title as the answer to **“what am I choosing?”** and the input as **“how am I narrowing it?”** The shared shape stays familiar while each source changes the candidates and Enter action.
		- Press `?` in normal mode while focused on a picker window to see the actions available in that context.
	- ## Related
		- [[LazyVim/Keyshort/Search]] documents the search keymaps that use the picker.
		- [[LazyVim/Keyshort/Explorer]] documents this setup's Explorer keymaps.
	- ## Sources
		- [snacks.nvim Picker documentation](https://github.com/folke/snacks.nvim/blob/main/docs/picker.md) documents the input, list, preview, source configuration, layouts, toggles, and actions.
		- [snacks.nvim Explorer source](https://github.com/folke/snacks.nvim/blob/main/lua/snacks/picker/config/sources.lua#L50) configures Explorer as a picker with its `sidebar` layout and tree-specific actions.
