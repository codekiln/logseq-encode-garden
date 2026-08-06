logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[oh-my-tmux]]

- # How can I turn mouse mode on using a keyboard shortcut in [[tmux]]?
	- ## [[AI Answer]]
		- **Short answer:** With [[oh-my-tmux]], press [[tmux/Prefix]] then `m` — that **toggles** mouse mode on and off. Stock tmux has no default key for this; use the command prompt or bind your own.
		- ### [[oh-my-tmux]] (likely your setup)
			- Chord: `<prefix> m` (e.g. `Ctrl-b` then `m`)
			- Documented on [[oh-my-tmux]] as toggling mouse mode on or off ([gpakosz/.tmux README](https://github.com/gpakosz/.tmux)).
			- Confirm the live binding: `tmux list-keys -T prefix | rg 'mouse|set.*mouse'` (see [[tmux/Q/How can I find all keyshorts including custom keybindings?]]).
		- ### One-shot without a dedicated key (stock or any config)
			- `Prefix :` then run `set -g mouse on` (same pattern as [[tmux/Cheat Sheet]]).
			- Turn off with `set -g mouse off`. Query with `show -gv mouse`.
		- ### Bind a toggle yourself (stock tmux)
			- Add to `~/.tmux.conf` (or run once at `Prefix :`):
			- ~~~tmux
			  bind m set -g mouse \; display-message 'Mouse: #{?mouse,ON,OFF}'
			  ~~~
			- Then `<prefix> m` toggles and shows the new state. Reload with `Prefix :` → `source-file ~/.tmux.conf` (or [[tmux/Keyshort/Reload Config]] if you use oh-my-tmux’s `Prefix r`).
			- Common recipe from [Stack Overflow — mouse toggle bindings](https://stackoverflow.com/questions/17445100/getting-back-old-copy-paste-behaviour-in-tmux-with-mouse) and [Unix & Linux — enable mouse support](https://unix.stackexchange.com/questions/516800/how-do-i-enable-tmux-mouse-support).
