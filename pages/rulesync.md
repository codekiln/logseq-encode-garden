# [dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync?tab=readme-ov-file#supported-tools-and-features)
	- ## Overview
		- > A Node.js CLI tool that automatically generates configuration files for various AI development tools from unified AI rule files. Features selective generation, comprehensive import/export capabilities, and supports major AI development tools with rules, commands, MCP, ignore files, and subagents. Uses the recommended `.rulesync/rules/*.md` structure, with full backward compatibility for legacy `.rulesync/*.md` layouts.
	- ## Installation
		- Pick one of the two
		- ### 1 - Install globally using npm:
			- ```bash
			  npm install -g rulesync
			  ```
		- ### 2 - Add to [[mise/Config/mise.toml]] in home directory
			- {{embed [[rulesync/mise]]}}
	- ## Usage
		- ### Basic Commands
			- **Import AI tool configs to unified rules files**:
				- ```bash
				  rulesync import [--targets <tool-names>]
				  ```
			- **Generate AI tool configs from unified rules files**:
				- ```bash
				  rulesync generate [--targets <tool-names>] [--features <feature-names>]
				  ```
			- #### Generate all AI tool configs
				- ```
				  rulesync generate --targets "*" --features "*"
				  ```
		- ### File Structure
			- Rulesync uses the `.rulesync` directory at the root of your project
			- Recommended structure:
				- `.rulesync/rules/*.md` - Rule files
				- `.rulesync/commands/*.md` - Command files (slash commands)
				- `.rulesync/subagents/*.md` - Subagent definitions
			- Legacy structure (still supported):
				- `.rulesync/*.md`
		- ### File Format
			- Rules, commands, and subagents are defined in Markdown files with YAML frontmatter
			- Rule file example:
				- ```yaml
				  ---
				  root: true               # Make this rule available globally
				  targets:                 # Which AI tools this applies to
				    - 'claude-code'
				    - 'cursor'
				  description: ''          # Optional description
				  globs:                   # File patterns this rule applies to
				    - '**/*.py'
				  ---
				  # Python Best Practices
				  
				  [Rule content here...]
				  ```
	- ## Supported Tools
		- > A Node.js CLI tool that automatically generates configuration files for various AI development tools from unified AI rule files. Features selective generation, comprehensive import/export capabilities, and supports major AI development tools with rules, commands, MCP, ignore files, and subagents. Uses the recommended `.rulesync/rules/*.md` structure, with full backward compatibility for legacy `.rulesync/*.md` layouts.
		- Rulesync supports both **generation** and **import** for All of the major AI coding tools:
		  | Tool | rules | ignore | mcp | commands | subagents |
		  | ---- | ---- | ---- |
		  | AGENTS.md | ✅ |  |  |  |  |
		  | Claude Code | ✅ | ✅ | ✅ | ✅ | ✅ |
		  | Codex CLI | ✅ | ✅ |  | 🎮 | 🎮 |
		  | Gemini CLI | ✅ | ✅ |  | ✅ | 🎮 |
		  | GitHub Copilot | ✅ |  | ✅ | 🎮 | 🎮 |
		  | Cursor | ✅ | ✅ | ✅ | ✅ | 🎮 |
		  | OpenCode | ✅ |  |  |  |  |
		  | Cline | ✅ | ✅ | ✅ |  |  |
		  | Roo Code | ✅ | ✅ | ✅ | ✅ | 🎮 |
		  | Qwen Code | ✅ | ✅ |  |  |  |
		  | Kiro IDE | ✅ | ✅ |  |  |  |
		  | Amazon Q Developer CLI | ✅ |  | ✅ |  |  |
		  | JetBrains Junie | ✅ | ✅ |  |  |  |
		  | AugmentCode | ✅ | ✅ |  |  |  |
		  | Windsurf | ✅ | ✅ |  |  |  |
		  | Warp | ✅ |  |  |  |  |
		- 🎮: Simulated Commands/Subagents (Experimental Feature)
	- ## Advanced Features
		- ### Command Line Options
			- `--targets <tool-names>`: Specify which AI tools to target
				- Use comma-separated values or "*" for all tools
				- Example: `--targets "claude-code,cursor"`
			- `--features <feature-names>`: Specify which features to generate
				- Options: "rules", "commands", "subagents", "mcp", "ignore"
				- Example: `--features "rules,commands"`
			- `--global`: Use global rules (in home directory) instead of project rules
			- `--verbose`: Enable verbose logging
		- ### Frontmatter Options
			- **Rules Files**:
				- `root`: Boolean, make rule available globally (default: false)
				- `targets`: Array of tool names this rule applies to
				- `description`: String, optional description
				- `globs`: Array of file patterns this rule applies to
			- **Commands Files**:
				- `targets`: Array of tool names this command applies to
				- `description`: Short description for the slash command
			- **Subagents Files**:
				- `targets`: Array of tool names this subagent applies to
				- `description`: Description of what the subagent does
	- ## Common Workflows
		- ### Syncing Between AI Tools
			- **Import from one tool, generate for others**:
				- ```bash
				  # Import from Cursor
				  rulesync import --targets cursor
				  # Generate for all other tools
				  rulesync generate --targets "*" --features "*"
				  ```
		- ### Creating Shared Rules
			- 1. Create rule files in `.rulesync/rules/*.md`
			- 2. Add appropriate frontmatter targeting desired tools
			- 3. Run `rulesync generate` to apply to all AI tools
		- ### Global vs Project-Specific Rules
			- Global rules apply to all projects
				- Import: `rulesync import --global`
				- Generate: `rulesync generate --global`
			- Project rules apply only to current project
				- Import: `rulesync import`
				- Generate: `rulesync generate`
	-