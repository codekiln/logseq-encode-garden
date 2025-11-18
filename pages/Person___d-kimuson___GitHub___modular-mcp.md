# [d-kimuson/modular-mcp](https://github.com/d-kimuson/modular-mcp)
	- **tagline**: A Model Context Protocol (MCP) proxy server that enables efficient management of large tool collections across multiple MCP servers by grouping them and loading tool schemas on-demand.
	- ## [[My Notes]]
		- How does this work?
		- via [[rulesync]] [here](https://github.com/dyoshikawa/rulesync/tree/main?tab=readme-ov-file#modular-mcp-experimental)
			- you define a description for each mcp server
	- ## Docs
		- ### 1 - Configuration
			- You define a schema with various MCP servers and just add a description
			-
		- ### 3 - [two tools registration](https://github.com/d-kimuson/modular-mcp?tab=readme-ov-file#3-two-tools-registration)
			- only two tools are registered: `get-modular-tools` and `call-modular-tool`.
		- ### 4 - On-Demand Tool Loading
			- LLM ends up calling these two tools
				- ```
				  get-modular-tools(group="playwright")
				  → Returns all playwright tool schemas
				  
				  call-modular-tool(group="playwright", name="browser_navigate", args={"url": "https://example.com"})
				  → Executes the navigation through the playwright MCP server
				  ```