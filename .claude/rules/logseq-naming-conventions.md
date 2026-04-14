---
paths:
  - journals/*.md
  - pages/*.md
---
# Logseq Naming Conventions
This is an extension to the logseq-flavored-markdown rule for maintaining consistent naming conventions in the knowledge graph.

## Singular vs Plural Naming Convention

### Core Principle
- Always use singular form in page names
- Use plural form in references through aliases
- This enables better extensibility through sub-namespaces

### Implementation
1. **Page Names**
   - Use singular form: `[[Related/Post]]` not `[[Related Topics]]`
   - Use singular form: `[[Person]]` not `[[People]]`
   - Use singular form: `[[Project]]` not `[[Projects]]`

2. **Aliases**
   - Add a plural or contextual form as an alias in the page's frontmatter when you want that link text to resolve to the singular canonical page.
   - Example:
     ```markdown
     ---
     alias:: [[Related Posts]]
     ---
     ```

3. **References**
   - Use the alias link text in references when you want the plural or contextual surface form: `[[Related Posts]]`
   - The alias resolves to the singular page name
   - This maintains consistency while allowing for sub-namespaces

### Benefits
- Enables creation of sub-namespaces under singular forms
- Maintains clean URL structure
- Allows for both singular and plural references
- Supports hierarchical organization

### Examples

<CORRECT_✅>
- [[Person/John Smith]] (singular person hub; see `[[Logseq/Entity/person]]` — do not use a parallel `[[People/...]]` alias)
- [[Project/Cursor]] (singular page name)
  - alias:: [[Projects/Cursor]]
- [[Related/Post]] (singular page name)
  - alias:: [[Related Posts]]
</CORRECT_✅>

<INCORRECT_❌>
- [[People/John Smith]] (plural in page name — not used for persons in this garden)
- [[Projects/Cursor]] (plural in page name)
- [[Related Topics]] (plural in page name)
</INCORRECT_❌>

### When to Use This Convention
- Creating new pages in the knowledge graph
- Adding aliases to existing pages
- Making references to pages
- Organizing hierarchical content

### When Not to Use This Convention
- When the page represents a collection or category that is inherently plural
- When the page is a temporary or utility page
- When the page is a system page or configuration page
