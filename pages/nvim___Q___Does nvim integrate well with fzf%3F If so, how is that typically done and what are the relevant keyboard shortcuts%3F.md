logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[fzf]], [[fzf/Keyshort]]
via:: [[2026-04-02 Thu]]
- # Does [[nvim]] integrate well with [[fzf]]? If so, how is that typically done and what are the relevant keyboard shortcuts?
	- ## Answer
		- [[AI/Response]]
			- **Yes.** [[nvim]] and **fzf** work together in a well-trodden way: fzf runs as a **terminal job** (Neovim’s `:terminal` / `termopen` path), so the picker stays fast and async while the editor owns the UI. The usual stack is the **junegunn** Vim layer: install both [**fzf** (includes the core Vim wrapper)](https://github.com/junegunn/fzf/blob/master/README-VIM.md) and [**fzf.vim**](https://github.com/junegunn/fzf.vim) (ready-made commands). Many Lua-first configs use [**fzf-lua**](https://github.com/ibhagwan/fzf-lua) instead, which still drives the **fzf** binary but is easier to wire from `init.lua`. For a **native-Lua** picker (not the fzf binary), people often use [**telescope.nvim**](https://github.com/nvim-telescope/telescope.nvim) instead—same role, different implementation.
			- ### Typical setup (pattern)
				- **Plugin managers:** e.g. `Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }` plus `Plug 'junegunn/fzf.vim'` ([fzf.vim README](https://github.com/junegunn/fzf.vim/blob/master/README.md)); or the equivalent lazy.nvim spec for **fzf-lua**.
				- **Commands you map yourself:** fzf.vim exposes Ex commands such as `:Files`, `:GFiles`, `:Buffers`, `:Rg` / `:RG`, `:Lines`, `:History`, `:Commits` (with fugitive), etc.—you bind keys to those. There is **no single global “Neovim default”** for leader keys; starter configs (LazyVim, Kickstart, personal dotfiles) choose mappings such as `<leader>ff` for files—compare your own [[fzf]] notes.
			- ### Shortcuts worth knowing (two layers)
				- **Inside most fzf.vim pickers** ([command table](https://github.com/junegunn/fzf.vim/blob/master/README.md)): **`Ctrl-T`** open in a new tab, **`Ctrl-X`** in a horizontal split, **`Ctrl-V`** in a vertical split; **`Alt-A` / `Alt-D`** select/deselect all in grep-style lists; preview toggle defaults to **`Ctrl-/`** when a preview window is configured (`g:fzf_vim.preview_window`).
				- **Optional fzf.vim mappings** (only if you add them—examples from the same README): **`<Leader><Tab>`** → `<plug>(fzf-maps-n)` (fuzzy-find your Normal-mode maps); insert-mode **`Ctrl-X Ctrl-F`** path completion, **`Ctrl-X Ctrl-L`** line completion, etc.
				- **Standalone fzf** (shell): keys like **`Ctrl-J` / `Ctrl-K`** or **`Ctrl-N` / `Ctrl-P`** move the selection; **`Enter`** accepts—see [`man fzf`](https://junegunn.github.io/fzf/) for the full keymap.
			- ### Sources
				- [junegunn/fzf.vim README](https://github.com/junegunn/fzf.vim/blob/master/README.md) (commands, splits, optional mappings)
				- [junegunn/fzf — Vim integration](https://github.com/junegunn/fzf/blob/master/README-VIM.md) (`fzf#run`, terminal behavior)
				- [ibhagwan/fzf-lua](https://github.com/ibhagwan/fzf-lua) (Lua-oriented alternative frontend)
	- ## My Notes
		- *placeholder*
