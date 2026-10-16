# My Dev Tool Preferences -  [[AI/Coding/Config]] Management - use [[rulesync]]
	- I use Rulesync to manage AI coding tool configurations across my projects.
	-
	- For the project instruction-file choice and Windows portability, see [[My/Pref/Dev/AI/Config/Management/Use AGENTS.md Without Symlinks]].
	- This allows me to maintain consistent rules and settings across different AI tools while keeping everything in version control.
	- ## only use [[rulesync]] to manage AI coding tool configurations
		- ### do not directly edit any individual agentic coding tool config (`.cursor`, `.claude`, etc) instead, update rulesync
			- then call [[rulesync/generate]]
		- ### use `rulesync.jsonc` for project defaults
			- generate for `agentsskills`, `claudecode`, `codexcli`; see [[My/Pref/Dev/AI/Config/Management/Rulesync]] for rationale
		- ### Kebab-case filenames
			- `logseq-page-naming.md`, `javascript-best-practices.md`
		- ### Category Organization with Prefixes
			- for ex. (`logseq-*`, `javascript-*`, `python-*`, etc.)
		- ### For now, commit generated [[AI/Coding/Config]]s
			- [[git/hooks]] can keep outputs current after checkout and merge. My dotfiles already use this; see [[My/Pref/Dev/AI/Config/Management/Rulesync]]. Keeping generated files in version control also makes them available where those hooks do not run.
	- ## Workflow
		- 1. **Setup**: Create `rulesync.jsonc` with project targets and features
		  2. **Rules**: Create minimal rule files in `.rulesync/rules/` with category prefixes
		  3. **Generate**: Run `mise x -- rulesync generate` to create tool configurations
		  4. **Commit**: Commit both `.rulesync/` directory and generated files
	- ## `rulesync.jsonc` Configuration File
		- ```jsonc
		  {
		    "$schema": "https://github.com/dyoshikawa/rulesync/releases/latest/download/config-schema.json",
		    "targets": [
		      "agentsskills",
		      "claudecode",
		      "codexcli"
		    ],
		    "features": ["rules", "skills"],
		    "outputRoots": ["."],
		    "global": false,
		    "delete": true,
		    "gitignoreTargetsOnly": true,
		    "verbose": false
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
		  mise x -- rulesync init
		  
		  # Import from existing tools
		  mise x -- rulesync import --targets claudecode --features rules,mcp,commands,subagents
		  
		  # Generate using rulesync.jsonc
		  mise x -- rulesync generate
		  
		  # Generate with overrides
		  mise x -- rulesync generate --targets cursor,claudecode --features rules,mcp
		  ```
-