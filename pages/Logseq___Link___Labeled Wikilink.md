tags:: [[Diataxis/Concept]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[Obsidian]], [[Logseq/mise/Task/fix-wikilink-labels]]

- # Labeled Wikilink
	- ## Overview
		- [[Obsidian]] writes a link with display text as `[[Target|Label]]`. [[Logseq]] has no such syntax: it reads `Target|Label` as one page name, so the link points at a page nobody meant and Logseq creates it as an empty page.
	- ## Context
		- Coding agents write this form in Logseq gardens out of Obsidian habit. [[Logseq/mise/Task/fix-wikilink-labels]] rewrites each one to `[[Target]]` before a commit lands.
		- Logseq's own labeled link is `[Label]([[Target]])`. In this garden, links stay plain: `[[Target]]`, with the sentence around it carrying any wording the label would have added.
