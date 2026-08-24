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
		- **[[tmux/session]] — one seat.** Named `<agent>-<REPO>-YYYY-MM-DD-<day>-HHMM`, and the [[tmux]] session name and the `claude` session name are meant to be the same string. The repository code says which checkout, so `C-b w` answers what a seat is working on without opening it: `LEG` is this garden, `MK` the work knowledge vault, `GL` the langserve repo, `DF` [[My/Dotfiles]]. Sessions are what [[tmux/Option/status-left]] draws, which is why [[tmux/Option/status-left-length]] matters here.
			- **The scheme is volatile, so read it rather than quoting it.** Five forms inside one week, three of them on [[2026-08-24 Mon]] alone. A page that quotes a current session name is wrong within days, and a successor cannot tell a stale literal from a live one. `tmux display-message -p '#{session_name}'` names the session the running pane is in; `tmux list-sessions` names every session on the server, which is a different question. A name captured at session start — the one `ListAgents` reports — ages silently through a rename.
			- A rename leaves window and pane ids alone — `@0`, `%0` and the `window.pane` indices are unchanged across one — so anything addressed by id keeps working. **The old session name stops resolving the instant the rename lands**, with `has-session` returning `can't find session`, so it is only name-addressed targets that break, and they break immediately rather than drifting. That is the argument for reading the name live instead of caching it.
			- A `claude` session's own name cannot be changed while it runs, so after a seat's tmux session is renamed the two names disagree until the next [[My/AI/Agent/Fleet/Bed Down]] respawn, which derives the new one from the tmux name.
			- **No dots in a session name.** A `-t` target is parsed as `session:window.pane`, so a dot anywhere in the name is read as a separator and every bare target fails against a window or pane that does not exist — `has-session` included, which is what a script would use to check. `DF` rather than `.F` for the dotfiles code for this reason: [[tmux/Q/Why does a session name containing a dot break every bare -t target?]].
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
		- Browser-shaped work takes `claude --chrome` first and Playwright only when that is unavailable, one browser task at a time across the fleet — [[My/AI/Agent/Fleet/Browser]].
		- Absorb rather than relay. A question answerable by reading something is not an escalation; it reaches the human only when a person outside the fleet is waiting on it, or when it needs authority only the human has.
		- **Announce a permission request before [[Person/codekiln]] is asked for it.** A dialog or a login prompt must never be the first they hear of it — on screen it names none of what they need, so a seat sends four facts up: who is asking, what permission, what it serves, and what happens if they decline. Where a wall is foreseeable — an SSO login, an expired credential, a push wanting a credential the seat does not hold — send them before hitting it. Where a dialog fires unforeseen, send them the moment it fires. The standard is not that every dialog is predicted; it is that nothing stays quiet once it has happened.
			- The dotfiles seat keeps the fleet's pending-request list as the top section of its own display, above everything else, on the grounds that a permission request is the one class of item where the human is the only possible actor. An empty section is stated rather than deleted, so that its absence cannot read as an oversight.
		- **Prefer the answer that needs no grant, and never take a standing grant to serve one narrow lookup.** A grant is not scoped to the query that motivated it: control of System Events given to the terminal application is given to every process that ever runs inside it, which on one machine is every seat in the fleet, for as long as the grant lasts. A read-only question about which applications are running is not worth that. Nor does a seat request a grant on another seat's behalf.
		- Durable opinions go in the garden, not hardcoded into a repository, which is why this page is here and not in [[My/Dotfiles]].
		- Write so that [[Person/codekiln]] never has to resolve a reference — name the thing again rather than pointing back at it, and never let a count stand in for the facts it counts: [[My/Pref/Writing/Never make the reader resolve a reference]].
		- Deliverables go on tracked paths, and **whether `tmp/` is one of them is a fact about the repository rather than about the fleet.** Check it per checkout with `git check-ignore`; do not carry the answer between repos.
			- Where `tmp/` is ignored, a secret scan that skips ignored paths is bypassed entirely by `git add -f` on a `tmp/` file.
			- Where it is not, there is no bypass and no privacy either: in this garden `.gitignore` carries no `tmp` rule, three notes under `tmp/` are tracked, and anything written there is published. Scan a working note for credential-shaped strings before committing it.
		- Fetch before trusting an ahead-behind count against a repository another seat also pushes to — [[git/Q/Does an ahead-behind count against origin reflect the remote's current state?]].
