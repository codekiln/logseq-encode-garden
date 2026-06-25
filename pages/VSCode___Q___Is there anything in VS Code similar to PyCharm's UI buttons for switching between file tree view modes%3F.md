logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[VSCode/Q/How do I increase the readability of file explorer in the sidebar]]

- # Is there anything in [[VSCode]] similar to [[PyCharm]]'s UI buttons for switching between file tree view modes?
	- ## [[AI Answer]]
		- **Short answer:** No built-in equivalent exists. VS Code's Explorer is a single flat file tree with no named view modes. The closest built-ins are collapsible Explorer sections and the Activity Bar's distinct view containers; third-party extensions fill the gap.
		- **PyCharm context:** PyCharm's Project panel has a dropdown that switches between named modes — *Project*, *Packages*, *Project Files*, *Open Files*, *Production*, *Tests*, *Scratches & Consoles* — each reorganising the tree differently without leaving the panel.
		- **VS Code built-ins:**
			- **Activity Bar icons** — each icon opens a completely different panel (Explorer file tree, Search, Source Control, Run & Debug, Extensions). These are separate tools, not alternative views of the same file tree.
			- **Explorer sections** — the Explorer panel has collapsible sub-sections: *Open Editors*, the workspace file tree, *Outline*, and *Timeline*. Sections can be hidden or reordered via right-click, but there is no mode switcher.
			- **Multi-root workspaces** — adding multiple folders to a workspace shows each root as a separate collapsible tree. Useful but not a "mode."
		- **Extension options** (closest to PyCharm-style view switching):
			- [Project Manager](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager) — adds a dedicated sidebar view for switching between saved projects; does not remode the file tree itself.
			- [Explorer Exclude](https://marketplace.visualstudio.com/items?itemName=PeterSchmalfeldt.explorer-exclude) — toggle visibility of file-type groups via toolbar buttons in the Explorer; conceptually closest to a mode switcher.
			- Custom tree-view extensions (e.g. file grouping by type, by git status) can approximate specific PyCharm modes.
		- **Bottom line:** VS Code deliberately keeps the Explorer minimal; view filtering is done through `files.exclude` settings or extensions rather than first-class UI mode buttons. See [[VSCode/Q/Is there a setting that hides or shows dot folders and dot files in the explorer panel on the left by default?]] for the settings approach.
