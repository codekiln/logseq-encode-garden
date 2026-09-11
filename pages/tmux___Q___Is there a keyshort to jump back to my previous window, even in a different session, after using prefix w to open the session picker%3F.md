logseq-entity:: [[Logseq/Entity/Question]]

- # Is there a keyshort to jump back to my previous window, even in a different session, after using [[tmux/Prefix]] `w` to open the [[tmux/session/Picker]]?
	- ## [[AI Answer]]
		- Short answer: not in one step by default, but two built-in keyshorts combine to do it.
		- [[tmux/Keyshort/Window/Last Window]] (`<prefix> l`, lowercase) only toggles within the **current session** — it will not follow you across sessions.
		- The piece that's missing is the **session** toggle: `<prefix> L` (capital L, default binding for `switch-client -l`) switches the client back to the **last session** it was attached to, including one you just left via the session picker.
		- So, after picking a window in another session with `<prefix> w`, press `<prefix> L` to return to the previous session, then `<prefix> l` if you also need to return to the previously active window inside it.
		- There is no single native keyshort that jumps straight back to the exact prior window regardless of session; it's this two-step combo (`<prefix> L` then, if needed, `<prefix> l`).
	- ## Is there a technical underpinning to bind this as one keyshort in a plugin?
		- Yes. [[tmux/Command]]s can be chained with `\;` in a single `bind-key`, so a plugin (or a plain config line) can bind one key straight to the combo, e.g. `bind-key W switch-client -l \; last-window`.
		- [[gpakosz/.tmux]]'s own `.tmux.conf` already does the two underlying pieces separately: `bind BTab switch-client -l` (last session) and `bind Tab last-window` (last window), confirming both primitives are ordinary bindable commands, not special-cased behavior.
		- For anything smarter than a fixed chain — e.g. only running `last-window` when the session actually changed, or tracking the *exact* previously active pane rather than tmux's own single last-session/last-window pointers — a plugin would use `run-shell` to call a script, and persist its own state between key presses with user options (`set -g @my_var ...`, read back via `#{@my_var}` or `show-options -gv`). The same `.tmux.conf` uses this exact user-option pattern (e.g. `@battery_percentage`, `@battery_charge`) to cache values across separate command invocations.
		- Hooks (`set-hook -g client-session-changed`, `pane-focus-in`, etc.) are the mechanism for updating that saved state automatically as focus moves, rather than only on the explicit keypress.
		- A TPM-installed plugin is just a `.tmux`-suffixed shell script that a user's config sources via `run-shell`, and which calls `bind-key`/`set-hook` itself — no different in kind from hand-written `bind-key` lines in `.tmux.conf`.
