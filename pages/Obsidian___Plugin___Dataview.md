logseq-entity:: [[Logseq/Entity/Software/Plugin]]
see-also:: [[App/Obsidian/Markdown]], [[Obsidian/Explanation/What a Base Is]]
date-created:: [[2021/05/03]]

- # [obsidian-dataview](https://github.com/blacksmithgu/obsidian-dataview)
	- [[Obsidian]] community plugin that treats the vault as a database and queries it from fenced code blocks. Metadata comes from YAML frontmatter and from inline fields written in the body of a note.
	- **Stars:** 9,327 · **License:** MIT · last pushed November 2025, so it is quiet compared with [[Obsidian/Plugin/obsidian-tasks]].
	- Docs: [Dataview documentation](https://blacksmithgu.github.io/obsidian-dataview/)
	- ## Inline fields
		- Anywhere in a note's body, `key:: value` names a field on the surrounding block. Wrapped in square brackets or parentheses, `[key:: value]` puts the field mid-sentence and hides the key from Obsidian's rendered view.
		- On a checkbox line this is how a todo picks up fields without emoji: `- [ ] Renew the domain [due:: 2026-09-30] [priority:: high]`.
		- The double colon is the whole mechanism, which is why the syntax reads plainly in `nvim` and survives any Markdown tool that does not know about it — a reader sees the brackets and the words.
	- ## Queries
		- A fenced `dataview` block holds a query in Dataview Query Language: `TABLE`, `LIST`, `TASK` and `CALENDAR` over `FROM` a folder or tag, with `WHERE`, `SORT` and `GROUP BY`.
		- `TASK` queries are the ones aimed at todos: they collect checkbox lines across the vault and render them as an interactive list whose checkboxes write back to the source file.
		- `dataviewjs` blocks run JavaScript against the same index.
		- ~~~
		  ```dataview
		  TASK
		  FROM "Journals"
		  WHERE !completed AND due <= date(today) + dur(7 days)
		  SORT priority DESC, due ASC
		  ```
		  ~~~
	- ## Where it stops
		- Every query is evaluated by the plugin's own engine inside Obsidian. A static site generator reading the same files sees a code block and nothing else — [[QuartzMD/Q/Which Obsidian technique for rich todos renders on a QuartzMD site?]] works through what that costs and what recovers it, and [[Obsidian/Explanation/What a Base Is]] explains why [[Obsidian/Feature/Bases]] keeps its fields somewhere a site build can reach them.
		- [[Obsidian/Plugin/obsidian-tasks]] reads and writes Dataview's bracketed fields as an alternative to its own emoji, so the two conventions can share one vault.
	- ## Sources
		- [Dataview — Adding metadata](https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/)
		- [Dataview — Query types](https://blacksmithgu.github.io/obsidian-dataview/queries/query-types/)
