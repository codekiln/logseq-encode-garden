logseq-entity:: [[Logseq/Entity/Question]]

- # Does [[Obsidian]] have a dedicated way of making [[Slideshows]]? [[Logseq]] has built-in [[reveal.js]] support; is there anything like it in Obsidian, or with plugins?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Slides](https://help.obsidian.md/plugins/slides) in the Obsidian help, plus the community plugin pages linked below:
			- **Short answer:** Yes. Obsidian ships a core plugin named **Slides**, and community plugins add reveal.js and Marp workflows on top of it.
			- **Core Slides plugin (built in):**
				- Run `Start presentation` from the command palette, or right-click a note's tab and choose **Start presentation**.
				- Any note works as a deck. Separate slides with `---` on its own line, surrounded by blank lines.
				- Navigate with the arrow keys or Spacebar; `Escape` ends the presentation.
				- The help page documents nothing beyond this: no themes, transitions, speaker notes, fragments, or export.
			- **Community plugins for reveal.js-style decks:**
				- [Advanced Slides](https://www.obsidianstats.com/plugins/obsidian-advanced-slides) — markdown-based reveal.js presentations inside Obsidian. The closest match to Logseq's reveal.js support.
				- [Slides Extended](https://community.obsidian.md/plugins/slides-extended) — a fork of Advanced Slides that embeds notes into slides, previews edits live, applies themes, and exports to PDF or HTML.
			- **Community plugins for Marp decks** (a different Markdown slide framework, not reveal.js):
				- [Marp Slides](https://community.obsidian.md/plugins/marp-slides) — preview and export to HTML, PDF, PPTX, or images through the Marp CLI.
				- [Marp Extended](https://community.obsidian.md/plugins/marp-extended) — create, preview, present, and export Marp decks.
				- [Marp](https://community.obsidian.md/plugins/marp)
			- **Choosing:** use core Slides for a quick read-through of a note. Use Advanced Slides or Slides Extended when you want reveal.js features like themes and PDF export. Use Marp when you want PPTX output.
