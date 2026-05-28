logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Jason Allum]]
tags:: [[Task/Management/Git-Friendly]]
alias:: [[Person/Jason Allum/GitHub/beadwork]]
via:: [[Claude/Code/Reddit/26/02/Am I an idiot for using Beads]]

- # [jallum/beadwork](https://github.com/jallum/beadwork)
	- [[CLI/Tool]] that implements a git-backed issue tracker for AI agents.
	- ## [[Data/Model]]
		- plans, progress, and decisions live as files on an orphan branch instead of mixing into the main worktree.
	- ## [[My Notes]]
		- [design.md looks like what I've thought about building](https://github.com/jallum/beadwork/blob/main/docs/design.md)
			- > All data lives on a git orphan branch, manipulated directly in the object database via [go-git](https://github.com/go-git/go-git). Every operation is an atomic commit. Sync uses fetch-rebase-push with intent replay on conflict.
			- > For storage layout and sync mechanics, see [docs/design.md](https://github.com/jallum/beadwork/blob/main/docs/design.md).
		- ~44 [[Github/Star]]s as of [[2026-05-26 Tue]]
		- includes [[Self/Update]] - To update an existing install: `bw upgrade`.
	- ## [[CLI commands]]
		- ```
		  bw init                                           # initialize in any git repo
		  bw onboard                                        # print bootstrap snippet for CLAUDE.md / GEMINI.md
		  bw create "Fix auth bug" --type bug -p 1          # create an issue
		  bw ready                                          # list unblocked work
		  bw comment bw-a1b2 "Fixed in latest deploy"       # add a comment
		  bw close bw-a1b2                                  # close it
		  bw sync                                           # push to remote
		  ```
	- ## Features
		- Dependencies - see `bw dep`
	- ## [[Engineering Choices]]
		- written in [[Go]]; see [source for bw executable here](https://github.com/jallum/beadwork/tree/main/cmd/bw)
	- ## [[Installation]]
		- ### Getting the [[Executable]]
			- #### [[GitHub/Release]] [jallum/beadwork/releases](https://github.com/jallum/beadwork/releases/latest)
				- ##### Installing globally with [[mise]]
					- `mise use -g jallum/beadwork`
			- #### [[Installer]] script
				- `curl -fsSL https://raw.githubusercontent.com/jallum/beadwork/main/install.sh | sh`
		- ### [[AI/Agent/Setup]] [here](https://github.com/jallum/beadwork/tree/main#agent-integration)
			- > `bw onboard` prints a snippet for your project's agent instructions file (CLAUDE.md, GEMINI.md, etc.). Once installed, agents automatically load workflow context via `bw prime` at the start of each session.