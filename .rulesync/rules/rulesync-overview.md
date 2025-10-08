---
root: false
targets:
  - '*'
description: 'Guide for creating and managing rulesync rules and configurations'
globs: ["**/*.md"]
---

# Rulesync Overview

This guide explains how to create and manage rulesync rules, helping you maintain consistent AI rules across different AI coding tools.

## Rulesync and how to update claude code commands, rules, subagents, gitignore
* don't directly update claude code configuration
* instead, use rulesync configuration to update claude code
* for info about rulesync, check out the repo: ~/GitHub/others/forks/rulesync
* if that is not available, use https://github.com/dyoshikawa/rulesync

## Rule File Structure

Every rule file should follow this structure:

```markdown
---
root: boolean           # Whether this rule is available globally
targets:                # List of AI tools this rule applies to (optional if using rulesync.jsonc)
  - 'tool-name-1'
  - 'tool-name-2'
description: 'string'   # Brief description of what this rule does
globs:                  # File patterns that, if in context, will activate this rule (default to [])
  - 'glob-pattern-1'
  - 'glob-pattern-2'
---

# Rule Title

Rule content in markdown format...
```

**Note**: When using `rulesync.jsonc` for project configuration, you only need to specify `targets` and other settings in individual rule files when they differ from your project defaults. This keeps your rules clean and avoids duplication.

## Supported Tools

Rulesync supports a wide range of AI development tools:

- **AGENTS.md** - For agent-based development
- **Claude Code** - Anthropic's Claude Code assistant
- **Codex CLI** - OpenAI Codex command line interface
- **Gemini CLI** - Google's Gemini AI CLI
- **GitHub Copilot** - GitHub's AI pair programmer
- **Cursor** - AI-powered code editor
- **OpenCode** - Open source AI coding assistant
- **Cline** - AI coding assistant
- **Roo Code** - AI development environment
- **Qwen Code** - Alibaba's Qwen AI coding assistant
- **Kiro IDE** - AI-powered IDE
- **Amazon Q Developer CLI** - AWS AI development tool
- **JetBrains Junie** - JetBrains AI assistant
- **AugmentCode** - AI code augmentation tool
- **Windsurf** - AI coding platform
- **Warp** - AI terminal

## Available Features

Rulesync supports five main features:

1. **rules** - Generate rule files for AI tools
2. **ignore** - Generate ignore files (like .gitignore)
3. **mcp** - Generate MCP (Model Context Protocol) configurations
4. **commands** - Generate command definitions
5. **subagents** - Generate subagent configurations

## YAML Frontmatter Options

### Required Fields

- `root`: Boolean value indicating if this rule is available globally
  - `true`: Rule is available globally across all projects
  - `false`: Rule is only available in the current project
- `description`: String describing the rule's purpose
  - Always include this for clarity and organization
  - Helps with rule management and debugging

### Optional Fields (Override Project Defaults)

When using `rulesync.jsonc`, these fields are optional and only needed when they differ from your project configuration:

- `targets`: Array of AI tool names that should apply this rule
  - Example: `['claudecode', 'cursor']`
  - Use `*` to target all supported tools
  - **Omit if same as project defaults**

- `globs`: Array of file patterns this rule applies to
  - Example: `['**/*.js', 'src/**/*.ts']`
  - Rules only apply to files matching these patterns
  - **Omit if using default patterns**

- `ignore`: Boolean value (default: `false`)
  - `true`: Files matching this rule's globs will be ignored
  - `false`: Files matching this rule's globs will be processed

## Example Rule Files

### Project Overview Rule (Using Project Defaults)

```markdown
---
root: true
description: "Project overview and development guidelines"
---

# Project Overview

This is a comprehensive guide for AI coding assistants working on this project.

## Key Guidelines
- Follow established coding standards
- Use consistent naming conventions
- Write clear, maintainable code
- Include appropriate documentation
```

### Language-Specific Rule (Overriding Targets)

```markdown
---
root: false
targets: ["claudecode", "cursor"]
description: "JavaScript best practices"
globs: ["**/*.js", "**/*.jsx"]
---

# JavaScript Best Practices

When working with JavaScript code, follow these guidelines:

1. Use `const` and `let` instead of `var`
2. Prefer arrow functions for anonymous functions
3. Use template literals for string interpolation
4. Use destructuring assignment when appropriate
5. Use modern ES6+ features when available
```

### Minimal Rule (Only Override What's Different)

```markdown
---
root: false
description: "Python coding guidelines"
globs: ["**/*.py"]
---

# Python Guidelines

Follow PEP 8 style guidelines and use type hints where appropriate.
```

### Example File Organization

```
.rulesync/rules/
├── project-overview.md
├── logseq-page-naming.md
├── logseq-asset-management.md
├── javascript-best-practices.md
├── python-coding-standards.md
├── git-commit-conventions.md
└── testing-guidelines.md
```

## Best Practices

