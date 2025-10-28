tags:: [[Blog]], [[Simon Willison]], [[Claude]], [[Documentation]]
date-created:: [[2025/10/25]]
created-by:: [[Person/Simon Willison]]
source:: https://simonwillison.net/2025/Oct/25/claude-docs/

- # [Claude Docs Best Practices - Simon Willison](https://simonwillison.net/2025/Oct/25/claude-docs/)
	- ## Key Insight
		- Documentation best practice for Claude Code:
			- > If you have an `AGENTS.md` file, you can source it in your `CLAUDE.md` using `@AGENTS.md` to maintain a single source of truth.
	- ## Context
		- This tip addresses documentation organization in [[Claude Code]]
		- Enables centralized agent configuration management
		- Prevents duplication across documentation files
	- ## Implementation
		- Create a dedicated `AGENTS.md` file for agent configurations
		- Reference it in `CLAUDE.md` using the `@` syntax
		- Maintains consistency across documentation
	- ## Related
		- [[AI/Coding]]
		- [[Documentation]]
		- [[Claude]]
		- [[My/Dev/Tool/Pref/AI/Coding/Config/Management]]
