# Checklist: Rulesync skill with progressive disclosure

## Before writing

- [ ] **Problem**: What single class of user requests should trigger this skill?
- [ ] **Level 1**: Draft `description` first; can a stranger agent say yes/no without reading the body?
- [ ] **Level 2**: What is the minimum sequence that completes 80% of tasks?
- [ ] **Level 3**: What belongs in `references/` or `scripts/` instead of the body?

## While writing `SKILL.md`

- [ ] YAML has no long prose, duplicated docs, or reference tables.
- [ ] Body opens with the shortest working path; edge cases point to `references/`.
- [ ] Every `references/*.md` file is linked from the body with a **when to read** cue.
- [ ] Scripts have a stated contract: command, cwd assumptions, expected output.

## Token discipline pass

- [ ] Remove text the base model already knows unless it is safety- or repo-specific.
- [ ] No essential step exists **only** in a bundled file unless the body says when to load it.
- [ ] Large command catalogs or API dumps live in `references/`, not in the body.

## Troubleshooting

| Symptom | Likely fix |
|--------|------------|
| Skill rarely triggers | Add concrete triggers and examples to `description`; narrow or broaden scope explicitly. |
| Agents load too much | Move sections to `references/`; split topics; shorten body to a workflow index. |
| Duplication across skills | Shared content belongs in a rule, command, or one shared reference linked from several skills. |
| Generate does not update tool skills | Add `"skills"` to `features` in `rulesync.jsonc` and run `rulesync generate` for your targets. |

## Optional: Logseq garden mirror

In the logseq-encode-garden graph, the same authoring ideas are summarized as a Diataxis how-to page titled **rulesync/How To/Write Skills With Progressive Disclosure** (filesystem: `rulesync___How To___Write Skills With Progressive Disclosure.md`). Use that page for human-oriented narrative; this skill stays repo-local for agents.
