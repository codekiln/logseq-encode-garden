tags:: [[MCP/Server]], [[JavaScript]], [[Logseq]], [[TypeScript]]
alias:: [[Person/Joel Hooks/GitHub/logseq-mcp-tools]]

- # Logseq MCP Tools (Node.js)
	- GitHub: [joelhooks/logseq-mcp-tools](https://github.com/joelhooks/logseq-mcp-tools)
	- npm: [@joelhooks/logseq-mcp-tools](https://www.npmjs.com/package/@joelhooks/logseq-mcp-tools)
	- ## Overview
		- ### [[My Notes]]
			- [[2025-05-10 Sat]]
			  id:: 681f9493-061c-4f53-a033-26ad6c1ea18f
				- a [[Typescript]] mcp server written by a well-known dev [[Person/Joel Hooks]]. It can create pages and even suggest links between topics, but it doesn't have an insert node or node level editing.
		- A Node.js MCP server (MIT-licensed) that uses the Model Context Protocol SDK and Logseq's HTTP API. It focuses on both basic graph access and higher-level analysis.
	- ## Features
		- Core tools for retrieving pages and content
		- Advanced read functions:
			- Journal entry summaries over date ranges
			- Backlink listing
			- Free-form Datalog queries via `smartQuery`
		- AI-powered analysis:
			- Knowledge gap detection
			- Connection suggestions between pages
	- ## Status
		- **Active** – created in 2025
		- ~20⭐ on GitHub
		- Small but active community
		- [[Person/Joel Hooks]] is a well-known developer
	- ## Compatibility
		- Developed and tested on macOS
		- Works on Linux/Windows
		- Requires Node.js
	- ## Installation
		- Via npm/pnpm: `npm install @joelhooks/logseq-mcp-tools`
		- Or via Smithery CLI: `npx @smithery/cli install @joelhooks/logseq-mcp-tools`
	- ## Usage
		- Run server with `npm start` or `npx tsx index.ts`
	- ## Limitations
		- Write access limited to page level
		- No direct block insertion/editing
		- No real-time updates