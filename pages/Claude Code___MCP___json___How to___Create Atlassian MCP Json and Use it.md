alias:: [[Claude Code/MCP/json/How To/Create Atlassian MCP Json and Use it]], [[Anthropic/App/Claude Code/MCP/json/How to/Create Atlassian MCP Json and Use it]]
tags:: [[Diataxis/How To]], [[Claude Code]], [[MCP]], [[Atlassian]]

- # How to create Atlassian MCP json and use it with Claude Code
	- ## Overview
		- Use this when you want one session-specific MCP config file that loads only the official Atlassian remote SSE MCP server.
	- ## Prerequisites
		- `claude` CLI is installed and available in your shell.
		- `node` and `npx` are available in your shell.
		- You can sign in to your Atlassian Cloud org in a browser.
	- ## Steps
		- ### 1. Create a JSON file with one MCP server
			- Create a file such as `atlassian-only.mcp.json` with exactly one server definition:
			- ~~~json
			  {
			    "mcpServers": {
			      "atlassian": {
			        "command": "npx",
			        "args": [
			          "-y",
			          "mcp-remote",
			          "https://mcp.atlassian.com/v1/sse"
			        ]
			      }
			    }
			  }
			  ~~~
		- ### 2. Start Claude with that MCP config
			- Run:
			- ~~~bash
			  claude --mcp-config ./atlassian-only.mcp.json --strict-mcp-config
			  ~~~
			- Use `--strict-mcp-config` so only servers from this file are loaded.
		- ### 3. Complete OAuth once prompted
			- When `[[mcp-remote]]` opens your browser, sign in and grant access to the Atlassian site you want.
			- After successful auth, tokens are cached in `~/.mcp-auth`.
		- ### 4. Verify inside Claude
			- Run `/mcp` in Claude Code and confirm the Atlassian server is listed.
			- Run a simple Atlassian tool call to confirm connectivity.
	- ## Troubleshooting
		- If auth loops or fails, clear local cache and retry:
			- `rm -rf ~/.mcp-auth`
		- If `mcp-remote` is not found, verify `node`/`npx` are installed and available in `PATH`.
	- ## Related
		- [[Claude Code]]
		- [[mcp-remote]]
		- [[MCP/Atlassian/Q/Can Atlassian authentication be system wide and cached]]
		- [[MCP/Atlassian/Q/Can I authenticate without loading the server into context]]
