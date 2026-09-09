alias:: [[Obsidian/Bases]], [[Obsidian/Plugin/Bases]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[Obsidian/Explanation/What a Base Is]], [[Obsidian/Feature/Task_Lists]]
date-created:: [[2025/05/21]]

- # [Bases](https://obsidian.md/help/bases)
	- Core [[Obsidian]] plugin that turns a set of notes into a database view. Each row is a file; each column is a frontmatter property, a built-in file property, or a formula. [Obsidian 1.9.0](https://obsidian.md/changelog/2025-05-21-desktop-v1.9.0/) shipped it as "a new core plugin that lets you turn any set of notes into a powerful database."
	- [[Obsidian/Explanation/What a Base Is]] explains a base from the beginning — what it gathers, why a row has to be a file, and how it compares with Dataview and Tasks.
	- Being core matters for a vault that has to stay readable elsewhere: there is no community plugin to install, keep updated, or lose when the vault is opened by something other than Obsidian.
	- ## Where a base lives
		- A `.base` file, which Obsidian opens in its own view editor.
		- A fenced code block tagged `base` inside an ordinary note, so the view sits on the page it belongs to ([Bases syntax](https://obsidian.md/help/bases/syntax)).
	- ## Views
		- **Table** — files as rows, properties as columns. Obsidian 1.9.
		- **Cards** — a grid of cards, with an optional image property. Obsidian 1.9.
		- **List** — bulleted or numbered. Obsidian 1.10.
		- **Map** — pins on a map, needs the Maps plugin. Obsidian 1.10.
		- **Kanban** — cards in columns, grouped by a property. Obsidian 1.14 ([Bases views](https://obsidian.md/help/bases/views)).
	- ## Syntax
		- A base is YAML with `filters`, `formulas`, `properties`, `summaries`, and `views`. Filters compose with `and` / `or` / `not`; a view names its own `type`, `groupBy`, `order`, `limit`, and `summaries`.
		- ~~~
		  filters:
		    and:
		      - file.hasTag("todo")
		      - note.status != "done"
		  formulas:
		    days_left: "(note.due - today()).days"
		  properties:
		    note.priority:
		      displayName: "Priority"
		  views:
		    - type: kanban
		      name: "By status"
		      groupBy:
		        property: note.status
		      order:
		        - file.name
		        - note.priority
		        - note.due
		        - formula.days_left
		  ~~~
		- Property access reads `note.<property>` for frontmatter, `file.name` / `file.folder` / `file.tags` / `file.created` / `file.modified` for the file itself, and `formula.<name>` for a computed column. `if()`, `contains()`, `date()`, `duration()`, `now()`, `today()`, `min()`, `max()` and `link()` are available to formulas.
	- ## What this gives a todo
		- Priority, due date, status and tags become typed frontmatter properties, so a base can filter on them, group a kanban by status, sort by due date, and compute how many days remain.
		- Because a row is a file, a todo modeled this way is a page of its own. A `- [ ]` line inside a page carries no properties and no base sees it — see [[Obsidian/Feature/Task_Lists]] for what a plain checkbox line does hold, and [[Obsidian/Plugin/obsidian-tasks]] for the plugin that puts fields on the line instead.
	- ## Sources
		- [Bases — Obsidian Help](https://obsidian.md/help/bases)
		- [Bases views](https://obsidian.md/help/bases/views)
		- [Bases syntax](https://obsidian.md/help/bases/syntax)
		- [Obsidian 1.9.0 desktop changelog](https://obsidian.md/changelog/2025-05-21-desktop-v1.9.0/)
