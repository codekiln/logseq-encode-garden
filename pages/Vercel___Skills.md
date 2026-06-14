logseq-entity:: [[Logseq/Entity/Concept]]
created-by:: [[Person/Guillermo Rauch]]

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
	- ## Local path source limitation
		- [[My Notes]]
			- ### [[2026-06-08 Mon]] inability to use [[Vercel/Skills]] to manage skills [[Declar/at/ive/ly]]
			  id:: 6a26aa7f-5148-47da-9432-5818cc34dfc6
				- [[tldr]]
					- I considered using `skills` cli instead of `rulesync` for declaratively managing skills, but  confusingly, it doesn't work for local directories the way it should. It does populate a skills lockfile, but it uses absolute paths which are machine specific.
				- longer description
					- `npx skills add ./local-path` works for one-time install but **`skills-lock.json` always stores the absolute path** — `source-parser.ts` calls `resolve()` on any input before writing the lock file, so relative paths are never stored
					- Additionally, `update.ts` explicitly skips `sourceType: "local"` entries during `npx skills update`, so local sources are never updatable via the CLI
					- Together these make declarative, portable skill installation from a local directory impossible: the lock file encodes a machine-specific absolute path (including the OS username), and the update mechanism ignores it anyway
					- This severely limits `vercel/skills` as a declarative install tool for dotfiles repos that manage skills as local source files
				- TODO Research whether there are open GitHub issues or PRs on [vercel-labs/skills](https://github.com/vercel-labs/skills) addressing relative path support in `skills-lock.json`
				- **Workaround**: Until this is resolved, continue using [[rulesync]] for skills management in dotfiles — rulesync generates directly into `.claude/skills/` from `.rulesync/skills/` without a lock file abstraction
	- ## Ecosystem context
		- Competitor to [[skillshare]] (cross-agent skills sync) and [[rulesync]] (broader scope: rules, commands, subagents, MCP config in addition to skills)
		- See [[AI/Coding/Tool/Report/25/Skills Comparison]] for comparative analysis; [[Claude/Code/Skill/Project]] was the first prominent skills implementation in this ecosystem