logseq-entity:: [[Logseq/Entity/Software/Plugin]]
date-created:: [[2021/03/19]]

- # [obsidian-tasks](https://github.com/obsidian-tasks-group/obsidian-tasks)
	- Full-featured task management for [[Obsidian]]: track tasks vault-wide, query and filter with `tasks` code blocks, and configure custom checkbox statuses.
	- **Stars:** 4,002 · **License:** MIT
	- frequently updated
	- ## Key features
		- Built-in task [status types](https://publish.obsidian.md/tasks/Getting+Started/Statuses/Status+Types): Todo (` `), In Progress (`/`), Done (`x`), Cancelled (`-`)
			- also includes [Custom Statuses](https://publish.obsidian.md/tasks/Getting+Started/Statuses/Custom+Statuses)
		- built-in task [priorities](https://publish.obsidian.md/tasks/Getting+Started/Priority)
		- `tasks` fenced code blocks for vault-wide queries with filtering, grouping, and sorting
			- [[My Note]] *probably doesn't render well in Obsidian [[QuartzMD]] *
		- integrates with [[Person/Matthew Meyers/GitHub/obsidian-kanban]]
		- Custom status symbols and cycling configured under **Settings → Tasks → Task statuses**
		- Recurrence rules, due/scheduled/start dates, and priority markers
	- ## Fields on the line
		- The plugin's own format puts each field on the task line as an emoji followed by a value, in [Tasks Emoji Format](https://publish.obsidian.md/tasks/Reference/Task+Formats/Tasks+Emoji+Format):
			- due `📅`, scheduled `⏳`, start `🛫`, created `➕`, done `✅`, cancelled `❌`
			- priority `🔺` highest, `⏫` high, `🔼` medium, `🔽` low, `⏬` lowest; normal priority carries no emoji
			- recurrence `🔁`, on-completion `🏁`, task id `🆔`, blocked by `⛔`
			- ~~~
			  - [ ] Complete project report 📅 2026-09-16 ⏫ 🆔 abc123 ⛔ def456
			  ~~~
		- The same fields can be written as [[Obsidian/Plugin/Dataview]] inline fields instead, in [Dataview Format](https://publish.obsidian.md/tasks/Reference/Task+Formats/Dataview+Format): `[due:: 2026-09-16]`, `[scheduled:: 2026-09-14]`, `[start:: 2026-09-15]`, `[priority:: high]`, `[repeat:: every day when done]`. Tasks reads both bracket and parenthesis forms and writes square brackets.
			- ~~~
			  - [ ] Complete project report [due:: 2026-09-16] [priority:: high]
			  ~~~
	- ## On a [[QuartzMD]] site
		- Fields on the line are ordinary characters, so both formats reach the site intact: the emoji format shows the emoji and the date, and the Dataview format shows the bracketed key and value. Neither becomes a badge or a chip without a stylesheet or a transformer written for it.
		- A fenced `tasks` query block is not executed. Quartz renders it as a code block showing the query text.
		- [[QuartzMD/Q/Which Obsidian technique for rich todos renders on a QuartzMD site?]] compares this against [[Obsidian/Feature/Bases]], which Quartz does render.
