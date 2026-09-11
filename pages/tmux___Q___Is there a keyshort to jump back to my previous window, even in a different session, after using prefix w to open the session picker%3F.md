logseq-entity:: [[Logseq/Entity/Question]]

- # Is there a keyshort to jump back to my previous window, even in a different session, after using [[tmux/Prefix]] `w` to open the [[tmux/session/Picker]]?
	- ## [[AI Answer]]
		- Short answer: not in one step by default, but two built-in keyshorts combine to do it.
		- [[tmux/Keyshort/Window/Last Window]] (`<prefix> l`, lowercase) only toggles within the **current session** — it will not follow you across sessions.
		- The piece that's missing is the **session** toggle: `<prefix> L` (capital L, default binding for `switch-client -l`) switches the client back to the **last session** it was attached to, including one you just left via the session picker.
		- So, after picking a window in another session with `<prefix> w`, press `<prefix> L` to return to the previous session, then `<prefix> l` if you also need to return to the previously active window inside it.
		- There is no single native keyshort that jumps straight back to the exact prior window regardless of session; it's this two-step combo (`<prefix> L` then, if needed, `<prefix> l`).
