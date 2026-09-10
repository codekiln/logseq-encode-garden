see-also:: [[nvim/ShaDa File]]

- # viminfo File
	- **viminfo** is [[vim]]'s on-disk store for editor state that should survive quit — command/search history, registers, marks, the buffer list, and related session residue. Controlled by the `'viminfo'` option; read/written with `:rviminfo` / `:wviminfo`.
	- [[nvim]] replaced this with the [[nvim/ShaDa File]] (option `'shada'`, commands `:rshada` / `:wshada`). ShaDa is MessagePack-based and **not** format-compatible with viminfo — sharing one file between Vim and Neovim breaks.
	- Default location is typically `~/.viminfo` (or a path set via the `n` flag in `'viminfo'`). Keep that path Vim-only if both editors are on the machine.
