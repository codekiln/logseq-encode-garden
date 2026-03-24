---
name: rulesync-create-skill
description: >-
  Create or refactor a Rulesync skill under .rulesync/skills/<skill-name>/ using
  progressive disclosure: small YAML for discovery, a lean SKILL.md body, and
  optional references/ and scripts/ loaded only when needed. Use when the user
  asks for a new skill, wants an oversized SKILL.md split up, or should align a
  skill with staged-loading practices for AI agents.
targets: ["*"]
---

# Rulesync: create a progressive-disclosure skill

## When this applies

Use this skill for **authoring or restructuring** `.rulesync/skills/<skill-name>/`, not for learning the Rulesync CLI. For CLI reference, use the `rulesync` documentation skill or [file-formats.md](../rulesync/file-formats.md#rulesyncskillsskillmd) in this repo.

## Quick start

1. Pick a **kebab-case** directory name under `.rulesync/skills/<skill-name>/` (match the skill’s `name` in frontmatter when practical).
2. Add `SKILL.md` with YAML containing at least `name`, `description`, and `targets` (see [file-formats.md](../rulesync/file-formats.md#rulesyncskillsskillmd) for tool-specific keys such as `claudecode.allowed-tools` or `codexcli.short-description`).
3. Write `description` so another agent can decide **from that field alone** whether to load the skill: what it does, **when** to use it (verbs, tools, file types, user intents). Do not put tutorials or long tables in YAML.
4. In the markdown **body**, put only the **shortest happy path** and guardrails. Link to `./references/...` for depth; use `./scripts/` for repeatable automation (invoke via shell; prefer trusting stdout over pasting full source).
5. Before finishing, run the checklist in [references/checklist.md](./references/checklist.md).

## Deeper material (load on demand)

- [references/layers.md](./references/layers.md) — map progressive disclosure levels to Rulesync layout and Rulesync-specific notes.
- [references/checklist.md](./references/checklist.md) — design review, token discipline, troubleshooting.

## After files exist

If this project uses `rulesync generate`, ensure `rulesync.jsonc` includes `"skills"` in `features`, then run generate for your targets so tool-specific skill outputs stay in sync.
