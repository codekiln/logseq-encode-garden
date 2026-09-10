logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tuicr/Wishlist]]
- # Is there a way to copy text from the [[tuicr]] PR description and quote it in a comment?
	- ## [[AI Answer]]
		- **Short answer:** Not as a first-class tuicr action. In-app visual yank (`y` after mouse/keyboard selection) copies **diff source lines** (and hunk/file headers), not PR-description panel text. To reuse description wording in a comment, use the terminal's **bypass selection**, paste into the comment box, and add Markdown `>` yourself if you want a block quote.
		- ### What yank covers
			- Mouse drag in the diff, then `y`, copies the selected **source lines** ([Keybindings — Mouse](https://github.com/agavra/tuicr/blob/main/docs/KEYBINDINGS.md)).
			- Keyboard visual mode + `y` uses the same path: `copy_visual_selection` only pulls from diff/`ExpandedContext` content via `content_for_side`, or whole hunk/file headers via `atomic_text_for_annotation`. `PrInfoLine` (the Overview / PR description panel from [#495](https://github.com/agavra/tuicr/pull/495)) is neither.
			- Plain `y` / `:clip` exports the **review** (comments + structure), not the PR body. `Y` copies the **comment at the cursor**. `:copy-url` copies the open PR URL only.
		- ### Practical workaround for quoting description text
			- 1. In the Overview / PR description area, hold the terminal **bypass modifier** and drag to select (usually **Shift** or **Option/Alt** — documented in [Keybindings — Mouse](https://github.com/agavra/tuicr/blob/main/docs/KEYBINDINGS.md)), then copy with the terminal/OS clipboard shortcut.
			- 2. Start a comment with `c` (line), `C` (file), or `<leader>c` (review-level).
			- 3. Paste into the comment box (bracketed paste is supported in comment mode and in `comment_vim` mode). Prefix lines with `>` for a Markdown block quote — tuicr does not auto-wrap pasted text as a quote.
		- ### Outside tuicr
			- If bypass selection is awkward in your multiplexer/terminal stack, pull the body with `gh pr view --json body -q .body` (or open the PR in the browser) and paste into the comment the same way.
		- Sources: local clone `github.com/agavra/tuicr` (`src/app/visual.rs`, `src/app/navigation.rs` `content_for_side` / `atomic_text_for_annotation`, `docs/KEYBINDINGS.md`); [KEYBINDINGS.md on GitHub](https://github.com/agavra/tuicr/blob/main/docs/KEYBINDINGS.md); PR [#495](https://github.com/agavra/tuicr/pull/495).
