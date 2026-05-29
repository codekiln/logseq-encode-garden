logseq-entity:: [[Logseq/Entity/Article]]
source-link:: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
date-created:: [[2026/05/28]]
via:: [[2026-05-28 Wed]]

- # [Introducing dynamic workflows in Claude Code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)
	- ## Summary
		- **Dynamic workflows** enable [[Anthropic/Model/Claude/4.8/Opus]] to tackle complex, multi-stage engineering projects by orchestrating parallel subagents—sometimes numbering in the tens or hundreds—within a single session, automatically verifying results before delivery.
		- Users trigger workflows directly or via the **ultracode** setting, which determines when workflow deployment is appropriate.
	- ## Use Cases
		- Codebase-wide bug hunts, profiler-guided optimization audits, and security audits
		- Large migrations and modernization efforts
	- ## Early Adopter Results
		- **Klarna** and **CyberAgent** report strong results
		- Complete port of the **Bun** programming language from Zig to Rust: ~750,000 lines of code, 99.8% test suite compatibility, completed in eleven days
	- ## Availability
		- Research preview across Claude Code CLI, desktop app, VS Code extension, and API platforms including **Amazon Bedrock** and **Vertex AI**
		- Organization admins can manage workflow availability in settings
		- Token consumption is higher than standard Claude Code sessions
