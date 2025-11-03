tags:: [[VSCode]], [[Terminal]], [[Diataxis/How To]]

- # How To Fix Ctrl+C Not Working in VS Code Integrated Terminal
	- ## Overview
		- This guide helps you fix issues where Ctrl+C (SIGINT) doesn't work to interrupt processes running in VS Code's integrated terminal
		- Useful when running long-lived processes like `caffeinate` or other commands that should be interruptible
		- Addresses VS Code terminal keybinding interception and signal handling issues
	- ## Prerequisites
		- VS Code installed and running
		- Access to VS Code settings
		- A command or process that needs to be interruptible with Ctrl+C
	- ## Steps
		- ### 1. Enable sendKeybindingsToShell Setting
			- Open VS Code Settings (Cmd+, on macOS or Ctrl+, on Windows/Linux)
			- Search for `terminal.integrated.sendKeybindingsToShell`
			- Check the box or set the value to `true`
			- This allows terminal keybindings to pass through to the shell instead of being intercepted by VS Code
		- ### 2. Configure commandsToSkipShell (Alternative Method)
			- Open VS Code Settings
			- Search for `terminal.integrated.commandsToSkipShell`
			- Click "Edit in settings.json"
			- Remove `workbench.action.terminal.sendSequence` from the array if present
			- Or ensure Ctrl+C keybindings are not blocked by other commands in this list
		- ### 3. Verify the Fix
			- Open a new integrated terminal in VS Code
			- Run a test command like `caffeinate -d -i -m -s` or `sleep 30`
			- Press Ctrl+C
			- The command should interrupt successfully
		- ### 4. Alternative: Use External Terminal (If Issue Persists)
			- If the integrated terminal still has issues, run long-lived processes in your system's native terminal application
			- On macOS: Open Terminal.app
			- On Windows: Open PowerShell or Command Prompt
			- On Linux: Open your default terminal emulator
			- Run your command there where Ctrl+C works reliably
		- ### 5. Alternative: Background Process and Kill by PID
			- If you must use VS Code terminal and Ctrl+C doesn't work:
			- Run your command in the background by appending `&`:
			  ~~~bash
			  caffeinate -d -i -m -s &
			  ~~~
			- Note the process ID (PID) that appears
			- When you need to stop it, run:
			  ~~~bash
			  kill <PID>
			  ~~~
			- Or use `pkill` to find and kill by process name:
			  ~~~bash
			  pkill -f caffeinate
			  ~~~
	- ## Troubleshooting
		- If Ctrl+C still doesn't work after enabling `sendKeybindingsToShell`:
			- Restart VS Code to ensure settings take effect
			- Check if you have VS Code extensions that might intercept terminal input
			- Verify your shell profile (`.zshrc`, `.bashrc`) doesn't override signal handling
		- If the setting doesn't appear in Settings UI:
			- Open `settings.json` directly (Cmd+Shift+P → "Preferences: Open User Settings (JSON)")
			- Add manually: `"terminal.integrated.sendKeybindingsToShell": true`
		- For commands that specifically ignore SIGINT:
			- Some processes like `caffeinate` may need SIGTERM instead:
			  ~~~bash
			  kill -TERM <PID>
			  ~~~
			- Or force kill with SIGKILL (use as last resort):
			  ~~~bash
			  kill -9 <PID>
			  ~~~
	- ## Related
		- [VS Code Terminal Advanced Documentation](https://code.visualstudio.com/docs/terminal/advanced)

