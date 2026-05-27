logseq-entity:: [[Logseq/Entity/Software/Project]]
alias:: [[playwright-mcp]]
see-also:: [[Playwright/CLI]], [[AI/Coding/History/Phase/5 - Context Engineering/MCP Servers]]

- # [Playwright MCP](https://github.com/microsoft/playwright-mcp)
	- Official Microsoft **Model Context Protocol** server for browser automation with [Playwright](https://playwright.dev).
	- Exposes web interaction through structured **accessibility snapshots** rather than screenshots, so agents can operate on deterministic structured data without vision models.
	- Typical install via MCP client config running `npx @playwright/mcp@latest` (npm package [@playwright/mcp](https://www.npmjs.com/package/@playwright/mcp)).
	- Requires Node.js 18+; works with VS Code, Cursor, Claude Desktop, and other MCP clients.
	- Contrast with [[Playwright/CLI]]: MCP suits persistent browser context, rich page introspection, and long-running agentic loops; the CLI targets token-efficient command-and-skill workflows for coding agents.
