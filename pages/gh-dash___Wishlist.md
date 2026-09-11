logseq-entity:: [[Logseq/Entity/Wishlist]]

- # Wishlist
	- Upstream feature ideas for [[gh-dash]] — candidates for a future issue or PR against [dlvhdr/gh-dash](https://github.com/dlvhdr/gh-dash).
	- ## Mark PR as draft (inverse of ready for review)
		- [[gh-dash/Q/Does gh-dash have a keyshort like W ready for review which is the inverse (mark as draft)?]]
		- Wanted: a built-in key (and `builtin:`) that converts a ready PR back to draft — the inverse of `W` / `builtin: ready`.
		- Today only `W` → `gh pr ready` exists; convert-to-draft needs a custom `command:` with `gh pr ready --undo`, and the dashboard row may need a manual refresh afterward.