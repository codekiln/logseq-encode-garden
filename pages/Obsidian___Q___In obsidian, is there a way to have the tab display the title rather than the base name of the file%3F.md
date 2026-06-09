logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]

- # In [[Obsidian]], is there a way to have the tab display the title rather than the base name of the file?
	- ## [[My Notes]]
		- Experimentally confirmed: setting `title: Potato` in `Tomato.md` does **not** change the tab — the tab still shows `Tomato`. The `title` property affects the Properties panel only; it does not override the tab label or inline document title in core Obsidian.
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** No built-in way. Core [[Obsidian]] always shows the **base filename** (no extension) in the tab regardless of any frontmatter property. To show a different label in the tab you must either rename the file or install a community plugin.
			- **What `title:` frontmatter actually does:** Obsidian 1.4+ recognises `title` as a first-class property and surfaces it in the Properties panel, but it does **not** override the tab label or the inline document title. Experimentally confirmed: a file named `Tomato.md` with `title: Potato` still shows `Tomato` in the tab.
			- **Options to show a custom title in the tab:**
				- 1. **Rename the file** — simplest; the tab always reflects the filename.
				- 2. **[[Obsidian/Plugin/Front Matter Title]]** — community plugin that reads a chosen frontmatter key (e.g. `title`) and uses it as the display name in tabs, the file explorer, and graph view.
				- 3. **[Filename Heading Sync](https://github.com/dvcrn/obsidian-filename-heading-sync) plugin** — keeps the H1 heading and filename in sync; the tab still shows the filename but the heading and filename always match.
			- ### Sources
				- [[Obsidian/Plugin/Front Matter Title]]
				- [Filename Heading Sync plugin — GitHub](https://github.com/dvcrn/obsidian-filename-heading-sync)
