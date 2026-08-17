see-also:: [[tmux/Session/Q/How can I give the session name more room in the status line?]]

- Each [[tmux/session]] can have a name. by default this appears in the leftmost part of the [[tmux/Status Line]]
	- Only the first nine characters of it appear there, because [[tmux/Option/status-left-length]] defaults to `10` and the bracket in [[tmux/Option/status-left]] takes one column.
