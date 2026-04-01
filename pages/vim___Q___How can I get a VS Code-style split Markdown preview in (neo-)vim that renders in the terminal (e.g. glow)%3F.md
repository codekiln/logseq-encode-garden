logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[glow]], [[Terminal/Q/Is there a terminal-native Markdown viewer or a cat-like CLI that renders Markdown in the terminal?]], [[Glow/Q/How do I use Glow as a default pager for markdown documents when I'm in a terminal?]]
via:: [[2026-04-01 Wed]]

- # How can I get a VS Code–style split [[Markdown]] preview in (neo-)[[vim]] that renders in the terminal (e.g. [[glow]])?
	- ## My Notes
		- Want editor split + ANSI/TUI rendering, not browser HTML preview.
	- ## Answer
		- [[AI/Response]]
			- **Yes — several patterns exist**, but there is no single “official” Neovim feature that is exactly VS Code’s Markdown preview with a **terminal** renderer. You combine **splits** + **`:terminal`** (or a plugin) + a CLI like **`glow`** (or `mdcat`, Pandoc `-t ansi`, etc.).
			- ### Plugin-shaped options
				- **[glow.nvim](https://github.com/ellisonleao/glow.nvim)** — wraps the **`glow`** binary and shows rendered Markdown inside Neovim (historically popular). The repo has been **archived**; treat it as “works until it doesn’t,” not a long-term bet. It is still a common reference implementation for “glow inside Neovim.”
				- **[mdpreview.nvim](https://github.com/mrjones2014/mdpreview.nvim)** — described as a **live-reloading** preview using a **configurable CLI renderer** (defaults toward **`glow`**), with a **split window** workflow. Marked **WIP** and low activity; worth a try if you want split + auto-refresh, but expect rough edges.
			- ### Minimal DIY (split + terminal + glow)
				- Open a vertical split and run glow on the **file on disk**: e.g. `:vsplit | terminal glow -p %` (adjust paths; **`glow`** must be installed). This approximates “split preview” when you save and re-run or use a mapping.
				- For **unsaved buffers**, a small Lua pattern is to **write a temp file**, open `:terminal glow -p <tempfile>`, and clean up on `TermClose`; see [Haylin Moore’s walkthrough](https://hayl.in/posts/nvim-glow/) for a concrete example. You can extend that with **`BufWritePost`** / **`TextChanged`** autocmds if you want nearer-to-live updates (mind performance and flicker).
			- ### “Smart” preview without a separate terminal pane
				- **[render-markdown.nvim](https://github.com/MeanderingProgrammer/render-markdown.nvim)** gives a **rich in-buffer** Markdown view (headings, callouts, etc.) using Neovim’s UI — **not** the same as piping through **`glow`**, but it matches the “stay in the editor” spirit when HTML preview plugins feel heavy.
			- ### Outside Neovim
				- A **terminal multiplexer split** (e.g. **tmux**) with Neovim in one pane and `glow -p` (optionally wrapped with **`watchexec`** / **`entr`** on save) in the other is a dependable pattern when you want zero Lua and true full-terminal rendering.
			- ### Sources
				- [ellisonleao/glow.nvim](https://github.com/ellisonleao/glow.nvim)
				- [mrjones2014/mdpreview.nvim](https://github.com/mrjones2014/mdpreview.nvim)
				- [MeanderingProgrammer/render-markdown.nvim](https://github.com/MeanderingProgrammer/render-markdown.nvim)
				- [Haylin Moore — nvim keybind for rendering markdown in glow](https://hayl.in/posts/nvim-glow/)
