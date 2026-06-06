logseq-entity:: [[Logseq/Entity/concept]]

- # Vercel Skills Ecosystem
	- Vercel's open agent skills platform: a registry of security-audited, installable agent skills discoverable through a web interface and a CLI.
	- ## Components
		- [[Vercel/Skills/Web]] — registry browser at [skills.sh](https://www.skills.sh); skills browsable by topic (React, Next.js, databases, testing, etc.)
		- [[Vercel/Skills/CLI]] — `npx skills` installer backed by [vercel-labs/skills](https://github.com/vercel-labs/skills); installs into [[Claude/Code]], Cursor, Codex, GitHub Copilot, Gemini CLI, Cline, and 20+ other tools
	- ## Vercel Labs skill repos
		- [vercel-labs/skills](https://github.com/vercel-labs/skills) — main CLI and registry (21.4k ★)
		- [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
		- [vercel-labs/next-skills](https://github.com/vercel-labs/next-skills)
		- [vercel-labs/slack-agent-skill](https://github.com/vercel-labs/slack-agent-skill)
		- [vercel-labs/skills-detector](https://github.com/vercel-labs/skills-detector)
		- [vercel-labs/skills-handler](https://github.com/vercel-labs/skills-handler)
		- [vercel-labs/sitecore-skills](https://github.com/vercel-labs/sitecore-skills)
		- [vercel-labs/academy-skills](https://github.com/vercel-labs/academy-skills)
	- ## Ecosystem context
		- Competitor to [[skillshare]] (cross-agent skills sync) and [[rulesync]] (broader scope: rules, commands, subagents, MCP config in addition to skills)
		- See [[AI/Coding/Tool/Report/25/Skills Comparison]] for comparative analysis; [[Claude/Code/Skill/Project]] was the first prominent skills implementation in this ecosystem
