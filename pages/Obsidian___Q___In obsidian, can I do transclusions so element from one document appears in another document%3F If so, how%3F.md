logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]
see-also:: [[Obsidian/Q/Is there a VS Code extension that helps obsidian users have an obsidian-compatible view of obsidian markdown files and navigate between wiki links?]]

- # In obsidian, can I do transclusions so element from one document appears in another document? If so, how?
	- ## My Notes
		- Obsidian’s docs call this **embedding**; community discussion often calls the same behavior **transclusion** (live include of source content).
	- ## Answer
		- [[AI/Response]]
			- **Yes.** In Obsidian you **embed** another note (or part of it) by prefixing an internal wikilink with `!`. The embedded region updates when the source changes; you usually **edit in the source note**, not inside the embed preview.
			- **Whole note** — put this on its own line where you want the body to appear:
				- ~~~
				  ![[Source note title]]
				  ~~~
			- **Only the section under one heading** — append `#` plus the heading text (match the heading in the source file):
				- ~~~
				  ![[Source note title#Heading text]]
				  ~~~
			- **A single block** (paragraph, list, blockquote, table, etc.) — link to a **block id** with `#^…`:
				- ~~~
				  ![[Source note title#^block-id]]
				  ~~~
				- Add a block id in the source (e.g. end a paragraph with `^my-id`, or use **Copy block link** from the UI) so `#^my-id` is stable. For structured blocks, Obsidian’s help places the `^id` line per their “link to a block” instructions.
			- **Caveats** — block references are **Obsidian-specific** (not portable CommonMark). Some block types have linking/embed limitations called out in help (e.g. parts of tables/callouts).
			- ### Sources
				- [Embed files — Obsidian Help (Mintlify)](https://www.mintlify.com/obsidianmd/obsidian-help/linking/embed-files)
				- [Internal links — obsidian-help source (GitHub)](https://github.com/obsidianmd/obsidian-help/blob/main/en/Linking%20notes%20and%20files/Internal%20links.md)
