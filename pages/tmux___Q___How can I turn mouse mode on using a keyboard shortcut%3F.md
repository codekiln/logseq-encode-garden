logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tmux/Keyshort/Enable Mouse]]
- # How can I turn mouse mode on using a keyboard shortcut in [[tmux]]?
	- ## [[AI Answer]]
		- **Short answer:** Stock tmux has no dedicated mouse key. Open the [[tmux/Command/Prompt]] with [[tmux/Prefix]] `:` and run `set -g mouse on`. Review card: [[tmux/Keyshort/Enable Mouse]].
		- ### Steps
			- 1. `<prefix> :` (e.g. `Ctrl-b` then `:`)
			- 2. Type `set -g mouse on` → Enter
			- Off: `set -g mouse off`. Query: `show -gv mouse`.
			- Runtime-only — gone after `tmux kill-server`. Same pattern as [[tmux/Cheat Sheet]].
		- ### Optional: bind a toggle in your config
			- ~~~tmux
			  bind m set -g mouse \; display-message 'Mouse: #{?mouse,ON,OFF}'
			  ~~~
			- Then `<prefix> m` toggles. Reload with `<prefix> :` → `source-file ~/.tmux.conf`.
			- Recipes: [Stack Overflow — mouse toggle bindings](https://stackoverflow.com/questions/17445100/getting-back-old-copy-paste-behaviour-in-tmux-with-mouse), [Unix & Linux — enable mouse support](https://unix.stackexchange.com/questions/516800/how-do-i-enable-tmux-mouse-support).
