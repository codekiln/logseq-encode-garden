tags:: [[Claude Code]], [[Diataxis/How To]]
alias:: [[Anthropic/App/Claude Code/How To/Export Conversation to File]]

- # How To Export [[Claude Code]] Conversations to Files
	- ## Overview
		- This guide shows you how to save Claude Code conversation history to files for backup, sharing, or documentation purposes.
		- **Note**: Claude Code does not have a built-in export feature that I could find as of [[2025-07-18 Fri]], so these are manual workarounds.
		- For users who want to preserve conversation context, share discussions with team members, or maintain records of coding sessions.
	- ## Prerequisites
		- Claude Code CLI installed and authenticated (`claude --version` should work)
		- Terminal access with basic command-line skills
		- (Optional) Text editor for viewing exported files
	- ## Methods and Workarounds
		- ### Manual Copy-Paste Method
			- **During an active session**:
				- Select all conversation text in your terminal
				- Copy to clipboard (Cmd+C on macOS, Ctrl+C on Windows/Linux)
				- Paste into a text file in your preferred editor
				- Save with descriptive filename (e.g., `claude-session-2025-01-15.txt`)
			- **From terminal history**:
				- Use `history` command to find Claude Code commands
				- Copy relevant conversation output
				- Save to file for future reference
		- ### Community Extractor Tools
			- Claude Code keeps every prompt/response pair in plain-text JSONL files under `~/.claude/projects/<project-id>/transcript.jsonl`
			- **Finding Session IDs**:
				- **From within an active session**:
					- Use `/status` to see current session information including provider and model
					- Use `/help` to see all available slash commands
					- Use `/cost` to see session usage statistics
					- **Note**: These commands show session metadata but may not display the session ID directly
				- **Use Claude Code's built-in session picker**:
					- Run `claude --resume` to see an interactive list of all sessions
					- The picker shows: Modified date, Created date, Message count, and Description
					- Example output:
					  ~~~
					      Modified    Created     # Messages Git Branch     Summary
					  ❯ 1. 1m ago      1h ago             111 mn/PD-30064_Cr This session is being continued from a previo...
					    2. 1 week ago  1 week ago         427 -              FastAPI Service Template with JSON Logging Setup
					  ~~~
					- Use arrow keys to navigate and press Enter to select a session
					- The session ID is the UUID in the project directory path
				- **Alternative: List project directories**:
					- Session IDs are stored in the project directory structure: `~/.claude/projects/<session-id>/`
					- Use `ls ~/.claude/projects/` to list all available session IDs
					- The most recent session is typically the one with the latest timestamp
					- Session IDs are UUIDs (e.g., `abc12345-def6-7890-ghij-klmnopqrstuv`)
				- **Pro tip**: Use `claude --resume` to see human-readable descriptions, then match them to the UUID directories
			- **Claude Conversation Extractor** – CLI tool that converts JSONL transcripts to clean Markdown
				- Install with `pip install claude-conversation-extractor`
				- Basic usage: `claude-extract <session-id>` to extract a specific session
				- Advanced usage: `claude-extract --all` to extract all sessions
				- Outputs clean Markdown with proper code block formatting
				- [GitHub](https://github.com/ZeroSumQuant/claude-conversation-extractor)
				- [PyPI](https://pypi.org/project/claude-conversation-extractor/)
			- **claude-code-log** – Converts JSONL transcripts to minimalist HTML
				- Install with `pip install claude-code-log`
				- Usage: `claude-code-log <session-id>` to generate HTML output
				- Preserves code blocks, timestamps, and conversation structure
				- Outputs a single HTML file that can be opened in any browser
				- [PyPI](https://pypi.org/project/claude-code-log/)
				- [GitCode](https://gitcode.com/gh_mirrors/cl/claude-code-log/overview)
			- **claude-transcript** – Simple Markdown converter for Claude Code sessions
				- Install from GitHub: `pip install git+https://github.com/jflam/claude-transcript.git`
				- Usage: `claude-transcript <session-id>` to convert to Markdown
				- Lightweight tool focused on clean Markdown output
				- Works with the same JSONL transcript files as other tools
				- [GitHub](https://github.com/jflam/claude-transcript)
		- ### Session Recording Methods
			- **[[Linux/script/command]]** records the full interactive session to a log file
				- ~~~bash
				  script -f claude_$(date +%F).log claude code
				  ~~~
				- You can replay it with [[Linux/script/command/scriptreplay]] `scriptreplay` later
				- [Red Hat Documentation](https://www.redhat.com/en/blog/record-terminal-script-scriptreplay)
				- [LFCS Certification eBook](https://www.tecmint.com/record-and-replay-linux-terminal-session-commands-using-script/)
			- **tee command** for read-only output (simple but loses your keystrokes)
				- ~~~bash
				  claude code | tee claude_output.log
				  ~~~
			- **asciinema** for shareable demos
				- ~~~bash
				  asciinema rec -c "claude code"
				  ~~~
				- Captures keystrokes and timing in a lightweight *.cast file you can embed on the web
				- [asciinema.org](https://asciinema.org/)
				- [asciinema docs](https://docs.asciinema.org/manual/cli/quick-start/)
		- ### [[MCP/Server/Filesystem]] Method
			- **Set up filesystem MCP server** (if not already configured):
			  ~~~bash
			  claude mcp add filesystem npx -y @modelcontextprotocol/server-filesystem ~/Desktop ~/Downloads
			  ~~~
			- **Ask Claude to save conversation directly**:
				- "Save our conversation to a file called 'claude-session.txt' on my Desktop"
				- Claude will create the file with the full conversation content
		- ### Browser & GUI Options
			- **Web version (claude.ai)** has an official export feature
				- Settings → Privacy → Export data button
				- Emails you a zip containing chat JSON plus CSV
				- [Anthropic Help Center](https://support.anthropic.com/en/articles/9450526-how-can-i-export-my-claude-ai-data)
			- **Claude Exporter** Chrome extension
				- Free Chrome extension that saves any web chat to PDF, Markdown, text, CSV, or JSON with one click
				- Handy if teammates use the browser UI rather than Claude Code
				- [Chrome Web Store](https://chromewebstore.google.com/detail/claude-exporter-save-clau/elhmfakncmnghlnabnolalcjkdpfjnin)
		- ### Version Control Method
			- **Git version control** for transcript history
				- Put `~/.claude/projects` under Git
				- Every time you finish a session, commit the changed transcript
				- Provides chronological history that's diff-able and reviewable
	- ## Workflow Recommendations
		- Pick whichever mix matches your workflow:
			- Extractor tools for polished docs
			- `script` or `asciinema` for live capture
			- Git for incremental backups
	- ## Troubleshooting
		- **File permissions**: Check write permissions in target directory
		- **Large conversations**: Consider breaking into smaller files for better manageability
		- **MCP server not working**: Ensure the filesystem server is properly configured and connected
		- **Extractor tools not working**: Verify the transcript files exist in `~/.claude/projects/<project-id>/transcript.jsonl`
	- ## Related
		- [[Claude Code/Tutorial/Connect to MCP Servers]]