logseq-entity:: [[Logseq/Entity/Question]]
tags:: [[Question]]

- # In [[Obsidian]], is there a command that inserts a callout, and what are those colored Info / Warning / Danger blocks called?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Callouts — Obsidian Help](https://help.obsidian.md/callouts)
		- **Short answer:** Yes — Obsidian calls them **callouts**. Open the Command Palette (`Cmd+P` / `Ctrl+P`) and run **`Insert callout`**. That inserts a default `[!note]` callout (or wraps selected text). They are the colored Info / Warning / Danger-style boxes; older docs and plugins sometimes call the same idea **admonitions**.
		- **Syntax:** a blockquote whose first line is `> [!type]`:
			- ~~~markdown
			  > [!warning] Title here
			  > Body text…
			  ~~~
		- **Built-in types** (each has its own color/icon; aliases in parentheses): `note`, `abstract` (`summary`, `tldr`), `info`, `todo`, `tip` (`hint`, `important`), `success` (`check`, `done`), `question` (`help`, `faq`), `warning` (`caution`, `attention`), `failure` (`fail`, `missing`), `danger` (`error`), `bug`, `example`, `quote` (`cite`).
		- **Extras:** add `+` or `-` after the type for foldable callouts; in Live Preview, right-click the callout title to change type; CSS snippets/plugins can define custom types.
		- ### Sources
			- [Callouts — Obsidian Help](https://help.obsidian.md/callouts)
