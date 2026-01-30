# [mcp-remote - npm](https://www.npmjs.com/package/mcp-remote)
	- Connect an MCP Client that only supports local (stdio) servers to a Remote MCP Server, with auth support.
	- [GitHub: geelen/mcp-remote](https://github.com/geelen/mcp-remote)
	- ## Overview
		- `mcp-remote` bridges the gap between MCP clients (like [[CursorAI]], [[Claude Code]], [[Claude Desktop]]) that only support stdio transport and remote MCP servers that use HTTP/SSE with OAuth authentication.
		- When a remote server like [[Atlassian/MCP]] requires OAuth 2.1, `mcp-remote` handles the browser-based authorization flow and token management locally.
	- ## Key Features
		- OAuth 2.1 authentication with browser-based flow
		- Token caching in `~/.mcp-auth` (system-wide)
		- HTTP and SSE transport strategies
		- Custom headers for API key auth
		- Multiple tenant support via `--resource` flag
		- Standalone authentication via `mcp-remote-client`
	- ## Security Analysis
		- **Assessment Date**: 2026-01-30
		- ### Overall Verdict: ✅ Safe to Use
			- This package has been vetted and is considered safe for use in development workflows.
		- ### Maintainer Credibility
			- **[[Person/Glen Maddern]]** (geelen)
				- 1.5K GitHub followers
				- Co-creator of [[CSS Modules]] and [[styled-components]]
				- Well-established in the frontend community
			- **[[Person/Sunil Pai]]** (threepointone)
				- 3.9K GitHub followers
				- Works at [[Cloudflare]] on Agents/AI platform
				- Creator of [[PartyKit]] and glamor
				- Prominent JavaScript developer
		- ### Package Health (via Snyk/Socket)
			- **Health Score**: 84/100
			- **Known Vulnerabilities**: None
			- **License**: MIT
			- **Weekly Downloads**: ~107K (Popular)
			- **Last Updated**: December 2025
			- **Maintenance**: Healthy release cadence
		- ### Dependencies (4 direct)
			- `express` — well-maintained web framework
			- `open` — opens URLs in browser (for OAuth)
			- `strict-url-sanitise` — URL validation
			- `undici` — HTTP client (Node.js core team maintained)
		- ### Security Practices
			- ✅ HTTPS enforced by default (requires `--allow-http` flag for HTTP)
			- ✅ Follows MCP OAuth 2.1 Authorization specification
			- ✅ Credentials stored locally (`~/.mcp-auth`), not transmitted
			- ✅ Per-server token isolation (hashed by URL + resource + headers)
			- ✅ Debug logging available for auth troubleshooting
		- ### Considerations
			- ⚠️ Marked as "experimental" by authors
			- ⚠️ No formal SECURITY.md policy in repo
			- ⚠️ Local tokens in `~/.mcp-auth` readable by other processes with user permissions
			- ⚠️ 59 open issues (typical for popular projects)
		- ### Recommendation
			- Safe for developer workstations. For enterprise/team use, consider:
				- Periodically clearing `~/.mcp-auth` and re-authenticating
				- Monitoring the repo for security advisories
				- Using the self-hosted [[mcp-atlassian]] with API tokens for more control
	- ## Usage
		- ### Basic Configuration
			- ~~~json
			  {
			    "mcpServers": {
			      "atlassian": {
			        "command": "npx",
			        "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/sse"]
			      }
			    }
			  }
			  ~~~
		- ### Standalone Authentication
			- Authenticate without loading the MCP server into an AI context:
			- ~~~bash
			  npx -p mcp-remote@latest mcp-remote-client https://mcp.atlassian.com/v1/sse
			  ~~~
		- ### Multiple Tenants
			- Use `--resource` flag to isolate OAuth sessions per tenant:
			- ~~~json
			  {
			    "mcpServers": {
			      "atlassian_org1": {
			        "command": "npx",
			        "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/sse", "--resource", "https://org1.atlassian.net/"]
			      }
			    }
			  }
			  ~~~
	- ## Token Storage
		- Credentials stored in `~/.mcp-auth` (or `$MCP_REMOTE_CONFIG_DIR`)
		- Tokens keyed by hash of: server URL + resource flag + custom headers
		- Clear with: `rm -rf ~/.mcp-auth`
	- ## Related
		- [[MCP/Atlassian/Q/Can Atlassian authentication be system wide and cached]]
		- [[MCP/Atlassian/Q/Can I authenticate without loading the server into context]]
		- [[Atlassian/MCP/How To/Set up in Cursor]]
		- [[mcp-atlassian]]