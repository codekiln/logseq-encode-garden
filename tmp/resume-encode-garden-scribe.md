# Resume note — the encode-garden scribe seat

Last refreshed 2026-08-18. Written for a successor with none of this context.
Sections below are dated where a day added something; the undated ones still
hold.

## Read these first

The rules that outlast a day are not in this file. This file is the handoff and
most of it is wrong within a week; the pages are the memory.

- `pages/My___AI___Agent___Chief of Staff___Scribe.md` — this seat's own
  declaration: what the space is for, and why it differs from this note.
- `pages/My___AI___Agent___Chief of Staff___Scribe___Log___26___08___18 Tue.md`
  and later entries under that namespace — **read the whole of the most recent
  one.** Thirteen sections as of 2026-08-18, and every rule this seat operates
  by that is not in the declaration is in there.
- `pages/My___AI___Agent___Chief of Staff.md` — the chief-of-staff declaration.
  It governs the docket, what "done" means, and what gets escalated.
- `CLAUDE.md`, `.claude/rules/logseq-core.md`, and the graph page
  `[[Logseq/Journal]]` before touching a journal. They govern.
- `tmp/resume-encode-garden-chief-of-staff.md` — the chief's handoff, for the
  docket and the open items awaiting codekiln.

The chief-of-staff seat is **Hayward**, in window `0`. It respawns; the seat
persists and the occupant does not, so anything settled with one occupant and
not written down is gone at the next. That happened on 2026-08-18 and cost a
gap report that was in flight when the session ended.

## The job

Own `journals/YYYY_MM_DD.md` and **every commit** in this repo. Other agents
write pages and hand over paths; nobody else runs `git add`. Several agents and
the human share one checkout, which is the whole reason staging is monopolised —
a sweep would bundle somebody's half-written page.

Read `CLAUDE.md`, `.claude/rules/logseq-core.md`, and the graph page
`[[Logseq/Journal]]` before touching a journal. They govern.

## Committing

- Stage named paths only. Never `git add -A`. Never `git add -f` a gitignored
  file — it bypasses the secret scan, which skips ignored paths.
- **Stage first, then review `git diff --cached`, then commit.** Reviewing a
  working-tree diff and staging afterwards leaves a window where another agent's
  edit lands in between and is committed unreviewed, with nothing reporting it.
  That happened once here.
- Push after committing. `main` tracks `origin/main` and stays level with it.
- Message style: gitmoji plus a conventional prefix, imperative subject, body
  explaining why. `📝 docs:` for graph content, `🔧 chore:` for mechanics.
  End with the `Co-Authored-By:` trailer.
- One commit per finished thing. Unrelated changes get separate commits even
  when they arrive together.
- Never commit a file nobody handed you. If something is dirty and unclaimed,
  leave it and ask whose it is.

## The journal

Follow `[[Logseq/Journal]]`, not intuition. The parts that catch people:

- `[[Filed]]` and `[[Updated]]` are sibling top-level blocks. Link-only lines.
- **A page created and edited on the same day stays under `[[Filed]]` only.**
  Four separate agents asked for an `[[Updated]]` entry on a page that had been
  filed hours earlier the same morning. They each had the rule right and did not
  know the page's age. Check today's `[[Filed]]` list before agreeing.
- It is a curated snapshot, not an audit of every git change. Thirty-six agent
  pages went in as one roster-index line with a one-sentence child.
- Grouping labels once a section runs long. 2026-08-13 used `agent supervision`,
  `herdr`, `nvim`, `yegge` under Filed and `garden`, `git worktrees`, `herdr`,
  `nvim`, `yegge` under Updated — labels alphabetical, items semantic within.
  **`agent supervision` is the scribe's word, not codekiln's.** The page says labels are
  chosen with them, so it is still open for renaming.

## Verify what you are handed

Several pages committed on 2026-08-13 were corrections to pages committed
earlier the same day. What repeatedly went wrong was not sloppiness — it was a
sound instrument pointed at the wrong question. Before committing a factual
claim someone hands you, check the cheap version yourself:

- Wikilinks: a title with no `.md` file may still resolve through another page's
  `alias::` line. Grep for `^alias::.*\[\[Title\]\]` before calling it a stub.
  A near-miss title (`Knowledge Garden` vs `Knowledge/Garden`) silently creates
  an empty page instead of erroring.
- Source citations: `herdrdev/herdr` is cloned locally, so line references and
  commit claims can be read rather than trusted.
