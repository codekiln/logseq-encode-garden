logseq-entity:: [[Logseq/Entity/Software/Project]]
alias:: [[playwright-cli]]
see-also:: [[Playwright/MCP]], [[CLI/Tool]], [[Browser/Headless]]

- # [Playwright CLI](https://github.com/microsoft/playwright-cli)
	- Official Microsoft CLI for common Playwright actions: record and generate Playwright code, inspect selectors, and take screenshots.
	- Aimed at **coding agents** (Claude Code, GitHub Copilot, and similar): exposes browser automation as concise CLI commands and installable **skills**, which the project positions as more token-efficient than loading large MCP tool schemas and accessibility trees.
	- Install globally with `npm install -g @playwright/cli@latest`; optional `playwright-cli install --skills` for agent skill bundles.
	- Requires Node.js 18+.
	- Contrast with [[Playwright/MCP]]: MCP suits persistent browser context and rich page introspection; this CLI suits high-throughput agent loops that must share context with large codebases and tests.
