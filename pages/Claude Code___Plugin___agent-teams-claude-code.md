logseq-entity:: [[Logseq/Entity/Software/Plugin]]
created-by:: [[Person/Victor del Rosal]]
date-created:: [[2026/02/26]]

- # [agent-teams-claude-code](https://github.com/victordelrosal/agent-teams-claude-code)
	- Field manual for building multi-agent systems in [[Claude Code]], written for AI instances. 28 files covering architecture, patterns, examples, and industry playbooks; built by a 5-agent team.
	- **Stars:** 0 · **License:** none
	- ## Key distinctions covered
		- **Agent Teams (experimental)** — requires feature flag; peer-to-peer messaging between named Claude instances
		- **Subagents (stable)** — orchestrator-worker pattern via the Task tool
		- **CLI Pipelines (stable)** — headless Claude invocations via Unix pipes
	- ## Architecture
		- Team lead coordinates independent teammates via shared DAG task lists
