# Logseq Pages: Logical vs On-Disk

Logseq maintains a **graph** of pages. A page in that graph can exist in two distinct states:

## Two States of a Logseq Page

### 1. On-Disk Page
- Has a corresponding `.md` file (e.g., `pages/Topic___Subtopic.md`)
- Contains actual content authored by the user
- Appears in the graph with its content

### 2. Logical (Reference-Only) Page
- Has **no** `.md` file on disk
- Exists in the graph purely because something links to it: `[[Topic/Subtopic]]`
- Logseq tracks it as a node in the graph, but it has no file content
- Appears as an empty page in the Logseq UI — this is **normal and intentional**

## Critical Rule: Absence of File ≠ Absence of Page

**An agent MUST NOT assume the set of Logseq pages equals the set of `.md` files on disk.**

A page referenced as `[[Namespace/Page]]` anywhere in the graph exists as a logical page, even if no `pages/Namespace___Page.md` file is present.

### Wrong Interpretation
> "I searched for `pages/AI___Concept___Transformer.md` and it doesn't exist, so the page `[[AI/Concept/Transformer]]` doesn't exist in this garden."

### Correct Interpretation
> "There is no on-disk content for `[[AI/Concept/Transformer]]`, but it may still exist as a logical page if anything links to it."

## How to Check Whether a Page Exists

**To check if a page exists in the graph**, search for references to it across all files:
```bash
grep -r "AI/Concept/Transformer" pages/ journals/
```
If any file contains `[[AI/Concept/Transformer]]`, the page exists logically in the graph.

**Do NOT rely solely on**:
```bash
ls pages/AI___Concept___Transformer.md   # ← insufficient — only finds on-disk pages
```

## When to Create a `.md` File

Only create a `.md` file when there is **actual content to put in it**.

- ✅ Create a file when you have notes, documentation, or structured content to add
- ❌ Do NOT create an empty or stub file just to "establish" the page in the graph — linking with `[[Namespace/Page]]` is sufficient
- ❌ Do NOT create a file with only frontmatter and no content, unless the frontmatter itself carries meaningful metadata

## When Linking Is Enough

When adding a reference to a topic in a note or journal entry, simply write `[[Namespace/Page]]`. This is a valid, complete action. You do not need to also create the `.md` file for the link to be meaningful.

Example — this is complete and correct:
```
- Learning about [[AI/Concept/Attention Mechanism]] today
```
No file `pages/AI___Concept___Attention Mechanism.md` is required for this link to work.

## Summary

| Situation | What to do |
|-----------|------------|
| Need to check if page exists | `grep -r "[[Page/Name]]"` across files |
| Linking to a topic | Use `[[Namespace/Page]]` — no file needed |
| Adding real content | Create the `.md` file |
| No content yet | Do not create the file; linking is enough |
