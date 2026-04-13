logseq-entity:: [[Logseq/Entity/question]]
via:: [[2026-04-06 Mon]]

- # How can I search for the [[boolean/AND]] of multiple terms in [[rg]]?
	- ## [[My Notes]]
		- ### initial query
			- using [[rg/-e PATTERN]] multiple times searches for the [[boolean/OR]] of all the terms; according to [[rg/manpage]],
				- ((69dca805-55f5-4bad-8c83-c81495946547))
			- one common way I've used in the past with [[grep]] is piping; one can do `grep lazygit | grep worktree` to find places that reference both `lazygit` and `worktree`. But when using options like [[rg/--files-with-matches]], not certain that would work.
		- ### follow-up reflection
			-
	- ## Answer
		- [[AI/Response]]
			- There is no single `rg` flag for "match all of these patterns" the way repeated [[rg/-e PATTERN]] means "match any of these patterns" ([[boolean/OR]] per [[rg/manpage]] and the [[rg/-e PATTERN]] excerpt).
			- **Line-level AND (each pattern appears on the same output line)**
				- Fixed order: one regex such as `foo.*bar`; add [[rg/-w]] or [[rg/-F]] when you care about word boundaries or literal punctuation instead of regex syntax.
				- Default regex engine, arbitrary order: bracket permutations (`foo.*bar|bar.*foo`) or filter with a shell pipeline (`rg 'foo' . | rg 'bar'`), same spirit as the [[grep]] example in [[My Notes]].
				- With [[rg/--pcre2]], you can use lookaround; e.g. `rg --pcre2 '(?=.*foo)(?=.*bar)'` matches lines that contain both substrings (`-P` is the short form). Background: [ripgrep FAQ — lookaround / backreferences](https://github.com/BurntSushi/ripgrep/blob/master/FAQ.md#fancy).
			- **File-level [[boolean/AND]] (each pattern appears somewhere in the same file)**
				- Run [[rg/--files-with-matches]] twice: list paths for the first term, then search only those paths for the second, e.g. `rg -l --null 'foo' | xargs -0 rg -l 'bar'` ([[rg/--null]] emits paths separated by [[ASCII/C0/NUL]] so `xargs -0` survives spaces or odd characters). Intersecting two sorted `rg -l` lists with `comm -12` is the same idea in another shape.
			- Caveats: [[rg/--pcre2]] is missing in some package builds (the FAQ describes the error) and is often slower than the default engine for large trees.