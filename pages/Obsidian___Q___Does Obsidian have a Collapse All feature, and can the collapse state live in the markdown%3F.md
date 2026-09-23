logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Logseq/Block/Attribute/collapsed]]
via:: [[PKM/Log/26/09/23 Wed - Stacked Discussions in Multi-Tier Gardens]]
- # Does [[Obsidian]] have a Collapse All feature, and can the collapse state live in the markdown like [[Logseq/Block/Attribute/collapsed]]?
	- ## [[AI Answer]]
		- **Short answer:** yes to Collapse All — it ships as **Fold all headings and lists**, bindable to a [[Keyshort]]. No to the second half out of the box: Obsidian keeps fold state in `localStorage`, so it never reaches the file and never survives a sync. Two community plugins fix that by writing a `%% fold %%` comment onto the folded line, which is the closest thing Obsidian has to `collapsed:: true`.
		- ### The native Collapse All
			- [[Answer/Official]] from [Folding - Obsidian Help](https://obsidian.md/help/folding).
			- **Fold all headings and lists** collapses the whole note; **Unfold all headings and lists** reverses it. Both are ordinary commands, so either can take a hotkey in **Settings → Hotkeys**.
			- **Fold heading** and **Fold indent** must be on under **Settings → Editor** for folding to work at all.
			- **Fold more** and **Fold less** act on the section under the cursor rather than the note, for finer control.
			- The file explorer and the outline pane carry their own collapse-all buttons; those fold the tree, not the document.
		- ### Why the state does not reach the file
			- Obsidian stores fold state in `localStorage`, which is per-device. It is lost on a reinstall, and it never crosses to another machine — no sync tool moves it, because it is not in the vault. See [How Obsidian stores data](https://obsidian.md/help/data-storage).
			- This is the structural difference from [[Logseq]]. Logseq writes `collapsed:: true` as a block property in the markdown itself, so the fold travels with the file and is visible to anything that reads it.
		- ### Plugins that put the fold in the document
			- Both write `%% fold %%` onto the folded line. It is Obsidian's native comment syntax, so it is invisible in Reading view and inert to any other tool reading the file — closer to a hidden marker than to Logseq's declared property.
			- **[Creases](https://github.com/liamcain/obsidian-creases)** by Liam Cain — in the community directory, ~45k downloads. Works on **headings and lists**. Adds *Toggle crease*, *Fold along creases*, *Iron out the creases*, *Crease the current folds*, and vim-style fold-level commands. The model is deliberate: a crease is a fold you declared, not a record of how you last left the note.
			- **[Foldstate](https://github.com/samhopwell/obsidian-foldstate)** — manual install only, not in the directory. **Headings only**, and only in Live Preview or Source mode. The model is automatic: every fold and unfold rewrites the marker, so the file records the note's current state.
			- **[Sync Folds](https://github.com/itsonlyjames/obsidian-sync-folds)** takes the third path — fold state goes into the plugin's own `data.json` rather than the note. It syncs across devices but leaves the markdown untouched, so it does not answer the question as asked.
		- ### Which one matches the preference
			- For a fold that lives in the document and is set on purpose, **Creases** is the closer fit: it is maintained, in the directory, and covers lists as well as headings.
			- For a fold that mirrors how the note was last left, without any deliberate act, **Foldstate** is the only one that does it — at the cost of a manual install and heading-only coverage.
		- ### Scope of this answer
			- Drawn from the official Obsidian help and the plugins' own repositories. Download counts and update dates were read in September 2026.
