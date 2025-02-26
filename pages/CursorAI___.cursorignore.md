alias:: [[.cursorignore]]

- # .cursorignore
	- ## Overview
		- The `.cursorignore` file is a configuration file that lets you exclude files and directories from Cursor's codebase indexing
		- It follows the same syntax as `.gitignore`
		- Located in the root of your project
	- ## Key Features
		- ### Respects .gitignore
			- Files listed in `.gitignore` are automatically ignored by default
			- `.cursorignore` can be used to specify **additional** files to ignore
		- ### Scope (Updated in [[CursorAI/v/0.46 - Agent is ready and UI Refresh]])
			- Files in `.cursorignore` are now:
				- Blocked from being added in chat
				- Blocked from being sent up for tab completions
				- Excluded from codebase indexing
			- For indexing-only control, use the new `.cursorindexingignore` file
	- ## Example Configurations
		- ### Ignore Specific Files
			- Here's how to ignore specific files and patterns:
				- ~~~sh
				  # Ignore all files in the `dist` directory
				  dist/
				  
				  # Ignore all `.log` files
				  *.log
				  
				  # Ignore specific file `config.json`
				  config.json
				  ~~~
		- ### Include Only Specific Files
			- Here's how to include only certain files (e.g., only Python files in the `app` directory):
				- ~~~sh
				  # ignore everything
				  *
				  # do not ignore app
				  !app/
				  # do not ignore directories inside app
				  !app/*/
				  !app/**/*/
				  # don't ignore python files
				  !*.py
				  ~~~
	- ## Troubleshooting
		- The ignore file syntax follows `.gitignore` patterns exactly
		- For troubleshooting, search for similar `.gitignore` issues on platforms like StackOverflow
		- Common example: To ignore all files except those with a specific extension, you need to:
			- 1. First ignore everything
			- 2. Then explicitly allow directories
			- 3. Finally allow the specific file extension
	- ## References
		- [Official Cursor Documentation on Ignore Files](https://docs.cursor.com/context/ignore-files)
		- [Git documentation on gitignore patterns](https://git-scm.com/docs/gitignore)
		- [Cursor Changelog - v0.46](https://www.cursor.com/changelog/agent-is-ready-and-ui-refresh)