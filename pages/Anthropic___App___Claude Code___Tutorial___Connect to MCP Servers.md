tags:: [[Diataxis/Tutorial]]

- # Tutorial: Connect Claude Code to [[MCP Servers]] (Filesystem & Web Browser)
	- ## Summary
		- In this tutorial we’ll plug two real **Model Context Protocol (MCP)** servers into the **Claude Code** CLI: a local **Filesystem** server (stdio transport) and Apify’s **RAG Web Browser** server (SSE transport). When you finish, Claude can read / write local files and browse the live web in the same chat.
	- ## Before You Start
		- *Requirements*  
		  1. **Node.js ≥ 18** — check with `node --version`.  
		  2. **Claude Code** CLI — install via `npm i -g @anthropic-ai/claude-code` ([npm page](https://www.npmjs.com/package/@anthropic-ai/claude-code)).  
		  3. `ANTHROPIC_API_KEY` exported in your shell (get one in the [Anthropic Console](https://console.anthropic.com)).  
		  4. For web browsing: an **Apify** account and `APIFY_TOKEN` ([Apify RAG Web Browser actor](https://apify.com/apify/rag-web-browser)).
		- *Shell shown* — commands use Bash/macOS or WSL. On Windows PowerShell, adjust paths and environment-variable syntax.
	- ## Steps
		- ### 1. Install & log in to Claude Code
			- ~~~bash
			  npm install -g @anthropic-ai/claude-code
			  claude login           # opens browser to authenticate
			  ~~~
		- ### 2. Verify tooling
			- ~~~bash
			  node --version         # prints v18+  
			  claude --version       # prints CLI version
			  ~~~
		- ### 3. Add the **Filesystem** MCP server (stdio)
			- Start the server in one terminal, exposing two folders:  
			  ~~~bash
			  npx -y @modelcontextprotocol/server-filesystem ~/Desktop ~/Downloads
			  ~~~  
			  The server stays running and communicates over stdio. Package info: [server-filesystem on npm](https://www.npmjs.com/package/@modelcontextprotocol/server-filesystem).
			- In a second terminal, register it with Claude Code:  
			  ~~~bash
			  claude mcp add filesystem npx -y @modelcontextprotocol/server-filesystem \
			   ~/Desktop ~/Downloads
			  ~~~
			- Confirm connection:  
			  ~~~bash
			  claude mcp list
			  # ➜  filesystem  connected  stdio
			  ~~~
		- ### 4. Add the **Apify RAG Web Browser** server (SSE)
			- Export your Apify token:  
			  ~~~bash
			  export APIFY_TOKEN="your-actual-token"
			  ~~~
			- Register the SSE server (pre-loads the actor):  
			  ~~~bash
			  claude mcp add web-browse --transport sse \
			   "https://actors-mcp-server.apify.actor/sse?token=${APIFY_TOKEN}&actors=apify/rag-web-browser"
			  ~~~
			- Check status:  
			  ~~~bash
			  claude mcp list
			  # ➜  web-browse  connected  sse
			  ~~~
		- ### 5. Use the servers in a session
			- Launch interactive mode:  
			  ~~~bash
			  claude
			  ~~~
			- Try local file operations:  
			  > Create a file called **notes.txt** on my Desktop containing a haiku about MCP.
			- Try web search:  
			  > Search for the latest MCP spec release notes and summarise them.
			- Claude will ask for permission, invoke the tool, and stream results.
		- ### 6. Share configuration (optional)
			- Scope the servers to the current project so teammates get them in git:  
			  ~~~bash
			  claude config add mcp.project filesystem
			  claude config add mcp.project web-browse
			  git add .claude/config.json
			  git commit -m "Add MCP servers"
			  ~~~
	- ## Verification
		- `claude mcp list` shows **filesystem** and **web-browse** as *connected*.
		- Running `/mcp` inside an interactive session displays green status dots.
		- File-creation and web-search requests succeed without errors.
	- ## What You Learned
		- Installing and authenticating **Claude Code**.
		- Running a stdio MCP server with **server-filesystem**.
		- Connecting to a remote SSE server via **Apify**.
		- Checking and sharing MCP configuration with your team.
	- ## Next Steps
		- Browse the [Model Context Protocol server gallery](https://modelcontext.org/servers) to discover more tools.
		- Scaffold your own server with `npx @modelcontextprotocol/create-server`.
		- Combine multiple servers to build end-to-end workflows (e.g., DB + browser + scratchpad).