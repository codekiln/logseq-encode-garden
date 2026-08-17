alias:: [[tmux session groups]], [[tmux session group]]

- # What does [tmux new-session -t <session-group-name>](https://man.openbsd.org/tmux#new-session) do? [[card]]
	- ## [[My Answer]]
		- It's a way of sharing windows between sessions. I'm not to
	- ## [[Official Answer]]
		- Sessions in the same group **share the same set of windows**
			- new windows **are linked to all sessions in the group**
			- any windows **closed removed from all sessions**
		- The `group-name` argument may be:
			- the name of an **existing group**
				- then the new session created is added to that group
			- the name of an **existing session**
				- the new session is added to the same group as that session, creating a new group if necessary
				- [[My Note]] *they are combined*
			- the name for a **new group** containing only the new session
	-