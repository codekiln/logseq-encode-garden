---
tags:: [[My/Dev/Tool/Pref/AI/Coding/Config/Management]]
---

# My Dev Tool Preferences - AI Coding Config Management

## Overview

I use Rulesync to manage AI coding tool configurations across my projects. This allows me to maintain consistent rules and settings across different AI tools while keeping everything in version control.

## Key Principles

- **Project-first configuration**: Use `rulesync.jsonc` for project defaults
- **Minimal rule content**: Every rule goes to AI context - keep it concise
- **Kebab-case filenames**: `logseq-page-naming.md`, `javascript-best-practices.md`
- **Category organization**: Use prefixes (`logseq-*`, `javascript-*`, `python-*`, etc.)
- **Commit generated files**: No git hooks needed, everything in version control

## Workflow

1. **Setup**: Create `rulesync.jsonc` with project targets and features
2. **Rules**: Create minimal rule files in `.rulesync/rules/` with category prefixes
3. **Generate**: Run `npx rulesync generate` to create tool configurations
4. **Commit**: Commit both `.rulesync/` directory and generated files

## Configuration File

```jsonc
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

## Rule File Structure

```markdown
---
root: false
description: "Brief description of rule purpose"
globs: ["**/*.js", "**/*.jsx"]  # Only if different from project defaults
---

# Rule Title

Concise, actionable guidance only.
```

## Directory Structure

```
.rulesync/
├── rules/           # Rule files (*.md) - organized by category
├── commands/        # Command definitions (*.md)
├── subagents/       # Subagent configurations (*.md)
├── .mcp.json        # MCP server configurations
└── .rulesyncignore  # Files to ignore during processing
```

## Example File Organization

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

## Commands

```bash
# Initialize rulesync
npx rulesync init

# Import from existing tools
npx rulesync import --targets claudecode --features rules,mcp,commands,subagents

# Generate using rulesync.jsonc
npx rulesync generate

# Generate with overrides
npx rulesync generate --targets cursor,claudecode --features rules,mcp
```

## Supported Tools

- **Claude Code** - Anthropic's Claude Code assistant
- **Cursor** - AI-powered code editor
- **Codex CLI** - OpenAI Codex command line interface
- **Gemini CLI** - Google's Gemini AI CLI
- **GitHub Copilot** - GitHub's AI pair programmer
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

1. **rules** - Generate rule files for AI tools
2. **ignore** - Generate ignore files (like .gitignore)
3. **mcp** - Generate MCP (Model Context Protocol) configurations
4. **commands** - Generate command definitions
5. **subagents** - Generate subagent configurations

## Best Practices

1. **Use Project Configuration First**: Set up `rulesync.jsonc` with your project defaults
2. **Always Include Descriptions**: Every rule should have a clear description
3. **Use Kebab-Case Filenames**: Name files with kebab-case
4. **Organize by Category**: Use prefixes to group related rules
5. **Keep Content Minimal**: Every rule goes to AI context - write only essential information
6. **Minimize Frontmatter**: Only include fields that differ from project defaults
7. **Commit Generated Files**: Keep everything in version control

## Resources

- **Rulesync Repository**: ~/GitHub/others/forks/rulesync
- **GitHub Repository**: https://github.com/dyoshikawa/rulesync
- **Installation**: `npm install -g rulesync`