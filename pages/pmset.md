tags:: [[Mac/CLI]], [[CLI/Tool]]
see-also:: [[CaffeinateCLI]], [[MacOS/How To/Keep a Mac Awake with the Lid Closed]]

- # [`pmset`](https://keith.github.io/xcode-man-pages/pmset.1.html)
	- Built-in macOS command for reading and changing power management settings: sleep timers, wake events, hibernation, and whether the system sleeps at all.
	- Reading settings works as any user. Changing one needs root, so writes run under `sudo`.
	- ## Usage
		- ~~~sh
		  pmset -g                 # settings in use now, plus system-wide settings
		  pmset -g custom          # settings for each power source
		  pmset -g assertions      # processes currently holding the Mac awake
		  sudo pmset -a <setting> <value>
		  ~~~
		- `-a`, `-b`, `-c` and `-u` apply a setting to all power sources, battery, charger, or UPS.
	- ## `disablesleep`
		- `sudo pmset -a disablesleep 1` stops the system from sleeping, including when the lid closes. `sudo pmset -a disablesleep 0` turns sleep back on, which is the macOS default.
		- `pmset -g` shows the value as `SleepDisabled` under "System-wide power settings".
		- `man pmset` does not document this setting.
		- [[MacOS/How To/Keep a Mac Awake with the Lid Closed]] uses it, through mise tasks that record the earlier value and restore it.
	- ## Related settings
		- `lidwake` wakes the Mac when the lid opens.
		- `sleep`, `displaysleep` and `disksleep` are idle timers in minutes, with `0` meaning never.
	- ## mise tasks
		- [[pmset/mise/Task/lid-awake/enable]]
		- [[pmset/mise/Task/lid-awake/restore]]
		- [[pmset/mise/Task/lid-awake/install-sudoers]]
