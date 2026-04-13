logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]
see-also:: [[Obsidian/Q/In obsidian, can I do transclusions so element from one document appears in another document? If so, how?]]

- # In [[Obsidian]], how can I link to a heading in another file?
	- ## Answer
		- [[AI/Response]]
			- In the default **wikilink** style, append `#` and the **heading text** after the note name: `[[Some note#Exact heading text]]`. That opens the other file and jumps to that heading (anchor link). Official examples use forms like `[[About Obsidian#Links are first-class citizens]]`.
			- **Same file:** type `[[#` and choose a heading in the current note, e.g. `[[#Preview a linked file]]`.
			- **Subheadings under a path:** you can chain multiple `#` segments so each segment targets the next heading level under the previous one (documented for deep outlines).
			- **Different display text:** `[[Some note#Heading|label you want shown]]`.
			- **Find headings across the vault:** use `[[##` (optionally followed by text) to search headings globally, not only in the current file.
			- If **wikilinks** are disabled, Obsidian still supports **Markdown-style** internal links; the destination must be **URL-encoded** (including spaces and the `#` fragment) per the internal-links docs.
			- ### Sources
				- [Obsidian Help — Internal links (source on GitHub)](https://github.com/obsidianmd/obsidian-help/blob/master/en/Linking%20notes%20and%20files/Internal%20links.md)
				- [Readable mirror — “Link to a heading in a note”](https://retypeapp.github.io/obsidian/links/#link-to-a-heading-in-a-note)
