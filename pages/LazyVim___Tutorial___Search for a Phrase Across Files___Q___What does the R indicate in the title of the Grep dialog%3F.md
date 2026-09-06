logseq-entity:: [[Logseq/Entity/Question]]
- # What does the `R` indicate in the title of the `Grep` dialog?
	- ## [[AI Answer]]
		- `R` marks the regex toggle's non-default state: regex matching is off, so the search is using fixed strings. The [[nvim/Plugin/snacks.nvim/Picker]] is configured to show the badge when its `regex` option is `false`.
		- A useful reminder is **`R` visible → read the text literally**. Press `<Alt-r>` again and the `R` disappears as regex matching returns.
