logseq-entity:: [[Logseq/Entity/Question]]

- # Is there a command like `more` that is the opposite of `less`?
	- ## [[AI Answer]]
		- **Short answer:** yes — `more` itself. It's not really the "opposite" of `less`, though; it's the older, simpler pager that `less` was written to replace.
		- **`more`** shipped first, in 3BSD (1978). It pages forward through text one screen at a time and, in its original form, can't scroll backward.
		- **`less`** came later (Mark Nudelman, 1983-85) as a more capable pager: backward scrolling, search, and the ability to start before the whole input has loaded. Its name is a pun on "less is more" — `less` does *more* than `more`, hence the joke.
		- So there's no separate command that's the naming "opposite" of `less` — `more` already is, and it predates `less`. On most modern systems (Linux, macOS) the `more` binary is a distinct, more limited implementation from `less`, not just an alias for it.
		- **Bonus in the same joke lineage:** `most`, a pager written to do even more than `less` (multi-file, multi-window, wider horizontal scrolling support).
