tags:: [[Idea]]
date-created:: [[2026-03-25 Wed]]

- # Proto Session — [[2026-03-25 Wed]] — AI Terminal Coach (zsh × tmux × garden search)
	- Continues [[Learning/Idea/26/03/Terminal toolbelt learning and Readwise-like CLI/Proto Session/26/03/21 Sat]]: short coach turns, user runs commands first, coach reacts to paste or pane capture where applicable.
	- ## [[2026-03-25 Wed]] — Focus for this session
		- **Problem thread (user-owned wording):** After dotfiles / `~/.zshrc` changes, want **fresh zsh context across many tmux panes** without disturbing panes where a **foreground TUI or agent** (e.g. lazygit, cursor-agent) is running.
		- **Skill thread:** Build **CLI habit** for answering “did I already write this down?” against this repo (`pages/`, `journals/`) — **coach does not pre-search the garden for the user** on this thread unless the user pastes hits.
		- **Open loop carried from Sat:** Prior note about tmux + zsh refresh may exist as a **`___Q___` question page**; user to **rediscover via `rg`**, not via coach retrieval.
	- ## [[2026-03-25 Wed]] — Coach prompts issued (answers withheld here)
		- **Constraint clarification:** Separate three ideas in your own words: (1) *new login shell*, (2) *re-reading config in an existing interactive shell*, (3) *doing something tmux-scoped to a pane*. Which of these **must not** disturb the **current foreground process** in a pane?
		- **Observation drill:** In one disposable pane, start a long-running foreground program you do not care about, then ask yourself what happens if you send **Enter** vs **a newline from a script** vs **`source`** — **without** looking up the answer until you have a hypothesis.
		- **`tmux` doc habit:** Pick **one** of: `man tmux` in a **pinned pane** (Sat pattern), or `tmux list-commands` / `tmux list-keys` as a **table of contents**. Find how to learn **send-keys / command mode / targets** on your own — goal is **repeatable lookup path**, not a one-liner to memorize.
		- **Garden search ladder (repo root):**
			- 1. **`rg` scope:** Restrict to `pages/` and `journals/` so assets and tooling noise stay out — write the two path arguments you will always use.
			- 2. **Question pages:** Your graph often encodes “I had a question” as filenames containing a **`___Q___` segment** (see Sat session). Craft an **`rg` invocation** that lists **only filenames** matching both **`tmux`** (or **`zsh`**) and that segment — *you* run it and paste top lines if you want coach feedback on flags.
			- 3. **Narrowing:** When a file list is too wide, switch from “search file names” to “search contents” in a **small** subset — decide the **smallest** second step (e.g. one file, or one subdirectory pattern) before widening again.
		- **Safety / privacy:** If using `tmux capture-pane` to show coach state, scrub secrets; same contract as Sat for “learning mode” logging.
	- ## [[2026-03-25 Wed]] — Session outcomes (fill as you go)
		- *Add what worked, what failed, and the exact commands you want to reuse — after you run them.*
