# Brief — `seat-improvement`

Hired by Hayward, the manager seat for `logseq-encode-garden`, in tmux session
`hayward-LEG-2026-08-26-wed-0930` on 2026-08-26. Written after scouting the evidence base, so the
measurements below are handed over rather than left for you to rediscover. Reproduce any of them
you intend to rely on; a fact inherited from a brief is still a guess until you measure it.

## The job

Find **one small thing to improve about the Hayward seat's ability to contribute**, based on how
this seat actually behaved yesterday, 2026-08-25. codekiln asked every seat for exactly one, and
Hayward is held to it all day, so deliver one — not a list, not a ranked shortlist.

**What counts.** A change to how this seat works: what it reads at wake, how it takes an
instruction, how it checks itself, what it hands a successor, where a rule lives so the agent who
needs it actually hits it.

**What does not count**, and each of these has been offered before and rejected:

- A repository backlog item — a page to fix, a link to repair, a sweep to run.
- A finding about the graph's content.
- A display item wearing a new hat: "put X on the Heads Up Display" is not an improvement to the
  seat, it is an item.
- Anything large. If it takes a project to adopt, it is the wrong size.

## The evidence base has two halves, and the second is the one that gets skipped

### Half one — the tracked documents

- `tmp/resume-encode-garden-chief-of-staff.md` — the seat's handoff. Note that commit `297a6e95`
  at 07:03 today re-added a section titled *Open items* that had been removed at `1334ec1d` on
  2026-08-24; the section itself dates from `2576dfe0` on 2026-08-18.
- `pages/My___AI___Agent___Chief of Staff.md` — what this seat is.
- `pages/My___AI___Agent___Chief of Staff___LEG Todos Heads Up Display.md` and its `___Detail.md`
  and `___Parked.md` siblings.
- `git log` since 2026-08-24 in this repository.

### Half two — the transcripts, which is where conduct is visible rather than self-report

Yesterday's Hayward seat ran three context windows. Their transcripts, located by matching the
`agentName` field the way `~/ghq/github.com/codekiln/dotfiles/tmp/fleet-2026-08-24/bin/ctx-check`
does. They all sit in one directory under `~/.claude/projects/`, the one whose name is this
repository's absolute path with every `/` rewritten as `-`; derive it rather than typing it:

~~~sh
D=~/.claude/projects/$(git -C ~/ghq/github.com/codekiln/logseq-encode-garden rev-parse --show-toplevel | tr / -)
~~~

- `hayward-LEG-2026-08-25-tue-0709` → `3f382e00-21bb-4b86-a26e-9edc3245cd40.jsonl`
- `hayward-LEG-2026-08-25-tue-1015` → `c4ee3c8e-a837-4a95-bd69-674f80c9f141.jsonl`
- `hayward-LEG-2026-08-25-tue-1510` → `0adf8053-5e8b-4fdf-9d70-140cdbd1d005.jsonl`

Monday's two are `hayward-LEG-2026-08-24-mon-1155` and `hayward-LEG-2026-08-24-mon-1218`, and the
six `encode-garden *` and `encode-garden-*` names in the same directory are contractors this seat
and its predecessors hired.

**These are 1.5MB to 2.6MB each. Do not read one whole.** Query them.

### The instrument, measured this morning rather than guessed

Each line is JSON. A line with `type` of `user` and a string `message.content` carries an inbound
message, and its `origin.kind` field separates where the message came from:

- `human` — arrived through the composer.
- `peer` — a cross-session message from another agent, wrapped in a `<cross-session-message>` tag
  naming the sender.
- `auto-continuation` and absent — harness-generated.

Counted across yesterday's three windows: **15 inbound messages arrived through the composer and
35 arrived as peer relays.** In the last window it was 1 against 10.

**One caveat that is yours to settle rather than mine to assert.** `origin.kind` of `human` means
the text arrived through the composer. It does not by itself establish that a person typed it —
another agent driving `send-keys` reaches the same field. If your finding turns on the difference,
establish it, and say how.

## Constraints

- **Do not push.** Commit your work; the push decision is Hayward's and it is not delegated.
- **Never `git add journals/2026_08_25.md`.** codekiln prunes change-log entries from their own
  working copy continuously, and staging that file resurrects lines they deleted on purpose. The
  same goes for any other file `git status` shows as modified that you did not modify: read
  `git diff --cached` before every commit and commit only your own lines.
- **`git grep -E` gives `\b` no meaning here** and reports no matches rather than erroring, which
  reads exactly like a genuine negative. Use `git grep -P '\bword\b'` in single quotes, and run a
  positive control before trusting a negative result.
- **`git ls-files <path>` settles whether a path is tracked.** `git check-ignore` answers a
  different question and an ignore rule on a tracked file is overruled by the index.
- **codekiln takes they/them**, and so does every other person these documents name. None has
  disclosed pronouns and a name is not evidence.
- **This repository's `tmp/` is tracked and published**, so your report is public. Write it knowing
  that, and keep other people's identifying details out of it.
- **Do not hire anyone.** Do the work yourself.

## Deliverable

1. **The improvement, in one or two sentences**, plus one more saying what changes about how the
   seat works. That is what Hayward reports upward, so write it to be quoted.
2. **The change itself, if it is a document change** — a page, the seat's charter, the handoff.
   Make it, small.
3. **A report at `tmp/report-seat-improvement.md`**, committed. For every claim it makes, say
   **how you established it** — the command, the file, the line — rather than only what you found.
   The check that caught the last contractor's inherited error was asking how, not what.
4. **Say what you considered and rejected**, briefly. Hayward needs to know the one was chosen
   rather than merely found first.

Then stop and report in this pane. Hayward reads the pane and takes delivery before the window is
closed.
