alias:: [[Claude/Code/Slash/fewer-permission-prompts]]
tags:: [[Agent/Command]], [[Claude/Code]]

- # Claude Code /fewer-permission-prompts
	- Scans conversation transcripts for common read-only [[Bash]] and [[MCP]] tool calls, then adds a prioritized allowlist to `.claude/settings.json` to reduce future permission prompts.
	- ## Usage
		- Run `/fewer-permission-prompts` inside a Claude Code session
		- Claude reviews recent transcripts for repetitive safe tool calls
		- Adds those calls to an allowlist in the project's `.claude/settings.json`
	- ## See also
		- [[Claude Code/Command/Slash]] — all Claude Code slash commands
		- [[Agent/Command]]
