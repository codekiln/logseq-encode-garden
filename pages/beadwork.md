logseq-entity:: [[Logseq/Entity/software-project]]
created-by:: [[Person/Jason Allum]]
tags:: [[Task/Management/Git-Friendly]]
alias:: [[Person/Jason Allum/GitHub/beadwork]]
via:: [[Claude Code/Reddit/26/02/Am I an idiot for using Beads]]

- # [jallum/beadwork](https://github.com/jallum/beadwork)
	- Git-native work management for humans and AI coding agents; plans, progress, and decisions live as files on an orphan branch instead of mixing into the main worktree.
	- [[My Notes]]
		- [design.md looks like what I've thought about building](https://github.com/jallum/beadwork/blob/main/docs/design.md)
			- > All data lives on a git orphan branch, manipulated directly in the object database via [go-git](https://github.com/go-git/go-git). Every operation is an atomic commit. Sync uses fetch-rebase-push with intent replay on conflict.
			- > For storage layout and sync mechanics, see [docs/design.md](https://github.com/jallum/beadwork/blob/main/docs/design.md).