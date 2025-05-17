tags:: [[Diataxis/How To]], [[mise]], [[zsh]], [[OhMyZsh]]

- # How To List Available [[mise/Tasks]] in zsh
	- ## Overview
		- **IMPORTANT NOTE** - If you have followed [[mise/How To/Install Mise Shell Completions in Zsh]], you should be able to just do [[mise/run]] then `tab` and get them autocompleted
		- This guide shows you **another** way to list and discover available mise tasks in your zsh shell
		- For developers who want to see what tasks they can run with `mise run <task-name>`
		- Includes how to view task descriptions and enable tab completion
	- ## Prerequisites
		- mise installed and activated in your shell
		- zsh with Oh My Zsh installed
		- At least one `mise.toml` file with defined tasks
	- ## Steps
		- ### 1. List All Available Tasks
			- Run the following command to see all available tasks:
			- ```bash
			  mise tasks ls
			  ```
			- This shows a table with:
				- Task name
				- Description (if provided)
				- Source (where the task is defined)
		- ### 2. View Extended Task Information
			- For more detailed information about tasks, use:
			- ```bash
			  mise tasks ls --extended
			  ```
			- This shows additional columns including:
				- Aliases
				- Dependencies
				- Hidden status
		- ### 3. Sort Tasks by Different Criteria
			- Sort tasks by name (default):
			- ```bash
			  mise tasks ls --sort name
			  ```
			- Sort by description:
			- ```bash
			  mise tasks ls --sort description
			  ```
			- Sort in descending order:
			- ```bash
			  mise tasks ls --sort name --sort-order desc
			  ```
		- ### 4. Show Hidden Tasks
			- To see tasks marked as hidden in your configuration:
			- ```bash
			  mise tasks ls --hidden
			  ```
		- ### 5. Enable Tab Completion
			- #### Basic Setup
				- Ensure mise is properly activated in your shell:
				- ```bash
				  eval "$(mise activate zsh)"
				  ```
				- Add to your `~/.zshrc` if not already present
			- #### Oh My Zsh Integration
				- Note: mise's tab completion may conflict with Oh My Zsh's completion system
				- If you experience issues, you can:
					- Disable Oh My Zsh's completion for mise commands
					- Or use mise's completion system exclusively
	- ## Troubleshooting
		- If tasks aren't showing up:
			- [[mise/How To/Install Mise Shell Completions in Zsh]]
			- Try running `mise doctor` to check your setup
		- If tab completion isn't working:
			- Ensure mise is properly activated in your shell
			- Check for conflicts with Oh My Zsh completions
			- Try running `mise completion zsh` to regenerate completions
		- If you see "command not found":
			- Make sure mise is in your PATH
			- Verify the activation line is in your `~/.zshrc`
	- ## Related
		- [[mise/How To/Install Mise Shell Completions in Zsh]]