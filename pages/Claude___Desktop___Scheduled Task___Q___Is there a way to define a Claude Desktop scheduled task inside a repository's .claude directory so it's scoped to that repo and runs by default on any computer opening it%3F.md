tags:: [[Claude/Desktop]], [[Claude/Code]], [[Q]]
logseq-entity:: [[Logseq/Entity/Question]]
title:: Claude/Desktop/Scheduled Task/Q/Is there a way to define a Claude Desktop scheduled task inside a repository's .claude directory so it's scoped to that repo and runs by default on any computer opening it?
see-also:: [[Claude/Desktop/Scheduled Task]]

- # Is there a way to define a [[Claude/Desktop/Scheduled Task]] inside a repository's `.claude` directory so it's scoped to that repo and runs by default on any computer opening it?
	- ## [[AI Answer]]
		- **Short answer:** No. Scheduled-task registration is per-machine, home-directory state — there's no supported way to commit a task definition into a repo's `.claude/` directory and have Desktop auto-register or auto-run it there on every machine.
		- [[Answer/Official]] from [Schedule recurring tasks in Claude Code Desktop](https://code.claude.com/docs/en/desktop-scheduled-tasks):
		- A scheduled task's editable prompt file lives at `~/.claude/scheduled-tasks/<task-name>/SKILL.md` (or under `CLAUDE_CONFIG_DIR` if that's set) — always a **home-directory** path, never something read out of the project's own `.claude/` folder.
		- Even that file is only part of the task: "Schedule, folder, model, and enabled state are not in this file: change them through the Edit form or ask Claude." Those fields live in Desktop's own local app state, tied to the machine that created the task — editing `SKILL.md` by hand changes only the name, description, and prompt body.
		- Creating a task also requires trusting a **working folder** through Desktop's UI (or a natural-language request in a session) — there's no config format that says "if a repo has this file in `.claude/`, register a task pointed at it."
		- **Net effect**: a scheduled task's identity (name, folder, schedule, model, permission mode) is registration state private to one Desktop installation. Nothing about it is discovered from repo contents, so opening the same repo on a second computer doesn't cause its scheduled tasks to reappear — each machine needs its own **New routine → Local** setup (UI or natural-language) pointed at that folder.
		- **Closest available workaround:** keep the *prompt content* itself in the repo — e.g. as a `.claude/skills/<name>/SKILL.md` or a plain instructions file — and make each machine's task Instructions field just reference it (e.g. "follow the workflow in `.claude/skills/daily-review/SKILL.md`"). That keeps the task's behavior version-controlled and consistent across machines, but the task's existence, folder binding, and schedule still have to be created once per machine through Desktop.
