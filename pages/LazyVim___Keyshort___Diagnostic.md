- [[Keyshort]] [[LazyVim]] [[LazyVim/Keyshort]]
	- **Next and Previous Diagnostic** [[Card]]
		- Shortcut: `]d` next, `[d` previous
		- Description: Jumps to the next or previous diagnostic in the buffer and opens its float. `]e` / `[e` restrict the jump to errors, `]w` / `[w` to warnings.
	- **Show Diagnostics for the Current Line** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-11T04:00:00.000Z
	  card-last-reviewed:: 2026-09-10T10:56:29.831Z
	  card-last-score:: 1
		- Shortcut: `<leader>cd`
			- [[Mnemonic]]
				- `c`: code
				- `d`: diagnostics
		- Description: Opens a floating window with the full text of every diagnostic on the cursor line — the readable version of a message truncated inline.
		- TODO provide a link to file(s)s of various languages where this can be tested in nvim with real diagnostics in a few languages; possibly in conjunction with a lazyvim lsp tutorial
		  id:: 6aa28c77-e9c2-4928-9ce9-76963a0c06f4
	- **Picker over Buffer Diagnostics** [[Card]]
		- Shortcut: `<leader>sD`
		- Description: Lists diagnostics for the current buffer only.
	- **Picker over All Diagnostics** [[Card]]
		- Shortcut: `<leader>sd`
		- Description: Lists diagnostics across every attached buffer.
		- [[My Question]]
		  id:: 6aa28180-52bf-4be1-92bf-33f0febb701e
			- I see `no results found for diagnostics` when I use this in a markdown document. Is this because it's not set up properly or because there are no diagnostics for the document, and how can I tell?
			- [[AI Answer]]
				- Short answer: mostly the first cause. Diagnostics are **off by default** for every filetype — `config/autocmds.lua` calls `vim.diagnostic.enable(false)` on `VeryLazy`, so `<leader>sd` shows nothing anywhere until `<leader>ud` turns diagnostics on for the session.
				- Second, [[LazyVim/plugins/extras/lang/markdown]] wires exactly one diagnostics source for markdown — `mfussenegger/nvim-lint` running `markdownlint-cli2` — installed correctly via Mason and confirmed working directly (`markdownlint-cli2 -` lints fine from stdin). Occasionally it can flash a one-off `ENOENT` notification right when a markdown file is the very first buffer opened: Mason only adds its `bin/` directory to `$PATH` once `mason.nvim` finishes its own setup, and that can race the first `nvim-lint` run triggered on the same buffer-open event. It self-resolves for the rest of the session once Mason's `$PATH` update lands.
				- To tell which case you are in: run `<leader>ud` first. If the picker still finds nothing on a markdown buffer *after* that, check `:messages` or the notification history (`<leader>n`) for a lingering `ENOENT`/`markdownlint-cli2` error — a one-time flash on file open is the harmless startup race above; a persistent one on every save means the linter genuinely isn't resolving and Mason needs a look (`:Mason`, search for `markdownlint-cli2`).
	- [[My Note]]
		- Case is the opposite of what a general LazyVim cheat sheet suggests: here lowercase `<leader>sd` is the *wide* list and uppercase `<leader>sD` is the *buffer* list.
		- Diagnostics start **disabled** — `config/autocmds.lua` calls `vim.diagnostic.enable(false)` on `VeryLazy`. None of these keys show anything until `<leader>ud` turns diagnostics on for the session (see [[LazyVim/Keyshort/UI/Toggle]]).
		- `<leader>xx` and `<leader>xX` open the same information as a persistent [[nvim/Plugin/trouble.nvim]] list rather than a picker.