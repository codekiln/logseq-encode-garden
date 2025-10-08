---
root: false
targets:
  - '*'
description: 'How I use Rulesync for AI coding tool configuration management'
globs: ["**/*.md"]
---

# Rulesync Usage

I use Rulesync to manage AI coding tool configurations across projects. This keeps rules consistent and in version control.

## How I Use It

- **Configuration**: Set up `rulesync.jsonc` with project targets and features
- **Rules**: Create minimal rule files in `.rulesync/rules/` with kebab-case names and category prefixes
- **Generate**: Run `npx rulesync generate` to create tool configurations
- **Commit**: Commit both `.rulesync/` directory and generated files

## Key Principles

- Project-first configuration via `rulesync.jsonc`
- Minimal rule content (everything goes to AI context)
- Kebab-case filenames with category prefixes (`logseq-*`, `javascript-*`, etc.)
- Commit generated files (no git hooks needed)

## Commands

```bash
# Initialize
npx rulesync init

# Import from existing tools
npx rulesync import --targets claudecode --features rules,mcp,commands,subagents

# Generate using rulesync.jsonc
npx rulesync generate
```

## More Information

For detailed documentation, see `pages/My___Dev___Tool___Pref___AI___Coding___Config___Management.md`.