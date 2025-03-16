### Official Description from UI
	- > When you specify file patterns here (e.g. `*.py` or `client/**/*.tsx`), this rule will automatically be included in AI responses for files matching those patterns.
- ### Activated when
	- [[CursorAI/Project Rule/Frontmatter/description]] is **empty**
	- [[CursorAI/Project Rule/Frontmatter/globs]] is **filled in with one or more [[globs]]**
	- [[CursorAI/Project Rule/Frontmatter/alwaysApply]] is `false`
- ### #Example [[Markdown Yaml Frontmatter]]
	- ```
	  ---
	  description: 
	  globs: *.txt
	  alwaysApply: false
	  ---
	  ```