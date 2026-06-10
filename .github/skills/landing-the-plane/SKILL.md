---
name: landing-the-plane
description: >-
  Complete an end-of-session checkout for this repo: file issues for remaining
  work, run quality gates if code changed, sync and push to remote, clean up git
  state, and hand off context. Use when the user says "land the plane", "wrap
  up", "finish the session", or asks to make sure everything is committed and
  pushed. Work is not done until `git push` succeeds.
---
# Landing the plane

When ending a work session, complete all steps. **Work is not complete until `git push` succeeds.**

## Mandatory workflow

1. File issues for remaining work.
2. Run quality gates if code changed (tests, lint, build as applicable).
3. Update issue status (close finished work, update in-progress work).
4. Sync and push to remote:
   ```bash
   git pull --rebase
   git push
   git status
   ```
   `git status` must show the branch is up to date with origin.
5. Clean up git state (e.g. stale stashes, pruned remotes).
6. Verify all local changes are committed and pushed.
7. Provide handoff context for the next session.

## Critical rules

- Work is not complete until `git push` succeeds.
- Never stop before pushing.
- Never say "ready to push when you are" — push.
- If push fails, resolve the problem and retry until it succeeds.
