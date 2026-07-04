---
name: readwise-skills-sync
description: >-
  Vendor and refresh the Readwise workflow skills (triage, quiz, book-review, …)
  from github.com/readwiseio/readwise-skills into this garden's .rulesync/skills/,
  then regenerate. Use when adding, updating, or auditing the vendored readwise
  skills, after upstream changes, or when bumping the rulesync version in mise.toml.
  Do not use the `readwise skills install` command or `rulesync import` for this.
targets: ["*"]
codexcli:
  short-description: Refresh the vendored Readwise skills in .rulesync/ and regenerate
---

# Readwise skills sync

The Readwise workflow skills are vendored into `.rulesync/skills/` from the upstream repo `github.com/readwiseio/readwise-skills` and compiled by rulesync like every other skill here. This skill fetches and refreshes them.

The decision to vendor (rather than use the vendor's own installer) is recorded on the garden page [[readwise-cli]]. In short: `readwise skills install` writes to user-global `~/.claude`, copies only each `SKILL.md` (dropping sibling scripts such as `build_graph.py`), and cannot exclude skills non-interactively; `rulesync import` round-trips through those user-global files and pulls in unrelated skills. Vendoring keeps the sources in-repo, project-scoped, and complete.

## What is vendored

- Every skill under the upstream `skills/` directory **except** `readwise-mcp` — this graph wires the `readwise` CLI (see [[readwise-cli]]), not the MCP server. The exclusion list is the `EXCLUDE` array in the sync script.
- Each skill's **full** directory, including sibling scripts (e.g. `highlight-graph/build_graph.py`), not just `SKILL.md`.
- `targets: ["*"]` is injected into each `SKILL.md` frontmatter — rulesync requires it and upstream omits it.

## Refresh

From the repo root:

~~~bash
mise exec -- bash .rulesync/skills/readwise-skills-sync/scripts/sync.sh
~~~

The script fetches each skill's files, injects the `targets` frontmatter, and runs `rulesync generate`. Review the diff (`git status --short .rulesync/skills .claude/skills .agents/skills`) before committing.

## When to run

- Upstream readwise skills change — a new skill appears or a `SKILL.md` is updated.
- Bumping the `rulesync` version in `mise.toml` — re-run and confirm the generated skills still validate against the new rulesync's skill schema (e.g. the `targets` frontmatter key is still accepted).

## Notes

- Vendored `SKILL.md` files are upstream copies with `targets` added — do not hand-edit them. Change behavior upstream, or adjust the sync script.
- To keep or drop a skill, edit `EXCLUDE` in `scripts/sync.sh`.
