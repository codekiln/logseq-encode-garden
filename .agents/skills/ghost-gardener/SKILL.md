---
name: ghost-gardener
description: >-
  Work the Ghost Gardener requests in today's journal. Collects the TODO blocks
  under the day's Ghost Gardener heading, shows the queue for one go-ahead, then
  carries each request out — marking it DOING while it runs, DONE when it lands
  — and records the pages touched under [[Filed]] / [[Updated]]. Use when the
  user says "ghost gardener", "do today's garden requests", "work my journal
  TODOs", or hands over a block ref pointing into a Ghost Gardener section of
  journals/YYYY_MM_DD.md.
metadata:
  short-description: Work today's Ghost Gardener journal requests
---
# Ghost Gardener

Today's journal is the work queue. [[Person/codekiln]] writes requests there during the day; this skill runs them.

## Scope

`journals/YYYY_MM_DD.md` for today, and only the blocks under a top-level heading naming the Ghost Gardener (`- # [[Ghost Gardener]], please`, `- # [[Ghost Gardener]] requests`). Earlier days are worked only when the user names the date. Everything else in the journal belongs to [[Person/codekiln]] — leave it alone.

## Workflow

1. **Collect.** Read today's journal. Under the Ghost Gardener heading, gather every block whose first token is `TODO` or `DOING`, in document order. A TODO nested under another TODO is a subtask: it finishes as part of its parent.
2. **Show the queue.** List the requests in a numbered list, each as one short line, and say which ones look ambiguous. Ask for a single go-ahead. Wait for it.
3. **Run each request.** For one request at a time:
   - Flip its marker to `DOING` and save the journal, so an interrupted session shows where it stopped.
   - Do the work, routing to the skill that owns it (see below).
   - Flip the marker to `DONE`.
4. **Write the change log.** Add the pages created and edited to `- # [[Filed]]` / `- # [[Updated]]` in today's journal, following [[Logseq/Journal]] — link-only lines, alphabetized group labels, a page under one section per day.
5. **Report.** In chat, say what landed and what stalled. Anything you could not finish stays at `DOING`.

## Routing

| The request asks for | Load |
|---|---|
| An entity page, entity type, or dedup question | `logseq-entity` |
| A `/Q/` question page | `logseq-question` |
| A term page | `logseq-term` command |
| A person hub | `logseq-person` command |
| A blog post, article, or essay import | `logseq-import-blog` command |
| Something from Readwise or Reader | `readwise-cli` |
| A YouTube video's notes | `logseq-youtube-notes` |
| A flashcard or Keyshort card | `logseq-flashcard` |
| A new skill or command under `.rulesync/` | `rulesync-create-skill`, then `rulesync generate` |
| Staging and committing the result | `git-conventions` |

A request naming a page that does not exist yet: check with `grep -r "Namespace/Page" pages/ journals/` before deciding it is missing.

## Requests that need a branch

A request may ask for a worker, a worktree and a pull request. Carry it through to an open PR.

- **In this garden**, the worktree goes under `.worktree`, following [[My/Pref/Dev/Tool/git/Worktree]].
- **In another repository** — dotfiles, herdr, rulesync, anything else — resolve it with `ghq list --full-path --exact <host/owner/repo>` and verify the checkout per [[My/AI/Rule/Work in ghq repos]] before writing anything. Ask before cloning a repository that is not already local.
- Branch and worktree names carry the ticket or the request they serve, per [[My/AI/Rule/Dev Workflow with Git and Tmux]].
- When the PR is open, put its link into the request block in place of any `TBD link to pr` placeholder, shaped by [[My/AI/Rule/How to Communicate Effectively With Me/A pointer carries a link, an id with a slug, and a reason]], then mark the request `DONE`.

## Editing the journal safely

Marker edits change one word on one line. [references/editing.md](./references/editing.md) has the mechanics — tab depth, `id::` lines, multi-line blocks, and what never gets rewritten. Read it before the first marker flip of a session.
