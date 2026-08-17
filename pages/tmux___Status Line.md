see-also:: [[tmux/Session/Q/How can I give the session name more room in the status line?]]

# Tmux Status Line
	- ![tmux status line diagram](https://github.com/tmux/tmux/wiki/images/tmux_status_line_diagram.png)
		- [[tmux/session/Name]]
		- [[tmux/Window/Index]]
		- [[tmux/Window/Name]]
		- [[tmux/Window/Last]]
		- [[tmux/Window/Current]]
		- [[tmux/Pane/Title]]
		- [[tmux/Status Line/Time and Date]]
	- ## Three parts, configured separately
		- A left component, a central window list, and a right component. `status-format[0]` assembles them; each end has a format string and a maximum width.
		- [[tmux/Option/status-left]] — the format string at the left end, holding the [[tmux/session/Name]] by default.
		- [[tmux/Option/status-left-length]] — the maximum width of that left component, `10` by default.
		- [[tmux/Option/status-right]] — the format string at the right end, holding the [[tmux/Pane/Title]], time and date.
		- [[tmux/Option/status-right-length]] — the maximum width of that right component, `40` by default.
		- The window list between them is drawn from `window-status-format` and takes whatever columns the two ends leave, showing `<` and `>` markers when the client is too narrow to hold all three.