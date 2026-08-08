alias:: [[AI Agent Hook]], [[AI Agent Hooks]]
logseq-entity:: [[Logseq/Entity/Term]]

- # AI Agent Hook
	- A hook is a deterministic event handler that an [[AI/Agent]] host runs around tool execution, session lifecycle, file changes, prompting, compaction, or subagent start and stop. Where a prompt persuades, a hook always fires, and it can block.
	- Unlike [[Agent/Skills]], hooks have no open specification. There is nothing to cite but each vendor's own reference, and the references do not agree.
	- ## Why hooks do not port
		- The same moment has a different name everywhere. Before a tool call is `PreToolUse` in [[Claude/Code/Hook]], `preToolUse` in [[CursorAI/Hook]], `BeforeTool` in [[GeminiCLI/Hook]], and `tool_execution_start` in [[PiAI/Hook]]. Compaction is `PreCompact`, `preCompact`, and `PreCompress` respectively.
		- Naming is the shallow part. A mapping still cannot preserve execution timing, input schemas, blocking behavior, or output semantics — which is why Cursor describes its Claude-hook support as a subset mapping rather than compatibility.
		- [[Codex/Hook]] is the one near-match: PascalCase events that track Claude's closely, and hook commands that receive `CLAUDE_PLUGIN_ROOT` and `CLAUDE_PLUGIN_DATA` as legacy aliases.
		- Trust models diverge too. Codex will not run a non-managed plugin hook until you review and trust its exact definition, tracked by hash. [[PiAI/Hook]] and [[OpenCode/Hook]] are ordinary extension code running with full system permissions.
		- [[rulesync]] carries hooks as one of its canonical components and emits per-host representations, which is the closest thing to portability available. See [[AI/Coding/Tool/Plugin/Report/26/Agentic Coding Plugin Systems and Cross-Provider Portability]].
	- Not to be confused with [[git/hook]] or [[DevContainer/Hook]].
	- ## [[Examples]]
		- [[Claude/Code/Hook]]
		- [[Codex/Hook]]
		- [[CursorAI/Hook]]
		- [[GeminiCLI/Hook]]
		- [[GitHub/CoPilot/CLI/Hook]]
		- [[OpenCode/Hook]]
		- [[PiAI/Hook]]
		- [[Junie]] does not list hooks as an extension component.
