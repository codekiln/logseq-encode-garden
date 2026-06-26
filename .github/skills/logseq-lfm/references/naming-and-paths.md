# Naming conventions and page/file paths

## Singular vs Plural Naming Convention

### Core Principle
- Always use singular form in page names
- Use plural form in references through aliases
- This enables better extensibility through sub-namespaces

### Implementation
1. **Page Names** — singular: `[[Related/Post]]` not `[[Related Topics]]`; `[[Person]]` not `[[People]]`; `[[Project]]` not `[[Projects]]`.
2. **Aliases** — add a plural/contextual form as an alias in the page's frontmatter when you want that link text to resolve to the singular page:
   ```markdown
   ---
   alias:: [[Related Posts]]
   ---
   ```
3. **References** — use the alias link text when you want the plural/contextual surface form: `[[Related Posts]]`. The alias resolves to the singular page name.

### Benefits
- Enables sub-namespaces under singular forms
- Clean URL structure; supports both singular and plural references; hierarchical organization

### Examples

<CORRECT_✅>
- [[Person/John Smith]] (singular person hub; see `[[Logseq/Entity/Person]]` — do not use a parallel `[[People/...]]` alias)
- [[Project/Cursor]] (singular page name) — alias:: [[Projects/Cursor]]
- [[Related/Post]] (singular page name) — alias:: [[Related Posts]]
</CORRECT_✅>

<INCORRECT_❌>
- [[People/John Smith]] (plural in page name — not used for persons in this garden)
- [[Projects/Cursor]] (plural in page name)
- [[Related Topics]] (plural in page name)
</INCORRECT_❌>

### When to Use
Creating new pages; adding aliases; making references; organizing hierarchical content.

### When NOT to Use
- When the page represents a collection/category that is inherently plural
- When the page is a temporary or utility page
- When the page is a system or configuration page

## File Naming vs. Link Format

| Context | Format | Example |
|---------|--------|---------|
| File on disk | `Namespace___SubNamespace___PageName.md` | `OpenAI___Model___GPT___4.md` |
| Link in content | `[[Namespace/SubNamespace/PageName]]` | `[[OpenAI/Model/GPT/4]]` |

### Common Mistakes to Avoid
1. ❌ **Do not create actual directories/folders** for namespaces
   - Wrong: `/pages/OpenAI/Academy.md` — Correct: `/pages/OpenAI___Academy.md`
2. ❌ **Do not use triple underscores in links**
   - Wrong: `[[OpenAI___Academy]]` — Correct: `[[OpenAI/Academy]]`
3. **When discussing Logseq hierarchies in the abstract** (prose, not a live link), put the path in backticks so it's visually distinct, e.g. `Person/Name/GitHub/Project`, `Lazygit/Keyshort/Some action`.

### Creating a New Page: Step by Step
1. Create the file with proper naming: `Namespace___SubNamespace___PageName.md`
2. Add content following LFM rules (bullets, proper indentation)
3. Add a journal entry using forward slashes in the link: `[[Namespace/SubNamespace/PageName]]`

### Examples
- File `/pages/Book___Clean Code.md` → Link `[[Book/Clean Code]]`
- File `/pages/Programming___Language___Python___Type Hints.md` → Link `[[Programming/Language/Python/Type Hints]]`
