see-also:: [[vim/viminfo File]]

- # ShaDa File
	- **ShaDa** ("shared data") is [[nvim]]'s on-disk store for editor state that should survive quit — command/search/input history, registers, marks, jump lists, the buffer list, and selected global variables. It is a **Neovim** concept: Vim's equivalent is the [[vim/viminfo File]].
	- [[Answer/Official]] from [shada ("shared data") file](https://neovim.io/doc/user/starting.html#shada-file) and [vim_diff — ShaDa](https://neovim.io/doc/user/vim_diff.html#shada): Neovim replaced Vim's text `viminfo` format with a binary MessagePack ShaDa file. The formats are **not interchangeable** — do not point Vim and Neovim at the same path.
	- ## Defaults and controls
		- Typical Unix path: `~/.local/state/nvim/shada/main.shada` (`$XDG_STATE_HOME/nvim/shada/…`).
		- Option `'shada'` (alias `'viminfo'` still accepted) selects *what* is remembered; `'N` caps how many files keep local marks; `f0`/`f1` toggles storing global/file marks `A`–`Z` and `0`–`9`.
		- Write/read on demand: `:wshada` / `:rshada` (legacy `:wviminfo` / `:rviminfo` still work as names).
		- Distinct from `:mksession` — sessions snapshot windows/buffers/layout; ShaDa holds marks, registers, and histories. Use both when both kinds of restore matter.
	- ## Why it exists (vs viminfo)
		- Concurrent Neovim instances **merge** by timestamp instead of blindly overwriting each other.
		- Forward/backward-compatible MessagePack layout; tools can inspect or concatenate ShaDa files more safely than classic viminfo text.
	- ## Related
		- Marks that ShaDa persists — [[vim/Q/What exactly are vim marks, and what are they good for?]]