1. **Use Project Configuration First**: Set up `rulesync.jsonc` with your project defaults, then only override in individual rules when necessary
2. **Always Include Descriptions**: Every rule should have a clear description for organization and debugging
3. **Use Kebab-Case Filenames**: Name files with kebab-case (e.g., `logseq-page-naming.md`, `javascript-best-practices.md`)
4. **Organize by Category**: Use prefixes to group related rules (`logseq-*`, `javascript-*`, `python-*`, etc.)
5. **Keep Content Minimal**: Every rule goes to AI context - write only essential, actionable information
6. **Minimize Frontmatter**: Only include `targets`, `globs`, and other fields in rule files when they differ from project defaults
7. **Use Organized Structure**: Place rules in `.rulesync/rules/` directory with descriptive filenames
8. **Be Specific with Globs**: Use specific glob patterns to ensure rules only apply to relevant files
9. **Use Clear Descriptions**: Make rule descriptions clear and concise
10. **Group Related Rules**: Keep related rules together in similarly-named files
11. **Specify Target Tools**: Only target the tools you actually use
12. **Organize by Domain**: Create separate rule files for different domains or technologies
13. **Keep Rules Focused**: Each rule file should focus on a specific concern
14. **Use Configuration Files**: Leverage `rulesync.jsonc` for project-wide settings
15. **Version Control**: Commit both your `.rulesync/` directory and all generated files to the repo
16. **Test Your Rules**: Use `--verbose` flag to debug rule application

## Common Command Patterns

### Initialize Rulesync

```bash
# Create necessary directories, sample rule files, and configuration file
npx rulesync init
```

### Import Rules from AI Tools

```bash
# Import from specific tools
npx rulesync import --targets claudecode
npx rulesync import --targets cursor
npx rulesync import --targets copilot

# Import specific features
npx rulesync import --targets claudecode --features rules,mcp,commands,subagents
```

### Generate Rules (Using Configuration File)

```bash
# Generate all features for tools specified in rulesync.jsonc
npx rulesync generate

# Generate with specific options (overrides rulesync.jsonc)
npx rulesync generate --targets cursor,claudecode --features rules,mcp
```

### Work with Global Rules (Experimental)

```bash
# Import to global rules directory
npx rulesync import --experimental-global --targets claudecode

# Generate from global rules directory
npx rulesync generate --experimental-global --targets "*"
```

### Experimental Features

```bash
# Generate simulated commands and subagents
npx rulesync generate --targets copilot,cursor,codexcli --features commands,subagents --experimental-simulate-commands --experimental-simulate-subagents
```

### Utility Commands

```bash
# Check rulesync version and help
npx rulesync --version
npx rulesync --help
```

## Configuration File

You can configure Rulesync by creating a `rulesync.jsonc` file in the root of your project. **Only the tools listed in `targets` will be generated**:

```jsonc
{
  // List of tools to generate configurations for - ONLY these will be generated
  "targets": ["cursor", "claudecode", "geminicli", "opencode", "codexcli"],
  
  // Features to generate
  "features": ["rules", "ignore", "mcp", "commands", "subagents"],
  
  // Base directories for generation
  "baseDirs": ["."],
  
  // Delete existing files before generating
  "delete": true,
  
  // Verbose output
  "verbose": false,
  
  // Experimental features
  "experimentalGlobal": false,
  "experimentalSimulateCommands": false,
  "experimentalSimulateSubagents": false
}
```

**Important**: Only the tools specified in the `targets` array will have their configuration files generated. This allows you to control exactly which AI tools get configuration files in your project.

## Directory Structure

Rulesync uses the following directory structure:

```
.rulesync/
├── rules/           # Rule files (*.md) - organized by category with kebab-case names
├── commands/        # Command definitions (*.md)
├── subagents/       # Subagent configurations (*.md)
├── .mcp.json        # MCP server configurations
└── .rulesyncignore  # Files to ignore during processing
```

### Rule File Naming Convention

- **Use kebab-case**: `logseq-page-naming.md`, `javascript-best-practices.md`
- **Organize by category**: Use prefixes to group related rules
  - `logseq-*` for Logseq-specific rules
  - `javascript-*` for JavaScript rules
  - `python-*` for Python rules
  - `git-*` for Git-related rules
  - `testing-*` for testing rules

### Content Guidelines

**Keep rules minimal and focused** - every rule file is added to AI context, so:
- Write concise, essential information only
- Avoid redundant content
- Focus on specific, actionable guidance
- Remove unnecessary examples or verbose explanations

## Troubleshooting

- **Rule not applying**: Check that file paths match your glob patterns
- **Missing rules**: Verify the rule was imported correctly and targets the right tool
- **Duplicate rules**: Look for conflicting rules with overlapping globs
- **Command not found**: Ensure rulesync is installed globally (`npm install -g rulesync`)
- **Permission errors**: Check file permissions in the target directories
- **Configuration issues**: Verify your `rulesync.jsonc` file syntax is correct