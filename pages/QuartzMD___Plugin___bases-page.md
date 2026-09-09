logseq-entity:: [[Logseq/Entity/Software/Plugin]]
see-also:: [[Obsidian/Feature/Bases]], [[Obsidian/Explanation/What a Base Is]]
date-created:: [[2026/07/24]]

- # [@quartz-community/bases-page](https://github.com/quartz-community/bases-page)
	- [[QuartzMD]] v5 plugin that renders [[Obsidian/Feature/Bases]] as HTML at build time, so a database view authored in Obsidian appears on the published site.
	- **Stars:** 4 · **License:** MIT · version 0.2.0
	- Why a build tool outside Obsidian can render a base at all: [[Obsidian/Explanation/What a Base Is]].
	- Installed with `npx quartz plugin add github:quartz-community/bases-page` and switched on in `quartz.config.yaml`.
	- ## What it reads
		- A `.base` file becomes a page of its own.
		- A fenced code block tagged `base` inside a note is replaced in place by the rendered view, so a dashboard can sit on the page whose work it tracks.
	- ## Views it knows
		- `table`, `list`, `cards`, `gallery`, and `board` — a column layout that groups entries by `groupBy.property` or `boardProperty`.
		- Obsidian's own kanban layout writes `type: kanban`, and version 0.2.0 registers that layout under the id `board`. A view Obsidian saved as kanban therefore renders on the site as the words `Unknown view type: kanban`. A site can close the gap by registering `kanban` through the plugin's `customViews` option in `quartz.ts`, which takes a renderer and returns JSX.
	- ## What survives the trip
		- Recursive `and` / `or` / `not` filter trees, formulas through the plugin's own expression engine, column summaries (Count, Average, Min, Max, Sum, Median, Checked, Unchecked, Empty, Filled, Unique among them), property display names, sorting, grouping, and wikilink resolution matching the site's link strategy.
		- Multiple views in one base become switchable tabs.
	- ## What it cannot do
		- Views are server-rendered once, when the site is built. They hold whatever the Markdown on disk said at that moment, and nothing about them updates in the reader's browser.
		- Pages carrying `unlisted: true` are dropped from every view, including from formula lookups through `.asFile()`, so an unlisted page cannot be read out of a base on a visible page.
	- ## Sources
		- [quartz-community/bases-page README](https://github.com/quartz-community/bases-page/blob/main/README.md)
		- [Quartz plugins](https://quartz.jzhao.xyz/plugins)
