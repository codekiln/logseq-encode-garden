tags:: [[Anthropic/App/Claude Code]], [[Diataxis/How To]]

- # How To Export Claude Code Conversations to Files
	- ## Overview
		- This guide shows you how to save Claude Code conversation history to files for backup, sharing, or documentation purposes.
		- **Note**: Claude Code does not have a built-in export feature that I could find as of [[2025-07-18 Fri]], so these are manual workarounds.
		- For users who want to preserve conversation context, share discussions with team members, or maintain records of coding sessions.
	- ## Prerequisites
		- Claude Code CLI installed and authenticated (`claude --version` should work)
		- Terminal access with basic command-line skills
		- (Optional) Text editor for viewing exported files
	- ## Steps
		- ### 1. Manual Copy-Paste Method (Workaround)
			- **During an active session**:
				- Select all conversation text in your terminal
				- Copy to clipboard (Cmd+C on macOS, Ctrl+C on Windows/Linux)
				- Paste into a text file in your preferred editor
				- Save with descriptive filename (e.g., `claude-session-2025-01-15.txt`)
			- **From terminal history**:
				- Use `history` command to find Claude Code commands
				- Copy relevant conversation output
				- Save to file for future reference
		- ### 2. Use MCP Filesystem Server (Workaround)
			- **Set up filesystem MCP server** (if not already configured):
			  ~~~bash
			  claude mcp add filesystem npx -y @modelcontextprotocol/server-filesystem ~/Desktop ~/Downloads
			  ~~~
			- **Ask Claude to save conversation directly**:
				- "Save our conversation to a file called 'claude-session.txt' on my Desktop"
				- Claude will create the file with the full conversation content
	- ## Troubleshooting
		- **File permissions**: Check write permissions in target directory
		- **Large conversations**: Consider breaking into smaller files for better manageability
		- **MCP server not working**: Ensure the filesystem server is properly configured and connected
	- ## Related
		- [[Anthropic/App/Claude Code/Tutorial/Connect to MCP Servers]]