Please also reference the following documents as needed:

@.claude/memories/commit-conventions.md description: "Commit conventions with optional ticket references" globs: ""
@.claude/memories/convert-from-md-to-lfm.md description: "" globs: ""
@.claude/memories/rulesync-overview.md description: "Guide for creating and managing rulesync rules" globs: "**/*.md,**/*.mdc"
@.claude/memories/diataxis-explanation.md description: "" globs: ""
@.claude/memories/diataxis-how-to.md description: "" globs: ""
@.claude/memories/diataxis-reference.md description: "" globs: ""
@.claude/memories/diataxis-tutorial.md description: "" globs: ""
@.claude/memories/journal-updates.md description: "Guidelines for updating journal entries when modifying pages" globs: ""
@.claude/memories/logseq-ai-model-details-page.md description: "" globs: ""
@.claude/memories/logseq-ai-model-reference.md description: "" globs: ""
@.claude/memories/logseq-asset-linker.md description: "" globs: ""
@.claude/memories/logseq-directory-structure.md description: "" globs: ""
@.claude/memories/logseq-flavored-markdown.md description: "" globs: ""
@.claude/memories/logseq-forum-post.md description: "" globs: ""
@.claude/memories/logseq-naming-conventions.md description: "" globs: ""
@.claude/memories/logseq-overview.md description: "" globs: ""
@.claude/memories/logseq-page-naming-reference.md description: "Reference for correct Logseq page naming and linking conventions" globs: ""
@.claude/memories/logseq-person.md description: "" globs: ""
@.claude/memories/logseq-slides.md description: "" globs: ""
@.claude/memories/logseq-youtube-notes.md description: "How to intake and format notes on a youtube video" globs: ""
@.claude/memories/typical-week-structure.md description: "" globs: ""
# Logseq Encode Garden - Instructions for Claude

## Repository Overview
This repository is a personal Logseq knowledge graph (not a project) containing personal notes, research, and thoughts. It's organized using Logseq's hierarchical structure with specific formatting requirements.

## Key Directories
- `pages/` - Contains all non-journal pages organized with namespaces using triple underscores (e.g., `Project___Tasks.md`)
- `journals/` - Contains daily journal entries in YYYY_MM_DD.md format
- `assets/` - Stores images, PDFs, and other attachments referenced in markdown files
- `logseq/` - Configuration directory for the Logseq graph
- `.ai-coding/` - Contains AI-related coding resources
- `tools/` - Contains utility scripts and tools
- `.cursor/rules/logseq-cursor-rules/` - Git submodule with Cursor AI rules for working with Logseq

## Working with Logseq Files

### Logseq Flavored Markdown (LFM) Rules
1. **Structure**: 
   - All content, including headings, must be prefixed with bullet points (`-`)
   - TAB indentation determines parent/child relationships
   - No blank newlines between content

2. **Headings**:
   - Format: `- # Heading Text` (note the bullet point before the #)
   - Nest properly: H2 under H1, H3 under H2, etc.

3. **No Ordered Lists**:
   - Use numbered bullet points instead: `- 1. First item`

4. **Namespaces**:
   - Pages can be hierarchical: `[[Project/Tasks]]`
   - In filesystem: `Project___Tasks.md` (triple underscore)
   - Don't invent new namespaces unless specifically requested

### Critical Warning
- **NEVER modify, add, or remove the `tags::` frontmatter** in any document
- The user has a specific tagging system that follows particular rules
- Always preserve existing frontmatter tags exactly as they appear

## Common Tasks
1. When searching the knowledge base, focus on using these search approaches:
   - Search for specific pages with namespaces
   - Look for related content in journal entries
   - Use tags to find themed content

2. When adding new content:
   - Follow Logseq Flavored Markdown syntax precisely
   - Respect existing namespaces
   - Don't create new namespace patterns without explicit instructions
   - Place journal entries in the appropriate YYYY_MM_DD.md file

3. Working with code:
   - Use proper code block syntax with triple tildes (`~~~`)
   - Maintain existing formatting patterns

## Special Instructions
- This is a personal knowledge graph, not a software project
- No need to create progress.md files for tracking work
- When creating new pages, follow existing naming conventions
- When adding content to journals, respect the date-based structure

## Git Submodule Management
- The repository contains a Git submodule at `.cursor/rules/logseq-cursor-rules/`
- When working with this submodule, use `git submodule` commands
- You have permission to run `git submodule` commands automatically