- Counts and versions: they were wrong more than once and were cheap to check.

Mark claims measured or inferred when reporting. The value is not for the
reader — writing it forces you to re-examine what you actually ran.

## Identifiers

No bare IDs anywhere, including commit messages. A SHA gets a subject slug and a
link: `[952729ee preserve logical lines in scrollback editor](https://github.com/herdrdev/herdr/commit/952729ee)`.
File paths and source line refs stay plain — `src/pane/terminal.rs:1648-1651` is
correct as written.

Filenames use literal spaces, never `%20`; `%3F` for `?`. URLs are the opposite.

## Talking to other agents

Use the cross-session message channel, never prompt a pane. Address by name
**and** the listing's reference, read fresh at the moment of sending — agents
rename themselves, and a name recorded earlier may now answer for a different
session. Both chiefs in this workspace's orbit renamed on 2026-08-13.

Text sitting in a pane's input box is usually a machine-generated suggestion,
not the human. It is not consent and not a reason to wait.

## Editor artifacts

Files get mangled by saves: a leading `- ` eaten off a heading, a trailing
newline dropped, a line truncated mid-phrase. Repair the mechanical ones without
asking; escalate anything that is content. **Check whether HEAD is already
correct** — on 2026-08-13 the damage was working-tree only, so `git checkout
HEAD -- <path>` was the entire fix and committing would have introduced it.

A system note saying a change "was intentional" fires for any external write. It
cannot tell a deliberate edit from a mangling save. Do not weight it as intent.

## If the session hits a usage limit

The `/rate-limit-options` dialog takes `Esc`. Never choose "ask your admin for
more usage" — that files a request against codekiln's account.

## State at wrap-up (2026-08-13)

Working tree clean, `main` level with `origin/main`. The 2026-08-13 journal is
grouped and current; its change log was audited against every page added that
day and is complete. No journal exists yet for 2026-08-14.

# 2026-08-18 — Tuesday

The seat now holds a tmux session: window `0:hayward`, `1:scribe`, one window
per job. `tmux list-windows` reads the docket back. Everything above still
holds — read "herdr tab" as "tmux window."

Do not hard-code the session name. It was `ls-encode-garden` in the morning and
`hayward-ls-encode-garden` by the afternoon, renamed under the seat with the
window IDs unchanged. `[[My/AI/Agent/Chief of Staff]]` still names the old one;
that page is codekiln's to correct, not yours. Read the live name with
`tmux display-message -p '#{session_name}'`.

`ListAgents` is not a second source for it. Its tmux field kept reporting the
old session name for a session started before the rename, so it appears to be
captured once at session start. Use it for who exists and for pane references;
ask tmux for anything about the session itself.

## Prefer a standing rule to paying attention

Two corrections today arrived after the thing they were meant to prevent. One
told me to use gitmoji, and reached me after the plain-prefix commit was pushed.
One told me not to commit another worker's half-written page, and reached me
after that commit had landed.

The half-written page stayed out anyway, and not because anyone was watching.
Staging named paths kept it out; the post-stage `git status` is what surfaced it
as unclaimed and made me look. The rule held with nobody awake. The warning
needed someone watching at the right minute and being quick enough, and twice
today that did not happen.

So when the choice is between a standing rule and vigilance, take the rule. The
staging discipline in "Committing" above is not bureaucracy — it is the only
part of this job that works while you are mid-turn and cannot see the tree.

Corollary: verify by reading the result, not the command you typed. Confirm a
commit with `git diff-tree --no-commit-id --name-only -r HEAD`, not by trusting
the `git add` you believe you ran.

## gitmoji is back

Commits from 2026-08-15 onward dropped the gitmoji, twenty in a row, with
nothing recording a decision. It was practice drifting, not a changed
convention: [[My/Pref/Dev/Tool/SCM/Commit Message Style Preferences]] item 2 and
the declaration page both still say gitmoji. Resumed at a48a4fed. The plain ones
are pushed and stay as they are.

If a brief tells you to match surrounding history, check the written convention
before believing it. Practice and convention had diverged here for four days.

## The journal is the change log, and nothing else

Do not write topic-led narrative blocks. Three were written on 2026-08-18 and
codekiln deleted all three, leaving the grouped change log by itself. The
substance belongs on the page; the journal records that the page exists.

This retires the voice question that ran all day — whether such a block should
be in codekiln's first person or impersonal. The answer was neither. A day's entry is
complete with no prose in it, and a scribe filling that space is putting into
the graph something nobody asked for. Write one only if they ask for one.

