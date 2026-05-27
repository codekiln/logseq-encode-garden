logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]

- # In [[Obsidian]], how can I change the default date format to YYYY-MM-DD?
	- ## Answer
		- [[AI/Response]]
			- **Short answer:** Obsidian does not offer one vault-wide “default date format” for every surface. Several core features already default to `YYYY-MM-DD`; where you can set a default, use **Settings → Core plugins → Daily notes** or **Templates**, or an explicit `{{date:YYYY-MM-DD}}` in templates. **Date properties** are always stored as `YYYY-MM-DD` in YAML; the **date picker display** follows your **OS regional format** unless you change system preferences.
			- **Already `YYYY-MM-DD` by default**
				- **Daily notes** — New daily notes are named with today’s date in `YYYY-MM-DD` unless you change **Date format** under the Daily notes plugin.
				- **Templates** — `{{date}}` uses `YYYY-MM-DD` unless you override the plugin’s **Date format** or use `{{date:…}}` with a [Moment.js format string](https://momentjs.com/docs/#/displaying/format/).
				- **Properties (YAML)** — `date` and `date & time` values are written in ISO form (`2020-08-21`, `2020-08-21T10:30:00`) regardless of how the picker looks in Live Preview.
			- **Set or restore `YYYY-MM-DD` in plugin settings**
				- **Daily notes:** **Settings → Core plugins → Daily notes → Date format** → `YYYY-MM-DD` (or another [Moment.js token string](https://momentjs.com/docs/#/displaying/format/) if you also want folder segments, e.g. `YYYY/MM/YYYY-MM-DD`).
				- **Templates:** **Settings → Core plugins → Templates → Date format** → `YYYY-MM-DD`. Commands **Insert current date** and template expansion use this default; per-call override: `{{date:YYYY-MM-DD}}`.
			- **Properties picker display (not storage)**
				- The calendar control for **Date** / **Date & time** properties follows your operating system’s short date format. On **macOS:** **System Settings → General → Language & Region → Dates** (adjust short date to year-month-day order if you want the picker to match ISO visually). Restart Obsidian after changing OS formats.
			- **Community plugins**
				- Plugins such as **Dataview**, **Tasks**, or **Projects** may have their own display or parse rules; check each plugin’s settings (forum guidance often points to Luxon/Moment format fields for Dataview). Obsidian core does not centralize those.
			- ### Sources
				- [Obsidian Help — Daily notes](https://github.com/obsidianmd/obsidian-help/blob/master/en/Plugins/Daily%20notes.md)
				- [Obsidian Help — Templates](https://github.com/obsidianmd/obsidian-help/blob/master/en/Plugins/Templates.md)
				- [Obsidian Help — Properties (Date)](https://github.com/obsidianmd/obsidian-help/blob/master/en/Editing%20and%20formatting/Properties.md)
				- [Obsidian Forum — Changing date format in my Obsidian Vault](https://forum.obsidian.md/t/changing-date-format-in-my-obsidian-vault/69941)