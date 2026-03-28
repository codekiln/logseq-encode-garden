---
description: 'Session completion workflow: land the plane by pushing all changes'
---
# Landing the Plane (Session Completion)

When ending a work session, complete all steps below. Work is not complete until `git push` succeeds.

## Mandatory Workflow

1. File issues for remaining work.
2. Run quality gates if code changed (tests, lint, build as applicable).
3. Update issue status (close finished work, update in-progress work).
4. Verify Beads health before sync:
   ```bash
   bd doctor --agent
   ```
   Do not use `bd sync`; this repo's supported Beads flow is `bd doctor` plus Dolt push/pull once the backend is healthy.
5. Sync and push to remote:
   ```bash
   git pull --rebase
   DOLT_REMOTE_PASSWORD=$(gh auth token) bd dolt push
   git push
   git status
   ```
   `git status` must show the branch is up to date with origin.
6. Clean up git state (for example: stale stashes, pruned remotes).
7. Verify all local changes are committed and pushed.
8. Provide handoff context for the next session.

## Critical Rules

- Work is not complete until `git push` succeeds.
- Do not tell agents or humans to run `bd sync`; it is not supported in the current CLI.
- Never stop before pushing.
- Never say "ready to push when you are"; the agent must push.
- If push fails, resolve the problem and retry until it succeeds.
