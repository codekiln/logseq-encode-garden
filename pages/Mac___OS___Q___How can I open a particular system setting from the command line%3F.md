# DONE How can I open a particular system setting from the command line?
	- ## General Idea
		- On macOS, you can open specific **System Settings** (or **System Preferences** on older macOS versions) using the `open` command in the Terminal.
		- To open the **Displays** settings, use the following command: `open "x-apple.systempreferences:com.apple.Displays-Settings.extension"`
		- ### General Syntax: `open "x-apple.systempreferences:<PREFERENCE-PANE>"`
		- ### Other Common Examples:
			- **General Settings:** `open "x-apple.systempreferences:com.apple.general-Settings.extension"`
			- **Battery Settings:** `open "x-apple.systempreferences:com.apple.Power-Settings.extension"`
			- **Keyboard Settings:** `open "x-apple.systempreferences:com.apple.Keyboard-Settings.extension"`
			- **Trackpad Settings:** `open "x-apple.systempreferences:com.apple.Trackpad-Settings.extension"`
	- ## DONE Are there any [[Zsh/OhMyZsh/Plugin]]s that handle the completion of mac system preferences from the command line? #Questionl ANS: AFAICT No
		- See also [[zsh/Q/Are there any directories of community plugins besides the zsh repo?]]
			- I searched in [[GitHub/zsh-users/zsh-completions]]
	- ## Research
		- [SystemPreferences/macos_preferencepanes-Ventura.md at main · bvanpeski/SystemPreferences](https://github.com/bvanpeski/SystemPreferences/blob/main/macos_preferencepanes-Ventura.md#finding-settings-sections)
			- > Apple has made discovering the proper URLScheme extensions for different sections of the app much easier in Ventura, thanks to the unification of settings that the new System Settings app brings. In fact, most of them are stored right inside of the System Settings application itself (`/System/Applications/System Settings.app/Contents/Resources/Sidebar.plist` You can combine the values in that plist with the `open x-apple-systempreferences:` command we all know and love and you're off to the races! If any new sections are added in the future, that plist is where you'll want to look.
			- > There are a few deeper settings beyond the sidebar that won't be in that plist. To uncover those you can leverage a line of shell script to pull a list of strings out of System Settings to identify any additional sections that you might have missed. `for pref in $(strings "/System/Applications/System Settings.app/Contents/MacOS/System Settings" | awk '/^com.apple./ {print $1 }'); do echo "$pref"; done` (hat tip to @bradtchapman in MacAdmin Slack for this one)
		- [Mac System Settings Links](https://macmost.com/mac-settings-links) [[2024/11]] [[Mac/OS/15/2]]
			- complete table that was up to date as of [[Nov 18th, 2024]]
			- it seems like there should be a github library out there that maps these out for all the apple versions
		- [Apple System Preferences URL Schemes](https://gist.github.com/rmcdongit/f66ff91e0dad78d4d6346a75ded4b751) [[GitHub/Gist]] - originally authored in [[2020/03]] for [[Mac/OS/10/15]]; latest comments from [[2024/12]]
			- claims that one can do `open -b com.apple.systempreferences /Path/To/Pane`, where the path is `/System/Library/PreferencePanes/`.
				- works
					- `open -b com.apple.systempreferences /System/Library/PreferencePanes/Appearance.prefPane` works
					- `open -b com.apple.systempreferences /System/Library/PreferencePanes/Displays.prefPane`
				- doesn't work
					- `open -b com.apple.systempreferences /System/Library/PreferencePanes/SoftwareUpdate.prefPane`
			- [comment](https://gist.github.com/rmcdongit/f66ff91e0dad78d4d6346a75ded4b751?permalink_comment_id=5222465#gistcomment-5222465) from [[GitHub/luckman212]] in [[2024/10]] said he found a protected (passkey required to access) file that listed quite a few; using [[jq]]
			  collapsed:: true
				- ```
				  TCC_SVC_PLIST='/System/Library/ExtensionKit/Extensions/SecurityPrivacyExtension.appex/Contents/Resources/TCCServiceList.plist'
				  plutil -convert json -o - -- $TCC_SVC_PLIST |
				  jq '"x-apple.systempreferences:com.apple.preference.security?" as $p |
				    map(select(.revealElementKeyName) | {
				      tcc: .tcc,
				      serviceName: .serviceName,
				      url: ($p + .revealElementKeyName)
				    })'
				  ```
				- ... sample output
				- ```
				  [
				    {
				      "tcc": "kTCCServiceAddressBook",
				      "serviceName": "CONTACTS",
				      "url": "x-apple.systempreferences:com.apple.preference.security?Privacy_Contacts"
				    },
				    {
				      "tcc": "kTCCServiceReminders",
				      "serviceName": "REMINDERS",
				      "url": "x-apple.systempreferences:com.apple.preference.security?Privacy_Reminders"
				    },
				    {
				      "tcc": "kTCCServiceBluetoothAlways",
				      "serviceName": "BLUETOOTH",
				      "url": "x-apple.systempreferences:com.apple.preference.security?Privacy_Bluetooth"
				    },
				  ```
				- ...
		- [Identifying System Preferences Panes - macOS Adventures](https://www.macosadventures.com/2022/02/10/identifying-system-preferences-panes/)
			- unread, looks possibly relevant
	-