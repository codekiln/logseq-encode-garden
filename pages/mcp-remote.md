alias:: [[MCP/npm/mcp-remote]], [[geelen/mcp-remote]]
tags:: [[MCP]], [[Security]]
maintainer:: [[Person/Glen Maddern]]

- # [geelen/mcp-remote](https://github.com/geelen/mcp-remote)
	- [npm: mcp-remote](https://www.npmjs.com/package/mcp-remote)
	- Remote MCP proxy that lets stdio-only clients connect to remote MCP servers with OAuth support.
	- ## Maintainer
		- Primary maintainer: [[Person/Glen Maddern]] (`geelen`)
		- Co-maintainer on npm: `threepointone` ([[Person/Sunil Pai]])
	- ## What it does
		- Bridges local stdio MCP clients to remote HTTP/SSE MCP servers.
		- Handles OAuth browser flow and token refresh for remote servers.
		- Caches auth state in `~/.mcp-auth` (or `$MCP_REMOTE_CONFIG_DIR`).
	- ## Security Evaluation (2026-02-13)
		- ### Verdict
			- Reasonable for developer workstations if you run a current version and trust the remote server.
			- Not a strong security boundary by itself; treat it as a convenience/auth bridge.
		- ### Confirmed findings
			- Known critical vulnerability existed: `CVE-2025-6514` / `GHSA-6xpm-ggf7-wc3p` (OS command injection risk with untrusted server interaction).
			- Affected range: `>=0.0.5` and `<0.1.16`.
			- Fixed in: `0.1.16+`.
			- Current npm latest at research time: `0.1.38` (released 2026-02-05), which is outside the affected range.
		- ### Project security posture
			- Upstream README explicitly labels project as experimental/proof-of-concept.
			- No `SECURITY.md` file found in the GitHub repo.
			- MIT licensed.
			- Direct runtime dependencies are small in count (`express`, `open`, `strict-url-sanitise`, `undici`).
		- ### Operational risks
			- Local OAuth/token artifacts in `~/.mcp-auth` are user-readable local files.
			- `--allow-http` exists; unsafe unless used only on a trusted private network.
			- Security depends heavily on trusting the target remote MCP server and keeping package version patched.
		- ### Practical hardening
			- Pin or enforce `mcp-remote>=0.1.16` (prefer current latest).
			- Avoid `--allow-http` on untrusted networks.
			- Restrict tool surface with `--ignore-tool` where useful.
			- Periodically clear `~/.mcp-auth` if auth state gets stale or after security incidents.
	- ## Example for Atlassian MCP
		- ~~~json
		  {
		    "mcpServers": {
		      "atlassian": {
		        "command": "npx",
		        "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/mcp"]
		      }
		    }
		  }
		  ~~~
	- ## Related
		- [[MCP/Atlassian/Q/Can Atlassian authentication be system wide and cached]]
		- [[MCP/Atlassian/Q/Can I authenticate without loading the server into context]]
		- [[Atlassian/MCP/How To/Set up in Cursor]]
		- [[mcp-atlassian]]
