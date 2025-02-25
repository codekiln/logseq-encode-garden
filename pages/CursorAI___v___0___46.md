alias:: [[CursorAI/v/0.46 - Agent is ready and UI Refresh]]

- # [Changelog - Feb 19, 2025 | Cursor - The AI Code Editor | Cursor - The AI Code Editor](https://www.cursor.com/changelog/agent-is-ready-and-ui-refresh)
	- ## [[CursorAI Agent Mode]] default
		- No more multiple tabs, e.g. Chat, Composer, and Agent, just one smart interface that adapts
	- ## UI refresh
		- new default Cursor themes designed for focus
		- simplified the @-context menu to make Agent more precise.
			- TODO #Q *what exactly is the change here?*
				- I've noticed a change in the last 24 hours about being able to drill into the file hierarchy, is that this?
	- ## Web search
		- [[CursorAI Agent Mode]] can now automatically search the web for up-to-date information without requiring explicit @Web commands.
	- ## Security
	  id:: 67bd9cae-648a-4958-9f5f-db961bf49650
		- Ignore files: [[CursorAI/.cursorignore]] now **blocks files from being added in chat or sent up for tab completions**, *in addition to ignoring them from indexing*.
		- **NEW:** [[CursorAI/.cursorindexingignore]] for specifically controlling file indexing
			- TODO #Q *when would I want to put something in `.cursorindexingignore` instead of `.cursorignore`?*
				- ... if I wanted something to be available to cursor in file references but not indexed? What's the use of that?
	- ## [[CursorAI/Project Rules]]
		- **New** capability to **apply rules globally**
		- **visual indicator** for **when rules are applied**
	- ## #MCP improvements
	  id:: 67bd9c43-1412-46a7-b94e-8bba322198cc
		- Agent can now automatically run MCP tools with Yolo mode
		- ### Configure Project Servers with `<project-root>/.cursor/mcp.json` #Awesome
			- TODO what's the json schema for this #q
		- Support for Agent to use [[MCP/Resource]] as context
			- I didn't know that Agent *didn't* support these ... this is essential to [[CursorAI/Idea/Proj Rules GitHub CLI AI SLDC/MCP]]