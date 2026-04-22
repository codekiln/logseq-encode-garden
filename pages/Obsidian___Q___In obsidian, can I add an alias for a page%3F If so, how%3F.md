logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]
see-also:: [[Obsidian/Q/In obsidian, how can I link to a heading in another file?]]

- # In obsidian, can I add an alias for a page? If so, how?
	- ## Answer
		- [[AI/Response]]
			- **Yes.** In Obsidian, a **note** (what you called a “page”) can have one or more **aliases**—alternative titles you can search for, link to, and surface in suggestions.
			- **How to add aliases**
				- Add an `aliases` property in the note’s **properties** block (YAML between `---` lines at the top of the file). Aliases should be a **list** (one per line with `- `, or another valid YAML list form).
				- You can also use **Add file property** from the command palette, **`Cmd/Ctrl+;`**, or the note tab **More actions** menu, then choose or create the `aliases` property.
				- Older vaults may still show deprecated singular `alias`; current docs use **`aliases`** (and the help notes `alias` was deprecated in favor of `aliases`).
			- **What you get**
				- When you type `[[` and start typing an alias, it appears in link suggestions (with a curved-arrow indicator per help). Inserting it typically becomes a wikilink that keeps the **canonical note name** but shows the alias as **display text** (similar to `[[Long Title|Short]]`), so other wikilink tools still resolve to the real file.
				- The **Backlinks** pane can help find **unlinked mentions** of alias text so you can promote them to links.
			- **Not the same as display text** — If you only want different link text in one spot, use Obsidian’s **custom link display text** option (see Internal links in Obsidian Help) instead of adding a vault-wide alias.
			- ### Sources
				- [Obsidian Help — Aliases (source on GitHub)](https://github.com/obsidianmd/obsidian-help/blob/master/en/Linking%20notes%20and%20files/Aliases.md)
				- [Obsidian Help — Properties / default properties (source on GitHub)](https://github.com/obsidianmd/obsidian-help/blob/master/en/Editing%20and%20formatting/Properties.md)
