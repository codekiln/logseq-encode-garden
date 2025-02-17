tags:: [[Idea]], [[MCP]]

- This idea is an extension to [[CursorAI/Idea/Use Project Rules to Integrate with GitHub CLI for an AI-Assisted SLDC]] that considers whether it might make sense to use a [[Model Context Protocol]] to interact with the [[GitHub/API]] to provide the same context that flat files would in that project.
- ## Finding an MCP server for the GitHub API
	- An example of an MCP server is available in [[Person/Kevin Leneway/Github/awesome-cursor-mpc-server]].
	- In this case, there may be an existing server available that interacts with the GitHub API
		- see [[CursorAI/Sites/cursor.directory/mcp]] for a list of MCP servers
			- There is one for GitHub listed, but it's incorrectly linked to the Linear server at this time
		- **official list** of MCP servers are at [[MCP/GitHub/servers]]
			- there's already one in [[MCP/GitHub/servers/GitHub]]
- ## Setting up [[MCP/GitHub/servers/GitHub]]
	- First step is to get the server deployed locally.
	- Do I just download the repo and go from there? or is there another way?
	- root of the repo - [Getting Started](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-getting-started)
		- Typescript-based servers in this repository can be used directly with `npx`.
		-