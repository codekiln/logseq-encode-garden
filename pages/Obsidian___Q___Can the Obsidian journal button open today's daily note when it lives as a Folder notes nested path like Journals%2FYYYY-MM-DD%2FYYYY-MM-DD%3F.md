logseq-entity:: [[Logseq/Entity/Question]]
tags:: [[Question]]

- # Can the [[Obsidian]] journal button open today's daily note when it lives as a [Folder notes](https://community.obsidian.md/plugins/folder-notes) nested path like `Journals/YYYY-MM-DD/YYYY-MM-DD`?
	- ## [[AI Answer]]
		- **Short answer:** Yes. The ribbon **Open today's daily note** button (and the matching command/hotkey) follows **Daily notes** core settings. Put the nested folder in **Date format**, not in Folder notes itself: **New file location** `Journals` + **Date format** `YYYY-MM-DD/YYYY-MM-DD` creates `Journals/2026-09-09/2026-09-09.md`. With Folder notes in the usual **inside-folder** mode (`FolderName/FolderName.md`), that file is already a valid folder note for the date folder.
		- ### Configure Daily notes (this drives the journal button)
			- Enable the **Daily notes** core plugin.
			- **Settings → Daily notes → New file location** → `Journals` (or your journals root).
			- **Date format** → `YYYY-MM-DD/YYYY-MM-DD` (Moment.js; `/` creates subfolders). Obsidian creates missing folders when opening/creating today's note.
			- Resulting path shape: `Journals/2026-09-09/2026-09-09.md` — same pattern as year/month nesting documented in [Obsidian Help — Daily notes](https://help.obsidian.md/plugins/daily-notes) (e.g. `YYYY/MMMM/YYYY-MMM-DD`).
		- ### Role of Folder notes
			- Folder notes does **not** need a special Daily notes integration for the journal button to hit that path. Daily notes creates/opens the file; Folder notes only attaches Notion-style folder → note behavior once the note matches your storage type (inside-folder same-name is the common match for this layout).
			- There is an open feature request to have Folder notes *itself* create date subfolders + matching folder notes from Daily notes ([issue #189](https://github.com/LostPaul/obsidian-folder-notes/issues/189)); that is unnecessary for this layout because the core **Date format** path already produces the nested folder note file.
		- ### Caveats
			- **Open previous / Open next daily note** has historically broken or been disabled when **Date format** includes folder segments; **Open today's daily note** (the journal button) still works. If you rely on prev/next, test those commands or use a community alternative (e.g. [Daily Named Folder](https://www.obsidianstats.com/plugins/obsidian-daily-named-folder), which documents the same `YYYYMMDD/YYYYMMDD` trick via core Daily notes).
			- Keep Folder notes storage type consistent with the path you generate (inside-folder same name). Outside-folder or index-file modes will not treat `…/2026-09-09/2026-09-09.md` as the folder note unless you reconfigure accordingly.
		- ### Sources
			- [Obsidian Help — Daily notes](https://help.obsidian.md/plugins/daily-notes) (automatic subfolders via Date format)
			- [Folder notes — community plugin](https://community.obsidian.md/plugins/folder-notes)
			- [Folder notes docs](https://lostpaul.github.io/obsidian-folder-notes/)
			- [Feature request: Folder notes × Daily notes integration](https://github.com/LostPaul/obsidian-folder-notes/issues/189)
			- [Forum: nest Daily notes via Date format](https://forum.obsidian.md/t/daily-notes-allow-formatting-file-location-subfolders-based-on-year-month/19711)
