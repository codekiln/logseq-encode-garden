tags:: [[Diataxis/Tutorial]]

- # Tutorial - adding a project-specific [[MCP Server]] to Cursor
	- ## What You'll Create
	  id:: 67e13751-0f8c-46e0-9b1f-01acee9914c7
		- A project-specific MCP server configuration that enhances Cursor's AI capabilities
		- A working example using a weather MCP server that can provide weather information
	- ## Prerequisites
		- [[CursorAI]] installed on your system
		- Basic familiarity with JSON
		- Node.js and npm with npx installed (for npm-based MCP servers)
	- ## Learning Goals
		- Understand what an MCP server is and how it extends Cursor's capabilities
		- Learn how to configure a project-specific MCP server
		- Successfully set up and test an MCP server
	- ## Steps
		- ### 1. Create the MCP Configuration File
			- In your project root, create a `.cursor` directory if it doesn't exist
			- Inside `.cursor`, create an `mcp.json` file
			- This file will define your project-specific MCP servers
		- ### 2. Configure Your MCP Server
			- Open `mcp.json` in your editor
			- Add the basic structure for MCP server configuration:
				- ~~~json
				  {
				      "mcpServers": {
				          "your-server-name": {
				              "command": "your-command",
				              "args": [
				                  "your",
				                  "arguments"
				              ]
				          }
				      }
				  }
				  ~~~
			- For example, to add a weather MCP server:
				- ~~~json
				  {
				      "mcpServers": {
				          "weather": {
				              "command": "npx",
				              "args": [
				                  "-y",
				                  "@h1deya/mcp-server-weather"
				              ]
				          }
				      }
				  }
				  ~~~
		- ### 3. Enable the MCP Server
			- Open Cursor Settings
			- Navigate to the MCP section
			- Find your newly added MCP server in the list
			- Enable it using the toggle switch
			- Click the refresh button to initialize the server
				- Note: You may need to click refresh multiple times until the status indicator turns green
		- ### 4. Test Your MCP Server
			- Open Cursor's Agent Mode
			- Ask a question that would require your MCP server
				- For the weather example: "What's the weather like in Tokyo?"
			- When prompted, approve the MCP tool use
			- Verify that you receive appropriate responses
	- ## What You've Learned
		- How to create and configure project-specific MCP servers
		- The structure of MCP configuration files
		- How to enable and test MCP servers in Cursor
	- ## Related
		- [[CursorAI/Docs/Context/Model Context Protocol]]
		- [[CursorAI/Settings/MCP]]
		- [[CursorAI/Agent Mode]]