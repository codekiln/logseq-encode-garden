created-by:: [[Person/codekiln]]

- # [Can anyone provide a full diff of default system keyboard shortcuts in VSCode vs in Cursor in Mac/Win etc? - Discussion - Cursor - Community Forum](https://forum.cursor.com/t/can-anyone-provide-a-full-diff-of-default-system-keyboard-shortcuts-in-vscode-vs-in-cursor-in-mac-win-etc/45333)
	- A colleague of mine showed me one way to do this:
		- Open the Command Palette (`Ctrl + Shift + P`).
		- Search for [[VSCode/Command/Preferences/Open/Default Keyboard Shortcuts JSON]] -  `Preferences: Open Default Keyboard Shortcuts (JSON)`.
		- This opens a read-only JSON file with all default keybindings.
		- Copy it and save it to {vscode,cursor}\_default\_bindings.js (by default, it’s not valid json).
		- use an AI model to sort it by `command`, then `when`, then `key`, then pretty print the json
		- use a differ on the resulting json files
	- Of course, it would be great if there was an easier way to easily view these results!