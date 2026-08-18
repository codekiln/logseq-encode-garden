# Resume note — encode-garden scribe, 2026-08-13

Written for a successor with none of this context.

## Resume this session

```
claude --resume encode-garden-scribe
```

herdr workspace `w2` (label `encode-garden`), tab `scribe`. The chief-of-staff
seat in this workspace is **Hayward** (`encode-garden-hayward`), renamed from
`encode-garden-chief-of-staff` at wrap-up. Its own note is
`tmp/resume-encode-garden-chief-of-staff.md` — read that one first for the
docket and the open items.

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
  **`agent supervision` is the scribe's word, not his.** The page says labels are
  chosen with him, so it is still open for renaming.

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

The seat now holds a tmux session, `ls-encode-garden`: window `0:hayward`,
`1:scribe`, one window per job. `tmux list-windows` reads the docket back.
Everything above still holds — read "herdr tab" as "tmux window."

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

## Topic blocks: write them, do not stub them

The worked example in `journals/2026_06_27.md` is in codekiln's own first
person. You are not codekiln — do not invent their experience. Write the block
impersonally and completely instead.

Do not leave a placeholder for them to fill. The change log is meant to answer
what the day found at any hour, and a stub answers nothing; a real block can be
rewritten into their voice, an empty one cannot without redoing the work.
Whether these should be first person at all is with codekiln as of today.

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

- Whether journal topic blocks should be first person, per above.
- Whether `tmux send-keys '<text>' Enter` in one call reliably drops the Enter,
  or whether that was a race from messaging a just-launched pane. It stranded a
  message twice today. Use the cross-session channel and the question is moot.
- Whether `[[Filed]]` takes `google drive` and `tmux` as labels once it runs
  past a handful. Labels are chosen with them, not by the scribe — the
  `agent supervision` label from 08/13 is still open because a scribe picked it.
- Whether to run `tmux set -gu status-right` and the same for `status-left` on
  the running server, clearing globals another project's layout script set with
  `set -g`. Hayward holds this one; a live tmux server is not the scribe's to
  touch.

## Reading the current state

A snapshot here goes stale within the hour, so determine state rather than
trusting a note about it:

- `git status --porcelain` — anything dirty that nobody handed you is not yours
  to commit. Ask Hayward in window `0:hayward` whose it is.
- `git rev-list --left-right --count origin/main...main` — expect two zeros.
- `journals/YYYY_MM_DD.md` — the day's topic blocks and change log.
- `git log --oneline` — what has landed, and in what style.
