logseq-entity:: [[Logseq/Entity/Question]]
tags:: [[Question]]
see-also:: [[Obsidian/Q/Is there a keyboard shortcut in Obsidian for quickly finding keyboard shortcuts in Obsidian?]], [[Obsidian/Q/In obsidian, how can I change the default date format to YYYY-MM-DD?]]

- # What's the fastest way to create a new page according to a template in [[Obsidian]]? Is there a keyboard shortcut?
	- ## Answer
		- [[AI/Response]]
			- **Short answer:** The core **Templates** plugin does **not** create a brand-new note from a template—it only **inserts** template text into the **active** note. Obsidian ships **no default hotkey** for template commands; you assign one under **Settings → Hotkeys**. For **fastest “new file + template content”**, use a community workflow (**QuickAdd** Template choice or **Templater** folder/trigger templates) and bind **that** command to a shortcut.
			- **Core Templates (insert only)**
				- Enable **Settings → Core plugins → Templates**, set **Template folder location**, then run **`Templates: Insert template`** (ribbon **Insert template**, or Command palette). Optional related commands: **`Templates: Insert current date`**, **`Templates: Insert current time`**.
				- **Keyboard shortcut:** none by default. Search **`Templates: Insert template`** in **Settings → Hotkeys**, click **+**, press your combo (many people use something like **Ctrl+Alt+T** / **Cmd+Option+T**—pick one that does not conflict).
				- **Two-step “new page” with core only:** **`File: Create new note`** (**Ctrl+N** / **Cmd+N**), then your **`Templates: Insert template`** hotkey or palette command—works but is slower than a single “create from template” command.
			- **Core plugins that create a new note with a template (specific flows)**
				- **Daily notes** — set **Template file location** in Daily notes settings; new daily notes get that template automatically (often bound via **Open today's daily note** hotkey, not a generic “any template” key).
				- **Unique note creator** — can use the same `{{date}}` / `{{time}}` variables when creating zettel-style notes; configure template in that plugin’s settings.
			- **Fastest general “new note from this template” (community)**
				- **QuickAdd** — add a **Template** choice (template path + target folder), run **`QuickAdd: Run QuickAdd`** once to verify, then in **Hotkeys** bind the choice’s command (e.g. **`QuickAdd: <your choice name>`**) to one key. One shortcut → new file in the right folder with template applied.
				- **Templater** — for automation beyond plain insertion: **Folder templates** (auto-apply when creating in a folder), **Trigger Templater on new file creation**, and/or add templates to **Templater’s hotkey list** so **`Templater: <template>`** is bindable.
			- **Net:** **Yes, you can use a keyboard shortcut**, but you (or a plugin) must **assign** it—except where Daily notes / Unique note creator already apply a configured template as part of their own “create note” commands.
			- ### Sources
				- [Obsidian Help — Templates (source on GitHub)](https://github.com/obsidianmd/obsidian-help/blob/master/en/Plugins/Templates.md)
				- [Obsidian Help — Hotkeys (source on GitHub)](https://github.com/obsidianmd/obsidian-help/blob/master/en/User%20interface/Hotkeys.md)
				- [QuickAdd — Template choice](https://quickadd.obsidian.guide/docs/Choices/TemplateChoice/)
				- [QuickAdd — Getting started](https://quickadd.obsidian.guide/docs/)
