logseq-entity:: [[Logseq/Entity/Keyshort]]
see-also:: [[vim/Q/In (neo-)vim or LazyVim, how can I open a file whose path a Markdown document gives from the repo root?]], [[nvim/Keyshort/Open/Open URL or Filepath Under Cursor]]
- [[Keyshort]] [[vim]] [[vim/Keyshort]] [[vim/Keyshort/Open]]
	- **Follow the File Path Under the Cursor**
		- Shortcut: `gf`
		- Description: Reads the filename at or after the cursor and edits it in the current window. Stock [[vim]], the same key in [[nvim]], and [[LazyVim]] leaves it alone.
		- The [[Mnemonic]]: `f` for **f**ile. `gf` stays inside the editor, while `gx` hands the target to the operating system.
	- **Open the same target somewhere other than the current window**
		- | Keys                | Where the file opens                                        |
		  | ------------------- | ----------------------------------------------------------- |
		  | `gf`                | the current window                                          |
		  | `<C-w>f`            | a horizontal split                                          |
		  | `<C-w>v` then `gf`  | a vertical split                                            |
		  | `<C-w>gf`           | a new tab                                                   |
		  | `gF`                | the current window, on the line named by a `path:12` suffix |
		  | `gf` in visual mode | the current window, taking the whole selection as the name  |
		- There is no stock vertical-split form of `gf`. Splitting the window first and following the path in the new one gets there in two keys.
		- `<C-o>` returns from the jump and `<C-i>` moves forward again — see [[vim/Keyshort/Jump/Back and Forward]].
	- **What decides whether the path resolves**
		- `isfname` decides where the name starts and ends. Two characters a [[Logseq]] filename leans on are in it by default: `_` carries the triple underscore of a namespace, and `%` carries the `%3F` that stands in for a question mark.
		- `path` is the list of directories the search runs through. Its default `.,,` means the directory of the file being edited, then the editor's working directory.
		- `suffixesadd` is empty on a [[Markdown]] buffer, so a target written without its `.md` fails until the option is set.
	- **Where it stops**
		- A space ends the name early. `isfname` holds no space, so `pages/A Page With Spaces.md` is read as `pages/A` and the search fails. Selecting the whole path and pressing `gf` in visual mode opens it, since the visual form ignores `isfname` and takes the selection whole.
		- The list marker counts as part of a filename. `-` is an `isfname` character, so `gf` with the cursor on the `-` of a bullet reads that dash as the name. From the space after it onward, the whole path is in reach.
		- A buffer-local mapping that steps past the marker puts the key back in reach from column 1 — [[vim/Q/In (neo-)vim or LazyVim, how can I open a file whose path a Markdown document gives from the repo root?]] carries it.
	- [[My Note]]
		- A path written from the repository root — the shape a garden page uses for `journals/2026_08_24.md` — resolves under `gf` only while the editor's working directory is that root. [[vim/Q/In (neo-)vim or LazyVim, how can I open a file whose path a Markdown document gives from the repo root?]] has the setting that frees it from the working directory.
		- For a link written as [[Markdown]] rather than as a bare path, [[LazyVim/Q/In LazyVim, how can I open a Markdown link with a keyboard shortcut?]] compares `gf` against `gx` and `gd` on the same target.
