month-created:: [[2025/03]]
date-created:: [[2025-03-20 Thu]]

- # [JustDo: The Ultimate Project Management Platform for Vibe Coding](https://justdo.com/blog/justdo-vibe-coding-project-management--justdo-the-ultimate-project-management-platform-for-vibe-coding)
	- [[My Notes]]
	  id:: 67ded1a3-6190-4b74-8ed8-8b88683c93b7
		- I don't quite get it. Somehow they are claiming that this [[Project/Management]] tool is better for [[AI Coding]] because the source code is available, and therefore the AI can modify it to your needs.
		- They have cursor rules in [[JustDo/GitHub/justdo]] here - [justdo/.cursor/rules at master · justdoinc/justdo](https://github.com/justdoinc/justdo/tree/master/.cursor/rules)  - so clearly they are trying to use it this way ... but I don't quite understand what they are thinking about how a downstream repo is supposed to use cursor to customize this. Are they expecting that we'll fork it and use the built-in rules ... ? Also, what exactly is the integration ... is it able to use MCP to integrate with JustDo?
			- FWIW it's worth, their [[CursorAI/Project Rules]] are well organized
	- Quotes
		- Unlike closed-source platforms that limit AI-assisted development, JustDo's available source code creates the perfect playground for vibe coding. LLM agents like those in Cursor or Claude Code can directly modify JustDo's codebase based on simple user prompts. The transparent architecture allows AI agents to understand system interactions and make targeted changes. JustDo's package-first design makes it natural for vibe coders to extend functionality without disrupting core systems.
		- The code contains extensive embedded instructions that teach AI agents about common workflows and architectural patterns. Clear naming conventions and code organization help LLMs predict where and how to implement changes.
		- you can create new plugins with simple prompts like "Add a time tracking plugin with Pomodoro functionality". Modify existing behaviors through natural language descriptions such as "Change the Kanban view to include color-coding based on priority". You can even extend the AI capabilities themselves by requesting to "Add sentiment analysis to task comments".