## What's the #[[VSCode/Command]] and #Keyshort to open a #Markdown preview to the side? #card - same as [[CursorAI/Command]] and [[CursorAI/Keyshort]]
	- Command: **Markdown: Open Preview to the Side**
	- Keyshort: `Cmd+K V`
	- [[VSCode/Keymap]]
		- ```json
		  {
		    "key": "cmd+k v",
		    "command": "markdown.showPreviewToSide",
		    "when": "!notebookEditorFocused && editorLangId == 'markdown'"
		  }
		  ```