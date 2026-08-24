see-also:: [[tmux/Session/Q/How can I give the session name more room in the status line?]]

- Each [[tmux/session]] can have a name. by default this appears in the leftmost part of the [[tmux/Status Line]]
	- Only the first nine characters of it appear there, because [[tmux/Option/status-left-length]] defaults to `10` and the bracket in [[tmux/Option/status-left]] takes one column.
	- **A name with a dot in it cannot be targeted.** `-t` parses `session:window.pane`, so a dot is read as a separator and every bare target — `has-session` among them — resolves against a window or pane that is not there: [[tmux/Q/Why does a session name containing a dot break every bare -t target?]].
