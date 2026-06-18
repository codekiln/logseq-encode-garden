logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tmux/Option/mode-keys]], [[tmux/Option/status-keys]]

- # How can I query the current value of a [[tmux]] option?
	- ## [[AI Answer]]
		- **Short answer:** Use `tmux show-options` for session options and `tmux show-window-options` for window options; add `-g` to query the global (default) value.
		- ### Option types and their query commands
			- [[tmux]] options fall into two main scopes:
			- | Scope | Command | Example option |
			  |-------|---------|----------------|
			  | Session | `show-options` (alias `show`) | `status-keys` |
			  | Window | `show-window-options` (alias `showw`) | `mode-keys` |
		- ### Query a specific option
			- ~~~sh
			  # Session option — controls status-bar / command-prompt key mode
			  tmux show-options -g status-keys
			  # → status-keys vi

			  # Window option — controls copy-mode key bindings
			  tmux show-window-options -g mode-keys
			  # → mode-keys vi
			  ~~~
			- The `-g` flag reads the **global** (config-level) default. Omit `-g` inside a tmux session to read the current session or window value, which may differ if overridden at runtime.
		- ### Show only the value (no key name)
			- ~~~sh
			  tmux show-options -gv status-keys
			  # → vi
			  ~~~
		- ### Query from the tmux command prompt
			- Press `Prefix + :` to open the tmux command prompt and enter:
			- ~~~
			  show-options -g status-keys
			  show-window-options -g mode-keys
			  ~~~
		- ### Show all options at once
			- ~~~sh
			  tmux show-options -g          # all global session options
			  tmux show-window-options -g   # all global window options
			  ~~~
		- ### Sources
			- [tmux(1) man page — show-options](https://man.openbsd.org/tmux.1)
