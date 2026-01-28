alias:: [[GitHub/MCP/How To set up GitHub MCP in Cursor with 1Password fine-grained access token]]
tags:: [[CursorAI/Settings/MCP]], [[Diataxis/How To]]

- # How to set up a [[GitHub Fine-Grained Access Token]], store it in [[1Password]], and reference this in a GitHub [[MCP Server]] registered in [[CursorAI/.cursor/mcp.json]]
	- ## 1 - Follow [[GitHub/CLI/How to create a Fine Grained Personal Access Token]] to create a token
		- See also [[GitHub/API/Q/Is there a description of each API endpoint and what it can do]] - eventually, consider creating a page to do incremental requirements elicitation on which features are and are not needed.
		- After the token is created a dialog will pop up with a summary of , store it in [[1Password]]
			- In the notes,
	- ## 2 - OPTIONAL - [[1Password/Dev/CLI/Shell Plugin/GitHub/How To/Set Up]]
		- This will enable you to set up a connection between [[gh]] and 1Password
	- ## 3 - Install the [[op/run]] wrapper for the [[GitHub/MCP]] server
		- Install the following script into `~/.cursor/github-mcp/start-github-mcp.sh`
			- **note**: there may be better ways to do this - for example, it may be possible to do this by developing a custom [[1Password/Dev/CLI/Shell Plugin]] as described in [Build your own shell plugins (beta) | 1Password Developer](https://developer.1password.com/docs/cli/shell-plugins/contribute/)
				- ### 1 - `mkdir -p ~/.cursor/github-mcp`
				- ### 2 - `cursor ~/.cursor/github-mcp/start-github-mcp.sh`
				- ### 3 - paste in the `start-github-mcp.sh` script
					- ```zsh
					  #!/usr/bin/env zsh
					  #
					  # Name: start-github-mcp.sh
					  #
					  # Purpose:
					  #   - Securely retrieve a GitHub Personal Access Token (PAT) from 1Password
					  #   - Inject the token as an environment variable to Docker via `op run`
					  #   - Serve as a wrapper command for Cursor's MCP server configuration
					  #
					  # Installation:
					  #   1. Save this file in a secure location, for example:
					  #        ~/.cursor/github-mcp/start-github-mcp.sh
					  #
					  #   2. Make it executable:
					  #        chmod +x ~/.cursor/github-mcp/start-github-mcp.sh
					  #
					  #   3. In your ~/.cursor/mcp.json, point the "command" to this script. For example:
					  #        {
					  #          "mcpServers": {
					  #            "github": {
					  #              "command": "/Users/your-username/.cursor/github-mcp/start-github-mcp.sh",
					  #              "args": []
					  #            }
					  #          }
					  #        }
					  #
					  #
					  # Usage:
					  #   - Ensure `op` is installed and you're signed in to 1Password via the CLI.
					  #   - The script will automatically retrieve your GitHub PAT at runtime.
					  #   - No sensitive data will be written to disk.
					  
					  # Fail immediately if any command exits non-zero
					  set -euo pipefail
					  
					  ################################################################################
					  # Configuration
					  ################################################################################
					  
					  # Update these to match the vault/item/field in 1Password
					  VAULT="Private"
					  ITEM="GitHub MCP Token"
					  FIELD="token"
					  
					  ################################################################################
					  # Main Script
					  ################################################################################
					  
					  # 1. use the 1password secrets reference syntax to get the token
					  # See also https://developer.1password.com/docs/cli/secret-reference-syntax/#:~:text=To%20get%20a%20secret%20reference,reference%20from%20the%20JSON%20output.
					  ENV_FILE_CONTENT="GITHUB_PERSONAL_ACCESS_TOKEN=op://${VAULT}/${ITEM}/${FIELD}"
					  
					  # 2. Use process substitution to avoid saving a real .env file to disk
					  op run \
					    --env-file <(echo "${ENV_FILE_CONTENT}") \
					    -- \
					    docker run -i --rm \
					      -e GITHUB_PERSONAL_ACCESS_TOKEN \
					      ghcr.io/github/github-mcp-server
					  ```
				- ### 4 - customize configuration in `start-github-mcp.sh` script
					- customize this to match the values for where your github API token is stored
					- ```zsh
					  ################################################################################
					  # Configuration
					  ################################################################################
					  
					  # Update these to match the vault/item/field in 1Password
					  VAULT="Private"
					  ITEM="GitHub MCP Token"
					  FIELD="token"
					  ```
				- ### 5 - `chmod +x ~/.cursor/github-mcp/start-github-mcp.sh`
					- make the script executable
				- ### 6 - try running `~/.cursor/github-mcp/start-github-mcp.sh`
					- a dialog will pop up granting access to the vault
					- if successful, you should see `GitHub MCP Server running on stdio` as the last line of output
					- `Ctrl+C` to get out
	- ## 4 - update [[CursorAI/.cursor/mcp.json]] to reference the wrapper
		- ### 1 - `cursor ~/.mcp.json`
			- Edit this file to reference the startup script - be sure to update `<YOUR_USERNAME>`
			- ```json
			  {
			      "mcpServers": {
			        "github": {
			          "command": "/Users/<YOUR_USERNAME>/.cursor/github-mcp/start-github-mcp.sh",
			          "args": []
			        }
			      }
			    }
			  ```
		- ### 2 - authorize cursor with biometrics
			- I personally got three pop-ups - not sure why
	- ## 5 - test out MCP
		- ### 1 - In [[CursorAI/Agent]] try "Can you tell me what <YOUR_GITHUB_USERNAME>'s repositories you have access to"
			- you should get back a list
		- ### 2 - Press `Cmd+Shift+J` to open [[CursorAI/Settings/MCP]], view the `github` item - press refresh
			- it should turn green
		-
		-