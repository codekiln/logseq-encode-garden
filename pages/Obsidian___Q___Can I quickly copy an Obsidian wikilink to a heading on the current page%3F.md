logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]
see-also:: [[Obsidian/Q/What Obsidian keyboard shortcuts are most useful for pointing to pages and headings when working with external agentic coding tools like Claude Code?]], [[Obsidian/Q/In obsidian, how can I link to a heading in another file?]]

- # Can I quickly copy an [[Obsidian]] wikilink to a heading on the current page? [[card]]
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** Yes — in **Reading view** it takes one click with no plugins; in **Editing/Live Preview** you need a community plugin.
			- ### Reading view (no plugin needed)
				- Hover over any heading in the current note. A **chain-link icon** (§) appears to its right.
				- Click it → Obsidian copies `[[NoteName#Heading text]]` to the clipboard.
			- ### Editing / Live Preview (community plugin required)
				- Obsidian has **no built-in command** for copying a heading link from editing mode.
				- [[Obsidian/Plugin/Easy Copy]] (Community Plugins → `easy-copy`) — place cursor on the heading line, run **Easy Copy: Contextual Copy** from the command palette (or assign a hotkey). Writes `[[Note#Heading]]` to clipboard. Works on blocks and paragraphs too.
				- [[Obsidian/Plugin/Copy Link]] (`greetclammy/copy-link`) — similar commands covering files, headings, and blocks including anchor forms.
			- ### Sources
				- [Obsidian Help — Internal links](https://help.obsidian.md/Linking+notes+and+files/Internal+links)
				- [Easy Copy plugin — Obsidian Community Plugins](https://obsidian.md/plugins?id=easy-copy)
				- [Copy Link plugin — GitHub](https://github.com/greetclammy/copy-link)
