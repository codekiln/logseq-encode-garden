alias:: [[Obsidian/Feature/Checklists]], [[Obsidian/Feature/Checkboxes]], [[Obsidian/Feature/Todos]], [[Obsidian/Feature/Task lists]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[Obsidian/Q/Does Obsidian have the ability to handle kanban-style TODO DOING DONE todos?]], [[App/Obsidian/Markdown]], [[Markdown/Flavor]], [[Logseq]], [[PTKM]]
- # [Task lists — checkboxes & todos (Obsidian)](https://help.obsidian.md/syntax#Task%20lists)
	- ## Overview
		- **Core feature:** GitHub-Flavored Markdown **task lists** in any vault note—each line is a list item with a checkbox in the brackets. Obsidian calls these *task lists* in help; people also say checklists, checkboxes, or todos.
		- **Storage:** Plain markdown on disk (`- [ ]` / `- [x]`). No separate task database in core.
		- **States in core:** Incomplete (` ` inside brackets) and complete (`x`, or other characters—see syntax). No built-in `TODO` / `DOING` / `DONE` keywords like [[Logseq]]; see [[Obsidian/Q/Does Obsidian have the ability to handle kanban-style TODO DOING DONE todos?]] for plugin and migration paths.
	- ## Official documentation
		- Primary: [Basic formatting syntax — Task lists](https://help.obsidian.md/syntax#Task%20lists) (same page as [Editing and formatting / Basic formatting syntax](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax#Task%20lists))
		- List nesting (indent): same guide, [Nesting lists](https://help.obsidian.md/syntax#Nesting%20lists) — `Tab` / `Shift+Tab` on selected list items
		- Customizable command hotkeys: [Hotkeys](https://help.obsidian.md/User+interface/Hotkeys)
		- OS-level editing keys (not rebindable in Obsidian): [Editing shortcuts](https://help.obsidian.md/Editing+and+formatting/Editing+shortcuts)
		- Parser details: [Obsidian Flavored Markdown](https://help.obsidian.md/Editing+and+formatting/Obsidian+Flavored+Markdown)
	- ## Syntax
		- **Minimal task line:** hyphen, space, opening bracket, space, closing bracket, space, description.
		- **Incomplete:** `- [ ] Buy milk`
		- **Complete:** `- [x] Buy milk` (lowercase `x` is conventional; Obsidian treats other characters inside the brackets as “checked” too)
		- **Custom markers (still one checkbox):** e.g. `- [?] Maybe`, `- [-] Cancelled` — any character in the brackets can represent done/custom state in core; plugins may assign meaning (e.g. **Tasks** uses `/` for in progress)
		- **Nesting:** indent subtasks with a tab (or spaces consistent with the parent list). Mix ordered, unordered, and task lists in one outline.
		- **Not core:** leading `TODO` / `DOING` keywords, due dates on the line, vault-wide task queries, or kanban columns—those need community plugins or a different tool surface.
	- ## Where it applies
		- **Any markdown note** in the vault (including daily notes if you use them).
		- **Live Preview and Source mode:** edit the markdown; checkbox UI appears in Live Preview where supported.
		- **Reading view:** click the checkbox to toggle; Obsidian rewrites the bracket character in the file ([help — Task lists](https://help.obsidian.md/syntax#Task%20lists)).
		- **Publish:** task list syntax renders on [Obsidian Publish](https://help.obsidian.md/Obsidian+Publish/Obsidian+Publish) sites as normal HTML checkboxes (interactivity depends on publish settings).
		- **Embeds / transclusions:** task lines in embedded content follow the same markdown rules as the source note.
		- **Outside core:** **Tasks**, **Dataview**, **TODOseq**, [[obsidian-kanban]], etc. add query UIs, extra statuses, or boards on top of this syntax—see [[Obsidian/Q/Does Obsidian have the ability to handle kanban-style TODO DOING DONE todos?]].
	- ## Keyboard shortcuts & commands
		- **Discover or rebind:** `Ctrl+P` / `Cmd+P` (Command palette) shows each command’s current hotkey; **Settings → Hotkeys** lists all bindings ([Hotkeys](https://help.obsidian.md/User+interface/Hotkeys)).
		- **Toggle checkbox status** (core): default **`Ctrl+L`** (Windows/Linux) / **`Cmd+L`** (macOS). Cycles/creates checkbox state on the current line; rebindable. (Older builds used `Ctrl+Enter` / `Cmd+Enter` for this; current default moved link-opening to that chord—see [Obsidian 1.2.10 desktop changelog](https://obsidian.md/changelog/2023-03-21-desktop-v1.2.10/).)
		- **Indent / outdent list items** (including tasks): **`Tab`** / **`Shift+Tab`** on selection ([Nesting lists](https://help.obsidian.md/syntax#Nesting%20lists)).
		- **New line inside a list item without breaking numbering:** **`Shift+Enter`** ([Lists](https://help.obsidian.md/syntax#Lists)).
		- **Toggle bullet ↔ numbered list** (optional): command **Toggle bullet/numbered list** — assign in Hotkeys if you convert plain bullets to tasks often.
		- **Reading view only:** no default “clickless” hotkey beyond toggling via **Toggle checkbox status** or pointer click on the checkbox.
		- **Common plugin override:** **Tasks** recommends replacing **Toggle checkbox status** with **Tasks: Toggle task done** (often mapped to `Ctrl+Enter` / `Cmd+Enter`) for multi-state tasks ([Tasks plugin](https://publish.obsidian.md/tasks/Introduction)).
	- ## Behavior notes
		- **Creation:** type `- [ ]` manually, paste templates, or run **Toggle checkbox status** on a line to introduce checkbox syntax.
		- **Completion:** `x` (or another chosen character) inside `[ ]`; clicking in Reading view updates the file.
		- **Queries:** core has no “all open tasks in vault” view; use search (`task:` / `path:` operators in search, or plugins).
		- **Logseq contrast:** [[Logseq]] uses block-level `TODO` / `DOING` / `DONE` markers and built-in task queries; plain `- [ ]` in Logseq is not the same workflow as Obsidian’s primary task model.
	- ## Examples
		- ~~~
		  - [ ] Draft outline
		  	- [ ] Collect sources
		  	- [x] Skim intro paper
		  - [x] Send recap email
		  ~~~
		- Mixed outline:
		- ~~~
		  1. Phase one
		     - [ ] Subtask A
		     - [x] Subtask B
		  2. Phase two
		     - [ ] Subtask C
		  ~~~
