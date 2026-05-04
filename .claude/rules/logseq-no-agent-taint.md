---
paths:
  - journals/*.md
  - pages/*.md
---
# No Agent Taint in Logseq Pages

When editing Logseq graph content, do not copy user instructions, AI coding agent rationale, task constraints, implementation notes, or process commentary into the page unless the user explicitly asks to record them as knowledge-garden content.

Before writing any prose block, ask: would this sentence still belong on the page if a human had written it later in Logseq, without the surrounding AI task context?

## Keep out of graph pages

- Explanations of why the AI coding agent chose an approach.
- Mentions of the user's request, prompt, or instructions as the reason content exists.
- Caveats about what the agent did or did not do.
- Status notes about importing, creating, updating, preserving, checking, or verifying content.
- Meta-commentary about the source changing, the agent avoiding a snapshot, or the edit being intentionally lightweight.

## Put in the final response instead

Operational caveats belong in the chat response, not in Logseq pages. Examples:

- "I did not snapshot the roadmap."
- "I used an iframe."
- "I preserved existing tags."
- "I could not run the link checker."

## Examples

Bad page content:

~~~markdown
- This page intentionally points at the changing source rather than snapshotting roadmap content.
- Added because the user asked an AI coding agent to import this without reading it.
- Keeping this lightweight because the source changes daily.
~~~

Better page content:

~~~markdown
- # [Logseq Public Roadmap](https://example.com/roadmap)
~~~

## Review checklist

Before finishing a graph edit, scan added lines for high-risk signs of agent-tainted prose:

- "intentionally"
- "because the user asked"
- "I"
- "we"
- "this edit"
- "snapshot"
- "agent"
- "instruction"
- "request"

These phrases are not always wrong, but they require a second look. If the line explains the editing process instead of the page subject, remove it from the graph and mention it only in the final response.
