tags:: [[MCP]], [[Atlassian]], [[Q]]
- # Can [[Atlassian]] [[MCP]] authentication be system wide and cached?
	- When signing in to Atlassian MCP in Cursor via OAuth in the browser, the authentication does not persist to other tools like [[Claude Code]] or cursor-agent CLI.
	- ## Answer
		- **Short answer**: Yes, but only if all tools use [[mcp-remote]] with *identical* configurations. Otherwise, each tool requires separate authentication.
		- ### How mcp-remote stores credentials
			- `mcp-remote` stores OAuth tokens in `~/.mcp-auth` (or `$MCP_REMOTE_CONFIG_DIR`)
			- Tokens are keyed by a **hash** of the server URL + resource flag + custom headers
			- If two tools invoke `mcp-remote` with the exact same arguments, they share the cached token
		- ### Why authentication doesn't persist across tools
			- Different tools store MCP configurations differently:
				- **Cursor**: `~/.cursor/mcp.json`
				- **Claude Code**: `~/.claude.json` (via `claude mcp add`)
				- **Claude Desktop**: `~/Library/Application Support/Claude/claude_desktop_config.json`
			- If the command arguments differ *at all* (even whitespace or argument order), `mcp-remote` generates a different hash → separate OAuth session
		- ### Solutions
			- #### Option 1: Ensure identical mcp-remote invocations
				- Configure each tool to use the *exact* same command:
				- ~~~json
				  {
				    "command": "npx",
				    "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/sse"]
				  }
				  ~~~
				- Once authenticated in one tool, other tools with identical config will reuse `~/.mcp-auth` tokens
			- #### Option 2: Use self-hosted mcp-atlassian with API tokens
				- The unofficial [[mcp-atlassian]] server supports API token authentication
				- Store your Atlassian API token in environment variables or [[1Password]]
				- No OAuth flow required — works identically across all tools
				- See [[mcp-atlassian/How To/Install with 1Password Creds]]
			- #### Option 3: Re-authenticate in each tool
				- Run `/mcp` in Claude Code and authenticate separately
				- Each tool maintains its own OAuth session
				- Tokens refresh automatically within each tool
		- ### Current limitations
			- The official [[Atlassian/MCP]] server (Rovo MCP) **requires OAuth 2.1** — API keys and OIDC are not supported
			- There is no central system-wide OAuth token store that all MCP clients share by design
			- `mcp-remote` is the closest to system-wide caching, but requires configuration consistency
	- ## My Notes
		- The root issue is that MCP client tools (Cursor, Claude Code, etc.) each have their own configuration systems and don't coordinate on how they invoke `mcp-remote`
		- A potential improvement would be for `mcp-remote` to normalize configurations before hashing, or for tools to adopt a shared MCP configuration standard
	- ## Related
		- [[MCP/Atlassian/Reference/Authentication API Key vs OAuth]]
		- [[Atlassian/MCP/How To/Set up in Cursor]]
		- [[mcp-atlassian]]
		- [[mcp-remote]]
		- [[Claude Code/Tutorial/Connect to MCP Servers]]
