---
targets:
  - '*'
root: false
globs: []
cursor:
  alwaysApply: false
---
# Formatting Forum Posts in Logseq

This rule defines the standard format for importing and structuring forum posts in Logseq, including posts from Cursor, Reddit, Stack Overflow, and other forums. This rule works in conjunction with [[logseq-person.mdc]] for handling person references.

### ⚠️ CRITICAL: DO NOT MODIFY FRONTMATTER TAGS ⚠️

- **NEVER** modify, add, or remove the `tags::` frontmatter item specifically
- The `tags::` frontmatter (e.g., `tags:: [[MyTagHere]], [[MySecondTagHere]]`) is strictly protected
- Even if you think a tag is missing or incorrect, DO NOT change the `tags::` frontmatter
- This restriction applies ONLY to the `tags::` frontmatter item, not to other page attributes

### Basic Structure

- Forum posts should be structured hierarchically using Logseq's bullet-point system
- Each post should start with a title that links to the original post
- Use proper indentation with TAB characters
- All content must be prefixed with bullet points (`-`)

### Required Sections

1. **Title and Link**
   - Format: `- # [Post Title - Forum Name](original-url)`
   - Include the forum name in the title for clarity
   - Example: `- # [How can I increase the indexing depth for @docs? - Discussion - Cursor - Community Forum](https://forum.cursor.com/t/how-can-i-increase-the-indexing-depth-for-docs/77949)`

2. **Metadata**
   - Include creation date if available: `date-created:: [[YYYY/MM/DD]]`
   - Include author if available:
     - For known persons: `created-by:: [[Person/Full Name]]`
     - For usernames: `created-by:: [[ForumName/User/Username]]`
   - Add relevant tags: `tags:: [[ForumName]], [[Topic]]`

3. **Content Sections**
   - Original Poster: `- ## #[[Original Poster]]`
     - For known persons: `[[Person/Full Name]]`
     - For usernames: `[[ForumName/User/Username]]`
   - Responses: `- ## #[[Response]]`
     - Format each response with appropriate reference
   - Related Topics: `- ## #[[Related/Post]]`
   - My Notes: `- ## #[[My Notes]]` (for your personal annotations)

### User References

When referencing users in forum posts:

1. **Initial Reference**
   - Use site-specific user namespaces for usernames:
     - Cursor Forum: `[[CursorAI/Forum/User/Username]]`
     - Reddit: `[[Reddit/User/Username]]`
     - Stack Overflow: `[[StackOverflow/User/Username]]`
   - Only create `[[Person/Full Name]]` references when:
     - The person is known across multiple platforms
     - Their real identity is confirmed
     - They are a significant contributor or maintainer
     - They have a substantial online presence

2. **Person References**
   - Follow [[logseq-person.mdc]] for creating/updating person references
   - Only create new person pages for significant contributors
   - Update existing person pages if found
   - Include:
     - Basic bio information
     - Relevant links (GitHub, LinkedIn, etc.)
     - Image link if available
   - Add entry in today's journal linking to the new person

3. **Formatting**
   - Use appropriate namespace based on context
   - Include user references for:
     - Original poster
     - Respondents
     - Mentioned users

### Formatting Guidelines

1. **Quotes and Code**
   - Use `>` for quoted text
   - Use triple backticks (```) for code blocks
   - Preserve original formatting within quotes

2. **Links and References**
   - Use double brackets `[[]]` for internal references
   - Use regular markdown links `[]()` for external links
   - Include full URLs for external references

3. **User References**
   - Use site-specific namespaces for usernames
   - Use `[[Person/Full Name]]` only for confirmed identities
   - Include user links when available

### Example Structure

<CORRECT_✅>
~~~markdown
tags:: [[ForumName]], [[Topic]]
date-created:: [[2025/04/11]]
created-by:: [[CursorAI/Forum/User/johndoe]]

- # [Post Title - Forum Name](https://forum.example.com/post/123)
  - ## #[[Original Poster]]
    - [[CursorAI/Forum/User/janesmith]]
      - First point of the original post
      - Second point with a quote:
        - > This is a quoted section
      - Code example:
        ~~~
        def example():
            return "Hello"
        ~~~
  - ## #[[Response]]
    - [[Person/John Smith]]  # Known person with confirmed identity
      - > Response content here
    - [[CursorAI/Forum/User/bobjohnson]]  # Username only
      - > Another response
  - ## #[[Related/Post]]
    - [Related Post 1](https://forum.example.com/post/456)
    - [Related Post 2](https://forum.example.com/post/789)
  - ## #[[My Notes]]
    - Personal observations or annotations
~~~
</CORRECT_✅>

### Common Forums and Their Specific Requirements

1. **Cursor Forum**
   - Include category in title (e.g., "Discussion", "Feature Requests")
   - Use `[[CursorAI/Forum]]` tag
   - Include version numbers when relevant
   - Format usernames as `[[CursorAI/Forum/User/Username]]`

2. **Reddit**
   - Include subreddit in title (e.g., "r/learnpython")
   - Use `[[Reddit]]` tag
   - Include upvote count if significant
   - Format as `[[Reddit/SubredditName]]`
   - Format usernames as `[[Reddit/User/Username]]`

3. **Stack Overflow**
   - Include question ID in title
   - Use `[[StackOverflow]]` tag
   - Include answer scores
   - Format as `[[StackOverflow/User/Username]]`
   - Format usernames as `[[StackOverflow/User/Username]]`

4. **Other Forums**
   - Use appropriate forum-specific tags
   - Include relevant metadata
   - Follow the basic structure while adapting to forum-specific needs
   - Format usernames as `[[ForumName/User/Username]]`

### Best Practices

1. **Content Organization**
   - Keep related content together
   - Use proper indentation
   - Maintain clear hierarchy

2. **Cross-References**
   - Link to related pages in your knowledge base
   - Use appropriate namespaces
   - Avoid creating duplicate content

3. **Metadata**
   - Include all available metadata
   - Use consistent date formats
   - Tag appropriately

4. **Code and Technical Content**
   - Preserve code formatting
   - Include language specification in code blocks
   - Maintain original indentation

5. **Images and Media**
   - Include image links when available
   - Use proper markdown image syntax
   - Preserve image context

6. **User References**
   - Prefer site-specific namespaces for usernames
   - Only create person pages for significant contributors
   - Update existing person pages when found
   - Include relevant biographical information
   - Link to external profiles when available
