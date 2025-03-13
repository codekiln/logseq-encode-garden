# [Suppressing background requests in IDEs](https://developer.1password.com/docs/ssh/agent/security/)
	- It’s **very common for IDEs and Git GUI clients to periodically run `git fetch` in the background** on currently open repositories.
		- This feature is often enabled by default and **may result in unexpected authorization prompts from 1Password**, especially if you're unaware of an application's auto-fetch behavior.
	- 1Password helps to **suppress prompts if it detects that the app or window the request originated from is not in the foreground**.
		- The 1Password icon in your device's menu bar, taskbar, or system tray **will display an indicator dot** when a prompt **has been suppressed**.
		- If you need to access the prompt, **select the 1Password icon** and select **SSH request waiting**. The authorization prompt will be brought to the foreground.