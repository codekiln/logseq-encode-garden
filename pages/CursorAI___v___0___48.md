tags:: [[CursorAI/Changelog]]
date-created:: [[2025-03-23 Sun]]

- # [Changelog - Mar 23, 2025 | Cursor - The AI Code Editor | Cursor - The AI Code Editor](https://www.cursor.com/en/changelog/chat-tabs-custom-modes-sound-notification)
	- [[My Notes]]
		- [[2025-05-09 Fri]] you now have to ask cursor to "search the codebase" which is a bit slower than using an at-command. I suppose one could create a custom rule.
	- ### Built-in modes & custom modes (beta)
		- Agent and Ask modes are the built-in modes in Cursor, now with the option to add custom modes. We've also renamed "Edit" to "Manual" to better reflect its behavior.
		- ### deprecation of [[CursorAI/@/Codebase]]
			- Ask mode now has access to all search tools by default, so the `@Codebase` tool has been removed. It will automatically search the codebase when needed.
			- If you want to force a search, **simply ask Cursor in natural language to "search the codebase"**.
			- You can disable search from Ask in the mode menu, which will result in Ask only seeing the context you have provided.
		- Read more about [Agent](https://docs.cursor.com/chat/agent) and [Ask](https://docs.cursor.com/chat/ask).
-