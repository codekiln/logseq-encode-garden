alias:: [[GitHub/Agentic Workflow]]
logseq-entity:: [[Logseq/Entity/Software/Project]]

- # [GitHub Agentic Workflows](https://github.github.com/gh-aw/)
	- Repository: [github/gh-aw](https://github.com/github/gh-aw). [[GitHub/Star]]: 5552 (checked [[2026-11-01 Sun]]).
	- [[GitHub/CLI/Extension]] that compiles Markdown workflow files into standard [[GitHub/Action]] workflows that run an AI coding agent.
	- Each workflow file has YAML frontmatter for triggers, permissions, tools, and the AI engine; the Markdown body tells the agent what to do. `gh aw compile` turns it into a `.lock.yml` file that Actions runs.
	- Engines: GitHub Copilot, [[Claude/Code]], [[Codex]], Google Gemini, and Pi.
	- Agent jobs run read-only and sandboxed by default. Writes back to GitHub go through separate `safe-outputs` jobs with scoped permissions.
	- Suited to tasks that need judgment, such as issue triage, pull request review, CI failure investigation, and keeping docs current. Builds, tests, and deploys stay in ordinary Actions workflows.
	- Install with `gh extension install github/gh-aw`.
	- Written in [[Go]].
