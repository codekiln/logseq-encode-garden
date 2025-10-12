---
root: false
targets:
  - '*'
description: Logseq Page Naming and Linking Reference'
globs: ['journals/*.md', 'pages/*.md']
---
This document serves as a quick reference for creating and linking to pages in the Logseq knowledge garden.

## File Naming vs. Link Format

| Context | Format | Example |
|---------|--------|---------|
| File on disk | `Namespace___SubNamespace___PageName.md` | `OpenAI___Model___GPT___4.md` |
| Link in content | `[[Namespace/SubNamespace/PageName]]` | `[[OpenAI/Model/GPT/4]]` |

## Common Mistakes to Avoid

1. ❌ **Do not create actual directories/folders** for namespaces
   - Wrong: `/pages/OpenAI/Academy.md`
   - Correct: `/pages/OpenAI___Academy.md`

2. ❌ **Do not use triple underscores in links**
   - Wrong: `[[OpenAI___Academy]]`
   - Correct: `[[OpenAI/Academy]]`

## Creating a New Page: Step by Step

1. Create the file with proper naming: `Namespace___SubNamespace___PageName.md`
2. Add content following Logseq Flavored Markdown rules (bullet points, proper indentation)
3. Add a journal entry using forward slashes in the link: `[[Namespace/SubNamespace/PageName]]`

## Examples

### Example 1: Simple Namespace

- File: `/pages/Book___Clean Code.md`
- Link: `[[Book/Clean Code]]`

### Example 2: Multi-level Namespace

- File: `/pages/Programming___Language___Python___Type Hints.md`
- Link: `[[Programming/Language/Python/Type Hints]]`

Following these conventions ensures that the knowledge garden maintains consistent organization and linking.