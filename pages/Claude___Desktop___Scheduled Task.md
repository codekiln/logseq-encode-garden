tags:: [[Claude/Desktop]], [[Claude/Code]], [[Diataxis/Explanation]], [[AI/Automation]]
see-also:: [[Claude/Routine]], [[Claude/Code/Q/What is the difference between the schedule command in Claude Code CLI and Routines in Claude Desktop's Code tab?]]

- # [Schedule recurring tasks in Claude Code Desktop](https://code.claude.com/docs/en/desktop-scheduled-tasks)
	- ## Overview
		- A **Desktop scheduled task** is a **Local routine**: created from [[Claude/Desktop]]'s **Routines** sidebar page → **New routine** → **Local**. It runs **on the user's machine** with direct access to local files and tools, starting a **new session automatically** at a chosen time/frequency.
		- It only fires while **Desktop is open** and the **computer is awake**—the opposite tradeoff from a cloud [[Claude/Routine]] (Anthropic-managed infrastructure, works even with the machine off, but no local file access).
		- The Desktop **Routines** page is the shared UI for both kinds: choosing **Local** creates a scheduled task (this page); choosing **Cloud** creates a [[Claude/Routine]].
	- ## Distinguishing from `/loop`
		- **Desktop scheduled task ≠ `/loop`**, even though both run on the local machine. The difference is **whether a session must already be open**:
			- A **scheduled task** starts a **brand-new session by itself** at the scheduled time—no session needs to be open beforehand. It survives app restarts because it's saved to disk.
			- **`/loop`** only keeps **an already-open session** repeating a prompt on an interval; it does not create new sessions and stops the moment that session closes.
		- **`/loop` is not CLI-only.** Since [[Claude/Desktop/Code]] is "basically [[Claude/Code]] but inside the desktop app," `/loop` works the same way inside a Desktop **Code tab** session as it does in a terminal—it is a **property of the session**, not of which surface (CLI vs Desktop) hosts it.
		- **Storage differs accordingly**: a scheduled task is a durable file at `~/.claude/scheduled-tasks/<task-name>/SKILL.md` (YAML frontmatter `name`/`description` + prompt body); a `/loop` (or `CronCreate`) task is **session-local**, restored on `--resume`/`--continue` only if unexpired, and **expires after 7 days**.
	- ## Compare scheduling options[^1]
		- | | [[Claude/Routine]] (Cloud) | Scheduled task (Desktop, this page) | `/loop` |
		  |---|---|---|---|
		  | Runs on | Anthropic cloud | Your machine | Your machine |
		  | Requires machine on | No | Yes | Yes |
		  | Requires open session | No | No | Yes |
		  | Persistent across restarts | Yes | Yes | Restored on `--resume` if unexpired |
		  | Access to local files | No (fresh clone) | Yes | Yes |
		  | MCP servers | Connectors configured per task | Config files and connectors | Inherits from session |
		  | Permission prompts | No (runs autonomously) | Configurable per task | Inherits from session |
		  | Customizable schedule | Via `/schedule` in the CLI | Yes | Yes |
		  | Minimum interval | 1 hour | 1 minute | 1 minute |
	- ## Create a scheduled task[^1]
		- **Routines** (sidebar) → **New routine** → **Local**, then fill in:
			- **Name**: converted to lowercase kebab-case, used as the folder name; must be unique.
			- **Description**: short summary shown in the task list.
			- **Instructions**: written like any prompt-box message; includes pickers for **permission mode** and **model**, plus the working folder and an **isolated worktree** toggle.
			- **Schedule**: see options below.
		- A trusted **folder** is required before saving; Desktop prompts to trust it if needed.
		- Natural language also works from any session: *"set up a daily code review that runs every morning at 9am"* (recurring) or *"remind me at 3pm tomorrow to check the deploy"* (one-time, self-disables after firing).
		- By default a run uses the working directory **as-is**, including uncommitted changes; enable the **worktree** toggle to give each run its own isolated git worktree.
	- ## Schedule options[^1]
		- **Manual**—no schedule, runs only via **Run now**.
		- **Hourly**—every hour.
		- **Daily**—time picker, defaults to 9:00 AM local time.
		- **Weekdays**—like Daily, skips Saturday/Sunday.
		- **Weekly**—time picker + day picker.
		- For anything the picker doesn't offer (every 15 minutes, first of the month, a single future timestamp), ask Claude in a Desktop session in plain language.
	- ## How scheduled tasks run[^1]
		- Desktop checks the schedule **every minute** while open and starts a fresh session when a task is due, independent of any manual sessions already open. Each task gets a small deterministic delay (a few minutes, same offset every time) to stagger API traffic.
		- Firing produces a desktop notification and a new session under a **Scheduled** section in the sidebar; it behaves like any other session (edit files, run commands, commit, open PRs).
		- If the computer sleeps through the scheduled time, that run is **skipped**. **Keep computer awake** (Settings → Desktop app → General) prevents idle sleep, but closing the laptop lid still sleeps it.
		- **Missed runs**: on app start / wake, Desktop starts **exactly one** catch-up run for the most recently missed time in the last 7 days and discards anything older—so a daily task asleep for six days runs **once**, not six times. Write prompts defensively if timing matters (e.g. "only review today's commits; if it's after 5pm, skip and summarize what was missed").
	- ## Permissions[^1]
		- Each task has its own **permission mode**, set at creation/edit. Allow rules from `~/.claude/settings.json` also apply.
		- **Ask mode** stalls the run until approved in the sidebar session; click **Run now** after creating a task and select "always allow" on each prompt so future runs auto-approve.
		- Connector tools an org sets to `ask`, and MCP tools marked `requiresUserInteraction`, prompt every call with no always-allow option—those runs stall each time.
	- ## Manage scheduled tasks[^1]
		- From a task's detail page: **Run now**, toggle **Active/Paused**, **Edit** (instructions/schedule/folder/etc.), **Review history** (including why a run was skipped), **Review allowed permissions**, and **Delete** (optionally also removing the `SKILL.md` and data under `~/.claude/scheduled-tasks/`).
		- A running task can reschedule or rewrite its own prompt via the `update_scheduled_task` MCP tool—e.g. moving a review earlier after detecting a release branch.
		- Editing the `SKILL.md` file directly changes only **name/description/prompt**; schedule, folder, model, and enabled state live outside the file and must go through the Edit form or a natural-language request.
	- ## Misconceptions
		- **"A scheduled task is the same mechanism as `/loop`."** Both are local, but a scheduled task creates its own new sessions on a timer with no open session required; `/loop` only extends a session that is already open, and stops when it closes.
		- **"`/loop` only exists in the terminal CLI."** [[Claude/Desktop/Code]] is Claude Code running inside the desktop app, so `/loop` behaves identically there.
		- **"Scheduled tasks work even if the computer is asleep or Desktop is closed."** They don't—that tradeoff belongs to cloud [[Claude/Routine]]s, not Local scheduled tasks.
	- ## Footnotes
		- [^1]: https://code.claude.com/docs/en/desktop-scheduled-tasks
		- [^2]: https://code.claude.com/docs/en/scheduled-tasks
		- [^3]: https://code.claude.com/docs/en/routines