alias:: [[nvim/Keyshort/Open/gx]]
logseq-entity:: [[Logseq/Entity/Keyshort]], [[Logseq/Entity/Card]]
- [[Keyshort]] [[nvim]] [[nvim/Keyshort]] [[nvim/Keyshort/Open]]
	- **Open the URL or Filepath Under the Cursor** [[Card]]
		- Shortcut: `gx`
		- Description: Hands whatever is under the cursor to the system's default handler — an `http` address opens in the browser, a file in whichever application claims it — and leaves the buffer where it is. Bound in normal and visual mode.
		- The [[Mnemonic]]: `x` for e**x**ternal. `gx` leaves the editor; `gd` and `gf` stay inside it.
	- [[My Note]]
		- A stock [[nvim]] core default, not something [[LazyVim]] adds — LazyVim only relabels it in [[nvim/Plugin/which-key.nvim]]. It routes the target through `vim.ui.open`, which shells out to `open` on [[macOS]]. That is why it behaves differently from vim's `gx`, which is netrw's.
		- Which of `gx`, `gf` and `gd` to reach for depends on what the link points at: [[LazyVim/Q/In LazyVim, how can I open a Markdown link with a keyboard shortcut?]] compares all three, and [[LazyVim/Tutorial/Browse a Markdown Knowledge Garden]] puts them in a browsing workflow.
