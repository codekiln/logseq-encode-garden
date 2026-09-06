logseq-entity:: [[Logseq/Entity/Question]]
- # Why does searching for `tags:: [[Diataxis/Tutorial]]` require turning off [[Regex]] matching in [[rg]]?
	- ## [[AI Answer]]
		- In a regular expression, square brackets delimit a [[Regex/Character Class]], which matches one character from a set. Rust's regex engine permits nested classes, so `[[Diataxis/Tutorial]]` is parsed as an outer class containing the inner class `[Diataxis/Tutorial]`. The brackets are syntax; they consume no text.
		- The nested class consumes one of the letters in `Diataxis/Tutorial`, or `/`. Because `T` is one of those letters, `tags:: ` followed by `T` satisfies the complete regex. `rg` looks for a matching substring, so the rest of the line does not have to match.
		- Pressing `<Alt-r>` turns off regex matching. The [[nvim/Plugin/snacks.nvim/Picker]] then runs `rg` with `--fixed-strings`, so every bracket, slash, and letter in `tags:: [[Diataxis/Tutorial]]` must appear in that order.
