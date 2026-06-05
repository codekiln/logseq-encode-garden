logseq-entity:: [[Logseq/Entity/Software/Project]]

- # [skillshare](https://skillshare.runkids.cc)
	- [github: runkids/skillshare](https://github.com/runkids/skillshare) · Go · 2.1k ★
	- Syncs agent skills to 60+ AI CLI tools (Claude Code, Codex, Cursor, Copilot, Gemini CLI, …) from a single command. Stores skills in `.skillshare/` (project) or a tracked Git repo (org-wide).
	- Features a `skillshare ui` web dashboard, team sharing via tracked repos, and built-in audit for prompt injection and data exfiltration. Install skills from GitHub, GitLab, Bitbucket, or self-hosted Git.
	- Narrower scope than [[rulesync]]: skillshare focuses on skills (with stronger team and security tooling); rulesync also handles rules, commands, subagents, and MCP across the same tool targets.
	- Both tools follow the agentskills.io open standard; see [[rulesync]] `## Skills` for a note on rulesync's `codexcli` adapter writing to the wrong directory (`.codex/skills/` vs `.agents/skills/`).
