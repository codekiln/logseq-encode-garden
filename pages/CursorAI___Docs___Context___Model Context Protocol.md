# [Cursor – Model Context Protocol](https://docs.cursor.com/context/model-context-protocol) - Adding an [[MCP Server]] to [[CursorAI/Settings/MCP]]
	- ## [[My Notes]]
		- ### #Example configuration
			- This can be placed at `.cursor/mcp.json` in any project, or at `~/.cursor/mcp.json` in a user's home directory.
			- ```json
			  // This example demonstrated an MCP server using the stdio format
			  // Cursor automatically runs this process for you
			  // This uses a Node.js server, ran with `npx`
			  {
			    "mcpServers": {
			      "server-name": {
			        "command": "npx",
			        "args": ["-y", "mcp-server"],
			        "env": {
			          "API_KEY": "value"
			        }
			      }
			    }
			  }
			  ```
-