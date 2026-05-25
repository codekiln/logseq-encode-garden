logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Codex/CLI]], [[Claude Code/Command/Slash/Docs/Comparison with Skills]], [[rulesync]], [[OpenSpec]]

- # Why doesn't [[Codex/CLI]] support slash commands?
	- ## Answer
		- [[My Answer]]
			- Codex has [deprecated what they called "custom prompts"](https://developers.openai.com/codex/custom-prompts) in favor of [[Agent/Skills]].
			- See [[Codex/GitHub/Issue/25/10 Look for custom prompts aka slash commands in project]]
		- [[AI/Response]]
			- **Short answer:** [[Codex/CLI]] **does** support slash commands for **built-in** session control (`/model`, `/permissions`, `/skills`, `/plan`, `/status`, and dozens more per [Slash commands in Codex CLI](https://developers.openai.com/codex/cli/slash-commands)). What it **does not** support (and OpenAI has removed) is **user-defined custom slash commands** like Claude Code's repo-local `.claude/commands/` or Rulesync-generated **native** `/command-name` workflows—the pattern many tools call "slash commands" in the agentic-coding ecosystem.
			- **What changed:** Older Codex builds let you add **custom prompts** as Markdown under `~/.codex/prompts/` and invoke them as `/prompts:<name>`. That path is **deprecated**; custom prompts were **removed starting in codex-cli 0.117.0** ([openai/codex#15941](https://github.com/openai/codex/issues/15941)). [Custom Prompts](https://developers.openai.com/codex/custom-prompts) now directs users to **skills** instead.
			- **OpenAI's stated direction:** Maintainers describe **skills as a superset** of what custom slash commands did—reusable instructions, repo-shareable under `.agents/skills/` (and related discovery paths), explicit invocation via `/skills` or `$skill-name` in the composer, and optional implicit use when enabled. They have **no current plans to restore** file-based custom slash commands ([openai/codex#22674](https://github.com/openai/codex/issues/22674)).
			- **Why the ecosystem says "Codex doesn't support slash commands":** Tools such as [[Claude Code]], [[CursorAI]], and [[rulesync]] treat **commands** as first-class generated artifacts (e.g. `.rulesync/commands/*.md` → real `/slash` entries). Rulesync's matrix marks **Codex CLI commands** as **simulated only** (🌏): for `codexcli`, use **`rulesync generate … --simulate-commands`** and invoke `s/your-command` in the prompt, or—preferably—generate **skills** (`--features skills`) and use Codex's `/skills` menu and `$skill` mentions ([Rulesync simulated features](https://github.com/dyoshikawa/rulesync/blob/main/.rulesync/skills/rulesync/simulated-features.md) in this repo).
			- **Practical substitutes in Codex:**
				- **Skills** — project or user skills; enabled skills show in the slash popup; invoke with `/skills` or `$skill-name` ([Codex skills](https://developers.openai.com/codex/skills)).
				- **Persistent instructions** — `AGENTS.md`, `config.toml` rules, and `/init` scaffolding.
				- **Built-in slash UX** — session steering (`/model`, `/permissions`, `/compact`, etc.) remains; it is not the same as shipping OpenSpec-style `/opsx:*` command packs.
			- **OpenSpec / multi-tool configs:** When a workflow installer offers "skills + commands," choose **skills only** for Codex (or **both** where Claude/Cursor get real commands and Codex gets the skill half). That matches OpenAI's removal of custom prompts and avoids expecting `/opsx:…` to exist natively in the Codex TUI.
			- Sources:
				- [Slash commands in Codex CLI](https://developers.openai.com/codex/cli/slash-commands) (built-in commands)
				- [Custom Prompts – Codex](https://developers.openai.com/codex/custom-prompts) (deprecated; migrate to skills)
				- [openai/codex#15941](https://github.com/openai/codex/issues/15941) (removal in 0.117.0)
				- [openai/codex#22674](https://github.com/openai/codex/issues/22674) (no plans to restore custom slash commands)