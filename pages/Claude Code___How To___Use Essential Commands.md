tags:: [[Diataxis/How To]]
alias:: [[Anthropic/App/Claude Code/How To/Use Essential Commands]]

- # How To Use Essential Claude Code Commands
	- ## Goal
		- Quickly apply five Claude Code commands that automate tests, reuse docs, save tokens, and deepen reasoning in any project.
	- ## Preconditions
		- Claude Code ≥ v1.0 installed and in `PATH`
		- MCP server linked to GitHub
		- Project open in Cursor or terminal with git initialized
	- ## Procedure
		- ### 1. Set Up Project Rules with `claude.md`
			- Run `/init` and confirm creation of `claude.md`.
			- Edit the file with rules such as:  
			  1. Write secure, best-practice Python code  
			  2. Generate & run tests for each function; iterate until tests pass  
			  3. Delete test scripts after success  
			  4. Commit after every new function
			- Commit `claude.md` to the repo so Claude Code enforces the rules automatically.
		- ### 2. Add Custom User Commands
			- Create `claude-commands/claude-docs.md` (or any `.md`) containing reference snippets.
			- Invoke it anywhere: `/user claude-docs "Give me a Claude API example"`. Claude Code injects the file’s content for instant answers.
		- ### 3. Run One-Shot File-Scoped Queries with `-p`
			- Pipe a single file to Claude Code to cut token usage:
			  ~~~bash
			  cat src/utils.py | claude -p "What does the sanitize_input function do?"
			  ~~~
			- Claude focuses only on the piped file, answers, then exits.
		- ### 4. Extract Context from Images
			- Drag-and-drop a screenshot (e.g., code from docs) into chat.
			- Prompt: “Extract the text” → Claude performs OCR; follow up with coding questions using the extracted text.
		- ### 5. Control Output & Encourage Deep Reasoning
			- Structured output:  
			  ~~~bash
			  claude -p "List 10 currency pairs with rates" --output-format json
			  ~~~
			- Extended thinking: prepend your query with **“Think deeply about …”** to trigger longer, more rigorous analysis.
	- ## Troubleshooting
		- *Command not found* → confirm `claude --version` returns correctly.
		- *Rules ignored* → ensure `claude.md` is at project root and committed.
		- *Token overrun* → use `-p` or split context into smaller files.
		- *Image OCR failed* → use clear PNG/JPG < 5 MB and retry drag-drop.
	- ## References
		- [Claude Code Official Documentation](https://docs.anthropic.com/en/docs/claude-code/overview)
		- [Project Rules with `claude.md`](https://docs.anthropic.com/en/docs/claude-code/project-rules)