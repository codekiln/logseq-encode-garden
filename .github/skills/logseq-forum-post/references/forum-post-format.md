# Formatting Forum Posts in Logseq

Standard format for importing and structuring forum posts in Logseq (Cursor, Reddit, Stack Overflow, and other forums). For person hubs, use the logseq-person router and `[[Logseq/Entity/person]]` (logseq-entity skill).

### ⚠️ CRITICAL: DO NOT MODIFY FRONTMATTER TAGS ⚠️

- **NEVER** modify, add, or remove the `tags::` frontmatter item specifically.
- The `tags::` frontmatter is strictly protected. Even if a tag seems missing or incorrect, DO NOT change it.
- This restriction applies ONLY to the `tags::` frontmatter item, not to other page attributes.

### Basic Structure

- Forum posts should be structured hierarchically using Logseq's bullet-point system.
- Each post starts with a title that links to the original post.
- Use TAB indentation; all content prefixed with `-`.

### Required Sections

1. **Title and Link** — `- # [Post Title - Forum Name](original-url)` (include the forum name; include category for clarity).
   - Example: `- # [How can I increase the indexing depth for @docs? - Discussion - Cursor - Community Forum](https://forum.cursor.com/t/how-can-i-increase-the-indexing-depth-for-docs/77949)`
2. **Metadata**
   - `date-created:: [[YYYY/MM/DD]]` if available.
   - Author: `created-by:: [[Person/Full Name]]` for known persons, else `created-by:: [[ForumName/User/Username]]`.
   - Tags: `tags:: [[ForumName]], [[Topic]]` (only when authoring a brand-new page; never edit existing tags).
3. **Content Sections**
   - Original Poster: `- ## #[[Original Poster]]` (person hub or `[[ForumName/User/Username]]`).
   - Responses: `- ## #[[Response]]`.
   - Related Topics: `- ## #[[Related/Post]]`.
   - My Notes: `- ## #[[My Notes]]`.

### User References

1. **Initial Reference** — use site-specific user namespaces:
   - Cursor Forum: `[[CursorAI/Forum/User/Username]]`
   - Reddit: `[[Reddit/User/Username]]`
   - Stack Overflow: `[[StackOverflow/User/Username]]`
   - Only create `[[Person/Full Name]]` when: the person is known across platforms, identity confirmed, significant contributor/maintainer, or substantial online presence.
2. **Person References** — follow `[[Logseq/Entity/person]]` and the logseq-person router; only create new person pages for significant contributors; update existing person pages if found; include bio, links (GitHub/LinkedIn), image if available; add a journal entry linking the new person.
3. **Formatting** — use the appropriate namespace; include user references for original poster, respondents, and mentioned users.

### Formatting Guidelines

1. **Quotes and Code** — use `>` for quoted text; triple backticks for code blocks; preserve original formatting within quotes.
2. **Links and References** — `[[]]` for internal references; markdown links `[]()` for external; include full URLs.
3. **User References** — site-specific namespaces for usernames; `[[Person/Full Name]]` only for confirmed identities.

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

1. **Cursor Forum** — include category in title (e.g., "Discussion", "Feature Requests"); use `[[CursorAI/Forum]]` tag; include version numbers when relevant; usernames as `[[CursorAI/Forum/User/Username]]`.
2. **Reddit** — include subreddit in title (e.g., "r/learnpython"); use `[[Reddit]]` tag; include upvote count if significant; format as `[[Reddit/SubredditName]]`; usernames as `[[Reddit/User/Username]]`.
3. **Stack Overflow** — include question ID in title; use `[[StackOverflow]]` tag; include answer scores; usernames as `[[StackOverflow/User/Username]]`.
4. **Other Forums** — use appropriate forum-specific tags; include relevant metadata; follow the basic structure; usernames as `[[ForumName/User/Username]]`.

### Best Practices

1. **Content Organization** — keep related content together; proper indentation; clear hierarchy.
2. **Cross-References** — link to related pages; use appropriate namespaces; avoid duplicate content.
3. **Metadata** — include all available metadata; consistent date formats; tag appropriately.
4. **Code and Technical Content** — preserve code formatting; include language spec in code blocks; maintain original indentation.
5. **Images and Media** — include image links when available; proper markdown image syntax; preserve image context.
6. **User References** — prefer site-specific namespaces; only create person pages for significant contributors; update existing person pages; include biographical info; link external profiles.
