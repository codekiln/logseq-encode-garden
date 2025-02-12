created-by:: [[Person/Ankit Pokhrel]]

- [[GitHub/ankitpokhrel/jira-cli]] defines a JIRA #CLI that's influenced by [[GitHub/CLI]].
	- It's written in [[Programming/Language/Go]]
- ## Jira Cli Installation
	- One of the available installation targets is using [[Docker]]
		- `docker run -it --rm ghcr.io/ankitpokhrel/jira-cli:latest`
			- this enters an interactive terminal. by default, this doesn't use any volume mounts, so if you want to create issues from local markdown pages, you'd have to modify that to include volume mounts.
	- ### Auth
		- [What are different ways of setting the Jira API token? · ankitpokhrel/jira-cli · Discussion #356](https://github.com/ankitpokhrel/jira-cli/discussions/356)
			- **3 ways** to set your Jira API token
				- **1 -** environment variable [[EnvVar]] - [[JIRA/CLI/EnvVar/JIRA_API_TOKEN]]
				- **2 - **[[dotfiles/.netrc]]
				- keychain password manager
- ## [[JIRA/CLI/Commands]] - see [here](https://github.com/ankitpokhrel/jira-cli?tab=readme-ov-file#commands)
	-