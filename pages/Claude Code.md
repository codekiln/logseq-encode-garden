alias:: [[Anthropic/App/Claude Code]]

- # [Claude Code overview - Anthropic](https://docs.anthropic.com/en/docs/claude-code/overview)
	- ## Todos
	  collapsed:: true
		- TODO create [[Diataxis/How To]] guide [[Anthropic/App/Claude Code/How To/Save and Restore Session History]] after reading through options at [[Anthropic/App/Claude Code/Docs/Memory Management]]
		  id:: 682c815f-e2a5-429b-b5cb-a033598ac14e
			- done
			  collapsed:: true
				- DONE try out [[claude --resume]]
				  id:: 682c86fe-043b-44a6-ac71-bd9829e3912c
				- DONE try asking claude to update its own memories
				  id:: 682c99c4-2ec5-4215-9cdd-ee6272bdeab9
			- TODO fill out page on [[claude --resume]], disambiguating it from [[claude --continue]]
			  id:: 682c891d-c2e3-4a21-829b-77ea8c442b73
			- TODO try out [[Claude Code/--continue]]
			  id:: 682c8929-0966-45d2-906d-35ec3534d4eb
			- TODO where does one find the [[Claude Code/Session/ID]] #Question ?
			  id:: 682c8788-cefa-43d6-9cd6-b587b8f3ddb2
			- TODO try out [[Claude Code/Command/Slash/memory]]
			  id:: 682c98a3-464d-43f8-8e49-0ff1905b5321
				- DONE figure out [[Claude Code/Bug/Failed to save memory: No tool use found in response]] when I try to use the memory command `#`
				  id:: 682de8d7-b688-4d2f-bb69-9f5295a70558
		- TODO try out and take notes on [[Claude Code/Docs/Tutorial/Run parallel Claude Code sessions with Git worktrees]]
		  id:: 682c8543-8869-4d54-a1ff-04c296c08f9a
		- TODO get or create a #Bug ticket at [[Anthropic/App/Claude Code/GitHub]] related to the session timeout of [[AWS/Bedrock]] via [[AWS SSM]]
	- ## [[My Notes]]
		- (reverse cron)
		- ### [[2026-02-13 Fri]]
			- #### [[MCP]] config research: session-specific vs persistent setup
				- Goal: run some terminal sessions with [[Atlassian/MCP]] enabled and some without it, while reusing auth where possible.
				- ### What Claude Code supports right now
					- Session-only MCP profile loading:
						- `claude --mcp-config <file-or-json> --strict-mcp-config`
						- `--strict-mcp-config` means only servers from `--mcp-config` are loaded for that run.
					- Persistent MCP registration with scope:
						- `claude mcp add -s local ...` (current project, local machine)
						- `claude mcp add -s project ...` (shared in project `.mcp.json`)
						- `claude mcp add -s user ...` (all projects for this user)
					- Config file locations by scope (per docs):
						- local: `.claude.json`
						- project: `.mcp.json`
						- user: `~/.claude.json`
				- ### Repo-specific pattern that scales to many repos + many servers
					- Keep per-profile JSON files (examples):
						- `~/.claude/mcp/profiles/base.json`
						- `~/.claude/mcp/profiles/atlassian.json`
						- `~/.claude/mcp/profiles/github-and-atlassian.json`
					- Start Claude with the profile you want for that session:
						- ~~~bash
						  claude --mcp-config ~/.claude/mcp/profiles/atlassian.json --strict-mcp-config
						  ~~~
					- Keep repo defaults in `.mcp.json` only for truly always-on project servers; use profile files + `--strict-mcp-config` for optional servers.
				- ### Shared auth across terminal sessions
					- For remote servers bridged with [[mcp-remote]], auth can be reused across sessions and across clients if config is identical.
					- `mcp-remote` stores tokens under `~/.mcp-auth` (or `$MCP_REMOTE_CONFIG_DIR`).
					- Token cache keys are derived from URL + `--resource` + headers, so even small differences create separate auth entries.
					- Practical implication:
						- Use exactly the same `mcp-remote` args in all profiles/clients if you want one shared Atlassian login.
				- ### Current Atlassian endpoint + example
					- Atlassian docs now show the MCP endpoint as `https://mcp.atlassian.com/v1/mcp` with `mcp-remote`.
					- ~~~json
					  {
					    "mcpServers": {
					      "atlassian": {
					        "command": "npx",
					        "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/mcp"]
					      }
					    }
					  }
					  ~~~
				- ### Existing KB pages relevant to this topic
					- [[MCP/Atlassian/Q/Can Atlassian authentication be system wide and cached]]
					- [[MCP/Atlassian/Q/Can I authenticate without loading the server into context]]
					- [[mcp-remote]]
					- [[Claude Code/Settings]]
					- [[Claude Code/Tutorial/Connect to MCP Servers]]
				- ### Follow-up
					- TODO create a [[Diataxis/How To]] for "Session-specific MCP profiles in Claude Code with shared mcp-remote auth"
		- ### [[2025-05-23 Fri]]
			- updated to [[Anthropic/App/Claude Code/v/1/0/2]]. Had a few issues with #AWS/Bedrock authentication but eventually (after enough restarting), managed to get it to work without changing anything.
		- ### [[2025-05-21 Wed]]
		  id:: 682ddfa2-67b1-4605-8e77-3b75720efe39
			- #Filed
				- ((682de8d7-b688-4d2f-bb69-9f5295a70558))
		- ### [[2025-05-20 Tue]]
		  id:: 682c80b1-ce64-4897-af05-d72371caf003
			- #### [[Claude Code Memory]]
				- I asked it to just look at the  saved to a text file that I copied and pasted from my last session in the terminal. there **must** be a better way ...
					- #Filed
						- ((682c815f-e2a5-429b-b5cb-a033598ac14e))
					- it actually worked pretty well to have it go over the previous text file "manually"
					- looked at [[Claude Code/--continue]] and [[Claude Code/--resume]] in `--help` - this is actually fairly intuitive, in theory.
						- ```
						    -c, --continue                  Continue the most recent conversation
						    -r, --resume [sessionId]        Resume a conversation - provide a session ID or interactively select a conversation to resume
						  ```
						- ((682c86fe-043b-44a6-ac71-bd9829e3912c))
							- ok `--resume` actually brings up a way to resume various sessions... cool Still don't see any [[Claude Code/SessionID]]
							- ```
							    Modified    Created     # Messages   Description
							  ❯ 1. [recent]   [recent]         25     [Redacted: System-generated message batch]
							  2. [recent]   [recent]          3     [Redacted: System-generated message batch]
							  3. [past]     [past]           61     [Redacted: File Upload Test]
							  4. [past]     [past]           59     [Redacted: Attachment Test]
							  5. [past]     [past]           59     [Redacted: Attachment Test]
							  6. [past]     [past]          145     [Redacted: Test]
							  ```
							- Awesome, this actually works REALLY well - it's a LOT more intuitive than [[Claude Code/Docs/CLI/usage]] let on; their example of `--resume` is claude -r "abc123" "Finish this PR" which assumes that you know what `abc123` is, and also, doesn't even mention that there is an interactive way to select the session.
						- #Filed
							- ((682c8788-cefa-43d6-9cd6-b587b8f3ddb2))
							- ((682c891d-c2e3-4a21-829b-77ea8c442b73))
							- ((682c8929-0966-45d2-906d-35ec3534d4eb))
				- When I tried [[Claude Code/Slash/memory]] it said
					- `To use a different editor, set the $EDITOR or $VISUAL environment variable.`
						- #Learned that [[Shell/Var/VISUAL]] `$VISUAL` was a thing
						  id:: 682c9937-4635-440b-874a-89e38bce4274
					- ((682c99c4-2ec5-4215-9cdd-ee6272bdeab9))
						- This actually worked fairly well. I asked it to update a specific directory's `CLAUDE.md` and it did.  I wish I had a better mental model for how this relates to "compacting."
					- #Filed
						- ((682c98a3-464d-43f8-8e49-0ff1905b5321))
						- ((682c99c4-2ec5-4215-9cdd-ee6272bdeab9))
				-
			- #### #CLI [[UX]]
				- I love how [[Claude Code]] able to link me to the test files in cursor from the CLI with my mouse! #Delight
				- I see "✓ Update installed · Restart to apply" and when I restarted via [[claude --resume]], I was given the option to resume my last session. Nice!
				- Really enjoying the way I was given the ability to auto accept all `poetry run ...` commands in a particular directory. Greatly speeds up the progress.
			- #### #Documentation
				- #Filed
					- ((682c8543-8869-4d54-a1ff-04c296c08f9a))
					-
		- [[2025-05-19 Mon]]
			- I saw in [[Anthropic/App/Claude Code/Docs/Costs/Background token usage]] [Manage costs effectively - Anthropic](https://docs.anthropic.com/en/docs/claude-code/costs#background-token-usage) that there is a [[claude --resume]] flag. Was looking for that on Friday
		- [[2025-05-16 Fri]]
			- Started using Claude Code. Very impressive first day.
			- Main problem was that my [[AWS/IAM/Role]] [[AWS/SSM]] session timed out in the middle of the session, and I couldn't figure out how to get [[Claude Code/Memory]] to work before EOD, so I just copied and pasted my terminal into a text file.
				- update: ((682c815f-e2a5-429b-b5cb-a033598ac14e))