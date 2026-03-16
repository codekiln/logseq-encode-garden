tags:: [[Claude Code]], [[Diataxis/How To]]
see-also:: [[Claude Code]]

- # How To Answer the Permission Dialog To Record Wildcard Permissions in Local Settings
	- ## Overview
		- When [[Claude Code]] asks for permission to run a command, you can edit the suggested permission entry before confirming to make it a wildcard that covers a broader class of commands.
		- This lets you grant bounded-but-flexible permissions that persist in `.claude/settings.local.json` without having to manually edit that file.
	- ## Prerequisites
		- [[Claude Code]] installed and running in a project
		- A session where Claude has just asked for permission to run a shell command
	- ## Steps
		- ### 1. Wait for the permission prompt
			- Claude will display a prompt asking whether to allow a specific command, e.g.:
				- ~~~
				  Allow bash command?
				  1. Yes, allow once
				  2. Yes, allow bd --no-daemon --specific-flag value
				  3. No
				  ~~~
		- ### 2. Select option 2
			- Press `2` and Enter to select the "allow and remember" option.
			- The full specific command string will appear in an editable field.
		- ### 3. Edit the command to a wildcard
			- Use the **Delete** (or Backspace) key to remove the overly-specific trailing arguments.
			- Replace them with `*` to match any arguments with that prefix.
			- Example: `bd --no-daemon --specific-flag value` → `bd --no-daemon *`
		- ### 4. Confirm
			- Press Enter to confirm.
			- [[Claude Code]] writes the permission to `.claude/settings.local.json` in the form:
				- ~~~json
				  "Bash(bd --no-daemon *)"
				  ~~~
		- ### 5. Verify (optional)
			- Open `.claude/settings.local.json` and confirm the entry looks as expected.
	- ## Troubleshooting
		- **The field isn't editable** — some terminal emulators may not support inline editing at the prompt; try a different terminal.
		- **Too broad a wildcard** — avoid patterns like `rm *` that could allow destructive commands. Be specific enough to cover your use case without opening up unintended commands.
