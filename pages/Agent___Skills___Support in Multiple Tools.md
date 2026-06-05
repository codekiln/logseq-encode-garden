logseq-entity:: [[Logseq/Entity/concept]]
see-also:: [[Agent/Skills/Dir]], [[Agent/Skills/Dir/Compatibility]], [[skillshare]], [[rulesync]]

- # Agent Skills: Support Across Multiple Tools
	- ## Overview
		- The [[Agent/Skills]] open standard defines what a skill file contains but does not mandate where skill directories live. Each vendor ships a native directory (`.claude/skills/`, `.gemini/skills/`, etc.), and `.agents/skills/` is the recommended cross-client interoperability path. The gap between these two conventions is the central challenge of multi-tool skill management.
	- ## The core tension
		- The spec recommends that clients scan `.agents/skills/` alongside their native path, but not all vendors have implemented this. A user who installs skills to `~/.agents/skills/` following the ecosystem convention will find those skills invisible in [[Claude/Code]], which only scans `~/.claude/skills/`.
		- This gap is documented in a live bug report: [Vercel skills issue #693](https://github.com/vercel-labs/skills/issues/693) — skills installed to `~/.agents/skills` are silently ignored by [[Claude/Code]].
	- ## How vendors currently handle `.agents/skills`
		- GitHub Copilot officially documents both `.agents/skills` and `~/.agents/skills` as valid skill locations alongside its native paths — strong evidence that `.agents/skills` is becoming a real interoperability target, not just a spec aspiration.
		- OpenAI [[Codex]] and Gemini CLI also scan `.agents/skills/` natively.
		- [[Claude/Code]] (as of mid-2026) does not natively scan `.agents/skills/`; a community issue ([anthropics/claude-code#31005](https://github.com/anthropics/claude-code/issues/31005)) requests this support.
		- See [[Agent/Skills/Dir/Compatibility]] for a full tool-by-tool matrix.
	- ## Dominant workarounds
		- ### Symlinks
			- Put skills in `~/.agents/skills/`, then symlink into `~/.claude/skills/`. Multiple practitioners recommend this, including an SSW engineering rule ([ssw.com.au/rules/symlink-agents-to-claude](https://www.ssw.com.au/rules/symlink-agents-to-claude)) and a dedicated blog post ([wow.pjh.is](https://wow.pjh.is/journal/share-skills-between-coding-agents)).
		- ### Sync tooling
			- [[skillshare]] ("One source, every agent") syncs skills from a single source to 60+ agent tools.
			- [[rulesync]] takes a broader scope: rules, commands, subagents, and MCP config in addition to skills, targeting the same set of tools.
	- ## Why convergence is slow
		- The spec defines what goes _inside_ a skill file, not where the directory lives. Vendors have pre-existing conventions they cannot rename without breaking existing users. Adopting `.agents/skills/` is an additive second lookup, not a rename — which makes adoption optional and therefore incremental.
	- ## Current state (mid-2026)
		- The dominant pattern in the practitioner community:
			- 1. Author skills once, in `.agents/skills/` (or `~/.agents/skills/` for user-level)
			- 2. Symlink into vendor-specific directories for tools that don't yet scan `.agents/skills/` natively
			- 3. Use a sync tool ([[skillshare]] or [[rulesync]]) for multi-agent teams or repos with many targets
			- 4. Watch for vendor convergence as GitHub Copilot's official support normalizes the interoperability path
