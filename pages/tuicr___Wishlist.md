logseq-entity:: [[Logseq/Entity/Wishlist]]

- # Wishlist
	- Upstream feature ideas for [[tuicr]] — candidates for a future issue or PR against [agavra/tuicr](https://github.com/agavra/tuicr).
	- ## Yank / quote PR description in a comment
		- [[tuicr/Q/Is there a way to copy text from the PR description and quote it in a comment?]]
		- Wanted: in-app selection (mouse drag or visual mode) over the Overview / PR description panel (`PrInfoLine`), with `y` copying that text — and a path to paste it into a comment as a Markdown `>` block quote, without relying on the terminal bypass modifier.
		- Today visual yank only covers diff source lines (plus hunk/file headers); the description panel is searchable and readable but not yankable through tuicr's own selection.
	- ## Wrap PR description text in Overview
		- [[tuicr/Q/In tuicr, is there a way to turn on word wrap for PR descriptions in Overview?]]
		- Wanted: a dedicated wrap toggle for the PR info/Overview panel so long description lines are easy to read without horizontal scrolling.
		- Today `:set wrap` / `wrap = true` only apply to the diff view; there is no separate config or command for PR-description wrapping.
	- ## Edit PR description in external editor and push back to forge
		- Wanted: open the PR description body directly in `$EDITOR` (for example `nvim`), then save-and-close to write the updated body back to the forge PR (GitHub/GitLab/Gitea/etc.) in one flow.
		- This would mirror tuicr's existing editor handoff ergonomics while extending them from file edits/comments to PR metadata editing.
