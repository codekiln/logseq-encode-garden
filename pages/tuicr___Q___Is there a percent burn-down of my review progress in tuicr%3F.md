logseq-entity:: [[Logseq/Entity/Question]]

- # Is there a percent burn-down of my review progress in [[tuicr]]?
	- ## [[AI Answer]]
		- **Short answer:** not literally a percentage — tuicr tracks review progress as a **`reviewed/total` fraction** in the file tree title (e.g. `Files · 2/12 · 12 of 58`), plus a "burn-down loop" behavior for `r` when reviewed files are hidden. There's no `%` figure anywhere in the docs or source.
		- The tree title's `reviewed/total` count is deliberately **not** scoped to the currently visible rows — it stays the true count of the whole review population even while files are hidden or filtered, "since scoping it to the visible rows would collapse it to `0/n` exactly when progress matters most" ([KEYBINDINGS.md](https://github.com/agavra/tuicr/blob/main/docs/KEYBINDINGS.md), "Hiding reviewed files").
		- The literal phrase **"burn-down"** in the docs refers to a workflow, not a stat: with `:set noreviewed` active (hiding already-reviewed files), pressing `r` on the file you're reading marks it reviewed *and* jumps you to the next unreviewed file, wrapping at the end — a "burn-down loop" through the remaining diff.
		- A file whose hunks are individually marked with `R` is not hidden by that toggle — only the file-level `r` flag counts toward hiding/burn-down.
		- Source: [KEYBINDINGS.md on GitHub](https://github.com/agavra/tuicr/blob/main/docs/KEYBINDINGS.md) ("Hiding reviewed files" section); confirmed in source comments in `src/app/file_filter.rs`, `src/app/reviewed.rs`, and `src/ui/file_list.rs` in local clone `github.com/agavra/tuicr`.
			- TODO turn these into github links following [[My/AI/Rule/How to Communicate Effectively With Me/A pointer carries a link, an id with a slug, and a reason]]
			  id:: 6aa41aa4-bf60-42b9-aa86-d716f4e45a9c