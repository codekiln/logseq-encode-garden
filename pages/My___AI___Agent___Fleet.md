tags:: [[Diataxis/Explanation]]
see-also:: [[My/AI/Agent/Chief of Staff]], [[tmux]], [[herdr]], [[Terminal/Multiplexer]]

- # Fleet
	- The set of AI agent seats [[Person/codekiln]] runs at once, and the harness that holds them. A seat is a standing role — a chief over one repository, a director over a group of them — and it outlives whichever session is sitting in it, the way [[My/AI/Agent/Chief of Staff]] describes for Hayward.
	- Since [[2026/08/24]] the harness is [[tmux]]. [[herdr]] is retired: its server was stopped that morning and its ~24 orphaned sessions killed.
	- ## What tmux gives that herdr did not
		- What [[herdr]] offered was agent-state detection on the pane border — blocked, working, done — read off screen patterns. What it could not offer was depth. A workspace held panes, and the agent name carried the whole address in 32 characters, so `<workspace-label>-<tab-label>` had to encode both the repo and the work item inside that budget.
		- [[tmux]] gives five nested levels instead of two, each one named separately and none of them competing for the same 32 characters. The hierarchy *is* the address, so no single name has to carry it.
		- One keystroke reads the whole thing back. `C-b w` opens [[tmux/Command/choose-tree]] in [[tmux/Mode/Tree]] — see [[tmux/session/Picker]] for what the picker's own keys do.
	- ## The five levels
		- **[[tmux/session]] — one seat.** Named `<seat>-<date>`: `hayward-2026-08-24`, `seneschal-2026-08-24`. The seat name says which role, the date says which day's run, and both survive a respawned pane. Sessions are what [[tmux/Option/status-left]] draws, which is why [[tmux/Option/status-left-length]] matters here.
		- **[[tmux/Window]] — one worker task.** Named for the task, never for the agent doing it. The window list is the seat's docket, and `tmux list-windows` reads it back. A window closes when its item is done; a window left open reports work in flight that is not.
		- **[[tmux/Pane]] — chat left, viewer right.** The right pane is `nvim` on the document being edited, or `gh dash` on a review queue. Created at 45% width:
			- ~~~sh
			  tmux split-window -h -p 45 -t '=<session>:<window>' 'nvim <file>'
			  ~~~
			- Quote every `-t` argument. A bare `=word` is a zsh expansion, not a tmux exact-match target — see [[tmux/Q/Why does a tmux -t =session target fail in zsh?]].
		- **The named `claude` session — one context window.** `claude -n '<name>'` records the name in the session's own transcript, which is how a session is addressed for messaging and how its context size is read without spending model tokens. See [[My/AI/Agent/Fleet/Bed Down]].
		- **The branch and [[git/worktree]] — where the work lands.** The bottom level is what makes two windows able to edit the same repository at once. `git stash` is the exception that ignores the boundary: the stash is repo-global across every worktree, so it is never used in a shared checkout.
	- ## Spawning a worker
		- One worker is one window in the spawning seat's own session, and it reads its brief from a file:
			- ~~~sh
			  tmux new-window -d -t '=<your-session>' -n '<task-name>' \
			    "claude -n '<prefix> <task-name>' --permission-mode auto \
			     'Read <brief-path> in full right now, before anything else. It is your brief. Then carry it out.'"
			  ~~~
		- **The brief goes by path, never interpolated into the command.** Content inlined into a double-quoted shell string has its backticked terms executed and silently replaced, which deletes exactly the measurements a brief exists to carry.
	- ## What the fleet expects of a seat
		- Bed down at 200k tokens rather than letting a session balloon — [[My/AI/Agent/Fleet/Bed Down]].
		- Browser work runs in the human's own Chrome profile, one task at a time across the fleet — [[My/AI/Agent/Fleet/Browser]].
		- Absorb rather than relay. A question answerable by reading something is not an escalation; it reaches the human only when a person outside the fleet is waiting on it, or when it needs authority only the human has.
		- Durable opinions go in the garden, not hardcoded into a repository, which is why this page is here and not in [[My/Dotfiles]].
		- Deliverables go on tracked paths. `tmp/` is gitignored, and a secret scan that skips ignored paths is bypassed entirely by `git add -f` on a `tmp/` file.
		- Fetch before trusting an ahead-behind count against a repository another seat also pushes to — [[git/Q/Does an ahead-behind count against origin reflect the remote's current state?]].
