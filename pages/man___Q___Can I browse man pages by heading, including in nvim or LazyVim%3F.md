logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[LazyVim/Tutorial/Navigate Man Pages by Heading]]
- # Can I browse `man` pages by heading, including in [[nvim]] or [[LazyVim]]?
	- ## [[AI Answer]]
		- **Short answer:** `man` finds and formats a manual page, then hands the result to a pager. The macOS `man` program and its usual pager, `less`, do not expose the page's headings as a navigable hierarchy. Neovim's built-in man-page viewer does: open the page with `:Man tmux`, then press `gO` for a table of contents.
		- ### In the terminal pager
			- The installed `/usr/bin/man` accepts `-P pager`; `MANPAGER` overrides `PAGER`. Its default is `less`, whose navigation is text-based: search for an uppercase heading with `/^COMMANDS$`, then use `n` and `N` to move among matches. A broader search such as `/^[A-Z][A-Z0-9 /_-]*$` finds many top-level headings. `less` does not parse those matches into an outline. [[Answer/Official]] from [OpenBSD man(1)](https://man.openbsd.org/man.1) and [less(1)](https://man.openbsd.org/less.1).
			- This machine currently sets `MANPAGER` to `col -bx | bat --language=man --style=plain --paging=always`. [[CLI/Tool/bat]] supplies highlighting and invokes a pager for scrolling, but it does not add heading-aware navigation.
		- ### In Neovim
			- From an open editor: `:Man tmux`.
			- From the shell: `nvim +'Man tmux'`.
			- In the man-page buffer, `gO` opens a location-list outline. Select an entry and press Enter to jump to it; `q` closes the outline or man window. On the installed `tmux(1)` page, Neovim finds the main headings plus many indented command and option entries, so the outline is more detailed than a list of top-level sections.
			- Put the cursor on a reference such as `printf(3)` and press `K` or `Ctrl-]` to open that man page; `Ctrl-T` returns. [[Answer/Official]] from [Neovim's man-page documentation](https://neovim.io/doc/user/filetype.html#man.txt) and [`gO` outline documentation](https://neovim.io/doc/user/various.html#gO).
			- For a one-off shell invocation using Neovim as the pager: `MANPAGER='nvim +Man!' MANWIDTH=999 man tmux`. `MANWIDTH=999` reduces hard wrapping before Neovim receives the formatted page. To make this the default, export those variables in the shell configuration; that would replace the current bat-based `MANPAGER` pipeline.
		- ### In LazyVim
			- The current [[LazyVim]] setup uses the [[nvim/Plugin/snacks.nvim/Picker]]. `<leader>sM` opens its **Man Pages** picker, which searches for a page to open. After choosing `tmux(1)`, press `gO` in the resulting man buffer to browse its internal outline. The picker chooses a manual page; Neovim's built-in `gO` provides the heading navigation. [[Answer/Official]] from [LazyVim's Snacks picker mappings](https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/plugins/extras/editor/snacks_picker.lua).
		- **Best fit:** use `:Man tmux` followed by `gO` when hierarchy matters. Keep `man tmux` with the current bat pager for quick linear reading and text search.
