tags:: [[GitHub/Issue/My]], [[Anthropic/App/Claude Code/Command/Slash/Custom]]

- # [Feature request: for claude code slash commands, support passing through claude-code-specific yaml markdown frontmatter keys to the generated command markdown files · Issue #413 · dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync/issues/413)
	- ## [[Original Poster]]
		- # Feature Request: Support Claude Code-Specific YAML Frontmatter Keys for Commands
		  
		  NOTE: *this feature request was drafted with the assistance of [this deepwiki thread](https://deepwiki.com/search/claude-code-slash-commands-all_82ed05e6-e4cf-4c98-af1f-295a538d8954).*
		- ## Summary
		  
		  Currently, rulesync commands defined in `.rulesync/commands/*.md` only support a minimal frontmatter schema with `description` as the only field that gets passed through to Claude Code slash commands. However, Claude Code's native slash command format [supports additional YAML frontmatter keys](https://docs.claude.com/en/docs/claude-code/slash-commands#frontmatter) like `allowed-tools`, `argument-hint`, `model`, and `disable-model-invocation` that enable powerful command customization. This feature request proposes adding support for passing through these Claude Code-specific keys from rulesync command definitions to generated Claude Code command files.
		- ## Current Limitation
		  
		  When converting from `RulesyncCommand` to `ClaudecodeCommand`, only the `description` field is extracted and passed through. The `ClaudecodeCommand` schema itself only defines `description` in its frontmatter, meaning there's no mechanism to specify tool-specific configuration like `allowed-tools` or `model`.
		- ## Precedent: Subagents Already Support This Pattern
		  
		  Interestingly, rulesync **subagents** already implement a solution to this exact problem. The `RulesyncSubagent` frontmatter schema includes a `claudecode:` section that allows tool-specific configuration. This configuration gets properly passed through during conversion to `ClaudecodeSubagent`.
		- ## Proposed Feature Specification
		- ### 1. Extend RulesyncCommand Frontmatter Schema
		  
		  Add a `claudecode:` section to the `RulesyncCommandFrontmatter` schema (similar to how subagents work)<cite />:
		  
		  ```yaml
		  ---
		  description: "Create a git commit"
		  claudecode:
		  allowed-tools: "Bash(git add:*), Bash(git status:*), Bash(git commit:*)"
		  argument-hint: "[message]"
		  model: "claude-3-5-haiku-20241022"
		  disable-model-invocation: false
		  ---
		  
		  Create a git commit with message: $ARGUMENTS
		  ```
		- ### 2. Supported Claude Code Keys
		  
		  The `claudecode:` section should support all Claude Code-specific frontmatter keys:
		- **`allowed-tools`**: Restrict which tools the command can use (e.g., `"Bash(git add:*), Bash(git status:*)"`)
		- **`argument-hint`**: Display hint for command arguments (e.g., `"[message]"` or `"[pr-number] [priority] [assignee]"`)
		- **`model`**: Specify which Claude model to use (e.g., `"claude-3-5-haiku-20241022"`)
		- **`disable-model-invocation`**: Whether to prevent `SlashCommand` tool from calling this command
		- ### 3. Conversion Behavior
		  
		  When generating Claude Code commands via `rulesync generate --targets claudecode --features commands`<cite />:
		  
		  1. Extract the `claudecode:` section from the rulesync command frontmatter
		  2. Merge these keys into the generated Claude Code command's YAML frontmatter
		  3. Preserve the `description` field at the top level (as it currently works)
		  4. For other tool targets (Cursor, Roo, etc.), ignore the `claudecode:` section
		- ### 4. Backward Compatibility
		- Existing commands without a `claudecode:` section should continue to work as they do today
		- The `description` field should remain at the top level of frontmatter for all tools
		- Other tool-specific sections (e.g., `roo:`, `cursor:`) could be added in the future following the same pattern
		- ## Example Usage
		  
		  **Input**: `.rulesync/commands/git-commit.md`
		  ```yaml
		  ---
		  description: "Create a git commit"
		  claudecode:
		  allowed-tools: "Bash(git add:*), Bash(git status:*), Bash(git commit:*)"
		  argument-hint: "[message]"
		  model: "claude-3-5-haiku-20241022"
		  ---
		  
		  Create a git commit with message: $ARGUMENTS
		  ```
		  
		  **Output**: `.claude/commands/git-commit.md` (after `rulesync generate`)
		  ```yaml
		  ---
		  allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
		  argument-hint: [message]
		  description: Create a git commit
		  model: claude-3-5-haiku-20241022
		  ---
		  
		  Create a git commit with message: $ARGUMENTS
		  ```
		- ## Benefits
		  
		  1. **Feature Parity**: Commands would have the same tool-specific configuration capabilities that subagents already have<cite />
		  2. **Full Claude Code Support**: Users could leverage all Claude Code slash command features through rulesync
		  3. **Consistent Pattern**: Follows the established `claudecode:` section pattern used by subagents 
		  4. **Extensibility**: The pattern could be extended to other tools (e.g., `roo:`, `cursor:`) in the future
		- ## Notes
		- The Roo command implementation already supports `argument-hint` as a top-level field, but this is tool-specific rather than following a general pattern
		- This feature would make commands a first-class citizen alongside subagents in terms of tool-specific configuration support
		- Global mode currently supports commands for Claude Code, so this feature would enhance that capability as well
	-