# [How I use git worktrees](https://notes.billmill.org/blog/2024/03/How_I_use_git_worktrees.html) - [[git/worktree]]
	- Bill Mill explains how to use Git worktrees to manage multiple branches in separate directories, making context switching and parallel development easier.
	- The default Git UI for worktrees is not very ergonomic, so Bill shares a Bash utility script that streamlines worktree management.
	- **Key trick:** The script checks for a `node_modules` folder and, if present, duplicates it to the new worktree directory using copy-on-write. This saves time by avoiding repeated `npm install` runs.
	- [Original blog post](https://notes.billmill.org/blog/2024/03/How_I_use_git_worktrees.html)
	- [Bill Mill's website](https://billmill.org) 