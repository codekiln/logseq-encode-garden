## What's the #VSCode/Command and #Keyshort to open a #Markdown Preview #card
	- Command: Markdown: Open Preview
	- Keyshort: Shift+Cmd+V
	- [[VSCode/Keymap]]
		- ```json
		  {
		    "key": "shift+cmd+v",
		    "command": "markdown.showPreview",
		    "when": "!notebookEditorFocused && editorLangId == 'markdown'"
		  }
		  ```