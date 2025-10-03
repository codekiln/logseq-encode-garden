---
root: false
targets:
  - '*'
description: 'Guide for creating and managing rulesync rules'
globs:
  - '**/*.md'
  - '**/*.mdc'
---

# Creating and Managing Rulesync Rules

This guide explains how to create and manage rulesync rules, helping you maintain consistent AI rules across different AI coding tools.

## Rule File Structure

Every rule file should follow this structure:

```markdown
---
root: boolean           # Whether this rule is available globally
targets:                # List of AI tools this rule applies to
  - 'tool-name-1'
  - 'tool-name-2'
description: 'string'   # Brief description of what this rule does
globs:                  # File patterns this rule applies to
  - 'glob-pattern-1'
  - 'glob-pattern-2'
---

# Rule Title

Rule content in markdown format...
```

## YAML Frontmatter Options

### Required Fields

- `targets`: Array of AI tool names that should apply this rule
  - Example: `['claude-code', 'cursor']`
  - Use `*` to target all supported tools

### Optional Fields

- `root`: Boolean value (default: `false`)
  - `true`: Rule is available globally across all projects
  - `false`: Rule is only available in the current project
- `description`: String describing the rule's purpose
- `globs`: Array of file patterns this rule applies to
  - Example: `['**/*.js', 'src/**/*.ts']`
  - Rules only apply to files matching these patterns
- `ignore`: Boolean value (default: `false`)
  - `true`: Files matching this rule's globs will be ignored
  - `false`: Files matching this rule's globs will be processed

## Example Rule Files

### JavaScript Best Practices Rule

```markdown
---
root: false
targets:
  - 'claude-code'
  - 'cursor'
description: 'JavaScript best practices'
globs:
  - '**/*.js'
  - '**/*.jsx'
---

# JavaScript Best Practices

When working with JavaScript code, follow these guidelines:

1. Use `const` and `let` instead of `var`
2. Prefer arrow functions for anonymous functions
3. Use template literals for string interpolation
4. Use destructuring assignment when appropriate
5. Use modern ES6+ features when available
```

### Python Ignore Rule

```markdown
---
root: false
targets:
  - 'claude-code'
  - 'cursor'
description: 'Ignore Python test files'
globs:
  - '**/test_*.py'
  - '**/tests/*.py'
ignore: true
---

# Python Test Files Ignore Rule

This rule tells AI coding tools to ignore Python test files.
```

## Best Practices

1. **Be Specific with Globs**: Use specific glob patterns to ensure rules only apply to relevant files
2. **Use Clear Descriptions**: Make rule descriptions clear and concise
3. **Group Related Rules**: Keep related rules together in similarly-named files
4. **Specify Target Tools**: Only target the tools you actually use
5. **Organize by Domain**: Create separate rule files for different domains or technologies
6. **Keep Rules Focused**: Each rule file should focus on a specific concern

## Common Command Patterns

### Import Rules from AI Tool

```bash
# Import from Cursor
rulesync import --targets cursor
```

### Generate Rules for AI Tools

```bash
# Generate for all tools
rulesync generate --targets "*" --features "*"

# Generate just rules for specific tools
rulesync generate --targets "claude-code,cursor" --features "rules"
```

### Work with Global Rules

```bash
# Import to global rules directory
rulesync import --global --targets cursor

# Generate from global rules directory
rulesync generate --global --targets "*"
```

## Troubleshooting

- **Rule not applying**: Check that file paths match your glob patterns
- **Missing rules**: Verify the rule was imported correctly and targets the right tool
- **Duplicate rules**: Look for conflicting rules with overlapping globs