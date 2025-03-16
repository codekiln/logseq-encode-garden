### Official Description from UI
	- > The agent can see this description and decide to read the full rule if it wants it.
- ### Activated when
	- [[CursorAI/Project Rule/Frontmatter/description]] is **filled in with a phrase that will activate the agent**
	- [[CursorAI/Project Rule/Frontmatter/globs]] is **empty**
	- [[CursorAI/Project Rule/Frontmatter/alwaysApply]] is `false`
- ### #Example [[Markdown Yaml Frontmatter]]
	- ```
	  ---
	  description: Use this when composing git commits
	  globs: 
	  alwaysApply: false
	  ---
	  ```