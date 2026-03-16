- # How can I quickly collapse and expand a block in [[nvim]]?
	- ## Answer
		- [[AI/Response]]
			- Use [[nvim]]'s built-in **folding** commands. The fastest way is `za` to toggle a fold open/closed under the cursor.
			- ### Core fold toggle commands
				- | Key | Action |
				  |-----|--------|
				  | `za` | Toggle fold under cursor (open if closed, close if open) |
				  | `zo` | Open fold under cursor |
				  | `zc` | Close fold under cursor |
				  | `zO` | Open fold and all nested folds recursively |
				  | `zC` | Close fold and all nested folds recursively |
				  | `zR` | Open **all** folds in the buffer |
				  | `zM` | Close **all** folds in the buffer |
			- ### Fold methods
				- Folding must be configured to work. Set a `foldmethod` in your config or per-buffer:
					- ~~~vim
					  set foldmethod=indent   " fold by indentation (good for Python, LFM)
					  set foldmethod=syntax   " fold by syntax (language-aware)
					  set foldmethod=marker   " fold between {{{ and }}} markers
					  set foldmethod=expr     " custom expression (used by tree-sitter plugins)
					  ~~~
				- For Logseq Flavored Markdown (indented bullets), `indent` is the most practical built-in option.
			- ### With tree-sitter (recommended for modern configs)
				- If you use [nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter), enable expression-based folding:
					- ~~~lua
					  vim.opt.foldmethod = "expr"
					  vim.opt.foldexpr = "nvim_treesitter#foldexpr()"
					  vim.opt.foldenable = false  -- start with all folds open
					  ~~~
			- ### With nvim-ufo (enhanced folding plugin)
				- [nvim-ufo](https://github.com/kevinhwang91/nvim-ufo) provides a more polished fold experience with virtual text showing the number of folded lines. It remaps `zR` / `zM` and supports LSP + tree-sitter providers.
			- ### Quick tip: disable folding on open
				- By default nvim may fold everything when you open a file. To start with all folds open:
					- ~~~vim
					  set nofoldenable
					  ~~~
					- or in Lua: `vim.opt.foldenable = false`
			- ### Sources
				- [Neovim folding documentation](https://neovim.io/doc/user/fold.html)
				- [nvim-treesitter folding](https://github.com/nvim-treesitter/nvim-treesitter#folding)
				- [nvim-ufo plugin](https://github.com/kevinhwang91/nvim-ufo)
