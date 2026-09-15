tags:: [[Diataxis/How To]]

- # How to find what's blocking a [[MacOS]] software update install
	- ## Overview
		- macOS sometimes fails to install a pending update and shows a generic "Software Update Not Installed" dialog without naming the app responsible.
		- Before installing an update that requires a restart, macOS has to terminate the logged-in user's apps. An app can refuse to quit, ask for more time, or hang, which cancels the process.
		- This guide finds the offending app using the Unified Log and `install.log`, for cases where the update stalled during that app-termination phase.
	- ## Prerequisites
		- Admin access to run `sudo` in Terminal on the affected [[Mac]].
		- A rough idea of when the failed update attempt happened, so the log search window can be scoped.
	- ## Steps
		- ### 1. Search `loginwindow` logs around the failure time
			- `loginwindow` coordinates quitting apps during logout, restart, and shutdown, including the restart a software update triggers.
			- Run the following, adjusting the interval (`--last 30m`, `2h`, `1d`) to cover when the update failed:
				- ~~~bash
				  sudo log show --last 4h --style compact \
				    --predicate 'process == "loginwindow"' \
				    | egrep -i 'BundleID|Path|quit|terminat|cancel|abort|timeout|restart|logout'
				  ~~~
			- Look for `BundleID` and `Path` values that appear near termination, cancellation, or timeout messages — these identify the app involved.
		- ### 2. Broaden the search if nothing turns up
			- Include `softwareupdated` and `runningboardd` alongside `loginwindow`:
				- ~~~bash
				  sudo log show --last 4h --style compact \
				    --predicate 'process == "loginwindow" OR process == "softwareupdated" OR process == "runningboardd"' \
				    | egrep -i 'quit|terminat|cancel|abort|timeout|restart|logout|prevent|refus|fail'
				  ~~~
		- ### 3. Check `/var/log/install.log`
			- This traditional log also records installation and update activity, though it's less likely to show why the app-termination phase failed, since that failure happens before the actual OS-update installation starts.
				- ~~~bash
				  sudo grep -Ei 'error|fail|abort|cancel|restart|logout|quit' /var/log/install.log | tail -200
				  ~~~
		- ### 4. Interpret a `previouslyRunningApps` list carefully
			- This list only records which apps were running so macOS can restore them after the restart — it is not a list of apps that blocked the update.
			- Correlate it with nearby termination or cancellation messages instead of treating it as the answer on its own.
	- ## Troubleshooting
		- **Logs are too noisy** — narrow the `--predicate` to `process == "loginwindow"` only, then widen the query if nothing turns up.
		- **No app name found in the logs** — the logs usually reveal *which* app blocked termination, but not *why*. Typical causes are an unsaved document, a modal confirmation dialog, an active transfer, an unresponsive process, or a bug in the app's shutdown handling. Quit the identified app manually, then retry the update.
		- **Nothing in the search interval** — increase `--last` to cover a longer window; some update attempts happen well before the failure dialog appears.
