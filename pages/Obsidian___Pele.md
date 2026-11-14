logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Steph Ango]]

- # [Pele](https://pele.run/)
	- [obsidianmd/pele](https://github.com/obsidianmd/pele) · [[GitHub/Star]]: 4412 (checked 2026-11-09).
	- Library that renders [[Mermaid]] diagrams to SVG, themed with CSS variables (`--pele-bg`, `--pele-fg`, `--pele-line`, and so on). Color changes apply without re-rendering.
	- Written in [[TypeScript]]. MIT license, zero dependencies.
	- Claims about 230 kB gzipped against Mermaid.js's 1.6 MB, and 0.05–0.3 ms renders against 6–82 ms. Supports every diagram type built into Mermaid 12.1.0, and adapts the layout on small screens instead of scaling the diagram down.
	- Built for [[Obsidian]] to render diagrams quickly and match the vault's theme.
	- Usage: `npm install pele`, then `render(mermaidText)` returns `{ svg }` to insert into the page.
