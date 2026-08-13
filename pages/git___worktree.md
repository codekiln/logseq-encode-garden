alias:: [[Git Worktrees]]

- # [[git]] worktree
	- ## Branch checkout is a per-branch lock, not a per-worktree pin
		- A worktree is a working directory with its own `HEAD` and index; `git switch` inside it behaves as in an ordinary clone. A worktree is not pinned to the branch it was created on.
		- The constraint runs the other way: a branch can be checked out in at most one worktree at a time. Switching to a branch another worktree holds fails with `fatal: '<branch>' is already used by worktree at <path>`.
		- Exempt from the lock
			- detached HEAD — `git switch --detach main` succeeds even while another worktree holds `main`
			- start points — `git switch -c task main` creates a branch *from* `main` without checking it out, so the lock never applies
		- Escape hatches when the lock is genuinely in the way: `git checkout --ignore-other-worktrees`, and `git worktree add --force`.
		- `git worktree list` reports the branch each worktree currently holds.
	- ## What crosses a branch switch
		- Untracked and ignored files stay in place: `.env`, `node_modules/`, build and test caches, language-server indexes. This is what makes reusing a worktree cheaper than creating a fresh one.
		- The stash is repo-global rather than per-worktree — [[git/worktree/Q/How does git stash interact with git worktrees]].
	- ## In this graph
		- Naming and placement: [[My/Pref/Dev/Tool/git/Worktree]].
		- A worktree kept alive across many branches as an agent inbox: [[AI/Coding/Idea/26/08/Standing agent inboxes on long-lived worktrees]].
