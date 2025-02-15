# [gh issue develop](https://cli.github.com/manual/gh_issue_develop)
	- `gh issue develop {<number> | <url>} [flags]`
	- Manage linked branches for an issue.
	- When using the `--base` flag, the new development branch will be created from the specified remote branch.
	- The new branch will be configured as the base branch for pull requests created using `gh pr create`.
	- ## Options
		- [[GitHub/CLI/gh/issue/develop/--base]]
			- `-b`, `--base <string>`
				- Name of the remote branch you want to make your new branch from
		- [[GitHub/CLI/gh/issue/develop/--branch-repo]]
			- `--branch-repo <string>`
				- Name or URL of the repository where you want to create your new branch
		- [[GitHub/CLI/gh/issue/develop/--checkout]]
			- `-c`, `--checkout`
				- Checkout the branch after creating it
		- [[GitHub/CLI/gh/issue/develop/--list]]
			- `-l`, `--list`
				- List linked branches for the issue
		- [[GitHub/CLI/gh/issue/develop/--name]]
			- `-n`, `--name <string>`
				- Name of the branch to create
	- ## #Examples
		- ```
		  # List branches for issue 123
		  $ gh issue develop --list 123
		  
		  # List branches for issue 123 in repo cli/cli
		  $ gh issue develop --list --repo cli/cli 123
		  
		  # Create a branch for issue 123 based on the my-feature branch
		  $ gh issue develop 123 --base my-feature
		  
		  # Create a branch for issue 123 and checkout it out
		  $ gh issue develop 123 --checkout
		  
		  # Create a branch in repo monalisa/cli for issue 123 in repo cli/cli
		  $ gh issue develop 123 --repo cli/cli --branch-repo monalisa/cli
		  ```