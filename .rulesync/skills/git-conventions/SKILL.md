---
name: git-conventions
description: >-
  Apply this repo's git conventions when staging and committing: use targeted
  `git add` (never `git add -A`), group changes logically, and write
  conventional commit messages (type: description, imperative mood). Use when
  the user asks to commit, stage, or write a commit message in this repo. Do not
  use for branch/PR review workflows.
targets: ["*"]
codexcli:
  short-description: Targeted git add + conventional commit messages for this repo
---

# Git conventions

## Staging

- Always use **targeted** `git add <paths>` then commit. **Do not** use `git add -A`.
  - Assume the working directory may contain things the user does not want committed.
  - Use `git status` and group changes together logically.
- If the user asks you to commit, commit your changes. If there are unrelated changes, notify the engineer that you didn't commit those (but don't ask approval to proceed with the targeted commit) unless there's a genuine merge conflict serious enough to require attention.

## Commit messages

Conventional format — `<type>: <description>` in imperative present tense ("add feature", not "added feature"), first line ≤ 50 chars.

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`, `ci`.

For full details (body/footer format, emoji prefixes, ticket-reference rules, non-ticket repos like this one), read [references/commit-conventions.md](./references/commit-conventions.md).
