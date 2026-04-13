## What's the #[[VSCode/Command]] and #Keyshort to open a #Markdown preview to the side? #card - same as [[CursorAI/Command]] and [[CursorAI/Keyshort]]
card-last-interval:: -1
card-repeats:: 1
card-ease-factor:: 2.5
card-next-schedule:: 2026-04-13T04:00:00.000Z
card-last-reviewed:: 2026-04-12T08:18:38.600Z
card-last-score:: 1
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