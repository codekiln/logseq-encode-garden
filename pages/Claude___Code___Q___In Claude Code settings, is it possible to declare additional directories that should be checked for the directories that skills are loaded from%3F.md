tags:: [[Claude/Code]], [[Q]]
alias:: [[Anthropic/App/Claude Code/Q/In Claude Code settings, is it possible to declare additional directories that should be checked for the directories that skills are loaded from]]
logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Claude/Code/Settings]], [[Claude/Code/Skill]], [[Agent/Skills/Dir]]

- # In [[Claude/Code]] settings, is it possible to declare additional directories that should be checked for the directories that skills are loaded from?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** There is **no** `settings.json` key that points Claude Code at arbitrary extra skill roots (for example a custom path like `~/my-skills`). Discovery is fixed to known layouts (`~/.claude/skills/`, project `.claude/skills/`, parent/nested project trees, plugins, enterprise). The closest settings-based knob is **`permissions.additionalDirectories`**, but that grants **file access only** and **does not** load skills from `.claude/skills/` inside those paths — unlike **`--add-dir`** / **`/add-dir`**, which **do** load skills when the added tree contains `.claude/skills/`.
			- **Built-in discovery (no extra setting):**
				- **Personal:** `~/.claude/skills/<skill-name>/SKILL.md` (all projects).
				- **Project:** `.claude/skills/<skill-name>/SKILL.md` in the starting directory, every **parent** up to the git/repo root, and **nested** `.claude/skills/` under subdirectories you work in (monorepos).
				- **Plugins / enterprise:** plugin `skills/` trees and managed settings (see [Extend Claude with skills](https://code.claude.com/docs/en/skills)).
			- **`permissions.additionalDirectories` in settings:** Documented on [Claude Code settings](https://code.claude.com/docs/en/settings) as extra working directories. The skills guide explicitly states this setting **does not** trigger skill discovery; only **`--add-dir`** and **`/add-dir`** load `.claude/skills/` from added paths ([Skills from additional directories](https://code.claude.com/docs/en/skills#skills-from-additional-directories)). Other `.claude/` config (subagents, commands, output styles) is also not discovered from `additionalDirectories`.
			- **Practical workarounds:**
				- Put shared skills under **`~/.claude/skills/`** or symlink skill folders there.
				- Use **`claude --add-dir /path/to/repo`** (or **`/add-dir`** in-session) when skills live in another checkout that has `.claude/skills/`.
				- Start Claude from the project root (or a parent) so ancestor `.claude/skills/` directories are picked up automatically.
			- **Cross-client note:** The Agent Skills spec recommends clients also scan **`.agents/skills/`** for interoperability ([[Agent/Skills/Dir]]); Claude Code’s primary native paths remain **`.claude/skills/`** per the official docs above.
