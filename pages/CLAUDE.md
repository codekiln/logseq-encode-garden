# Pages Directory - Instructions for Claude

## Directory Purpose
This directory contains all non-journal pages in the Logseq knowledge graph, representing permanent notes, concepts, projects, and reference materials.

## Pages Structure and Organization

### File Naming and Namespaces
- Files are named using the Logseq namespace convention: `Topic___Subtopic___Detail.md`
- Triple underscores (`___`) in filenames represent hierarchical slashes (`/`) in Logseq namespaces
- Example: `AI___Coding___Technique___Phased Planning.md` appears as `[[AI/Coding/Technique/Phased Planning]]` in Logseq

### Common Namespaces
The knowledge graph uses several consistent namespace patterns:
- `Person/` - Notes about specific individuals, often with nested structures (e.g., `Person/Name/Blog`)
- `AI/` - Artificial intelligence topics, often with `AI/Coding`, `AI/Tool`, etc.
- `GitHub/` - GitHub repositories and related resources
- `Book/` - Book notes and references
- `Project/` - Project-related notes and specifications

### Page Content Structure
1. **Page-level attributes**:
   - Often at the top of files, formatted as `attribute:: value`
   - CRITICAL: Never modify `tags::` frontmatter attributes
   - Common attributes: `alias::`, `tags::`, `public::`, etc.

2. **Content organization**:
   - All content uses Logseq Flavored Markdown (LFM)
   - All content must be prefixed with bullet points (`-`)
   - Proper heading hierarchy (`- #`, `- ##`, etc.)
   - Indentation using TAB character to indicate hierarchical relationships

## Working with Pages

### When Adding or Modifying Content
1. Follow existing namespace patterns and file naming conventions
2. Preserve page-level attributes, especially `tags::` frontmatter
3. Use proper LFM formatting with bullet points and indentation
4. Link related concepts using the `[[Page Name]]` syntax
5. Respect the existing content structure and organization

### When Creating New Pages
1. Check if a similar page already exists before creating new ones
2. Use appropriate namespaces based on the content type
3. Follow naming conventions consistent with similar pages
4. Structure content with proper headers and bullet points
5. Link the page to relevant existing pages

### When Searching or Analyzing
1. Consider the namespace hierarchy for context
2. Look for links to and from the page
3. Check for related content in different namespaces
4. Note any page-level attributes for classification

## Special Page Types

### Person Pages
- Typically contain biographical info and links to the person's work
- Often structured with sections for their background, contributions, and resources

### Project Pages
- Contain specifications, notes, and progress tracking for projects
- Often link to GitHub repositories and related resources

### Concept Pages
- Define and explore specific concepts with explanations and references
- Usually contain links to related concepts and examples

## Reference
Always refer to the main CLAUDE.md in the repository root for general guidelines and follow Logseq Flavored Markdown formatting rules precisely.