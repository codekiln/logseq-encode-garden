alias:: [[Claude Code Skills]]
see-also:: [[Codex/Skill]], [[Agent/Skills]]

- # Claude Code Skill
	- A [[Claude/Code]] skill is a `SKILL.md` file inside a named directory that extends what Claude can do, either through explicit invocation (`/skill-name`) or automatic discovery when relevant.
	- ## Command merger (2026)
		- [[Claude/Code]] merged custom commands into skills. A file at `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both create `/deploy` and work identically.
		- `.claude/commands/` files continue to work, but skills are the recommended format — they support supporting files, frontmatter invocation control, and automatic discovery by Claude.
		- This parallels [[Codex/CLI]] deprecating custom prompts in favor of [[Agent/Skills]] in codex-cli 0.117.0. See [[Codex/CLI/Q/Why doesn't CodexCLI support slash commands?]]
	- ## Open standard
		- Claude Code skills follow the [[Agent/Skills]] open standard ([agentskills.io](https://agentskills.io)), which works across multiple AI tools including [[Codex/CLI]].
		- Claude Code extends the standard with invocation control, subagent execution, and dynamic context injection.
	- ## Structure
		- ~~~
		  skill-name/
		  ├── SKILL.md        # required entrypoint
		  ├── reference.md    # optional supporting docs
		  └── scripts/
		      └── helper.sh   # optional scripts
		  ~~~
		- Each skill directory goes under a scope path; the directory name becomes the `/command`.
	- ## Scope levels
		- | Level | Path | Applies to |
		  | ---- | ---- | ---- |
		  | Personal | `~/.claude/skills/<name>/SKILL.md` | All projects |
		  | Project | `.claude/skills/<name>/SKILL.md` | This project only |
		  | Plugin | `<plugin>/skills/<name>/SKILL.md` | Where plugin is enabled |
	- ## Key frontmatter fields
		- | Field | Purpose |
		  | ---- | ---- |
		  | `description` | What the skill does; Claude uses this for auto-discovery |
		  | `when_to_use` | Additional trigger phrases appended to `description` |
		  | `disable-model-invocation` | `true` = only you can invoke (deploy, commit, etc.) |
		  | `user-invocable` | `false` = only Claude can invoke (background knowledge) |
		  | `allowed-tools` | Tools Claude can use without per-use approval when skill is active |
		  | `context` | `fork` = run in an isolated subagent |
		  | `agent` | Which subagent type to use when `context: fork` is set |
		  | `argument-hint` | Hint shown during autocomplete, e.g. `[issue-number]` |
		  | `paths` | Glob patterns that limit when skill auto-activates |
		  | `model` | Model override for the duration of the skill |
	- ## Dynamic context injection
		- Use `` !`command` `` in skill content to run shell commands before Claude sees the prompt — output replaces the placeholder inline.
		- Multi-line variant: fenced block opened with ` ```! `.
	- ## Invocation control summary
		- | Frontmatter | You can invoke | Claude can invoke |
		  | ---- | ---- | ---- |
		  | (default) | Yes | Yes |
		  | `disable-model-invocation: true` | Yes | No |
		  | `user-invocable: false` | No | Yes |
	- ## Docs
		- [Extend Claude with skills – Claude Code](https://code.claude.com/docs/en/skills)
