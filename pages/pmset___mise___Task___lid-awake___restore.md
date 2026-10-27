logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/dotfiles]]
task-config-root:: chezmoi/dot_config/mise
task-name:: pmset:lid-awake:restore
source-link:: https://github.com/codekiln/dotfiles/blob/main/chezmoi/dot_config/mise/tasks/pmset/lid-awake/executable_restore
see-also:: [[MacOS/How To/Keep a Mac Awake with the Lid Closed]]

- # Restore Lid-Close Sleep
	- Writes back the `SleepDisabled` value that [[pmset/mise/Task/lid-awake/enable]] recorded, then deletes the record. With no record it sets [[pmset]] `disablesleep 0`, the macOS default.
	- ## Invocation
		- ~~~sh
		  mise run pmset:lid-awake:restore
		  ~~~
	- ## Side effects
		- Runs `sudo /usr/bin/pmset -a disablesleep 0` or `1` when the current value differs from the recorded one, and skips `sudo` when they match.
		- Deletes `${XDG_STATE_HOME:-~/.local/state}/pmset-lid-awake/sleep-disabled-before` after the write succeeds.
	- ## Failure and recovery
		- A cancelled password prompt leaves the record in place; run restore again.
		- A record holding anything other than `0` or `1` stops the task before it writes. Delete the file and run restore to return to the default.
	- ## Source and help
		- ~~~sh
		  mise run pmset:lid-awake:restore --help
		  ~~~
