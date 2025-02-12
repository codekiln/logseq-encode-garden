- **Remove a [[Zsh/History]] entry and reload in all terminals**
	- **Find the command to remove**
		- ```sh
		  history | grep <command>
		  ```
	- **Delete the entry from history**
		- Removes the command from the current session's in-memory history but does not remove it from `~/.zsh_history`.
		- ```sh
		  history -d <line-number>
		  ```
	- **Remove it from the history file**
		- Permanently deletes the command from the history file but does not affect the current session until the file is reloaded.
		- ```sh
		  sed -i '' '/<command>/d' ~/.zsh_history
		  ```
	- **Reload history in all terminals**
		- ```sh
		  killall -SIGUSR1 zsh
		  ```
	- **Verify the command is gone**
		- ```sh
		  history | grep <command>
		  ```