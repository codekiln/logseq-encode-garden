logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/dotfiles]]
task-config-root:: chezmoi/dot_config/mise
task-name:: pmset:lid-awake:enable
source-link:: https://github.com/codekiln/dotfiles/blob/claude/172-lid-awake-tasks/chezmoi/dot_config/mise/tasks/pmset/lid-awake/executable_enable
see-also:: [[MacOS/How To/Keep a Mac Awake with the Lid Closed]]

- # Keep the Mac Awake with the Lid Closed
	- Turns off lid-close sleep with [[pmset]] `disablesleep 1`, after recording the current `SleepDisabled` value so [[pmset/mise/Task/lid-awake/restore]] can return to it.
	- ## Invocation
		- Runs from any directory, as a global task.
			- ~~~sh
			  mise run pmset:lid-awake:enable
			  ~~~
	- ## Side effects
		- Writes `0` or `1` to `${XDG_STATE_HOME:-~/.local/state}/pmset-lid-awake/sleep-disabled-before` when no record exists. A second enable keeps the first record.
		- Runs `sudo /usr/bin/pmset -a disablesleep 1` unless sleep is already disabled. The system-wide setting holds on battery as well as on the charger.
	- ## Access
		- Asks for a password unless [[pmset/mise/Task/lid-awake/install-sudoers]] has installed its rule, or Touch ID for `sudo` is enabled.
	- ## Source and help
		- ~~~sh
		  mise run pmset:lid-awake:enable --help
		  ~~~
