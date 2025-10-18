created-by:: [[Person/Eric Buess]]
alias:: [[Anthropic/App/Claude Code/GitHub/claude-code-docs]]

- # [ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs)
	- README
		- Local mirror of Claude Code documentation files from [https://docs.anthropic.com/en/docs/claude-code/](https://docs.anthropic.com/en/docs/claude-code/), updated every 3 hours.
		- ## [Installation](https://github.com/ericbuess/claude-code-docs/tree/main#installation)
			- Run this single command:
			- ```
			  curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/main/install.sh | bash
			  ```
			- This will:
			- Install to `~/.claude-code-docs` (or migrate existing installation)
			- Create the `/docs` slash command to pass arguments to the tool and tell it where to find the docs
				- [[My Note]] *this is installed in the `~/.claude/commands/docs.md` file*
			- Set up a 'PreToolUse' 'Read' hook to enable automatic git pull when reading docs from the ~/.claude-code-docs`
	- [[My Notes]]
		- [[2025-09-29 Mon]]
			- I'm surprised that this came from community contributor [[Person/Eric Buess]] rather than Anthropic.
			- It's a bit opinionated; it comes with an "installer" that will install it to `~/.claude-code-docs`, create the `/docs` slash command, which is kind of generic. This was noticed in [`/docs` command is generic · Issue #21 · ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs/issues/21)
				- > to change the name of the slash command, simply modify the file name of `~/.claude/commands/docs.md` to `~/.claude/commands/CUSTOM_NAME.md`.