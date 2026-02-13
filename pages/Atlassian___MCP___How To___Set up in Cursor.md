# How to set up the official Atlassian remote mcp server in [[CursorAI]] with [[mcp-remote]]
	- [Atlassian Remote MCP Server Beta Now Available for Desktop Applications](https://community.atlassian.com/forums/Atlassian-Platform-articles/Atlassian-Remote-MCP-Server-beta-now-available-for-desktop/ba-p/3022084) has some [[CursorAI]] instructions that don't appear in the help page [Using the Atlassian Remote MCP Server beta](https://community.atlassian.com/forums/Atlassian-Platform-articles/Using-the-Atlassian-Remote-MCP-Server-beta/ba-p/3005104)
	- ## Initial authentication before installing in Cursor
		- > [[mcp-remote]] prompts you to authenticate in your browser so you don't have to manage an API key
		- First, run `npx -y mcp-remote https://mcp.atlassian.com/v1/sse` (or let your IDE plug-in run it). The proxy starts and immediately launches a browser-based OAuth flow.
		- Once the web browser opens, you need to select your org id, which will likely be something like `<your-org>.atlassian.net` in the case of [[Atlassian/Cloud]].
			- A required dropdown labeled **“Use app on *”** appears first; it lists every Atlassian Cloud site you belong to (e.g., `<your-org>.atlassian.net`).
			- Select the site whose Jira/Confluence data you want the MCP server to reach. The token you’re about to issue is locked to that site; switching sites later means re-running the flow.
			- Below the dropdown the form groups requested scopes by product:
				- **Jira** – View / Update → `jira-work`
				- **Confluence** – View → comments, contents, pages, space details, `confluence-user`; Update → comments, pages; Search → `confluence`
				- **User** – View → `me`
			- Click **Accept/Allow**. The browser redirects to `http://localhost:3334/oauth/callback`; the CLI prints success and begins streaming. Your IDE can now read or write Jira issues and Confluence pages through the MCP server, subject to your normal product permissions.
	- ## Installing in Cursor
		- After you've run the above flow, add this to your Cursor `mcp.json`
			- ```json
			  {
			    "mcpServers": {
			  
			      // ... other mcp servers here
			  
			      "atlassian": {
			        "command": "npx",
			        "args": [
			          "-y",
			          "mcp-remote",
			          "https://mcp.atlassian.com/v1/sse"
			        ]
			      }
			    }
			  }
			  ```
			- You shouldn't need to enter an API key, because the oauth flow already happened above.
	- ## Testing it out
		- Go into Cursor's agent mode and ask it a question which should require using Atlassian. I did,
		- > can you tell me which `<PROJECT_ABBREVIATION>` tickets are assigned to me in the current sprint?
		- The response was three tool calls, each of which I had to confirm with Cmd+Enter:
			- `Called atlassianUserInfo`
			- `Called getAccessibleAtlassianResources`
			- `Called searchJiraIssuesUsingJql`
		- The result I got back was correct.
	- ## See also
		- [MCP Clients: Understanding the potential security risks - Work Life by Atlassian](https://www.atlassian.com/blog/artificial-intelligence/mcp-risk-awareness)