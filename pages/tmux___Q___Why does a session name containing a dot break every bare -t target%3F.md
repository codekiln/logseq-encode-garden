logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tmux/Q/Why does a tmux -t =session target fail in zsh?]], [[My/AI/Agent/Fleet]]

- # Why does a [[tmux]] session name containing a dot break every bare `-t` target?
	- ## [[AI Answer]]
		- **Short answer:** a `-t` target is parsed as `session:window.pane`, so a dot inside the *session name* is read as the window/pane separator. The lookup then runs against a window or a pane that does not exist, and the error names that window or pane rather than the session — which is why it reads as a missing session. Keep dots out of session names.
		- ### The parse, and where the name goes
			- `session:window.pane` is the target form. Every part is optional, so `hay-.F` is not rejected as malformed — it is accepted and split, with `F` taken as the pane.
			- The split happens on the first `:` and the first `.`, wherever they sit. A dot at the start of a suffix, in the middle of one, or in the middle of the name all break the same way; only the reported half changes.
		- ### Reproduced
			- Measured on [[2026-08-24 Mon]] against [[tmux/v/3.7b]], on an isolated socket rather than the server holding live work:
				- ~~~sh
				  tmux -L probe new-session -d -s 'hay-.F'
				  tmux -L probe list-sessions -F '#{session_name}'   # hay-.F — the session exists
				  ~~~
			- | target | exit | message |
			  | --- | --- | --- |
			  | `has-session -t '=hay-.F'` | `1` | `can't find pane: F` |
			  | `has-session -t 'hay-.F'` | `1` | `can't find pane: F` |
			  | `list-windows -t '=hay-.F'` | `1` | `can't find pane: F` |
			  | `new-window -d -t '=hay-.F'` | `1` | `can't specify pane here` |
			  | `has-session -t '=hay-D.F'` | `1` | `can't find window: hay-D` |
			  | `has-session -t '=hay.DF'` | `1` | `can't find window: hay` |
			  | `has-session -t '=hay-DF'` | `0` | — |
			- The last row is the control: the same name with the dot removed answers cleanly.
		- ### It is not the `=` prefix, and not the shell
			- `has-session -t 'hay-.F'` fails identically to `-t '=hay-.F'`, so exact-match plays no part. The target was quoted throughout, so zsh's equals expansion plays no part either — that is the separate fault on [[tmux/Q/Why does a tmux -t =session target fail in zsh?]].
			- The two share a symptom and nothing else. Both report a name as not found while the session is sitting in `list-sessions`, and neither message contains the word session.
		- ### Why the error text is the expensive part
			- The message moves with the dot. `hay-.F` reports a missing **pane**; `hay-D.F` reports a missing **window** named `hay-D`, a string that appears nowhere. Two instances of one fault do not look alike, so recognising the second from having debugged the first does not happen.
			- `new-window` fails with `can't specify pane here` — an argument-shape complaint about a command that was given no pane, which points away from the name entirely.
		- ### `has-session` cannot answer, which is the real cost
			- A script's existence check returns `1`, the same as for a session that is genuinely absent. Nothing downstream can tell a missing session from an unusable name, so the guard that would catch this is the thing the fault disables.
		- ### The workarounds, and why they are not a convention
			- A trailing colon disambiguates — `-t '=hay-.F:'` exits `0` — and an explicit window works too: `-t '=hay-.F:0'` lists panes normally.
			- Both are correct and neither is safe to build on. A naming scheme that holds only while everyone remembers a trailing colon fails at the first bare target anyone writes, including one written by a tool. An explicit window is also the case that hides the fault during testing: it is the one target shape a stray dot leaves alone, so a probe built from `session:0` targets passes on every input it is given.
		- ### Sources
			- [tmux(1) man page — COMMANDS](https://man.openbsd.org/tmux.1#COMMANDS) — defines the `session:window.pane` target form the parse above follows.
