alias:: [[Claude Code Subagent]], [[Claude Code Subagents]]

- # [Create custom subagents – Claude Code](https://code.claude.com/docs/en/sub-agents)
	- [[Claude/Code]]'s implementation of [[AI/Agent/Subagent]]: a Markdown file with YAML frontmatter, resolved from `.claude/agents/` for the project, `~/.claude/agents/` for every project, or a [[Claude/Code/Plugin]]'s `agents/` directory, in that precedence order.
	- Only `name` and `description` are required. The optional surface is the widest of any host — `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `effort`, `isolation` (set to `worktree` for a temporary [[git]] worktree), `color`, and `initialPrompt`. That richness is exactly what makes a Claude agent definition lossy to port anywhere else.
	- Each subagent runs in its own context window with its own system prompt, tool access, and permissions, so the delegating conversation gets back a summary rather than the search results.
	- [[Claude/Code/Plugin/agent-teams-claude-code]] packages a set of these as a unit.
