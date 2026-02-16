---
targets:
  - '*'
description: 'Format journal entries with editorial-style headings evocative of Harper''s Magazine, The Economist, and The New Yorker'
globs:
  - 'journals/*.md'
---

# Format Journal Entry Command

This command formats a Logseq journal entry with editorial-style headings that evoke the spirit of publications like Harper's Magazine, The Economist, and The New Yorker—particularly the wry, juxtaposed style of Harper's Index.

## Usage

Execute this command with the path to a journal file:

**Command:** `/logseq-format-journal <journal-file-path>`

**Example:**
```
/logseq-format-journal journals/2025_11_08.md
```

## Style Principles

The headings should have an "editorial" feel that is:

- **Wry and ironic**: Play with language, double meanings, and subtle humor
- **Juxtaposed**: Create interesting contrasts between sections
- **Dry and understated**: Avoid overt commentary; let the organization suggest meaning
- **Evocative**: Use clever wordplay, alliteration, or unexpected phrasing
- **Revealing through contrast**: The structure itself should hint at connections or tensions

## Operational Change Log Rule

When the journal includes page maintenance activity (new/imported pages or page updates), format those entries as concise link lists:

- The journal is a public-facing "now page" snapshot of technical adventures, not an audit log
- Use `[[Filed]]` for newly created or imported pages
- Use `[[Updated]]` for modified pages
- Default to bare link-only bullets under each section
- Do not add inline action text next to links (for example, avoid `[[Page]] updated to ...`)
- Do not use repetitive boilerplate such as `Imported [[...]]` or `Updated [[...]] with ...`
- Optional context is allowed only when meaningful to readers, and only as one sentence under the relevant link

Example:

```markdown
- [[Filed]]
	- [[Person/Example]]
		- Added from a conference note that introduced their research.
- [[Updated]]
	- [[Project/Example]]
```

### What This Command Does NOT Do

- **Does NOT create fictitious facts or statistics** (unlike Harper's Index itself)
- **Does NOT add content**—only reorganizes existing content under better headings
- **Does NOT change the actual content**—only the heading structure

## Heading Style Examples

Good editorial-style headings:
- "Protecting the Concentration" (suggests focus and preservation)
- "It's always Acronym-ious with AI" (wordplay on "acrimonious" and acronyms)
- "Freedom and/from Capitalism" (juxtaposition suggesting tension)
- "The Art of the Side-Note" (elevates a minor detail)
- "Tools That Think They're Platforms" (wry observation)
- "When Hierarchy Becomes Heirarchy" (playful redundancy)

Avoid:
- Generic headings like "Notes", "Thoughts", "Ideas"
- Overly descriptive headings that explain everything
- Headings that are too literal or obvious

## Implementation Approach

1. **Analyze the content** in the journal entry to understand themes, connections, and contrasts
2. **Group related items** that create interesting juxtapositions when placed together
3. **Create headings** that:
   - Use wordplay, alliteration, or clever phrasing
   - Suggest meaning through their relationship to other headings
   - Feel like section titles from a literary magazine
   - Are concise but evocative (typically 2-6 words)
4. **Maintain hierarchy** using Logseq's heading structure (##, ###, etc.)
5. **Preserve all content**—only reorganize under new headings

## Heading Generation Guidelines

When creating headings, consider:

- **Wordplay**: Can you play with the language? ("Acronym-ious", "Freedom and/from")
- **Contrast**: What interesting tensions exist? (old/new, free/constrained, tool/platform)
- **Elevation**: Can you elevate a mundane topic? ("The Art of...", "On the Nature of...")
- **Juxtaposition**: What items create interesting friction when grouped?
- **Understatement**: Can you say less to suggest more?

## Example Transformation

**Before:**
```markdown
- Some notes about AI
  - Fine tuning
  - Reinforcement learning
- Logseq thoughts
  - Math support
- Product ideas
  - Writebook
```

**After:**
```markdown
- ## It's always Acronym-ious with AI
  - [[AI/Fine Tuning/Supervised]] aka SFT
  - [[AI/Reinforcement Learning/from AI Feedback]] aka RAFT
- ## #[[AI Knowledge Gardening]]
  - [[Logseq/Math]]
- ## Freedom and/from Capitalism
  - Some inspirational stuff from [[Person/DHH]]
    - [[Once]] - an anti-SAAS manifesto
```

The headings transform generic categories into editorial-style sections that suggest meaning through their phrasing and juxtaposition.

## Notes

- Headings should feel natural and not forced
- It's okay to have a mix of serious and playful headings
- The goal is to make the journal entry feel more like a curated editorial piece
- When in doubt, err on the side of subtlety and understatement
