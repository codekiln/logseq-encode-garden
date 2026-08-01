logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[Claude Code/Plugin]], [[Claude Code/Plugin/Marketplace]], [[Claude Code Skills]]

- # Skills-Directory Plugin
	- ## Overview
		- A **skills-directory plugin** is an ordinary [[Claude Code/Plugin]] that Claude Code finds because it sits inside a *skills directory* — `~/.claude/skills/` or a project's `.claude/skills/`. One file flips a plain skill folder into a plugin: any folder there that holds a `.claude-plugin/plugin.json` manifest loads as a plugin named `<name>@skills-dir` on the next session, with no marketplace and no install step.
		- The `@skills-dir` suffix is the plugin's source label, the slot where a marketplace name would otherwise go. Claude Code reads such a plugin from where it lives; a [[Claude Code/Plugin/Marketplace]] install instead copies the plugin into the cache at `~/.claude/plugins/cache`. Discovery in place is what lets you edit the files directly and have the graph pick them up.
	- ## What a skills directory can hold
		- The same folder tree carries three different things, told apart by whether a `plugin.json` manifest is present.
		- | What you have | What it is |
		  | --- | --- |
		  | `<skills-dir>/foo/SKILL.md`, no manifest | A plain skill named `foo` |
		  | `<skills-dir>/foo/.claude-plugin/plugin.json` | A plugin `foo@skills-dir`, which can bundle its own skills, agents, hooks, and more |
		  | `<plugin>/skills/bar/SKILL.md` | A skill `bar` packaged inside a plugin |
		- So "skills-directory plugin" names only the middle row: a manifest sitting inside a skills directory. The first row is still just a skill; the third is a skill living inside some other plugin.
	- ## Where it loads from
		- The directory you put it in sets its scope and its trust requirements.
		- | Skills directory | Scope | Loads |
		  | --- | --- | --- |
		  | `~/.claude/skills/` | personal | In every project, since the location is yours alone |
		  | `<cwd>/.claude/skills/` | project | Only after you accept the workspace trust dialog for that folder |
		- A personal-scope plugin runs with no extra restrictions.
		- A project-scope plugin is checked into the repository and reaches everyone who clones it. Because that content arrives from the repo rather than from you, it loads only behind the same trust gate that governs `.claude/settings.json`, and the parts that run code are held back further:
			- MCP servers it declares go through the same per-server approval as a project `.mcp.json`.
			- LSP servers start only after you trust the workspace.
			- Background monitors stay off.
		- A project-scope `@skills-dir` plugin loads only from the `.claude/skills/` of the exact directory where you launch Claude Code. Plain skills and commands search upward to the repository root; this plugin type stays put, so launching from a subdirectory misses one that lives at the repo root. Launch from the repository root, or run `/reload-plugins` after changing directories.
	- ## Editing, reloading, disabling
		- Editing a skill's `SKILL.md` takes effect right away in the running session.
		- The plugin's other components — `hooks/`, `.mcp.json`, `agents/`, `output-styles/` — wait for a `/reload-plugins` or a restart to be picked up.
		- To stop loading one, delete its folder or disable it by name. There is no uninstall step, since nothing was installed from a marketplace.
		- ~~~bash
		  claude plugin disable my-tool@skills-dir
		  ~~~
	- ## Scaffolding one
		- `claude plugin init <name>` writes a starter plugin to `~/.claude/skills/<name>/`. On the next session it loads as `<name>@skills-dir` and appears in `/plugin` and `claude plugin list`.
	- ## References
		- [Plugins reference — Skills-directory plugins](https://code.claude.com/docs/en/plugins-reference#skills-directory-plugins)
