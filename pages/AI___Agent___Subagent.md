alias:: [[AI Subagent]], [[AI Subagents]]
logseq-entity:: [[Logseq/Entity/Term]]

- # Subagent
	- A subagent is a specialized agent definition with its own prompt, tools, model selection, context, or execution policy, which the main agent delegates to. The point is context: the side task runs in its own window and returns a summary instead of flooding the main conversation.
	- Like [[AI/Agent/Hook]] and unlike [[Agent/Skills]], there is no open specification — only each vendor's reference.
	- ## Why subagents do not port
		- The file format nearly converges and then doesn't. Markdown with YAML frontmatter in an `agents/` directory covers [[Claude/Code/Subagent]], [[CursorAI/Subagent]], [[GeminiCLI/Subagent]], [[GitHub/CoPilot/CLI/Subagent]] (as `*.agent.md`), and [[OpenCode/Subagent]] — but [[Codex/Subagent]] uses TOML in `~/.codex/agents/`, and [[PiAI/Subagent]] has no declarative format at all.
		- The real gap is capability. A Claude definition declares `model`, `effort`, `maxTurns`, `permissionMode`, `memory`, `background`, `hooks`, and `isolation: worktree`; Cursor documents a much smaller frontmatter surface; Gemini's are preview. Fields drop silently on the way across.
		- Standalone host configuration and packaged plugin composition are separate surfaces. Codex documents subagents fully and its plugin manifest still has no `agents` field, so a [[Codex/Plugin]] cannot ship one. "Does tool X support subagents" is the wrong question — ask which surface. See [[AI/Coding/Tool/Plugin/Report/26/Agentic Coding Plugin Systems and Cross-Provider Portability]].
	- Related but distinct: [[AI/Agent/Multi]] is about orchestrating agents; a subagent is the unit being orchestrated.
	- ## [[Examples]]
		- [[Claude/Code/Subagent]]
		- [[Codex/Subagent]]
		- [[CursorAI/Subagent]]
		- [[GeminiCLI/Subagent]]
		- [[GitHub/CoPilot/CLI/Subagent]]
		- [[Junie/Subagent]]
		- [[OpenCode/Subagent]]
		- [[PiAI/Subagent]]
