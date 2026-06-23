# My Dev Tool Preferences -  [[AI/Coding/Config]] Management - use [[rulesync]]
	- I use Rulesync to manage AI coding tool configurations across my projects.
	-
	- This allows me to maintain consistent rules and settings across different AI tools while keeping everything in version control.
	- ## only use [[rulesync]] to manage AI coding tool configurations
		- ### do not directly edit any individual agentic coding tool config (`.cursor`, `.claude`, etc) instead, update rulesync
			- then call [[rulesync/generate]]
		- ### use `rulesync.jsonc` for project defaults
			- use rulesync includes
			- only generate for [[Codex/CLI]], [[CursorAI]], [[Claude/Code]], [[GitHub/CoPilot/CLI]] for now
		- ### prefer skills to mcp and rules
			- each rule goes in context, which leads to bloat
		- ### Kebab-case filenames
			- `logseq-page-naming.md`, `javascript-best-practices.md`
		- ### Category Organization with Prefixes
			- for ex. (`logseq-*`, `javascript-*`, `python-*`, etc.)
		- ### For now, commit generated [[AI/Coding/Config]]s
			- In the future, we may consider [[git/hooks]] to run [[rulesync/generate]] on check-out, but that's more complicated in cloud-based workflows, so for now I prefer to keep everything in version control
	- ## Workflow
		- 1. **Setup**: Create `rulesync.jsonc` with project targets and features
		  2. **Rules**: Create minimal rule files in `.rulesync/rules/` with category prefixes
		  3. **Generate**: Run `npx rulesync generate` to create tool configurations
		  4. **Commit**: Commit both `.rulesync/` directory and generated files
	- ## `rulesync.jsonc` Configuration File
		- ```jsonc
		  {
		  "targets": ["cursor", "claudecode", "geminicli", "opencode", "codexcli"],
		  "features": ["rules", "ignore", "mcp", "commands", "subagents"],
		  "baseDirs": ["."],
		  "delete": true,
		  "verbose": false,
		  "experimentalGlobal": false,
		  "experimentalSimulateCommands": false,
		  "experimentalSimulateSubagents": false
		  }
		  ```
	- ## Rule File Structure
		- ```md
		  ---
		  root: false
		  description: "Brief description of rule purpose"
		  globs: ["**/*.js", "**/*.jsx"]  # Only if different from project defaults
		  ---
		  
		  # Rule Title
		  
		  Concise, actionable guidance only.
		  ```
	- ## Directory Structure
		- ```
		  .rulesync/
		  ├── rules/           # Rule files (*.md) - organized by category
		  ├── commands/        # Command definitions (*.md)
		  ├── subagents/       # Subagent configurations (*.md)
		  ├── .mcp.json        # MCP server configurations
		  └── .rulesyncignore  # Files to ignore during processing
		  ```
	- ## Example File Organization
		- ```
		  .rulesync/rules/
		  ├── project-overview.md
		  ├── logseq-page-naming.md
		  ├── logseq-asset-management.md
		  ├── javascript-best-practices.md
		  ├── python-coding-standards.md
		  ├── git-commit-conventions.md
		  └── testing-guidelines.md
		  ```
	- ## rulesync Commands
		- ```bash
		  # Initialize rulesync
		  npx rulesync init
		  
		  # Import from existing tools
		  npx rulesync import --targets claudecode --features rules,mcp,commands,subagents
		  
		  # Generate using rulesync.jsonc
		  npx rulesync generate
		  
		  # Generate with overrides
		  npx rulesync generate --targets cursor,claudecode --features rules,mcp
		  ```
-