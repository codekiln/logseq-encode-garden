logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Google/Drive/Q/Does Google Drive render relative Markdown links and image embeds?]], [[Foam/Q/How can I rename a Foam page so that all wikilinks to it are renamed too?]]

- # Will [[Logseq]] render relative markdown links? What about if a page is renamed, will it refactor relative markdown links to that page?
	- ## [[AI Answer]]
		- **Short answer:** No for page-to-page relative markdown like `[label](./Other.md)`. Logseq does not treat filesystem-relative `.md` paths as graph page links. Rename refactoring also does not update those paths — only tracked page refs (`[[Page]]`, and related `#tags` / properties Logseq indexes) get rewritten when you rename a page.
		- ### Rendering
			- Official page linking is wiki-style: `[[page name]]`, or labeled `[display text]([[page name]])`. External URLs use ordinary `[label](https://…)` markdown. [[Answer/Official]] from [Logseq docs — Markdown](https://github.com/logseq/docs/blob/master/pages/Markdown.md).
			- Relative links to **assets** do render (e.g. `![img](../assets/foo.png)`). That is file/media linking, not page linking.
			- Relative links to **other pages** as files — `[label](Other.md)`, `[label](./pages/Other.md)` — are not resolved to the existing page. A collaborator stated there is no “local markdown” page model: pages are flat by basename, and relative paths are incompatible with that design. Clicking such a link can open/create the wrong page (often from the link label), rather than navigating to the target file. [[Answer/Official]] from [Discussion #8003](https://github.com/logseq/logseq/discussions/8003) (incl. follow-up that relative local links were “not on the radar” as of 2023).
		- ### Rename / refactor
			- Renaming a page in Logseq rewrites **page references** elsewhere in the graph (`[[Old Name]]` → `[[New Name]]`, and most `#tag` / property refs Logseq tracks). That refactor walks blocks that reference the page in the DB — not arbitrary markdown path strings.
			- A relative `[label](./Old.md)` (or similar) is not a page reference, so rename will **not** rewrite it. Even labeled markdown forms that target a page title without `[[…]]` are weaker than wikilinks for rename/display behavior; prefer `[[Page]]` or `[label]([[Page]])` for links you want to survive renames.
		- ### Practical takeaway
			- Use `[[wikilinks]]` (or `[label]([[Page]])`) for inter-page links in Logseq. Use relative markdown only for assets/media. Do not rely on Obsidian/GitHub-style `[text](./sibling.md)` paths for graph navigation or rename safety.
