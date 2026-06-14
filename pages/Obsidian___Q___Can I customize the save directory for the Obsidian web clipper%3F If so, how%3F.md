logseq-entity:: [[Logseq/Entity/Question]]
tags:: [[Question]]

- # Can I customize the save directory for the Obsidian web clipper? If so, how?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** Yes — the save folder is set per **template**. Edit the default template's **Note location** field to any vault-relative path, and new clips will land there instead of `Clippings`.
			- **How to change it:**
				- 1. Open the Web Clipper extension and click the **template name** (or the pencil/gear icon) to enter template settings.
				- 2. Find the **Note location** field (sometimes labelled "Path" or "Folder").
				- 3. Replace `Clippings` with any vault-relative folder path, e.g. `Inbox/Web` or `Resources/Articles`.
				- 4. Save the template. All subsequent clips using that template will save to the new folder.
			- **Multiple save locations:** Create multiple templates, each with its own **Note location**. Use the template picker in the clipper popup to choose where a specific clip should land. Auto-apply rules (URL pattern matching) can select the right template automatically.
			- **Dynamic paths with variables:** The Note location field accepts [Web Clipper variables](https://help.obsidian.md/web-clipper/variables), so paths like `Clippings/{{date:YYYY-MM}}` are valid and will create dated subfolders.
			- **Sources:**
				- [Clip web pages — Obsidian Help](https://obsidian.md/help/web-clipper/capture)
				- [Templates — Obsidian Help](https://obsidian.md/help/web-clipper/templates)
				- [Variables — Obsidian Help](https://help.obsidian.md/web-clipper/variables)
				- [Forum: Obsidian Web Clipper set default folder?](https://forum.obsidian.md/t/obsidian-web-clipper-set-default-folder/96186)
