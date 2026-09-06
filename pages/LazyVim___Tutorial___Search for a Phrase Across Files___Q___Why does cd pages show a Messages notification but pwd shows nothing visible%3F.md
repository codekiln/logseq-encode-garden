logseq-entity:: [[Logseq/Entity/Question]]
- # Why does `:cd pages` show a `Messages` notification but `:pwd` shows nothing visible?
	- ## [[AI Answer]]
		- **Short answer:** in this garden's LazyVim setup, `folke/noice.nvim` takes over cmdline and message rendering by default. It routes both commands' plain messages through the same floating `Messages` view, but only the message triggered by `:cd` reliably renders on screen; a bare `:pwd` is recorded in `:messages` history without ever becoming visible.
		- LazyVim's own `ui.lua` configures `noice.nvim` by default, not as an opt-in extra. Noice's default routing sends plain messages (the kind produced by both `:cd` and `:pwd`) to a `notify`-style view whose backend list is `{ "snacks", "notify" }`, so it renders via [[nvim/Plugin/snacks.nvim/Notifier]] when available.
		- Testing directly in this repo's LazyVim configuration confirms the split: `:cd pages` reliably opens a floating `Messages` box reporting the new path, in a fresh session and repeatedly. A bare `:pwd`, run first thing or immediately afterward, never shows that box, even though its text is present in `:messages`.
		- Practical takeaway: don't rely on `:pwd` alone for visible confirmation here. `:cd`'s own message already reports the new directory, and running `:messages` afterward shows the recorded path even when no popup appeared.
