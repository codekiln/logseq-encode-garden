tags:: [[Diataxis/How To]], [[.mdc]]

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
		- [[JustDo/Blog/25/03/Major Lessons for Cursor v0.47.8]]
-