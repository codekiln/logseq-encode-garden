tags:: [[MCP]], [[Atlassian]], [[Q]]
- # Can I authenticate an [[MCP]] server without loading it into context?
	- Sometimes you want to complete the OAuth flow for a remote MCP server (like [[Atlassian/MCP]]) before starting an AI coding session, so the tools are ready without interruption.
	- ## Answer
		- **Yes** — use `mcp-remote-client` to authenticate standalone from the command line.
		- ### Standalone authentication with mcp-remote-client
			- Run this command (no MCP client needed):
			- ~~~bash
			  npx -p mcp-remote@latest mcp-remote-client https://mcp.atlassian.com/v1/sse
			  ~~~
			- This will:
				- 1. Open a browser for the OAuth authorization flow
				- 2. Complete token exchange and store credentials in `~/.mcp-auth`
				- 3. Attempt to list the tools & resources at the remote URL (verifying success)
			- Once complete, any MCP client using `mcp-remote` with the same URL will reuse the cached token.
		- ### For Atlassian specifically
			- ~~~bash
			  # Authenticate to Atlassian MCP standalone
			  npx -p mcp-remote@latest mcp-remote-client https://mcp.atlassian.com/v1/sse
			  ~~~
			- You'll be prompted to select your Atlassian org and grant permissions
			- After success, Cursor/Claude Code/etc. can use the server without re-authenticating
		- ### Use cases
			- Pre-authenticate before starting a coding session
			- Debug authentication issues (clearer error messages than in-client)
			- Verify credentials after running `rm -rf ~/.mcp-auth`
			- Test connectivity to remote MCP servers
	- ## My Notes
		- This is also useful for debugging — if authentication fails inside Cursor or Claude Code, running `mcp-remote-client` shows more detailed error output
	- ## Related
		- [[MCP/Atlassian/Q/Can Atlassian authentication be system wide and cached]]
		- [[mcp-remote]]
		- [[Atlassian/MCP/How To/Set up in Cursor]]
