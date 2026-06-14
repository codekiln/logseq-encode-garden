logseq-entity:: [[Logseq/Entity/Question]]

- # What is the MEMORY.md feature in [[Claude/Code]], can I customize where these files are stored, and is it based on an open spec like AGENTS.md?
	- ## [[AI Answer]]
		- [[AI/Response]]
		- **Short answer:** MEMORY.md is the index file for Claude Code's auto-memory system (v2.1.59+), stored by default at `~/.claude/projects/<project>/memory/`. The location can be customized via `autoMemoryDirectory` in user settings. It is not based on an open spec — it is Anthropic-proprietary; AGENTS.md is an OpenAI/Codex convention for agent instructions, which Claude Code does not natively read.
		- **What MEMORY.md is:**
			- Auto memory lets Claude accumulate knowledge across sessions without manual effort — build commands, debugging insights, architecture notes, code style preferences, workflow habits
			- The memory directory holds `MEMORY.md` as a concise index plus optional topic files (e.g. `debugging.md`, `api-conventions.md`)
			- Only the first 200 lines (or 25 KB) of `MEMORY.md` are injected into context at session start; topic files are read on demand via file tools
			- Claude decides what is worth saving — it does not write to memory every session
			- Memory is machine-local and shared across all worktrees of the same git repository
		- **Default storage location:**
			- `~/.claude/projects/<project>/memory/` where `<project>` is derived from the git repo path
			- Example: `/Users/you/.claude/projects/-Users-you-Documents-myrepo/memory/`
			- Directory layout:
				- ~~~
				  ~/.claude/projects/<project>/memory/
				  ├── MEMORY.md          # concise index, loaded every session
				  ├── debugging.md       # topic file, read on demand
				  └── api-conventions.md
				  ~~~
		- **Customizing the storage location:**
			- Set `autoMemoryDirectory` in `~/.claude/settings.json`:
				- ~~~json
				  {
				    "autoMemoryDirectory": "~/my-custom-memory-dir"
				  }
				  ~~~
			- Value must be an absolute path or start with `~/`
			- Accepted from policy settings and user settings (and `--settings` flag)
			- **Not** accepted from project or local settings — a cloned repo could otherwise redirect writes to sensitive paths
		- **Toggle and inspect auto memory:**
			- Auto memory is on by default; run `/memory` in a session to toggle it or browse saved files
			- Disable via settings: `"autoMemoryEnabled": false` or env var `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`
			- All memory files are plain Markdown — edit or delete them at any time
		- **Is it based on AGENTS.md or any open spec?**
			- No. MEMORY.md is proprietary to Claude Code's auto-memory system; there is no public specification
			- AGENTS.md is a convention from OpenAI/Codex for persistent agent *instructions* — a different concept (human-written rules, not agent-written notes)
			- Claude Code reads `CLAUDE.md` for instructions, not `AGENTS.md`; you can bridge both with `@AGENTS.md` inside `CLAUDE.md` so both tools share the same rules without duplication
			- No cross-agent open spec exists that covers MEMORY.md-style auto-written memory files
		- Sources: [How Claude remembers your project — Claude Code Docs](https://code.claude.com/docs/en/memory)
