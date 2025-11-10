---
# true that is less than or equal to one file for overview such as `AGENTS.md`, false for details such as `.agents/memories/*.md`
root: false
# * = all, or specific tools
targets:
  - '*'
description: 'How a Person is tracked in this Logseq knowledge garden'
# see https://github.com/isaacs/node-glob?tab=readme-ov-file#usage
globs: ['{journals,pages}/*.md']
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

1. **Search First**
   - Search in `pages/People___*.md`, `pages/Person___*.md`, and in any file matching `pages/**___People___*.md` or `pages/**___Person___*.md` to find if a person already exists
   - If it already exists, then you should **update** the existing entry
   - A single person should not have more than one person page

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

4. **Journal Entry**
   - If the person page is new, make an entry in today's journal page that links to that person
