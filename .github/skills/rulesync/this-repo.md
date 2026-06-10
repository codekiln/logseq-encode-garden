# How this repo uses Rulesync

This garden uses Rulesync to manage AI coding tool configurations: rules, commands, subagents, skills, MCP config, and ignore files — kept consistent and in version control.

## How it is used here

- **Configuration**: `rulesync.jsonc` sets the project targets (`copilot`, `cursor`, `claudecode`, `codexcli`) and features (`rules`, `ignore`, `commands`, `subagents`, `skills`). `delete: true` lets generate remove orphaned outputs for those targets.
- **Rules**: minimal rule files in `.rulesync/rules/` with kebab-case names and category prefixes (`logseq-*`, `git-*`, `rulesync-*`). The always-on core is intentionally small (`overview`, `logseq-core`); task-specific guidance lives in skills.
- **Commands**: reusable slash commands in `.rulesync/commands/`.
- **Subagents**: specialized subagents in `.rulesync/subagents/`.
- **Skills**: progressive-disclosure skills in `.rulesync/skills/<name>/` (SKILL.md + references/ + scripts/).
- **Generate**: `npx rulesync generate` (honor `rulesync.jsonc`; do not pass extra `--targets`, which would pollute the tree with configs for non-configured tools).
- **Commit**: commit both `.rulesync/` sources and the tracked generated files.

## Canonical sources vs generated outputs (binding)

- Edit **only** `.rulesync/` for rules/commands/skills/subagents/config. **Never** hand-edit tool outputs that `rulesync generate` writes (`.claude/`, `.cursor/`, `.github/`, `.codex/`) — regenerate from the repo root after source changes.

## Commands

```bash
# Initialize
npx rulesync init

# Import from existing tools (all features)
npx rulesync import --targets claudecode --features rules,mcp,commands,subagents

# Generate using rulesync.jsonc (all features)
npx rulesync generate
```

## Repository access

- **Local repository**: `~/GitHub/others/forks/rulesync`
- **GitHub repository**: https://github.com/dyoshikawa/rulesync

For human-oriented detail, see `pages/My___Dev___Tool___Pref___AI___Coding___Config___Management.md`.
