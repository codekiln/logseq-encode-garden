---
name: logseq-forum-post
description: >-
  Import and structure a forum post (Cursor Forum, Reddit, Stack Overflow, or
  other forums) into a Logseq page with title link, metadata, Original Poster /
  Response / Related / My Notes sections, and site-specific user namespaces. Use
  when the user pastes a forum thread or asks to capture/import a forum
  discussion. For person hubs use the logseq-person command and logseq-entity
  skill. Do not use for blog posts/articles (logseq-import-blog) or non-forum
  content.
metadata:
  short-description: Import forum threads into structured Logseq pages
---
# Logseq forum post import

Capture a forum thread as a hierarchical Logseq page.

## Quick path

1. Title block: `- # [Post Title - Forum Name](original-url)` (include category/subreddit/question-id as relevant).
2. Metadata: `date-created:: [[YYYY-MM-DD Ddd]]` (journal page-title format), `created-by::` (person hub for confirmed identities, else `[[ForumName/User/Username]]`).
3. Sections: `## [[Original Poster]]`, `## [[Response]]`, `## [[Related/Post]]`, `## [[My Notes]]`.
4. Apply `logseq-core` LFM rules; use `logseq-link-hygiene` before adding `[[...]]`.

## Critical

- `tags::` is protected per `logseq-core`. Add topical tags only where the format calls for them.
- Use site-specific user namespaces (`[[CursorAI/Forum/User/...]]`, `[[Reddit/User/...]]`, `[[StackOverflow/User/...]]`); only create `[[Person/Full Name]]` for confirmed cross-platform identities — route those through the logseq-person command + logseq-entity skill.

## Reference

- [references/forum-post-format.md](./references/forum-post-format.md) — full required sections, per-forum requirements (Cursor/Reddit/Stack Overflow/other), user-reference rules, quoting/code conventions, and a complete worked example.
