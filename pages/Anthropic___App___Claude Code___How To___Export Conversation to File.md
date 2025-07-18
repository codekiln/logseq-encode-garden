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
	- ## [[AI/Analysis]] from #o3
		- Claude Code keeps every prompt/response pair in plain-text JSONL files under `~/.claude/projects/<project-id>/transcript.jsonl`. There's no button to export them, but local storage means you can script your own pipelines.
		- ### Community extractors
			- **Claude Conversation Extractor** – CLI that scans the transcript directory and spits out clean Markdown
				- Install with `pip install claude-conversation-extractor`
				- [GitHub](https://github.com/ZeroSumQuant/claude-conversation-extractor)
				- [PyPI](https://pypi.org/project/claude-conversation-extractor/)
			- **claude-code-log** – turns the JSONL into minimalist HTML, preserving code blocks and timestamps
				- Install with `pip install claude-code-log`
				- [PyPI](https://pypi.org/project/claude-code-log/)
				- [GitCode](https://gitcode.com/gh_mirrors/cl/claude-code-log/overview)
			- **claude-transcript** – converts a session to Markdown
				- Lives on GitHub and works on the same JSONL files
				- [GitHub](https://github.com/jflam/claude-transcript)
		- ### Record as you work
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
		- ### Browser & GUI options
			- **Web version (claude.ai)** has an official export feature
				- Settings → Privacy → Export data button
				- Emails you a zip containing chat JSON plus CSV
				- [Anthropic Help Center](https://support.anthropic.com/en/articles/9450526-how-can-i-export-my-claude-ai-data)
			- **Claude Exporter** Chrome extension
				- Free Chrome extension that saves any web chat to PDF, Markdown, text, CSV, or JSON with one click
				- Handy if teammates use the browser UI rather than Claude Code
				- [Chrome Web Store](https://chromewebstore.google.com/detail/claude-exporter-save-clau/elhmfakncmnghlnabnolalcjkdpfjnin)
		- ### Other tricks
			- **Filesystem MCP server workflow** still works
				- Spin up the server once and ask Claude to `write_file` the whole transcript into a chosen directory
			- **Git version control** for transcript history
				- Put `~/.claude/projects` under Git
				- Every time you finish a session, commit the changed transcript
				- Provides chronological history that's diff-able and reviewable
		- ### Workflow recommendations
			- Pick whichever mix matches your workflow:
				- Extractor for polished docs
				- `script` or `asciinema` for live capture
				- Git for incremental backups