logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]
see-also:: [[Obsidian/Q/In obsidian, can I add an alias for a page? If so, how?]]

- # Does [[Obsidian]] allow a list of links to other [[Obsidian]] pages in the [[YAML]] markdown frontmatter?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** Yes. Obsidian supports **Link list** properties in YAML frontmatter — a list where each item is a wikilink `[[Page Name]]` that resolves to another note and appears in that note's backlinks.
			- ### How it works
				- In Obsidian 1.4+, frontmatter is surfaced as **Properties**. Each property has a type; the relevant types for page links are:
					- **Link** — a single wikilink to one note (`type: link` in the Properties view)
					- **Link list** — an array of wikilinks (`type: multitext` / shown as "List" with link items)
				- In raw YAML the list looks like:
					- ~~~yaml
					  ---
					  related:
					    - "[[Note One]]"
					    - "[[Note Two]]"
					  ---
					  ~~~
				- Obsidian resolves the wikilinks inside the list, so each linked note gains a **backlink** from the source note. The Properties pane renders them as clickable links.
				- You can also declare the type explicitly in **Settings → Properties** so Obsidian uses the link-picker UI when editing.
			- ### Caveats
				- The wikilinks must be quoted strings in YAML (bare `[[...]]` is not valid YAML, so Obsidian wraps them in `"` when written through the Properties UI).
				- Plain-text YAML parsers outside Obsidian will see these as strings, not live links.
				- The older `alias` / `aliases` property is a special case built into Obsidian core; custom link-list properties follow the same resolution logic but are user-defined.
			- ### Sources
				- [Obsidian Help — Properties](https://help.obsidian.md/Editing+and+formatting/Properties)
				- [Obsidian Help — Property types](https://help.obsidian.md/Editing+and+formatting/Properties#Property+types)
