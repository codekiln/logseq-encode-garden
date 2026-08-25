logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[vim/Keyshort/Open/Follow the File Path Under Cursor]], [[LazyVim/Q/In LazyVim, how can I open a Markdown link with a keyboard shortcut?]], [[LazyVim/Tutorial/Browse a Markdown Knowledge Garden]]

- # In (neo-)[[vim]] or [[LazyVim]], how can I open a file whose path a [[Markdown]] document gives from the repo root?
	- ## [[AI Answer]]
		- **Short answer:** `gf` opens it already, so long as the editor's working directory is the repository root. From a subdirectory or from outside the repository it reports `E447`. One buffer-local `includeexpr` frees it from the working directory and leaves ordinary relative paths alone.
		- ### `gf` from the repository root needs no setup
			- `path` defaults to `.,,`. The `.` is the directory of the file being edited; the empty entry between the commas is the editor's working directory. A bare `journals/2026_08_24.md` therefore resolves whenever the editor was started at the root of the graph, whatever subdirectory the page holding that line sits in.
			- Away from the root the same key reports `E447: Can't find file ... in path`, because neither entry in the default `path` reaches the repository root.
		- ### One setting frees it from the working directory
			- `includeexpr` rewrites the name and tries again. [[Answer/Official]] from [:help gf](https://neovim.io/doc/user/editing.html#gf): "If the file can't be found, 'includeexpr' is used to modify the name and another attempt is done."
			- Because it runs after the ordinary search misses, prefixing the repository root there costs nothing for a path that already resolves. A sibling `notes.md` still opens the sibling; `./sibling.md` still opens the file beside the page.
			- ~~~lua
			  -- lua/config/autocmds.lua
			  function _G.RootRelative(fname)
			    local buf = vim.api.nvim_buf_get_name(0)
			    local root = vim.fs.root(buf ~= "" and buf or vim.uv.cwd(),
			      { ".git", "logseq", ".marksman.toml" })
			    return root and (root .. "/" .. fname) or fname
			  end
			  vim.api.nvim_create_autocmd("FileType", {
			    pattern = "markdown",
			    callback = function()
			      vim.opt_local.includeexpr = "v:lua.RootRelative(v:fname)"
			      vim.opt_local.suffixesadd = ".md"
			    end,
			  })
			  ~~~
			- `suffixesadd` earns its place alongside: it is empty on a [[Markdown]] buffer, so a target written without its `.md` fails without it.
		- ### The root comes from the buffer, so the editor can start anywhere
			- `vim.fs.root` walks up from the path of the buffer itself. A page opened by full path from a home directory still resolves against its own repository.
			- Inside a [[git/worktree]] the `.git` entry is a file holding a pointer rather than a directory. `vim.fs.root` matches either shape, so a worktree checkout behaves like the main one.
			- `LazyVim.root()` reaches the same directory. Its spec is `{"lsp", {".git", "lua"}, "cwd"}`, and inside a [[Logseq]] graph the language server declines to start, which leaves the `.git` pattern to answer. Calling `vim.fs.root` arrives there without depending on that.
		- ### [[LazyVim]] binds nothing to this
			- Its root detection feeds the pickers, the `<leader>ft` terminal and `<leader>gg` lazygit. Nothing in it touches `gf`, `path`, `includeexpr` or `autochdir`, and no keymap of its own claims `gf` or `gF`.
		- ### Where it still stops
			- A space in the path ends the name early, so many of this graph's own filenames stay out of reach of a plain `gf`. Selecting the path and pressing `gf` in visual mode opens them. [[vim/Keyshort/Open/Follow the File Path Under Cursor]] has that variant and the rest of the set.
			- A file of the same name beside the page being read wins, and the one at the repository root becomes unreachable by `gf`. Appending the root to `path` instead of setting `includeexpr` behaves the same way, since `.` comes first in `path`.
			- The cursor may not rest on a bullet's `-`, which counts as a filename character.
			- A buffer-local mapping steps the cursor past a leading list marker before handing off to the stock key, which puts `gf` back in reach from column 1 of a bulleted line. It stands on its own: `includeexpr` decides what a name resolves against, this decides where the cursor is, and either one works without the other.
				- ~~~lua
				  vim.api.nvim_create_autocmd("FileType", {
				    pattern = "markdown",
				    callback = function(ev)
				      for _, key in ipairs({ "gf", "gF" }) do
				        vim.keymap.set("n", key, function()
				          local line = vim.api.nvim_get_current_line()
				          local col = vim.api.nvim_win_get_cursor(0)[2]
				          local s = line:sub(col + 1):match("^%s*[-*+]%s+()")
				          if s then
				            vim.api.nvim_win_set_cursor(0, { vim.fn.line("."), col + s - 1 })
				          end
				          vim.cmd("normal! " .. key)
				        end, { buffer = ev.buf, desc = "Follow file under cursor (list-marker tolerant)" })
				      end
				    end,
				  })
				  ~~~
				- The claim is `gf` and `gF` in normal mode on a [[Markdown]] buffer. Visual `gf` keeps its stock behaviour, and a cursor already sitting mid-path falls through untouched.
				- On a path that fails to open, the cursor stays where the marker skip left it, a column or two along from where the stock key would have left it.
		- ### The keys are the same in [[vim]]
			- `gf`, `<C-w>f`, `<C-w>gf` and `gF` are stock, so nothing about the answer changes between the two editors. The setup differs in two places: [[vim]] needs `filetype plugin on` before a `FileType` autocommand fires, and `vim.fs.root` is a [[nvim]] function.
			- ~~~vim
			  " .vimrc
			  filetype plugin on
			  function! RootRelative(fname) abort
			    let l:up = expand('%:p:h') . ';'
			    let l:hit = finddir('.git', l:up)
			    if empty(l:hit) | let l:hit = findfile('.git', l:up) | endif
			    if empty(l:hit) | return a:fname | endif
			    let l:root = substitute(fnamemodify(l:hit, ':p'), '/\.git/\=$', '', '')
			    return l:root . '/' . a:fname
			  endfunction
			  autocmd FileType markdown setlocal includeexpr=RootRelative(v:fname) suffixesadd=.md
			  ~~~
			- The `findfile` fallback is what carries a [[git/worktree]], where `finddir` alone finds no `.git` directory to stop at.
