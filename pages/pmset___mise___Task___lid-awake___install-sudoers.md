logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/dotfiles]]
task-config-root:: chezmoi/dot_config/mise
task-name:: pmset:lid-awake:install-sudoers
source-link:: https://github.com/codekiln/dotfiles/blob/claude/172-lid-awake-tasks/chezmoi/dot_config/mise/tasks/pmset/lid-awake/executable_install-sudoers
see-also:: [[MacOS/How To/Keep a Mac Awake with the Lid Closed]], [[Mac/OS/Q/How does Touch ID for sudo (PAM) work?]]

- # Allow the Lid-Awake Switch Without a Password
	- Installs a sudoers rule so [[pmset/mise/Task/lid-awake/enable]] and [[pmset/mise/Task/lid-awake/restore]] run without a password prompt.
	- ## Invocation
		- Run it in a terminal; it asks for `sudo` once and refuses to run without a TTY.
			- ~~~sh
			  mise run pmset:lid-awake:install-sudoers
			  mise run pmset:lid-awake:install-sudoers --remove
			  ~~~
	- ## Side effects
		- Writes `/etc/sudoers.d/pmset-lid-awake`, mode `0440`, owned by `root:wheel`. The rule lets the current user run `/usr/bin/pmset -a disablesleep 1` and `/usr/bin/pmset -a disablesleep 0` with `NOPASSWD`. Every other `sudo` command still asks for a password.
		- Checks the rule with `visudo -cf` before installing it, and the whole sudoers configuration with `visudo -c` after. A failed second check removes the file.
		- `--remove` deletes the file.
	- ## Trade-off
		- Any process running as the user can switch lid-close sleep without a prompt. Touch ID for `sudo` asks for a fingerprint each time instead, applies to every `sudo` command, and needs `pam_reattach` to work inside [[tmux]].
	- ## Source and help
		- ~~~sh
		  mise run pmset:lid-awake:install-sudoers --help
		  ~~~
