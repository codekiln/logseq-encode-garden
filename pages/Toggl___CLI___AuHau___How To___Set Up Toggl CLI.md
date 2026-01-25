tags:: [[Toggl]], [[CLI/Tool]], [[Diataxis/Tutorial]]

- # Tutorial: Set Up Toggl CLI
	- ## What You'll Create
		- A working Toggl CLI setup that allows you to interact with your Toggl Track account from the command line
		- You'll be able to start time entries, view current entries, list projects, and manage your time tracking using `toggl` commands
	- ## Prerequisites
		- A Toggl Track account (sign up at [toggl.com](https://toggl.com) if needed)
		- [[mise]] installed (per [[My Dev Tool Preferences]]) for managing environments and tools
		- [[uv]] available (mise can install it automatically with `mise use -g uv@latest`)
		- Basic familiarity with terminal/command prompt
	- ## Learning Goals
		- How to obtain a Toggl API token from your profile settings
		- How to install the Toggl CLI (`togglCli`) using `uv tool install` (per [[My Dev Tool Preferences]])
		- How to configure the CLI with your authentication token
		- How to verify your setup works
	- ## Steps
		- ### 1. Get Your Toggl API Token
			- Open your web browser and navigate to [track.toggl.com](https://track.toggl.com)
			- Sign in to your Toggl Track account if prompted
			- Click on your **Profile** in the sidebar (or click your name/email avatar)
			- Scroll down to find the **API Token** section near the bottom of your Profile Settings page
			- Click to reveal or view your API token
			- **Copy the token** - you'll need it in the next steps
			- Notice that this token provides access to your Toggl account, so keep it secure
			- The token is used to authenticate API requests to Toggl's services
		- ### 2. Install the Toggl CLI with uv
			- Open your terminal
			- Ensure `uv` is available (if managed by mise, it should already be on your PATH)
			- Install `togglCli` using `uv tool install` (per [[My Dev Tool Preferences]]):
				- ~~~bash
				uv tool install togglCli --pre
				~~~
			- Wait for the installation to complete
			- You should see a success message when installation finishes
			- Notice that `uv tool install` creates an isolated environment for the CLI tool, similar to pipx but faster
			- The tool is now available on your PATH as `toggl`
			- The pre-release version (`--pre`) includes the rewritten CLI with improved features
		- ### 3. Configure the CLI with Your Token
			- Run the Toggl CLI for the first time to trigger the bootstrap setup:
				- ~~~bash
				toggl --help
				~~~
			- The CLI will prompt you for setup information
			- When asked about authentication, you can either:
				- Enter your **username and password** (the CLI will convert these to an API token automatically), or
				- Enter your **API token directly** (use the token you copied in step 1)
			- The configuration will be saved to `~/.togglrc` on UNIX-like systems (macOS/Linux)
			- Notice that the bootstrap process creates the configuration file automatically
		- ### 4. Verify Your Setup
			- Test that the CLI is installed and working:
				- ~~~bash
				toggl --help
				~~~
			- You should see a list of available commands
			- Try viewing your current time entry to verify authentication:
				- ~~~bash
				toggl now
				~~~
			- If successful, you'll see information about your current time entry (or a message if no entry is running)
			- If you get an authentication error, double-check that your token was entered correctly during setup
		- ### 5. Try Starting a Time Entry (Optional)
			- Test starting a new time entry:
				- ~~~bash
				toggl start "Test entry"
				~~~
			- Replace "Test entry" with any description you want
			- You should see a success message confirming the time entry was started
			- Verify it's running:
				- ~~~bash
				toggl now
				~~~
			- You should see your active time entry displayed
			- Check your Toggl Track web interface to verify the entry appears there
		- ### 6. List Your Projects (Optional)
			- View your available projects:
				- ~~~bash
				toggl projects ls
				~~~
			- You should see a list of all your Toggl projects
			- This confirms that your authentication is working and you can access your Toggl data
	- ## What You've Learned
		- How to obtain a Toggl API token from your Profile Settings in Toggl Track
		- How to install the `togglCli` Python package using `uv tool install` with the pre-release flag (following [[My Dev Tool Preferences]])
		- How `uv tool install` creates isolated environments for CLI tools, preventing dependency conflicts
		- How to configure the CLI using the bootstrap setup process that creates `~/.togglrc`
		- How to verify your setup by checking current entries, starting entries, and listing projects
		- You can now use `toggl` commands to manage your time tracking from the terminal
	- ## Related
		- [[Toggl/CLI/AuHau]]
		- [[Toggl/AI/Report/26/01/AI control of Toggl - Options Jan 2026]]
		- [[Toggl/API]]
		- [AuHau/toggl-cli GitHub Repository](https://github.com/AuHau/toggl-cli)
		- [Toggl Track API Documentation](https://engineering.toggl.com/docs/)
		- [Toggl CLI Documentation](https://toggl.uhlir.dev/)
