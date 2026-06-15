logseq-entity:: [[Logseq/Entity/Question]]

- # Does [[Foam]] have an alias feature like [[Obsidian]] does?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** Partially — [[Foam]] supports a frontmatter `alias:` key that surfaces aliases in autocomplete, but unlike [[Obsidian]], bare `[[alias]]` wikilinks do **not** resolve to the target note; they create a new note instead.
			- ### Frontmatter `alias:` (since v0.18.5, June 2022)
				- Declare alternative names in YAML frontmatter using `alias:` (singular — [[Foam]] differs from [[Obsidian]]'s `aliases:`):
					- ~~~yaml
					  ---
					  alias: JavaScript, JS
					  ---
					  ~~~
				- Aliases appear in wikilink autocomplete; selecting one inserts `[[filename|alias]]` (display alias, underlying filename preserved).
				- Since v0.28.0 aliases are also indexed for VS Code's "Go To Symbol in Workspace" search.
			- ### Inline display alias
				- `[[note-filename|Display Text]]` renders as display text in preview (since v0.13.8).
				- Purely cosmetic — does not enable `[[Display Text]]` to resolve from elsewhere.
			- ### Critical limitation vs [[Obsidian]]
				- In [[Obsidian]], declaring `aliases: [JS]` makes `[[JS]]` resolve to that note anywhere in the vault.
				- In [[Foam]], writing `[[JS]]` when `JS` is a declared alias creates a **new** note instead of navigating to the aliased note. Confirmed in [issue #1066](https://github.com/foambubble/foam/issues/1066), closed as "not planned" — the maintainer cited Markdown compatibility concerns.
			- ### Workarounds
				- Use the pipe syntax every time: `[[high-cycle-fatigue|HCF]]` — autocomplete helps insert this form.
				- Use Markdown reference definitions within a single file: `[HCF]: high-cycle-fatigue` (works only within that file).
				- Name the file with the short form (e.g. `hcf.md`) and put the long title in a heading.
			- Sources: [PR #1014](https://github.com/foambubble/foam/pull/1014) · [Issue #1066](https://github.com/foambubble/foam/issues/1066) · [note-properties.md](https://github.com/foambubble/foam/blob/main/docs/user/features/note-properties.md)
