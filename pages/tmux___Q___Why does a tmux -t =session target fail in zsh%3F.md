logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tmux/session/Name]], [[Zsh]], [[My/AI/Agent/Fleet]]

- # Why does a [[tmux]] `-t =session` target fail in [[Zsh]]?
	- ## [[AI Answer]]
		- **Short answer:** [[Zsh]] eats the `=` before [[tmux]] ever sees it. `=word` is zsh's *equals expansion*, which substitutes the full path of the command `word` — and errors when there is no such command. Quote it:
			- ~~~sh
			  tmux new-window -d -t '=hayward-2026-08-24' -n build
			  ~~~
		- ### What each side means by `=`
			- To [[tmux]], a leading `=` on a `-t` target means **exact match**: `-t =mysession` matches the session named exactly `mysession` rather than the first session with that prefix. Useful whenever two sessions share a prefix — `hayward-2026-08-24` and `hayward-2026-08-24-scratch`.
			- To [[Zsh]], a leading `=` on an unquoted word means **look up this command and substitute its path**. The two conventions collide on exactly the argument where the tmux one is wanted.
		- ### Reproduced
			- ~~~sh
			  zsh -c 'print -r -- =ls'
			  # /bin/ls
			  zsh -c 'print -r -- =hayward-2026-08-24'
			  # zsh:1: hayward-2026-08-24 not found
			  zsh -c "print -r -- '=hayward-2026-08-24'"
			  # =hayward-2026-08-24
			  ~~~
			- The failure is reported by zsh, before the command runs at all. Nothing named tmux appears in the message, which is what makes it read like a missing session rather than a shell expansion.
		- ### It is an option, and it is on by default
			- The behavior is the `EQUALS` option. `setopt` does not list it, because `setopt` prints only what differs from the default — so its absence from that listing is what tells you it is on.
			- The negative test is what settles it:
				- ~~~sh
				  zsh -c 'unsetopt equals; print -r -- =nope'
				  # =nope
				  ~~~
			- Turning `EQUALS` off globally is the wrong fix. Quoting is local, needs no shell state, and is correct in every shell.
		- ### Where it bites
			- Any tmux command taking a target: `new-window -t`, `split-window -t`, `send-keys -t`, `respawn-pane -t`, `has-session -t`. Session, window, and pane targets are all affected, since the exact-match prefix is a property of the target syntax rather than of any one command.
			- [[Bash]] has no equals expansion, so a script that worked when run with `bash` fails when the same line is pasted into an interactive zsh prompt — measured on [[2026/08/24]] against `-t =reeve-2026-08-24`, which failed with `reeve-2026-08-24 not found`.
		- ### Sources
			- [zshexpn(1) — Filename Expansion](https://zsh.sourceforge.io/Doc/Release/Expansion.html#Filename-Expansion) — "If a word begins with an unquoted `=` … the rest of the word is taken as the name of a command … replaced with the full pathname."
			- [tmux(1) man page — COMMANDS](https://man.openbsd.org/tmux.1#COMMANDS) — a target beginning with `=` must match exactly.
