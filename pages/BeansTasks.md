logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Hendrik Mans]]
tags:: [[Task/Management/Git-Friendly]]
- # [hmans/beans](https://github.com/hmans/beans)
	- [[CLI/Tool]] that implements a git-backed issue tracker for AI agents.
	- ## Data Model
		- [[Markdown]] stored in `.beans/`
	- ## [[My Notes]]
		- includes a [[TUI]]
		- by [[2026-05-26 Tue]]
			- ~800 [[GitHub/Star]]s
			- hasn't been updated in a month
		- creator [[Person/Hendrik Mans]] has many established [[Open Source]] projects
		- includes [[AI/Coding/Tool/Plugin]]s
			- [[Claude Code Plugin]]
			- [[OpenCode/Plugin]]
	- ## [[Engineering Choices]]
		- written in [[Go]]
	- ## [[Installation]]
		- ### Getting the [[Executable]]
			- #### [[GitHub/Release]] [Releases · hmans/beans](https://github.com/hmans/beans/releases)
				- ##### install with [[mise]]
					- `mise use -g hmans/beans`
			- #### [[brew]] `brew install hmans/beans/beans`
		- ### [[AI/Agent/Setup]] [here](https://github.com/hmans/beans#agent-configuration)
			- The most basic way to teach your agent about Beans is to simply add the following instruction to your `AGENTS.md`, `CLAUDE.md`, or equivalent file:
			- ```
			  **IMPORTANT**: before you do anything else, run the `beans prime` command and heed its output.
			  ```
			- Some agents provide mechanisms to automate this step:
			- #### [Claude Code](https://github.com/hmans/beans#claude-code)
				- The README says "An official Beans plugin for Claude is in the works" but one appears to be available at https://github.com/hmans/beans/blob/main/.claude-plugin/marketplace.json
				- > for the time being, please manually add the following hooks to your project's `.claude/settings.json` file:
					- ```
					  {
					  "hooks": {
					    "SessionStart": [
					      { "hooks": [{ "type": "command", "command": "beans prime" }] }
					    ],
					    "PreCompact": [
					      { "hooks": [{ "type": "command", "command": "beans prime" }] }
					    ]
					  }
					  }
					  ```
	-
