tags:: [[Diataxis/How To]]

- # How to prevent cursor from trying to render its custom UI on top of [[.mdc]] files
	- Great #Tip to prevent Cursor from trying to render its custom UI on top of [[.mdc]] files - put this in [[VSCode/settings.json]]
		- ```
		  ...
		    "workbench.editorAssociations": {
		      "*.mdc": "default"
		    },
		    "files.associations": {
		      "*.mdc": "markdown"
		    }
		  ```
	- [[Via]]
		- [[Person/Brian Madison/GitHub/cursor-auto-rules-agile-workflow]]
		- [[CursorAI/Forum/25/02/The MDC editor is whack]]
-