logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tmux/Command/new-session/-t]]

- # What are [[tmux]] session groups good for?
	- ## [[AI Answer]]
		- **Short answer:** a session group lets **two or more terminals share one window list while each sits on a different window**. Shared *list*, not shared *view* — the terminals never show the same window unless you point them there.
		- Plain double-attach to one session mirrors the clients: switch window in one and the other follows, and both get squeezed to a shared size. A group breaks that coupling — one window list, independent current window and size per session.
		- [[Answer/Official]] from [tmux manual — new-session](https://man.openbsd.org/tmux#new-session): "Sessions in the same group share the same set of windows - new windows are linked to all sessions in the group and any windows closed removed from all sessions. The current and previous window and any session options remain independent and any session in a group may be killed without affecting the others."
		- ### The problem it solves
			- Without groups there are only two options for a second terminal, and both are bad:
				- 1. **Attach to the same session** — the second client is a mirror. Change window in one and it changes in the other. Sizes are negotiated between clients, so the bigger terminal gets letterboxed.
				- 2. **Create an unrelated session** — now there are two window lists to keep in sync by hand, and a window created in one is invisible from the other.
			- A session group is the middle option: **one workspace, several independent views onto it**.
			- Concretely, in the [[tmux/Tutorial/Kanban for Agentic Coding]] framing where a window is a card: a session `garden` holds cards `0: nvim`, `1: shell`, `2: claude`, `3: logs`. Left terminal parks on `0`, right terminal parks on `2`. Two cards visible at once, one deck — `Prefix c` from either terminal adds card `4` to both.
		- ### Shared vs. independent
			- | aspect                       | behavior across a group                                |
			  |------------------------------|--------------------------------------------------------|
			  | set of [[tmux/Window]]s      | **shared** — create or close in one, all members see it |
			  | current and previous window  | **independent** per session                            |
			  | session options              | **independent** per session                            |
			  | attached clients and size    | **independent** per session                            |
			  | killing a member             | **no effect** on the others                            |
		- ### When it is worth using
			- Not when one terminal is enough, and not when both things fit on one screen — that is what panes are for. Panes split a single card inside a single terminal; they cannot span two terminal windows or two monitors.
			- **Two terminals or two monitors on one project** — left screen sits on the editor window, right screen on logs, both drawing from the same window list.
			- **Different window sizes** — a laptop screen and an external monitor attached at once, each rendering at its own size instead of both shrinking to the smaller one.
			- **Pairing or demoing over ssh** — collaborators share the workspace but navigate it separately, rather than fighting over one cursor.
			- **Disposable views** — spin up an extra session to go look at something, kill it when done, and the original session keeps every window.
		- ### Creating one
			- `tmux new-session -t main` — new session in the same group as `main`, auto-named `main-1`. See [[tmux/Command/new-session/-t]] for how the `-t` argument resolves to an existing group, an existing session, or a new group.
			- `tmux new-session -d -t main -s main-view2` — same, but detached and explicitly named.
			- `-n` and a shell command are **rejected** when `-t` is used, because the new session inherits the group's windows rather than opening one.
		- ### Inspecting and tearing down
			- `tmux list-sessions -F '#{session_name} #{session_group} #{session_group_size}'` — which sessions are grouped and how large each group is. `#{session_grouped}` is the boolean form.
			- `tmux kill-session -t main` removes one member. `tmux kill-session -g -t main` kills **every** session in the group.
		- ### Related option
			- When group members are attached at different sizes, `window-size` (`largest` / `smallest` / `manual` / `latest`) decides which client's size a window renders at, and `aggressive-resize` resizes a window to the session currently displaying it. These matter mostly for full-screen programs.
