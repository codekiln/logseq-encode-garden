logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[vim/Keyshort/Move by Display Line]], [[nvim]]
via:: [[2026-04-01 Wed]]

- # How can I configure (neo-)vim so that by default it wraps in a way that takes word boundaries into account, rather than splitting words in the middle?
	- Same options in [[vim]] and [[nvim]]; they affect **display** only (buffer text is unchanged).
	- ## Answer
		- [[AI/Response]]
			- **Turn on soft wrap:** **`set wrap`** so long logical lines are shown on multiple screen rows instead of scrolling horizontally (`nowrap`).
			- **Break at nicer positions:** **`set linebreak`** (short form **`set lbr`**) so wrapped lines prefer breaks **before** characters listed in **`breakat`** (spaces, tabs, and punctuation by default), instead of chopping the line at the last character that fits in the window. See [`:help 'linebreak'`](https://vimhelp.org/options.html#'linebreak') and [`:help 'breakat'`](https://vimhelp.org/options.html#'breakat').
			- **Optional polish:** **`set breakindent`** indents continuation rows so wrapped blocks read more clearly ([`:help 'breakindent'`](https://vimhelp.org/options.html#'breakindent')). Tune with **`breakindentopt`** if needed.
			- **Make it default:** Put the **`set`** lines in **`~/.vimrc`**, **`~/.config/nvim/init.vim`**, or your **`init.lua`** (e.g. `vim.o.wrap = true`, `vim.o.linebreak = true`, `vim.o.breakindent = true`).
			- **Navigation:** With wrap on, use **`gj` / `gk`** for **display-line** motion (see [[vim/Keyshort/Move by Display Line]]); **`j` / `k`** still move by **buffer** lines.
			- **Not the same as auto-formatting:** **`textwidth`** + **`formatoptions`** control **inserting** hard line breaks when you type or use **`gq`**; **`linebreak`** only changes how an existing long line is **shown** when **`wrap`** is on.
	- ## My Notes
