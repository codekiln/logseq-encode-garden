---
paths:
  - '{journals,pages}/*.md'
---
# How a Person is tracked in this Logseq knowledge garden
This is an extension to the logseq-flavored-markdown rule for recording information about a person.

A person entry is a logseq page where the page title matches one of the following patterns:
- [[People/Full Name]] (corresponds to `pages/People___Full Name.md`)
- [[Person/Full Name]] (corresponds to `pages/Person___Full Name.md`)
- [[<AnyNamespace>/People/Full Name]] (e.g., `pages/HU___People___Full Name.md`)
- [[<AnyNamespace>/Person/Full Name]] (e.g., `pages/AI___Person___Full Name.md`)

### When to Create a Person Page

Person pages should only be created for individuals who meet one or more of these criteria:
- Known across multiple platforms (e.g., GitHub, Twitter, Stack Overflow)
- Have a confirmed real identity
- Are significant contributors or maintainers
- Have a substantial online presence
- Are key figures in their field

For other users, use site-specific namespaces:
- `[[CursorAI/Forum/User/Username]]` for Cursor Forum users
- `[[Reddit/User/Username]]` for Reddit users
- `[[StackOverflow/User/Username]]` for Stack Overflow users
- `[[ForumName/User/Username]]` for other forum users

### Creating a Person Page

If you are asked to make an entry for a person, you should:

1. **Search First - CRITICAL for Deduplication**
   - **Before creating or referencing a person page, you MUST search thoroughly:**
     - Search in `pages/People___*.md`, `pages/Person___*.md`, and in any file matching `pages/**___People___*.md` or `pages/**___Person___*.md`
     - Search by full name, partial name, username/handle, and common variations
     - Check aliases in existing person pages (read the `alias::` frontmatter)
     - Look for name variations (e.g., "Shawn Wang" vs "Shawn @swyx Wang" vs "@swyx")
   - **If a person page already exists:**
     - **DO NOT create a new page** - update the existing entry instead
     - **When referencing the person, use the canonical page name** (the actual filename), NOT aliases
     - Example: If page is `Person___Shawn @swyx Wang.md` with alias `[[Person/Shawn Wang]]`, reference it as `[[Person/Shawn @swyx Wang]]`, not `[[Person/Shawn Wang]]`
   - **A single person should NEVER have more than one person page** - this is a critical deduplication rule

2. **Verify Significance**
   - Confirm the person meets the criteria for a person page
   - If not, use the appropriate site-specific namespace instead

3. **Create/Update Page**
   - If a new person page is needed, create it under `[[Person/Full Name]]` by default
   - If the person is referenced in other contexts/namespaces (e.g., `[[People/Full Name]]`, `[[HU/Person/Full Name]]`), add aliases in the frontmatter to those contexts using `alias::` (not `aliases::`)
   - Look up the person on the internet
   - Create a person page for them if they meet the criteria
   - Link the person and a bit of their bio in their page
   - If possible add an image link
   - Include relevant external links (GitHub, LinkedIn, etc.)

4. **Referencing Existing Person Pages**
   - **Always use the canonical page name** when creating references in content
   - The canonical name is the actual page filename (e.g., `Person___Shawn @swyx Wang.md` → `[[Person/Shawn @swyx Wang]]`)
   - **Do NOT use aliases** when referencing - aliases are for backward compatibility, not for new references
   - If unsure of the canonical name, search for the person page first and use the exact page title

5. **Journal Entry**
   - If the person page is new, make an entry in today's journal page that links to that person
   - Use the canonical page name in the journal entry
