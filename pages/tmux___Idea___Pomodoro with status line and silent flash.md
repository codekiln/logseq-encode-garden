tags:: [[Idea]]
date-created:: [[2026-03-25 Wed]]

- # Pomodoro in tmux: status-line countdown and silent visual cue
	- ## Motivation
		- Currently using **Howler**, a macOS native timer app; want to move toward terminal-native workflows and strengthen [[CLI/Craftsmanship]].
		- Co-working and other shared spaces: audio alarms are often a bad fit — need **silent** end-of-interval signaling.
	- ## Concept
		- Run the [Pomodoro technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) with [[tmux]] so a **countdown** is visible in status bars (session and/or global), not only in a dedicated pane.
		- On wrap-up, use a **terminal-visible pulse** (e.g. brief invert / flash / highlight via tmux message styles, `display-message`, or controlled pane attributes) instead of sound.
	- ## Implementation angle (hypothesis)
		- Status updates: `#()` in `status-left` / `status-right` reading from a small state file or FIFO updated by a loop (`sleep 1`), similar in spirit to other status-line “notification center” sketches already noted for [[tmux]].
		- Flash: tmux client options or a short script that toggles styles and restores them; stay within terminal capabilities so it works over SSH.
	- ## Related in this graph
		- [[tmux/Idea/Toggl Track status in status line]] — sibling sketch: always-visible timer context from a **tracker** (vs local Pomodoro countdown)
		- [[tmux/Config]] — status-line and hooks
		- [[tmux/oh-my-tmux]] — if theme or status segments need coordination
