---
root: false
targets:
  - '*'
description: 'Commit conventions with optional ticket references'
---

# Commit Conventions

Follow these commit message conventions for all repositories.

## Basic Format
```
<type>: <description>

[optional body]

[optional footer(s)]
```

## Types
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation-only changes
- `style`: Changes that don't affect code meaning (white-space, formatting, etc)
- `refactor`: Code changes that neither fix a bug nor add a feature
- `perf`: Changes that improve performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools
- `ci`: Changes to CI configuration files and scripts

## Guidelines
- Write in imperative, present tense ("add feature" not "added feature")
- First line should be 50 characters or fewer
- Be descriptive and concise
- Reference documents: [[My/Dev/Tool/Pref/SCM]] in the knowledge base

## Ticket References
- **For Ticket-Based Projects**:
  - Include ticket ID and description as the last line: `PD-12345 Implement login flow`
  - Extract from branch name when possible (e.g., from `feature/PD-12345-description`)
- **For Non-Ticket Projects** (like this repository):
  - Ticket reference is not required
  - Focus on clear, descriptive commit messages following the conventional format

## Optional Extended Format
You can use emoji prefixes with types:
```
<emoji> <type>[optional scope]: <description>
```

Example: `✨ feat: Add new authentication method`