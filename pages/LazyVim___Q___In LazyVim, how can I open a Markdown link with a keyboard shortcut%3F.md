logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[LazyVim/Q/In LazyVim, how can I traverse wiki links in an Obsidian knowledge garden?]], [[LazyVim/plugins/extras/lang/markdown]]

- # In [[LazyVim]], how can I open a [[Markdown]] link with a keyboard shortcut?
	- ## [[AI Answer]]
		- **Short answer:** there are two keys, and the target decides which one. `gx` hands the target to the operating system — the right key for an `http` URL, which lands in the default browser. `gd` follows the link *inside* the editor and is the better key for a link to another file in the same repository: it fires from anywhere on the link, resolves a target with no extension, and jumps to the exact heading when the link carries a `#anchor`.
		- | Link target              | `gx`                       | `gf`                        | `gd`                            |
		  | ------------------------ | -------------------------- | --------------------------- | ------------------------------- |
		  | `https://…`              | default browser            | tries to fetch it as a file | nothing                         |
		  | `./file.md`              | the Mac app bound to `.md` | opens it, destination only  | opens it, anywhere on the link  |
		  | `./file.md#heading`      | fails                      | fails                       | lands on the heading            |
		  | `./file` (no extension)  | fails                      | needs `suffixesadd=.md`     | resolves to `file.md`           |
		  | destination with a space | truncated                  | fails                       | resolves in `<…>` or `%20` form |
		- ### `gx` — hand the target to the system
			- Stock [[nvim]] binds `gx` in normal and visual mode as a core default. [[LazyVim]] does not rebind it; it only relabels it "Open with system app" in [[nvim/Plugin/which-key.nvim]]. [[Answer/Official]] from [:help gx](https://neovim.io/doc/user/various.html#gx).
			- The mapping collects the target at the cursor and passes it to `vim.ui.open`, which shells out to `open` on [[macOS]]. That is the whole story: `gx` never opens anything in the current editor.
			- The `markdown_inline` treesitter highlights query tags the entire `[text](destination)` node with its destination, so `gx` fires from the label as readily as from inside the parentheses. It needs treesitter highlighting live on the buffer, which the Markdown extra provides.
			- Two consequences worth knowing for a relative link: the raw path goes to `open` verbatim, so a `.md` file opens in whatever app [[macOS]] has bound to `.md` rather than in the buffer; and that path is resolved against the working directory, not against the directory of the file being edited.
			- A language server advertising `textDocument/documentLink` would take priority over the treesitter path. Marksman does not advertise it, so on a Markdown buffer here the treesitter path is always the one that runs.
		- ### `gf` — follow a file path in the editor
			- Plain vim, no plugin involved: `gf` edits the filename under the cursor, `<C-w>f` opens it in a split, `<C-w>gf` in a new tab, and `gF` jumps to a line number trailing the path.
			- Unlike `gx`, the cursor must sit **on the destination** inside the parentheses. On the link label, `gf` grabs the label word and fails.
			- Resolution runs through `path`, which defaults to `.,,` — the leading `.` is the directory of the current file, so an ordinary relative link resolves the way the Markdown means it.
			- The gaps are real: `suffixesadd` is empty for Markdown, so an extensionless `./file` fails until it is set to `.md`; and a destination containing a space never resolves, with or without the `<…>` escape, because the filename is read through `isfname`, which stops at the space.
		- ### `gd` — follow the link with the language server
			- The [[LazyVim/plugins/extras/lang/markdown]] extra installs the Marksman language server, and [[LazyVim]] binds `gd` to go-to-definition for any server advertising `definition`. Marksman advertises `definition` and `references`, so `gd` and `gr` both work on a Markdown buffer. [[Answer/Official]] from the [Marksman README](https://github.com/artempyanykh/marksman).
			- This is the strongest of the three for an in-repository link. It fires from anywhere on the link, follows `./target.md#some-heading` to the heading line rather than the top of the file, resolves an extensionless `./bare` to `bare.md`, and handles a spaced destination written either `<./My Page.md>` or `./My%20Page.md`. A raw unescaped space is not a link at all, so nothing follows it.
			- `gr` lists references to the destination. `<C-o>` returns from the jump and `<C-i>` moves forward again — see [[vim/Keyshort/Jump/Back and Forward]].
			- Marksman only resolves cross-file links inside a project, meaning a Git repository or a directory holding a `.marksman.toml`. Opening from the root with `nvim .` is what makes this work.
			- When `gd` does nothing, `<leader>cl` shows the attached clients and `:Mason` shows whether Marksman is installed — see [[LazyVim/Keyshort/LSP/Navigation]].
		- ### When the built-ins are not enough
			- None of these three offers a picker over every link in the buffer, or a single key that follows a link and splits it into a new window on the way. A plugin covers that ground; the sibling question on traversing wiki links has the detail.
