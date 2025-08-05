# Using [[GitHub/MCP]] with the new remote server setup in Cursor and [[1Password/Dev/CLI]]
	- ## Problem
		- I've had a local github MCP server set up for a while; see
			- [[GitHub/MCP/How To/Set up in Cursor with 1Password GH token]]
			- [[Anthropic/App/Claude Code/How To/Set Up Github MCP with 1Password GH token and mise]]
		- Today, I saw that github has new instructions for cursor, using "Remote Server Setup (Recommended):  
		  https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-cursor.md
		- The guide suggests that we put the following in [[CursorAI/.cursor/mcp.json]], which uses the new "Streamable HTTP Configuration" which I'm not as familiar with in Anthropic's Model Context Protocol; this is my first or second time configuring it:
			- ```json
			  {
			  "mcpServers": {
			    "github": {
			      "url": "https://api.githubcopilot.com/mcp/",
			      "headers": {
			        "Authorization": "Bearer YOUR_GITHUB_PAT"
			      }
			    }
			  }
			  }
			  ```
		- Only problem with these instructions are: I prefer to use [[1Password]]'s [[op/run]] CLI for managing access to secrets. I don't like to have secrets on disk in plain text. So ... how can achieve the same effect of my method in [[GitHub/MCP/How To/Set up in Cursor with 1Password GH token]], but use 1password's CLI to wrap the invocation to MCP, but still use the "streamable HTTP configuration"?
	- ## Proposal from #o3
		- Cursor doesn’t yet expand environment variables inside the `headers` block of a **streamable-http** entry; tokens have to be literal (see forum reply: “For now, yes … you’re forced to deal with env vars.” ([Cursor - Community Forum](https://forum.cursor.com/t/how-to-use-environment-variables-in-mcp-json/79296))).
		  
		  Below are three work-arounds that keep your PAT out of `mcp.json` while still using the new HTTP transport.
		- ### 1 · Stay on the local (stdio) setup
		  
		  Your existing `start-github-mcp.sh` already pulls the token from 1Password at run-time via `op run` and starts the Docker image securely .
		  
		  If you’re happy with a local container, keep this approach and skip the remote guide altogether.
		- ### 2 · Lightweight local reverse proxy (recommended)
		- **Relay script** (`~/.cursor/github-mcp/relay.sh`):
		  
		  ```
		  #!/usr/bin/env bash
		  set -euo pipefail
		  VAULT="Private"; ITEM="GitHub MCP Token"; FIELD="token"
		  
		  op run --env-file <(echo "GH_PAT=op://${VAULT}/${ITEM}/${FIELD}") -- \
		  node - <<'JS'
		    import express from 'express';
		    import { createProxyMiddleware } from 'http-proxy-middleware';
		    const app = express();
		    const target = 'https://api.githubcopilot.com/mcp/';
		    app.use('/', createProxyMiddleware({
		      target,
		      changeOrigin: true,
		      headers: { Authorization: `Bearer ${process.env.GH_PAT}` },
		      pathRewrite: p => p          // keep /mcp/*
		    }));
		    app.listen(3799, () => console.log('MCP relay listening on :3799'));
		  JS
		  ```
		- **Make it executable:** `chmod +x ~/.cursor/github-mcp/relay.sh`.
		- **Update `~/.cursor/mcp.json`:**
		  
		  ```
		  {
		  "mcpServers": {
		    "github": {
		      "command": "/Users/<YOU>/.cursor/github-mcp/relay.sh",
		      "transport": "stdio"          // Script itself hosts HTTP; Cursor just starts it
		    },
		    "github-http": {
		      "url": "http://127.0.0.1:3799/",
		      "transport": "streamableHttp"
		    }
		  }
		  }
		  ```
		  
		  Cursor spawns the script (no secrets on disk); the script proxies over HTTP/SSE to GitHub with the injected header.
		- ### 3 · Caddy / Nginx one-liner
		  
		  If you prefer a declarative proxy:
		  
		  ```
		  op run --env-file <(echo "GH_PAT=op://Private/GitHub MCP Token/token") -- \
		  caddy run --config - <<'CF'
		  :3799 {
		  reverse_proxy https://api.githubcopilot.com {
		    header_up Authorization "Bearer {env.GH_PAT}"
		  }
		  }
		  CF
		  ```
		  
		  `mcp.json` then just points `url` at `http://localhost:3799/`.
		  These patterns give you the “remote” UX while keeping the PAT in 1Password and off disk. When Cursor eventually supports env-var interpolation in headers, you can simplify back to the official snippet.
	- ## Security review from [[AI/Prompt/Security Review AI Agent]]
		- ## Positive elements
			- **Secret stays out of `mcp.json`.** `op run` injects `GH_PAT` only into the Caddy process, avoiding plaintext on disk.
			- **HTTPS upstream with default TLS verification.** `reverse_proxy https://api.githubcopilot.com` inherits Caddy’s verified-TLS defaults — no insecure skip-verify flag. ([Caddy Web Server](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy?utm_source=chatgpt.com))
			- **Authorization header is redacted from logs by default** (`log_credentials` defaults to *on*). ([Caddy Web Server](https://caddyserver.com/docs/caddyfile/options?utm_source=chatgpt.com))
		- ## Key risks
			- | # | Risk | Notes & Likely CWE | Impact |
			  | ---- | ---- | ---- |
			  | 1 | **Listener bound to “:3799”.** Wildcard bind exposes the proxy to every interface. | CWE-306 (Improper Authentication) | Any process/user on the LAN can replay GitHub-API calls with your PAT. [Caddy Web Server](https://caddyserver.com/docs/caddyfile/options?utm_source=chatgpt.com) |
			  | 2 | **Secret in env.** `GH_PAT` is readable via `/proc/$PID/environ`, core dumps, or accidental debug prints. | CWE-798 (Use of Hard-coded Credentials) | Local privilege escalation; token theft. [Trend Micro](https://www.trendmicro.com/en_us/research/22/h/analyzing-hidden-danger-of-environment-variables-for-keeping-secrets.html?utm_source=chatgpt.com) |
			  | 3 | **Open proxy to full Copilot API.** Path is unrestricted; an attacker can hit other endpoints (e.g., usage-metering, account data) with your bearer token. | CWE-639 (Authorization Bypass) | Data leakage; unmetered spend. |
			  | 4 | **Header forwarding surface.** If untrusted clients reach port 3799 they can inject additional headers (e.g., `X-Forwarded-For`) that GitHub may honor. | CWE-444 (HTTP Header Injection) | Spoofed identity, rate-limit evasion. |
			  | 5 | **Patch management.** Caddy’s ecosystem had CVE-2024-21499 in a popular security plugin; staying current matters even if the plugin isn’t used. [wiz.io](https://www.wiz.io/vulnerability-database/cve/cve-2024-21499?utm_source=chatgpt.com) | CVE tracking gap | Future RCE/DoS if base image isn’t updated. |
			  | 6 | **Operational logging.** Turning on verbose or JSON logs and disabling redaction (`log_credentials off`) will leak the PAT. | CWE-532 (Information Exposure via Log Files) | Secret exfiltration via log aggregation. |
		- ## Mitigations
			- **Bind to loopback only**
				- ```
				  127.0.0.1:3799 {
				    reverse_proxy https://api.githubcopilot.com {
				        header_up Authorization "Bearer {env.GH_PAT}"
				    }
				  }
				  ```
				  
				  or add `bind 127.0.0.1` inside the site block. ([Caddy Web Server](https://caddyserver.com/docs/caddyfile/directives/bind?utm_source=chatgpt.com))
			- **Restrict routing** (defence-in-depth)
			  
			  ```
			  handle_path /mcp/* {
			    reverse_proxy ...
			  }
			  respond "404" 404
			  ```
			  
			  Limits token misuse to the MCP path.
			- **Run under a dedicated unprivileged user** (`setcap`, `systemd-sandbox`) so that only that UID can read `/proc/$PID/environ`.
			- **Use a Unix socket instead of TCP**
			  
			  ```
			  unix//run/mcp.sock {
			    reverse_proxy ...
			  }
			  ```
			  
			  Then point `mcp.json` at `unix//` to eliminate the attack surface.
			- **Rotate PAT via 1Password short-lived tokens.** Prefer GitHub fine-grained PATs scoped just to Copilot APIs.
			- **Harden logging**
			  
			  ```
			  log {
			    format json
			    filter {
			        fields request>headers>Authorization delete
			    }
			  }
			  ```
			  
			  Protects even if `log_credentials` is toggled.
			- **Patch cadence**: track Caddy release notes and CVE feeds (e.g., CVE-2024-21499) monthly.
		- ## Verdict
			- With loopback binding, path scoping, least-privilege user, and disciplined logging, the Caddy one-liner is acceptably secure for local development. Without those hardenings it exposes your GitHub PAT to any process on the host or network and should be avoided in production contexts.