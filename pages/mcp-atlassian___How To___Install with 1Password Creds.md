alias:: [[Atlassian/MCP/How To set up Atlassian MCP in Cursor with 1Password credentials]]
tags:: [[CursorAI/Settings/MCP]]

- # How to set up mcp-atlassian in [[CursorAI/Settings/MCP]] using 1Password
	- ## 1 - Store Atlassian credentials in [[1Password]]
		- ### For Cloud deployment:
			- Create entries in 1Password for:
				- Confluence:
					- URL (e.g., https://your-company.atlassian.net/wiki)
					- Username (your.email@company.com)
					- API Token (from Atlassian account settings)
				- Jira:
					- URL (e.g., https://your-company.atlassian.net)
					- Username (your.email@company.com)
					- API Token (from Atlassian account settings)
		- ### For Server/Data Center deployment:
			- Create entries in 1Password for:
				- Confluence:
					- URL (e.g., https://confluence.your-company.com)
					- Personal Access Token
					- SSL Verify setting (true/false)
				- Jira:
					- URL (e.g., https://jira.your-company.com)
					- Personal Access Token
					- SSL Verify setting (true/false)
	- ## 2 - OPTIONAL - [[1Password/Dev/CLI/Shell Plugin/Atlassian/How To/Set Up]]
		- This will enable secure access to your Atlassian credentials
	- ## 3 - Install the [[op/run]] wrapper for the [[Atlassian/MCP]] server
		- Install the following script into `~/.cursor/atlassian-mcp/start-atlassian-mcp.sh`
			- ### 1 - `mkdir -p ~/.cursor/atlassian-mcp`
			- ### 2 - `cursor ~/.cursor/atlassian-mcp/start-atlassian-mcp.sh`
			- ### 3 - paste in the `start-atlassian-mcp.sh` script
				- ```zsh
				  #!/usr/bin/env zsh
				  #
				  # Name: start-atlassian-mcp.sh
				  #
				  # Purpose:
				  #   - Securely retrieve Atlassian credentials from 1Password
				  #   - Inject the credentials as environment variables to Docker via `op run`
				  #   - Serve as a wrapper command for Cursor's MCP server configuration
				  #
				  # Installation:
				  #   1. Save this file in a secure location, for example:
				  #        ~/.cursor/atlassian-mcp/start-atlassian-mcp.sh
				  #
				  #   2. Make it executable:
				  #        chmod +x ~/.cursor/atlassian-mcp/start-atlassian-mcp.sh
				  #
				  #   3. In your ~/.cursor/mcp.json, point the "command" to this script.
				  
				  # Fail immediately if any command exits non-zero
				  set -euo pipefail
				  
				  ################################################################################
				  # Configuration - Update these to match your 1Password setup
				  ################################################################################
				  
				  # Vault name in 1Password
				  VAULT="Private"
				  
				  # For Cloud deployment:
				  CONFLUENCE_ITEM="Atlassian Confluence Cloud"
				  CONFLUENCE_URL_FIELD="url"
				  CONFLUENCE_USERNAME_FIELD="username"
				  CONFLUENCE_TOKEN_FIELD="api_token"
				  
				  JIRA_ITEM="Atlassian Jira Cloud"
				  JIRA_URL_FIELD="url"
				  JIRA_USERNAME_FIELD="username"
				  JIRA_TOKEN_FIELD="api_token"
				  
				  # For Server/Data Center deployment (uncomment and modify as needed):
				  # CONFLUENCE_ITEM="Atlassian Confluence Server"
				  # CONFLUENCE_URL_FIELD="url"
				  # CONFLUENCE_TOKEN_FIELD="personal_token"
				  # CONFLUENCE_SSL_VERIFY="false"
				  
				  # JIRA_ITEM="Atlassian Jira Server"
				  # JIRA_URL_FIELD="url"
				  # JIRA_TOKEN_FIELD="personal_token"
				  # JIRA_SSL_VERIFY="false"
				  
				  ################################################################################
				  # Main Script
				  ################################################################################
				  
				  # Create environment file content using 1Password secret references
				  ENV_FILE_CONTENT="
				  CONFLUENCE_URL=op://${VAULT}/${CONFLUENCE_ITEM}/${CONFLUENCE_URL_FIELD}
				  CONFLUENCE_USERNAME=op://${VAULT}/${CONFLUENCE_ITEM}/${CONFLUENCE_USERNAME_FIELD}
				  CONFLUENCE_API_TOKEN=op://${VAULT}/${CONFLUENCE_ITEM}/${CONFLUENCE_TOKEN_FIELD}
				  JIRA_URL=op://${VAULT}/${JIRA_ITEM}/${JIRA_URL_FIELD}
				  JIRA_USERNAME=op://${VAULT}/${JIRA_ITEM}/${JIRA_USERNAME_FIELD}
				  JIRA_API_TOKEN=op://${VAULT}/${JIRA_ITEM}/${JIRA_TOKEN_FIELD}
				  "
				  
				  # For Server/Data Center, uncomment and add:
				  # CONFLUENCE_SSL_VERIFY=${CONFLUENCE_SSL_VERIFY}
				  # JIRA_SSL_VERIFY=${JIRA_SSL_VERIFY}
				  
				  # Use process substitution to avoid saving credentials to disk
				  op run \
				    --env-file <(echo "${ENV_FILE_CONTENT}") \
				    -- \
				    docker run -i --rm \
				      -e CONFLUENCE_URL \
				      -e CONFLUENCE_USERNAME \
				      -e CONFLUENCE_API_TOKEN \
				      -e JIRA_URL \
				      -e JIRA_USERNAME \
				      -e JIRA_API_TOKEN \
				      ghcr.io/sooperset/mcp-atlassian:latest
				  ```
			- ### 4 - customize configuration in `start-atlassian-mcp.sh` script
				- Update the configuration section to match your 1Password setup:
					- `VAULT`: Your 1Password vault name
					- Item names and field names for your Confluence and Jira credentials
					- For Server/Data Center deployment, uncomment and modify the relevant sections
			- ### 5 - `chmod +x ~/.cursor/atlassian-mcp/start-atlassian-mcp.sh`
				- Make the script executable
			- ### 6 - try running `~/.cursor/atlassian-mcp/start-atlassian-mcp.sh`
				- A dialog will pop up granting access to the vault
				- If successful, you should see the MCP server starting
				- `Ctrl+C` to exit
	- ## 4 - update [[CursorAI/.cursor/mcp.json]] to reference the wrapper
		- ### 1 - `cursor ~/.cursor/mcp.json`
			- Edit this file to reference the startup script - be sure to update `<YOUR_USERNAME>`
			- ```json
			  {
			    "mcpServers": {
			      "mcp-atlassian": {
			        "command": "/Users/<YOUR_USERNAME>/.cursor/atlassian-mcp/start-atlassian-mcp.sh",
			        "args": []
			      }
			    }
			  }
			  ```
		- ### 2 - authorize cursor with biometrics
			- You may get multiple authorization prompts
	- ## 5 - test out MCP
		- ### 1 - In [[CursorAI/Agent Mode]] try "Can you search for pages in Confluence containing 'getting started'"
			- You should get back search results
		- ### 2 - Press `Cmd+Shift+J` to open [[CursorAI/Settings/MCP]], view the `mcp-atlassian` item - press refresh
			- It should turn green if the connection is successful