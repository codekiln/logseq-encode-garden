- **Remove a Zsh history entry and reload in all terminals**
	- **Find the command to remove**
		- ```sh
		  history | grep <command>
		  ```
	- **Delete the entry from history**
		- ```sh
		  history -d <line-number>
		  ```
	- **Remove it from the history file**
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