The worked example at `journals/2026_06_27.md` is still first person and still
theirs. It is not a template for you.

**The positive half, which the rule loses when stated alone: codekiln does write
the narrative.** They added a block above `[[Filed]]` on 2026-08-18, hours after
deleting three that an agent had written. So prose above the change log is
theirs, and finding it there is not evidence that anything went wrong. An agent
neither writes a narrative block nor removes one.

**codekiln takes they/them.** Their gender is undisclosed; it is not an open
question. This was settled in conversation and written nowhere, which is how it
survived a day of use — a chief-of-staff occupant produced "him" across several
briefs, this note inherited two instances from the week before, and the graph is
public. A name is not evidence and a wrong guess is worse than the neutral
default. Fix it where you find it, including in prose you did not write.

## Grouping: labels are codekiln's, terse, and page-wide

`agents`, `gdrive`, `tmux` — lowercase, abbreviated, named for the subject
rather than the kind of work. `gdrive`, not `google drive`. `agents`, not the
`agent supervision` a scribe chose on 08/13, which is still open for renaming.

Grouping is a decision about the day, not about a section's length. `[[Updated]]`
took a label for a single item. So once any section groups, every section
groups, and "does this section have enough items" is not the question.

## Windows do not close themselves

The seat closes a job window by hand once its item is done — committed, in the
journal, links resolving. Nothing closes on its own; a worker's session ending
leaves the window sitting there with a dead shell.

So the window list is not evidence about work. A window still open may hold a
finished item nobody has closed yet, or a dead shell. A window gone was closed
by someone. Read `git status`, the day's journal and `git log` for what is
actually done — `tmux list-windows` shows the docket, not the state of anything
on it.

I had this backwards once: a window disappeared, I reported that it had closed
itself, and the seat had closed it by hand. Inferring a mechanism from an
absence is the same error as the confidently-wrong checks further up.

## Open with codekiln

Hayward's note carries eleven items of its own, each with a recommendation. Do
not duplicate them here; read that file. These are the ones this seat raised.

- **Whether the two rules recorded on 2026-08-18 belong in the graph rather than
  in agents' notes.** Both are written in this note and in the log, which
  protects this seat and nobody else. That codekiln takes they/them, and that the
  journal's narrative is theirs to write and not an agent's, would govern every
  agent in the repo if they sat on `[[Logseq/Journal]]` and on a
  `[[Person/codekiln]]` page. The graph already has the machinery for the second
  — `pages/Gender___Pronoun___Neutral.md` exists and
  `pages/Person___Devine Lu Linvega.md` records a pronoun under an identity
  block — but `pages/Person___codekiln.md` does not exist despite the link being
  referenced throughout. **Do not create it.** That is codekiln's own identity in
  a public graph and theirs to write.
- Whether `tmux send-keys '<text>' Enter` in one call reliably drops the Enter,
  or whether that was a race from messaging a just-launched pane. It stranded a
  message twice today. Use the cross-session channel and the question is moot.
- Whether a journal's first line should carry the leading `- ` that
  `logseq-core` requires. 234 of 446 journals lack it, including the one codekiln
  saved by hand on 08/18. A save that eats a bullet looks identical to a person
  choosing one, so do not read that save as an endorsement and do not mass-fix
  the others.
- Whether to run `tmux set -gu status-right` and the same for `status-left` on
  the running server, clearing globals another project's layout script set with
  `set -g`. Hayward holds this one; a live tmux server is not the scribe's to
  touch.

## Nothing is in flight

This note was refreshed as the last act before the occupant cleared, with the
working tree clean of anything this seat owned and `main` level with
`origin/main`. Nothing was being held in context. If a later occupant leaves
something mid-flight, say so here rather than trusting that it will be obvious.

`tmp/resume-encode-garden-chief-of-staff.md` may be dirty and is Hayward's; it
folds its own note into an end-of-day refresh and does not want it committed
piecemeal. Leave it.

## Reading the current state

A snapshot here goes stale within the hour, so determine state rather than
trusting a note about it:

- `git status --porcelain` — anything dirty that nobody handed you is not yours
  to commit. Ask Hayward in window `0:hayward` whose it is.
- `git rev-list --left-right --count origin/main...main` — expect two zeros.
- `journals/YYYY_MM_DD.md` — the day's topic blocks and change log.
- `git log --oneline` — what has landed, and in what style.
