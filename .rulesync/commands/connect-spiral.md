---
targets:
  - '*'
description: Connect Spiral, Every's AI writing partner, to this agent over its remote MCP server
---
# Connect Spiral over MCP

Help me connect Spiral, an AI writing partner that learns and writes in my voice, to you over MCP. The garden page is [[Every/Spiral]].

Add its remote MCP server (Streamable HTTP) at https://api.writewithspiral.com/mcp/ the way your client adds remote MCP servers.

If a Spiral API key (`spiral_sk_...`) is already set in your environment, for example in `SPIRAL_TOKEN` or `SPIRAL_API_KEY`, send it as an `Authorization: Bearer` header and skip the browser sign-in. Otherwise the first connection opens a browser for me to sign in to Spiral and authorize access, so tell me when it's my turn. Never paste the key into a file or commit it.

If your client needs exact setup steps, https://writewithspiral.com/agents.md has per-client instructions. For Claude Code:

```bash
claude mcp add --transport http --scope user spiral https://api.writewithspiral.com/mcp/
```

With an API key, add `--header "Authorization: Bearer $SPIRAL_TOKEN"`. A server added mid-session may only load after the client restarts.

Once it's connected, confirm Spiral's tools are available (for example `spiral_check_quota`) and let me know I'm ready.
