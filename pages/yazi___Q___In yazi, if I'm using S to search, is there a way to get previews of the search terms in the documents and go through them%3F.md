logseq-entity:: [[Logseq/Entity/question]]

- # In [[yazi]], if I'm using `S` to search, is there a way to get previews of the search terms in the documents and go through them?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** Not natively — the built-in `S` (ripgrep) search returns a list of matching files but does not preview match context in the preview pane. Plugins that integrate [[fzf]] add previews.
			- **What `S` does:** Opens a [[ripgrep]] content search prompt. Results populate the file list incrementally; yazi shows matching files but does not scroll the preview pane to the matched line or highlight the match.
			- **Feature request:** [GitHub issue #1095](https://github.com/sxyazi/yazi/issues/1095) ("preview could highlight the first match") was closed as duplicate of [#3346](https://github.com/sxyazi/yazi/issues/3346), so native preview-at-match is a known open request.
			- **Plugins that add search previews:**
				- [[yazi/Plugin/fr.yazi]] (51 ★, [[Lua]]) — pipes [[rg]] results into [[fzf]] with [[bat]]-powered syntax-highlighted previews; navigate matches with `Ctrl-J/K` / arrow keys.
				- [[yazi/Plugin/yafg.yazi]] (12 ★, [[Lua]]) — fuzzy find + grep with interactive rg/fzf; opens selected match in your editor at the matched line.
				- [[yazi/Plugin/fazif.yazi]] (15 ★, Shell) — searches with `fd`, `rg`, `rga` and spawns fzf with preview.
			- **Navigation:** All plugin approaches rely on fzf for cycling through matches (standard fzf keys: arrow keys or `Ctrl-J/K`, `Enter` to confirm).
			- Docs: [yazi keymap](https://yazi-rs.github.io/docs/configuration/keymap/), [yazi plugins overview](https://yazi-rs.github.io/docs/plugins/overview/)
