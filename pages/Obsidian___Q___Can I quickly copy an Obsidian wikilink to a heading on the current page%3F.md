logseq-entity:: [[Logseq/Entity/Question]]
tags:: [[Question]]
see-also:: [[Obsidian/Q/What Obsidian keyboard shortcuts are most useful for pointing to pages and headings when working with external agentic coding tools like Claude Code?]], [[Obsidian/Q/In obsidian, how can I link to a heading in another file?]]

- # Can I quickly copy an [[Obsidian]] wikilink to a heading on the current page? [[card]]
  card-last-interval:: 4.28
  card-repeats:: 2
  card-ease-factor:: 2.7
  card-next-schedule:: 2026-06-28T13:25:36.380Z
  card-last-reviewed:: 2026-06-24T07:25:36.381Z
  card-last-score:: 5
	- ## [[My Answer]]
		- Obsidian has **no native command** to copy a heading wikilink — a community plugin is required in any view mode.
		- Went with [[Obsidian/Plugin/Easy Copy]]. Assigned `⌥⇧C` — the README-suggested `⌘⌥C` could not be registered in the [[Obsidian]] hotkeys UI.
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** Obsidian has no native "copy link to heading" command. A community plugin is required.
			- ### Community plugins that fill the gap
				- [[Obsidian/Plugin/Easy Copy]] (Community Plugins → `easy-copy`) — place cursor on the heading line, run **Easy Copy: Contextual Copy** from the command palette (or assign a hotkey). Writes `[[Note#Heading]]` to clipboard. Works on blocks and paragraphs too.
				- [[Obsidian/Plugin/Copy Link]] (`churnish/copy-link`, install via [[BRAT]]) — commands covering files, headings, and blocks in wikilink, embed, footnote, anchor, and `obsidian://` URL forms.
			- ### Sources
				- [Easy Copy plugin — Obsidian Community Plugins](https://obsidian.md/plugins?id=easy-copy)
				- [Copy Link plugin — GitHub](https://github.com/churnish/copy-link)
				- [Forum: Add "Copy Wikilink" command](https://forum.obsidian.md/t/add-copy-wikilink-command/56121)