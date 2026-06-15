logseq-entity:: [[Logseq/Entity/Question]]

- # How can I rename a Foam page so that all wikilinks to it are renamed too?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** rename the file through [[VS Code]]'s Explorer or "Rename File" command — [[Foam]] hooks into VS Code's `onDidRenameFiles` event and updates all `[[wikilink]]` references automatically.
			- ### Method: VS Code Explorer rename (F2 or right-click)
				- In the Explorer panel, select the file and press `F2` (or right-click → **Rename**).
				- VS Code fires the `onDidRenameFiles` workspace event; [[Foam]] listens for it and rewrites every `[[OldName]]` or `[[Old Title]]` wikilink across the workspace to `[[NewName]]`.
				- The change propagates to all `.md` files in the Foam workspace, including journals.
			- ### Why terminal renames won't work
				- Running `mv OldName.md NewName.md` in a shell bypasses VS Code's extension hooks entirely.
				- [[Foam]] never sees the rename, so existing `[[OldName]]` links become broken stubs.
			- ### Alternative: VS Code Command Palette
				- Open the Command Palette (`Cmd/Ctrl+Shift+P`) and run **File: Rename File**.
				- Same result as the Explorer F2 path — triggers the hook and updates all references.
