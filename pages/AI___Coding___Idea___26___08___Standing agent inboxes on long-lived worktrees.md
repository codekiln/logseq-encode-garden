tags:: [[Idea]]
date-created:: [[2026-08-13 Thu]]

- # Standing agent inboxes on long-lived [[git/worktree]]s
	- Instead of creating a worktree per task, keep a small set of **named, long-lived agents**, each owning one persistent worktree. The worktree becomes an inbox: send it a task, it works, it parks. Prompted by daily use of [[herdr]].
	- ## What [[herdr]] already supplies
		- Agents are addressable by a chosen name rather than only a pane ID — `herdr agent start|prompt|wait|rename <name>`.
		- Worktrees are first-class: `herdr worktree create|open|list|remove`, and worktree workspaces pack under their parent in the sidebar. That packing is per-repository and not settable, so an agent whose worktrees span several repos gets one group per repo rather than one under itself — [[herdr/Explanation/Where a Workspace Appears in the Sidebar]].
		- A name is unique only among *live* agents, and clears when that agent exits, is released, or is replaced. The durable identity is therefore the worktree workspace; the name is a label re-applied on `agent start`.
	- ## Why the worktree, not the branch, is the unit
		- A branch can be checked out in at most one worktree at a time — a per-branch lock, not a per-worktree pin. A standing worktree can cycle through branches indefinitely. Mechanics on [[git/worktree]].
		- Resting state between tasks: detached at `origin/main`. Clean tree, no branch held, nothing for another worktree to collide with.
		- Accepting a task never requires `main` to be checked out. `git switch -c task-N origin/main` uses it as a start point, which the lock does not restrict, so a standing agent never contends with the primary checkout.
	- ## What is actually saved
		- Not `git worktree add` — that is milliseconds.
		- Untracked and ignored files survive branch switches: `.env`, `node_modules/`, build caches, language-server indexes. That is the real prize, and it means the repos worth a standing agent are the ones with expensive setup, not the ones touched most often.
		- The agent's accumulated context, but only where the agent's identity is a **domain** (`docs`, `garden`, `frontend`) rather than a task queue. Across unrelated tasks the context has to be cleared between them, leaving only the environment saving.
	- ## Open questions
		- Queue discipline: an inbox implies tasks can arrive faster than they finish, but the worktree is one mutable checkout. Work has to be landed or parked before the next task is accepted.
		- The stash is repo-global rather than per-worktree, so several standing agents parking via stash share one stack — [[git/worktree/Q/How does git stash interact with git worktrees]].
		- Directory naming stops following the branch once a worktree outlives it — [[My/Pref/Dev/Tool/git/Worktree]].
