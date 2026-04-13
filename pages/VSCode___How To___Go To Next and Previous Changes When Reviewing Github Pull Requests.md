# How to go to the next and previous changes in [[VSCode/Extension/GitHub Pull Requests]]? #Q
	- ### What is #[[Keyshort/User]] and [[VSCode/Command]] for going to the next diff in [[VSCode/Extension/GitHub Pull Requests]]?: #card
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-04-13T04:00:00.000Z
	  card-last-reviewed:: 2026-04-12T08:20:59.093Z
	  card-last-score:: 1
		- [[VSCode/Command/GitHub Pull Requests/Go to Next Diff in Pull Request]]
			- **Command Name**: GitHub Pull Requests: Go to Next Diff in Pull Request
			- [[VSCode/Keymap]]
				- ```json
				  {
				    "key": "alt+j",
				    "command": "pr.goToNextDiffInPr"
				  }
				  ```
	- ### What is #[[Keyshort/User]] and [[VSCode/Command]] for going to the previous diff in [[VSCode/Extension/GitHub Pull Requests]]?: #card
		- [[VSCode/Command/GitHub Pull Requests/Go to Previous Diff in Pull Request]]
			- **Command Name:** GitHub Pull Requests: Go to Previous Diff in Pull Request
			- [[VSCode/Keymap]]
				- ```json
				  {
				    "key": "alt+k",
				    "command": "pr.goToPreviousDiffInPr"
				  }
				  ```