tags:: [[Obsidian]], [[Diataxis/Explanation]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[Obsidian/Feature/Bases]], [[Obsidian/Feature/Task_Lists]], [[Obsidian/Plugin/Dataview]], [[Obsidian/Plugin/obsidian-tasks]], [[QuartzMD/Plugin/bases-page]], [[QuartzMD/Q/Which Obsidian technique for rich todos renders on a QuartzMD site?]]
date-created:: [[2026/09/09]]

- # What a base is
	- ## Overview
		- [[Obsidian]] keeps notes as Markdown files in a folder on disk. A **base** is a saved view that gathers a set of those files and draws them as a table: one row per file, one column per piece of information the file carries.
		- What fills the columns comes from each note's own **properties** — the `key: value` lines in the YAML block at the top of a Markdown file, which Obsidian calls frontmatter and edits in a small form at the top of the page. A note about a piece of work might carry `status: doing`, `priority: high` and `due: 2026-09-16`. A base over those notes shows status and due date as columns, keeps only the ones still open, sorts the soonest to the top, and counts them.
		- So a base answers "show me every note that looks like this, with the fields I care about beside it."
	- ## Why it exists
		- A folder of Markdown files carries no index. To see every open piece of work across a vault, someone opens the notes one by one, or installs something that reads them.
		- That something used to be a community plugin. [[Obsidian/Plugin/Dataview]] brought its own query language in fenced code blocks; [[Obsidian/Plugin/obsidian-tasks]] brought its own fields on the checkbox line and its own query blocks. Each works well, and each is a dependency: it has to be installed, kept current, and trusted, and what it draws exists only while it runs.
		- Bases arrives with Obsidian. [Obsidian 1.9.0](https://obsidian.md/changelog/2025-05-21-desktop-v1.9.0/) shipped it as a core plugin, so a vault that uses it asks nothing of whoever opens it next. The fields it reads are ordinary frontmatter, and the view itself is a few lines of YAML.
	- ## Where a base lives
		- A base is YAML with `filters`, `formulas`, `properties`, `summaries` and `views`. Obsidian gives it a point-and-click editor, and the file underneath stays plain text that reads and edits fine in `nvim`.
		- It sits either in a `.base` file of its own, which Obsidian opens as a page, or inside a fenced code block tagged `base` in an ordinary note, so a dashboard can sit on the page whose work it tracks.
		- [[Obsidian/Feature/Bases]] lists the property names a base can read, the functions a formula can call, the layouts Obsidian can draw, and a worked example of the YAML.
	- ## A row is a file
		- This is the part that changes how a vault gets written. A base can show only what a file carries, so anything a base is meant to gather has to be a file.
		- A task written as `- [ ] Renew the domain` inside a page has nowhere to keep a due date or a status, because a Markdown list item has no properties. Promote that task to a note of its own and it gains frontmatter, and a base sees it.
		- The question a base puts to a vault is therefore which things deserve a page of their own. A checklist inside a page still reads well — [[Obsidian/Feature/Task_Lists]] covers what a plain checkbox line holds. What has to be gathered across pages becomes a page.
	- ## How this compares with Dataview and Tasks
		- The difference that matters is where the information is kept and where the answer is worked out.
		- [[Obsidian/Plugin/Dataview]] keeps fields inline, as `[due:: 2026-09-16]` anywhere in the body of a note, and answers queries from its own index. [[Obsidian/Plugin/obsidian-tasks]] keeps fields on the checkbox line as emoji and dates, and answers `tasks` queries from its own index. Both indexes live inside the plugin, in Obsidian's memory.
		- Bases keeps fields in the frontmatter Obsidian already understands, and describes the view in YAML that says what to gather. Reading a base takes a YAML parser and a walk over the vault's frontmatter, so a program that is not Obsidian can read one and draw the same table.
		- Dataview and Tasks can hold a task on one line inside the page it belongs to, which a base cannot do. Where their fields and a base overlap, [[QuartzMD/Q/Which Obsidian technique for rich todos renders on a QuartzMD site?]] compares them field by field.
	- ## Why a base reaches a published site
		- A [[QuartzMD]] site is built once, by a program that reads the Markdown on disk and writes HTML. Obsidian is not running during that build, so no community plugin is running either, and whatever a plugin works out live in the app contributes nothing to the page a reader loads ([Quartz — Obsidian compatibility](https://quartz.jzhao.xyz/features/Obsidian-compatibility)).
		- What a plugin *wrote into the file* does reach the site, because it is text. Dataview's `[due:: 2026-09-16]` publishes as those visible characters, and a fenced `dataview` block publishes as a code block showing the query.
		- A base is stored text through and through: the properties sit in each note's frontmatter, and the view is YAML. A build tool can read both and draw the table itself. [[QuartzMD/Plugin/bases-page]] does that, rendering table, list, cards, gallery and board layouts into HTML while the site builds, and swapping a fenced `base` block for the rendered view in place.
		- A view built this way holds whatever the Markdown said at the moment of the build, and stays that way in the reader's browser.
	- ## Misconceptions
		- **"Bases is a plugin I have to install."** It arrives with Obsidian, in the core plugin list.
		- **"A base stores my tasks."** Each note stores its own properties. A base is a saved question about them, so deleting a base leaves every note as it was.
		- **"A base replaces Dataview and Tasks."** It covers the same ground for anything modeled as a page of its own. A field on a line inside a page is still what those plugins are for.
		- **"A kanban authored in Obsidian publishes as a board."** Obsidian writes that layout as `type: kanban`, and bases-page 0.2.0 registers the layout under the id `board`, so the site shows the words `Unknown view type: kanban` until a `kanban` renderer is registered through the plugin's `customViews` option — see [[QuartzMD/Plugin/bases-page]].
	- ## Sources
		- [Bases — Obsidian Help](https://obsidian.md/help/bases)
		- [Bases syntax](https://obsidian.md/help/bases/syntax)
		- [Bases views](https://obsidian.md/help/bases/views)
		- [Obsidian 1.9.0 desktop changelog](https://obsidian.md/changelog/2025-05-21-desktop-v1.9.0/)
		- [quartz-community/bases-page](https://github.com/quartz-community/bases-page)
		- [Quartz — Obsidian compatibility](https://quartz.jzhao.xyz/features/Obsidian-compatibility)
