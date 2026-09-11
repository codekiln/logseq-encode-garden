logseq-entity:: [[Logseq/Entity/Question]]

- # In [[tuicr]], can I compose a PR comment in [[nvim]] to get [[vim]] keybindings and Markdown rendering?
	- ## [[AI Answer]]
		- **Short answer:** Partially, via a config flag — but there is no way to shell out to a real external `nvim` process (and no Markdown preview) for the comment box specifically.
		- tuicr's comment box has a `comment_vim` config option (default `false`); when set (or toggled at runtime with `:vim` / `:set vim!`), the box switches to [`edtui`](https://github.com/preiter93/edtui) modal editing — `hjkl`, `w`/`b`/`e`, `dd`/`D`/`ciw`/`x`, `u`/`Ctrl-r`, visual `v`+`y`/`d`/`p`, `:w`/`:q`-style save/cancel. That is a real Vim-modal *emulation* built into the comment box, not `nvim` itself — no plugins, no LSP, no Markdown rendering. Verified in `agavra/tuicr`: `docs/CONFIG.md`, `docs/KEYBINDINGS.md` ("Comment mode"), and `src/app/comment_vim.rs`.
		- Separately, tuicr does shell out to `$EDITOR` (see `src/editor.rs`, `:edit` command in `docs/KEYBINDINGS.md`) — but only to open the **focused diff file** in your real editor, not the comment text box.
		- [[tuicr/Wishlist]] already tracks the closest related idea — editing the PR **description** in `$EDITOR` — following the same "hand off larger text to an external editor" shape that could extend to comments.
		- **Workaround today:** enable `comment_vim = true` for Vim-modal editing inside tuicr, or draft the comment in real `nvim` and paste the finished Markdown into the comment box for full editor ergonomics plus live Markdown preview (e.g. via a plugin like [glow](https://github.com/charmbracelet/glow) or an in-editor Markdown renderer).
		- Filed as a wishlist item: [[tuicr/Wishlist]] → "Compose PR/review comments in `$EDITOR`".
