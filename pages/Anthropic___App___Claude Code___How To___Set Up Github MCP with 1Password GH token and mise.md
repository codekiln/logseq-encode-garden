alias:: [[GitHub/MCP/How To/Set up MCP in Claude Code with 1Password GH Token and mise]]
tags:: [[Diataxis/How To]]

- # How to set up a single-repository MCP with fine-grained permissions for a single repository
	- ## Impetus
		- From a security perspective, it's a good idea to maintain some discipline when integrating [[MCP Servers]]:
			- [[InvariantLabsAI/Blog/25/05/GitHub MCP Exploited: Accessing private repositories via MCP]] [here](https://invariantlabs.ai/blog/mcp-github-vulnerability) describes an attack that depends on mixing write-access to protected and unprotected repositories with [[GitHub Fine-Grained Personal Access Token]]s. Instead, github PAT security token hygiene dictates that each project should have its own fine-grained personal access token.
			- As described in [[GitHub/MCP/How To/Set up in Cursor with 1Password GH token]], it's better to use a [[Secrets Manager]] with [[Biometric]] authentication at the CLI, using [[op/run]] to wrap the GitHub MCP server in a [[1Password/Dev/CLI]] command which extracts the project token from the secrets manager after prompting for biometric authentication.
	- ## This guide describes how to define [[mise/Tasks]] which
		- 1 - will launch claude code in project-specific way similar to, but not identical to [[Anthropic/App/Claude Code/How To/Bootstrap Claude Code with Mise + UV-Powered Okta Role Assumption]].
		- 2 - launch a [[GitHub/MCP]] server in a way that wraps it in [[op/run]], referencing the [[1Password Secret Reference]] pointing to the [[GitHub Fine-Grained Personal Access Token]] for that repository.
	- ## Prerequisites
		- 1 - a [[GitHub/Repo]] has already been created and has some content in it. It does not matter if it is public or private, but it should be owned by you.
		- 2 - A [[GitHub Fine-Grained Personal Access Token]] has already been created that grants several repository permissions to just the project repository, such as the ability to read and write issues. The token has been stored in [[1Password]].
		- 3 - a home directory [[mise/Config/mise.toml]] has been created with a run configuration this in it (see also [[Anthropic/App/Claude Code/How To/Bootstrap Claude Code with Mise + UV-Powered Okta Role Assumption]] for context)
			- ```toml
			  [tasks.claude]
			  # run mise install && mise reshim before running this.
			  description = "Run Claude Code CLI"
			  run = "npx @anthropic-ai/claude-code $@"
			  ```
	- ## Procedure
		- ### 1  Add a private env file
			- Create **`github-mcp.env`** in the project root:
			  ~~~env
			  # **DO NOT COMMIT THIS FILE**
			  GITHUB_PERSONAL_ACCESS_TOKEN=op://DevSecrets/<repo>-gh-pat/token
			  ~~~
			- Ensure `.gitignore` excludes both `.env` and `github-mcp.env`, as different developers may have different secrets references.
		- ### 2  Define the [[GitHub/MCP]] [[mise/Task]] task [[mise/Config/mise.toml]] along with a task to run [[MCP/Inspector]] to test it, using [[1Password/Dev/op/run]] to load a [[GitHub Fine-Grained PAT]] [[1Password Secret Reference]] from an [[EnvVar/.env]] file
			- ~~~toml
			  
			  [tasks.gh-mcp]
			  description = "Start GitHub MCP server (using github-mcp.env)"
			  alias       = "mcp"
			  run = '''
			  #!/usr/bin/env bash
			  set -euo pipefail
			  op run --env-file=github-mcp.env -- \
			    docker run -i --rm \
			      -e GITHUB_PERSONAL_ACCESS_TOKEN \
			      ghcr.io/github/github-mcp-server
			  '''
			  
			  [tasks.gh-mcp-inspect]
			  description = "Launch MCP Inspector UI against gh-mcp"
			  alias       = "inspect"
			  run = '''
			    #!/usr/bin/env bash
			    set -euo pipefail
			    # Pass "mise run gh-mcp" so Inspector starts the server itself
			    # you will then need to
			    npx -y @modelcontextprotocol/inspector mise run gh-mcp
			  '''
			  
			  ~~~
			-
		- ### 3  Test the connection to the GitHub MCP Server with [[MCP/Inspector]]
			- 1 - run `mise run gh-mcp-inspect`
				- This will output a localhost port which you should click on in order to view it in your browser.
			- 2 - (in browser) - click Connect
			- 3 - test out the connection by using one of the tools that are enabled for the [[GitHub Fine-Grained Access Token]] you supplied in `github-mcp.env`, for example, `get_issue`
			- Once the connection is successful, proceed. If the connection is not successful, debug here before continuing.
		- ### 4  Create a project-scoped `.mcp.json` and run [[Claude Code]] to test
			- 1 - Either enter `mise run claude mcp add gh -s project mise run gh-mcp`, which will create this file in the repository root:
				- ~~~json
				  {
				    "mcpServers": {
				      "gh": {
				        "type": "stdio",
				        "command": "mise",
				        "args": [
				          "run",
				          "gh-mcp"
				        ],
				        "env": {}
				      }
				    }
				  }
				  ~~~
			- 2 - `mise run claude` to open claude code, which should read the file above
			- 3 - the first time, you will need to give permission to claude to use this MCP server
			- 4 - use `/mcp` command to check out mcp connection inside of claude
			- 4 - ask Claude to execute the same tool you used to test the GitHub MCP Server. For example, if you endowed the PAT with the permission to read issues, try
				- > Let's test your MCP connection - can you find the first github issue?
				- ```
				  > Let's test your MCP connection - can you find the first github issue?
				  
				  ⏺ I'll use the GitHub API to search for the first issue in this repository.
				  
				  ⏺ gh:list_issues (MCP)(owner: "boingo", repo: "langgraph-assistant-migrator", state: "all", sort: "created", direction: "asc")
				    ⎿  Error: MCP error -32603: failed to list issues: GET https://api.github.com/repos/boingo/langgraph-assistant-migrator/issues?direction=asc&sort=created&state=all: 404 Not Found []
				    ⎿  Interrupted by user
				  
				  > you have tried `boingo` instead of using git to inspect this repository's owner - why?
				  
				  ⏺ You're right, I made an assumption without checking the repository owner. Let me check the git configuration to find the correct owner.
				  
				  ⏺ Bash(git config --get remote.origin.url)
				    ⎿  git@github.com:codekiln/langgraph-assistant-migrator.git
				  
				  ⏺ Now I'll try again with the correct owner:
				  
				  ⏺ gh:list_issues (MCP)(owner: "codekiln", repo: "langgraph-assistant-migrator", state: "all", sort: "created", direction: "asc")
				    ⎿  [
				         {
				           "id": 3121550442,
				           "number": 1,
				       … +49 lines (ctrl+r to expand)
				  
				  ⏺ Found it. Issue #1 is titled "test issue" with description "test issue description", created by codekiln.
				  ```
				- It should succeed. If it does not, debug, comparing to the output of MCP Inspector.
	- ## Troubleshooting
		- **401 Unauthorized** — verify PAT scopes and the secret reference in `github-mcp.env`.
		- **`github-mcp.env` missing** — copy the template in *Step 1* and add your secret reference.
	- ## References
		- [[Anthropic/App/Claude Code/Docs/Tutorial/Set up Model Context Protocol]] [here](https://docs.anthropic.com/en/docs/claude-code/tutorials#set-up-model-context-protocol-mcp)
		- [Fine-grained PAT creation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#fine-grained-personal-access-tokens)
		- [1Password CLI — `op run`](https://developer.1password.com/docs/cli/secrets-scripts/)
		- [GitHub MCP Server README](https://github.com/github/github-mcp-server)
		- [mise Tasks](https://mise.jdx.dev/tasks/) · [mise Environments](https://mise.jdx.dev/environments/)