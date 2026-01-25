tags:: [[Readwise]], [[CLI/Tool]], [[Diataxis/Tutorial]]

- # Tutorial: Get Auth Token and Set Up Readwise CLI
	- ## What You'll Create
		- A working Readwise CLI setup that allows you to interact with your Readwise Reader library from the command line
		- You'll be able to add articles, list documents, and manage your reading list using `rw-cli` commands
	- ## Prerequisites
		- A Readwise account (sign up at [readwise.io](https://readwise.io) if needed)
		- Python 3.7 or later installed on your system
		- Basic familiarity with terminal/command prompt
	- ## Learning Goals
		- How to obtain a Readwise API access token
		- How to install the Readwise Reader CLI (`rw-cli`)
		- How to configure the CLI with your authentication token
		- How to verify your setup works
	- ## Steps
		- ### 1. Get Your Readwise Access Token
			- Open your web browser and navigate to [readwise.io/access_token](https://readwise.io/access_token)
			- Sign in to your Readwise account if prompted
			- You'll see your access token displayed on the page
			- **Copy the token** - you'll need it in the next steps
			- Notice that this token provides access to your Readwise account, so keep it secure
			- The token format is used in API requests with the header: `Authorization: Token YOUR_TOKEN_HERE`
		- ### 2. Install the Readwise Reader CLI
			- Open your terminal
			- Install `rw-cli` using pip:
				- ~~~bash
				pip install readwise-reader-cli
				~~~
			- Wait for the installation to complete
			- You should see a success message when installation finishes
		- ### 3. Configure the CLI with Your Token
			- Set your Readwise access token as an environment variable:
				- ~~~bash
				export READWISE_ACCESS_TOKEN="your_token_here"
				~~~
			- Replace `your_token_here` with the actual token you copied in step 1
			- Notice that we're using the environment variable `READWISE_ACCESS_TOKEN` which the CLI will automatically detect
			- **Optional:** To make this permanent, add the export command to your shell configuration file:
				- For zsh (macOS default): `~/.zshrc`
				- For bash: `~/.bashrc` or `~/.bash_profile`
				- Add the line: `export READWISE_ACCESS_TOKEN="your_token_here"`
		- ### 4. Verify Your Setup
			- Test that the CLI is installed and working:
				- ~~~bash
				rw-cli --help
				~~~
			- You should see a list of available commands
			- Try listing your documents to verify authentication:
				- ~~~bash
				rw-cli list
				~~~
			- If successful, you'll see a list of documents from your Readwise Reader library
			- If you get an authentication error, double-check that your token is set correctly
		- ### 5. Try Adding an Article (Optional)
			- Test adding a new article to your Reader library:
				- ~~~bash
				rw-cli add https://example.com/article
				~~~
			- Replace the URL with any article you want to save
			- You should see a success message confirming the article was added
			- Check your Readwise Reader to verify the article appears in your library
	- ## What You've Learned
		- How to obtain a Readwise API access token from the Readwise website
		- How to install the `rw-cli` Python package using pip
		- How to configure the CLI using the `READWISE_ACCESS_TOKEN` environment variable
		- How to verify your setup by listing documents and adding articles
		- You can now use `rw-cli` commands to manage your Readwise Reader library from the terminal
	- ## Related
		- [[Readwise/AI/Report/26/01/AI control of Readwise - Options Jan 2026]]
		- [[Readwise/CLI]]
		- [Readwise API Documentation](https://readwise.io/api_deets)
		- [Readwise Reader API Documentation](https://readwise.io/reader_api)
		- [rw-cli GitHub Repository](https://github.com/Scarvy/readwise-reader-cli)
