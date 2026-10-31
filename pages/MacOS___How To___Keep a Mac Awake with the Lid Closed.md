tags:: [[Diataxis/How To]]
logseq-entity:: [[Logseq/Entity/Diataxis/How To]]
see-also:: [[pmset]], [[CaffeinateCLI]]

- # How To Keep a Mac Awake with the Lid Closed
	- ## Overview
		- Keep a MacBook running with its lid closed, for example while a render or an agent session finishes, then put lid-close sleep back the way it was.
		- The switch is the [[pmset]] setting `disablesleep`. [[CaffeinateCLI]] holds off idle sleep but does not keep the Mac awake through a lid close.
	- ## Prerequisites
		- The `pmset:lid-awake:*` tasks from [[Person/codekiln/GitHub/dotfiles]], applied with `chezmoi apply`. They were added in [codekiln/dotfiles#173 Keep the Mac awake with the lid closed and restore it](https://github.com/codekiln/dotfiles/pull/173).
		- An admin account, for the one `sudo` prompt in step 1.
	- ## Steps
		- ### 1. Allow the switch without a password
			- If you want to skip the password prompt, install the sudoers rule once. It covers only `pmset -a disablesleep 1` and `pmset -a disablesleep 0` for your user.
			- ~~~sh
			  mise run pmset:lid-awake:install-sudoers
			  ~~~
			- If you skip this step, each switch asks for your password, or for Touch ID if `pam_tid.so` is enabled in `/etc/pam.d/sudo_local`.
		- ### 2. Turn lid-close sleep off
			- ~~~sh
			  mise run pmset:lid-awake:enable
			  ~~~
			- The task records the current `SleepDisabled` value before changing it.
		- ### 3. Close the lid
			- The Mac keeps running on battery too, so keep it out of a closed bag and away from blankets.
		- ### 4. Put lid-close sleep back
			- ~~~sh
			  mise run pmset:lid-awake:restore
			  ~~~
			- Restore writes back the value recorded in step 2. With no record it turns sleep back on.
	- ## Troubleshooting
		- To check the current state, run `pmset -g | grep SleepDisabled`. `1` means the Mac stays awake with the lid closed.
		- If the Mac still sleeps when the lid closes, run `pmset -g` and look for `SleepDisabled 1`. If it reads `0`, run step 2 again.
		- If `install-sudoers` says there is no TTY, run it in a terminal yourself. It needs to ask for your password once.
		- To return to a password prompt on every switch, run `mise run pmset:lid-awake:install-sudoers --remove`.
