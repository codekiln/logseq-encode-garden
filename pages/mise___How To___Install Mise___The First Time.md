tags:: [[Diataxis/How To]]

- # How to Install Mise for the First Time
	- ## Goal
		- Install and configure mise, a tool for managing programming language runtimes and development tools.
	- ## Preconditions
		- A Unix-like operating system (macOS, Linux, or WSL)
		- Basic familiarity with the command line
		- Git installed (for version control)
	- ## Procedure
		- ### 1. Install the mise CLI
			- Run the following command in your terminal:
				- ~~~
				  curl https://mise.run | sh
				  ~~~
			- This will install mise to `~/.local/bin/mise`
			- Verify the installation:
				- ~~~
				  ~/.local/bin/mise --version
				  ~~~
			- If the curl command fails, try downloading the binary directly from [mise releases](https://github.com/jdx/mise/releases)
		- ### 2. Choose an Activation Method
			- #### Option A: Project-Specific Setup (Recommended for First-Time Users)
				- This option is best if you want to try mise with a specific project first
				- No shell configuration changes required
				- You'll need to prefix commands with `mise exec` or use `mise run`
				- Example:
					- ~~~
					  mise exec -- python --version
					  ~~~
			- #### Option B: Global Setup (Recommended for Regular Users)
				- This option makes mise available system-wide
				- Add the following to your shell's configuration file:
					- For bash (`~/.bashrc`):
						- ~~~
						  echo 'eval "$(~/.local/bin/mise activate bash)"' >> ~/.bashrc
						  ~~~
					- For zsh (`~/.zshrc`):
						- ~~~
						  echo 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc
						  ~~~
					- For fish (`~/.config/fish/config.fish`):
						- ~~~
						  echo '~/.local/bin/mise activate fish | source' >> ~/.config/fish/config.fish
						  ~~~
				- Restart your shell or source your configuration file
				- Verify activation:
					- ~~~
					  mise --version
					  ~~~
		- ### 3. Configure Your Projects
			- Create a `mise.toml` file in your project root to manage tools and tasks
			- Basic configuration example:
				- ~~~
				  [tools]
				  python = "3.13"
				  node = "20"
				  
				  [tasks]
				  test = "pytest"
				  lint = "ruff check ."
				  ~~~
			- For more advanced configuration options, see the [mise configuration guide](https://mise.jdx.dev/configuration.html)
	- ## Troubleshooting
		- ### Installation Issues
			- If the curl command fails, try downloading the binary directly from [mise releases](https://github.com/jdx/mise/releases)
			- Ensure `~/.local/bin` is in your PATH
		- ### Activation Issues
			- If `mise` command is not found after activation:
				- Check that the activation line was added correctly to your shell config
				- Verify the path to mise binary (`~/.local/bin/mise`)
				- Try restarting your shell
		- ### Project-Specific Issues
			- If mise doesn't pick up project configuration:
				- Run `mise config ls` to see which config files are active
				- Ensure you're in the project root directory
				- Check that your `mise.toml` file is properly formatted
	- ## Next Steps
		- Learn about [mise configuration](https://mise.jdx.dev/configuration.html)
		- Explore [available tools](https://mise.jdx.dev/tools.html)
		- Read about [task management](https://mise.jdx.dev/tasks.html)
	- ## References
		- [Official mise documentation](https://mise.jdx.dev/)
		- [mise installation guide](https://mise.jdx.dev/installing-mise.html)
		- [mise configuration guide](https://mise.jdx.dev/configuration.html)
		- [mise tools guide](https://mise.jdx.dev/tools.html)
		- [mise tasks guide](https://mise.jdx.dev/tasks.html)