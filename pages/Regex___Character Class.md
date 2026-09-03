logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[Regex]], [[rg]], [[rg/-F]]
- # Character Class
	- ## Motivating Examples
		- `config\.[jt]s` matches both `config.js` and `config.ts`: `[jt]` allows either letter at the same position.
		- `2026[-/]09[-/]03` matches both `2026-09-03` and `2026/09/03`: each `[-/]` allows either date separator.
		- `#[0-9A-Fa-f]{6}` matches a six-digit CSS hex color such as `#09aF3C`: `[0-9A-Fa-f]` allows a decimal digit or a hexadecimal letter, and `{6}` repeats that choice six times.
		- Character classes are useful when several acceptable strings differ at one or more character positions.
	- ## Overview
		- A **character class** is a part of a regular expression that matches one character from a set. `[abc]` matches `a`, `b`, or `c`; it does not match the three-character sequence `abc`.
		- The square brackets delimit the class. They are regex syntax and are not characters that the class consumes.
	- ## Common Forms
		- `[abc]` matches one listed character.
		- `[a-z]` matches one character in a range.
		- `[^abc]` matches one character other than the listed characters.
		- A quantifier changes how many characters a class may consume: `[abc]+` matches one or more consecutive characters chosen from the set.
	- ## Inner and Outer Character Classes
		- Rust regex syntax permits one bracketed character class to appear inside another. In `[[Diataxis/Tutorial]]`, the brackets pair like this:
			- ~~~text
			  [[Diataxis/Tutorial]]
			  │└─────────────────┘│  inner: `[Diataxis/Tutorial]`
			  └───────────────────┘  outer: `[[Diataxis/Tutorial]]`
			  ~~~
		- Read the four brackets from left to right: the first `[` opens the outer class, the second `[` opens the inner class, the first `]` closes the inner class, and the last `]` closes the outer class.
		- Nesting combines **sets of allowed characters**; it does not create another position in the matched text. Because this outer class contains only the inner class, `[[Diataxis/Tutorial]]` allows the same single characters as `[Diataxis/Tutorial]` and still consumes exactly one character.
		- The inner class allows any one of the distinct letters in `Diataxis/Tutorial`, or `/`. Repeated letters do not change the set.
		- Nesting becomes useful with set operations. `[0-9&&[^4]]` intersects the outer digit range `0-9` with the inner class `[^4]`, producing “one digit other than `4`.” This is the same inner-and-outer structure, used deliberately instead of accidentally.
	- ## Why `tags:: T` Matches
		- In the regex `tags:: [[Diataxis/Tutorial]]`, `tags:: ` is literal text and `[[Diataxis/Tutorial]]` is one nested character class.
		- The character class consumes one allowed character. `T` is allowed because it appears in `Tutorial`, so the complete matched substring can be `tags:: T`.
		- A normal `rg` search looks for a matching substring. It does not require the rest of the line to match, so text after the `T` is irrelevant unless the regex adds an end anchor such as `$`.
	- ## Match the Brackets Literally
		- Escape the brackets when retaining regex mode: `tags:: \[\[Diataxis/Tutorial\]\]`.
		- Use `rg -F 'tags:: [[Diataxis/Tutorial]]'` to treat the whole pattern as fixed text; see [[rg/-F]].
		- In the [[nvim/Plugin/snacks.nvim/Picker]], `<Alt-r>` selects the fixed-string form by setting `regex` to `false`, which makes the picker add `--fixed-strings` to the `rg` command.
	- ## Misconceptions
		- A character class describes alternatives for one character, not alternatives for words or phrases.
		- Doubling the brackets does not escape them in Rust regex syntax. It creates a nested character class.
		- Fixed-string search changes how the entire pattern is interpreted. Escaping changes the meaning of individual regex characters while leaving the rest of the pattern as regex syntax.
	- ## Sources
		- [Rust `regex` syntax — Character classes](https://docs.rs/regex/latest/regex/#character-classes) gives examples of nested classes, grouping, intersection, difference, and symmetric difference.
		- [Rust `regex-syntax` — `ClassSet`](https://docs.rs/regex-syntax/latest/regex_syntax/ast/enum.ClassSet.html) describes the parsed contents of a bracketed class as a union that may include another bracketed class or a binary set operation.
		- [ripgrep README — Is it really faster than everything else?](https://github.com/BurntSushi/ripgrep/blob/master/README.md#is-it-really-faster-than-everything-else) identifies Rust's regex engine as the foundation of [[rg]].
