logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[1Password]]
date-created:: [[2026-06-05 Fri]]

- # [1password-claude-plugin](https://github.com/1Password/1password-claude-plugin)
	- [[GitHub/Star]] count: 3 (checked [[2026-09-30 Wed]])
	- [[Claude/Code/Plugin]] for [[1Password/Environment]]s, built by 1Password. The repo is its own [[Claude/Code/Plugin/Marketplace]]: `/plugin marketplace add 1Password/1password-claude-plugin`, then `/plugin install 1password@1password`.
	- Three pieces:
		- a `PreToolUse` [[Claude/Code/Hook]] that checks, before every Bash command, that each 1Password-mounted `.env` exists, is a named pipe, and is switched on in 1Password. It blocks the command when one is not, and fails open when 1Password or `sqlite3` is missing.
		- a `1password-environments` skill carrying the import-and-mount workflow, which the MCP server's own docs leave out
		- `.mcp.json` that launches the local `1password-mcp` server from [[1Password/Environment/MCP]]. It has the same eight tools as [[1Password/GitHub/1password-codex-plugin]].
	- macOS and Linux only. On [[Windows]] the hook exits without a decision, and the skill falls back to `op run --environment=<id>` ([[1Password/Dev/op/run]]) because Environments has no local `.env` mounts there.
	- The GitHub description still calls it "a Claude desktop extension (MCPB) for macOS". That fits the first commit, a June 2026 port of 1Password's [[kiro.dev]] plugin to MCPB. By September it had become a Claude Code plugin, and no MCPB bundle remains in the repo.
	- Written in [[Bash]].
