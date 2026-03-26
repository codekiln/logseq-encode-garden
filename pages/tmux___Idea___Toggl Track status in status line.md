tags:: [[Idea]]
date-created:: [[2026-03-25 Wed]]

- # Show Toggl Track state in the tmux status bar
	- ## Motivation
		- Same spirit as [[tmux/Idea/Pomodoro with status line and silent flash]]: keep **time context** visible from any pane without reaching for a GUI.
		- While still on **Toggl Track**, mirror “what’s running now?” (description, project, elapsed) in `status-left` / `status-right` instead of only checking the app or browser.
	- ## Concept
		- `#()` segment in [[tmux/Config]] that prints a short string for the **current time entry** — compact enough for the status line.
		- Likely backed by [[Toggl/CLI/AuHau/How To/Set Up Toggl CLI]] (`toggl now` or equivalent) or a tiny cache file updated on an interval so the status line does not hammer the API every refresh.
	- ## Relation to migration
		- This is **interim** polish on the current stack. Longer-term goal: [[Toggl/Idea/Migrate off Toggl Track]] to a tracker that fits terminal-first workflow without the same vendor lock-in.
	- ## Related in this graph
		- [[Toggl/CLI/Python/AuHau/toggl-cli]]
		- [[Toggl/AI/Report/26/01/AI control of Toggl - Options Jan 2026]]
		- [[tmux/oh-my-tmux]] — if a theme already reserves status segments
