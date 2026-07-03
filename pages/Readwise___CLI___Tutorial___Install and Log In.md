tags:: [[Readwise]], [[CLI/Tool]], [[Diataxis/Tutorial]]
see-also:: [[readwise-cli]], [[Readwise/CLI]], [[Readwise/Reader]], [[rw-cli]]

- # Tutorial: Install and Log In to the Readwise CLI
	- ## What You'll Create
		- A working install of the official [[readwise-cli]] `readwise` command, authenticated to your account, ready to search and read your [[Readwise]] and [[Readwise/Reader]] library from the terminal.
	- ## Prerequisites
		- A Readwise account (sign up at [readwise.io](https://readwise.io) if needed)
		- Node.js and `npm` (version 18 or later)
		- Basic familiarity with the terminal
	- ## Learning Goals
		- How to install the official `@readwise/cli` package
		- How to authenticate with browser OAuth (`readwise login`)
		- How to authenticate headlessly with an access token (`readwise login-with-token`) for scripts, CI, and AI agents
		- How to confirm the CLI is set up and discover its commands
	- ## Steps
		- ### 1. Install the CLI
			- Open your terminal and install the package globally:
				- ~~~bash
				  npm install -g @readwise/cli
				  ~~~
			- Confirm the install by checking the version:
				- ~~~bash
				  readwise --version
				  ~~~
			- You will see a version number printed.
			- Notice that in this garden the CLI is already pinned in `mise.toml`, so running `mise install` from the repo root provides the `readwise` command without a global npm install.
		- ### 2. Log In with Your Browser (Recommended)
			- Start the OAuth flow:
				- ~~~bash
				  readwise login
				  ~~~
			- Your default browser opens a Readwise authorization page.
			- Sign in if prompted, then approve access.
			- Return to the terminal — you will see a confirmation that you are logged in.
		- ### 3. Log In with a Token (Headless / CI / Agents)
			- Use this path instead when there is no browser — a server, a CI job, or an AI agent session.
			- Open [readwise.io/access_token](https://readwise.io/access_token) and copy your access token.
			- Authenticate with the token:
				- ~~~bash
				  readwise login-with-token YOUR_TOKEN_HERE
				  ~~~
			- Replace `YOUR_TOKEN_HERE` with the token you copied.
			- Notice that this token grants full access to your account — keep it secret, and prefer a per-user login over committing it anywhere.
		- ### 4. Confirm You're Set Up
			- Check your configuration:
				- ~~~bash
				  readwise config show
				  ~~~
			- List the available commands:
				- ~~~bash
				  readwise --help
				  ~~~
			- Notice that once you are authenticated, commands like `reader` and `search` appear that were hidden before login.
		- ### 5. Run Your First Search
			- Search your library for a topic you've read about:
				- ~~~bash
				  readwise search "logseq"
				  ~~~
			- You will see matching results drawn from across your highlights and documents.
			- Explore what else you can do — each command has its own help:
				- ~~~bash
				  readwise reader --help
				  ~~~
	- ## What You've Learned
		- How to install the official `@readwise/cli`
		- How to authenticate both interactively (`readwise login`) and headlessly (`readwise login-with-token`)
		- How to confirm your setup and discover the command surface
		- You can now search and read your library from the terminal — see [[readwise-cli]] for the full feature set, and `readwise skills` for the AI-agent workflow skills vendored in this garden.
	- ## Related
		- [Readwise CLI (official)](https://readwise.io/cli)
		- [Readwise API Documentation](https://readwise.io/api_deets)
		- [Readwise Reader API Documentation](https://readwise.io/reader_api)
