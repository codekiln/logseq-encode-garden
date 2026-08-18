# Resume note — Hayward, the encode-garden chief-of-staff seat

Last refreshed 2026-08-18. Written for a successor with none of this context.

## Read these first

- `pages/My___AI___Agent___Chief of Staff.md` — this repository's declaration of
  what a chief of staff is *here*: the docket, what "done" means, which subagent
  shapes this repo uses, the commit policy and why, and what gets settled versus
  escalated. **It governs.** Read it before operating.
- `pages/My___AI___Agent___Chief of Staff___Log___26___08___13 Thu.md` and the
  later log pages under that namespace — what days in the seat actually taught.
- `pages/My___AI___Agent___Chief of Staff___Scribe.md` — the scribe's declaration
  and its own memory space, with a date-namespaced log beneath it. Read the
  scribe's recent log entries; several of today's settled rules live there rather
  than here.
- `CLAUDE.md`, `.claude/rules/logseq-core.md`, and the graph page
  `[[Logseq/Journal]]` before touching a journal. They govern.

## Where the seat runs

A tmux session, window `0` is `hayward`, with the standing scribe beside it and
one window per job.

**Do not hard-code the session name.** It was `ls-encode-garden` and became
`hayward-ls-encode-garden` mid-day on 2026-08-18, under a `<seat>-<repo>` sweep
that also renamed peer sessions. Read the live name from `tmux list-sessions`.

`ListAgents` is not a second source for it. Its tmux field still reported the old
name after the rename — it is captured at session start, not read live. Reliable
for who exists and for pane references; unreliable for anything about the session
itself.

## Standing arrangement

The **scribe** owns `journals/YYYY_MM_DD.md` and **every commit**. Other agents
write pages and hand over paths; nobody else runs `git add`. Several agents and
the human share one checkout, which is the whole reason staging is monopolised.

Agent-to-agent traffic goes over the **cross-session message channel**, not
`tmux send-keys`. A lone `send-keys '<text>' Enter` call delivers the text and
strands it unsent in the recipient's input box when they are mid-turn. The
command succeeds either way, so nothing reports the failure, and it looks
identical to an agent ignoring you. It happened twice on 2026-08-18 and both
times made a correction arrive too late to matter.

**A handoff is complete when the file is committed**, readable from `git log`
without being told. An acknowledgement is a courtesy. Waiting on one makes
completion depend on both parties still existing — a worker was closed mid
handshake on 2026-08-18 and its acknowledgement was refused.

**Job windows are closed by the seat, by hand.** Nothing self-closes. A window
list is the docket; a window left open past its commit reports work in flight
that is not.

## Settled on 2026-08-18 — do not relitigate

- **The journal carries the change log and no agent-written narrative.** codekiln
  deleted all three topic-led blocks from that day's journal themselves. Do not
  write them.
- **Grouping labels are terse and subject-named**, chosen by codekiln: `agents`,
  `gdrive`, `tmux`, `claude code`. Spaces, not hyphens — spaces are attested in
  this graph, hyphens are not. Grouping is a page-wide decision, not a
  per-section count: a section with one item still gets its label.
- **Headings name the finding; they do not allude to it.** codekiln's objection
  was that allusive titles are obscure. This is their standing plain-writing
  preference reaching a place it had not been applied, so expect it to apply to
  page prose too, not only titles.
- **Commit messages carry a gitmoji** — `📝 docs:` for page and journal work.
  The convention is stated on `[[My/Pref/Dev/Tool/SCM/Commit Message Style Preferences]]`
  and on the declaration; twenty commits had drifted away from it without any
  decision being recorded.
- **The `Co-Authored-By` trailer follows whoever wrote the content.** It is a
  structured field that forges read and display, not a courtesy, so it stays off
  commits carrying codekiln's own words. `attribution.commit` in `settings.json`
  is where it is configured. Do not tidy the exception into consistency.

## Open items — all awaiting codekiln, none actionable unasked

1. **Two repair sweeps, best run as one pass** since the page sets overlap.
   `docs.claude.com` is now entirely a redirect host and splits two ways: Claude
   Code slugs go to `code.claude.com/docs/en/<slug>`, everything else to
   `platform.claude.com/docs/en/<path>`. 14 pages, 16 occurrences, 15 unique
   URLs. A naive host replacement breaks the three that went to `platform`.
   Separately, `claude config <sub>` appears in 5 pages and **no longer exists**
   in the CLI — worse than a redirect, which still works.
2. **The declaration page names the wrong tmux session** since the rename.
   Recommendation: describe the naming pattern rather than the literal name, so
   it survives the next one.
3. **Two repairs to `[[Logseq/Journal/Section/Friction]]`**: it instructs filing
   under **garddiff**, a mechanism with no journal appearance since 2026-05-12;
   and `[[Logseq/Journal]]` calls it a *recurring* section when it has appeared
   twice ever, last five months ago.
4. **The Filed/Updated line form.** Five variants across the graph, no page
   states which. Recommendation: `- # [[Filed]]` — the plurality, and the only
   common form satisfying `logseq-core`'s bullet rule. **Nobody should touch the
   234-of-446 journals whose first line lacks a bullet** until codekiln says what
   caused it; a save that eats a bullet is indistinguishable from a person
   choosing one.
5. **Whether the send-keys failure earns a `.rulesync/` rule.** It has now
   happened twice, which was the bar. Argument against: almost no agent here
   messages another, so the rule costs every reader to serve two.
6. **Which page owns the settings precedence list** — `[[Claude/Code/Settings]]`
   and `[[Claude/Code/Settings/Override]]` now both carry it, both correct, and
   they will drift.
7. **Aliases**, suggested and unwritten since aliases are human-curated:
   `[[Google/Workspace/AI]]` (recommended), a relative-path phrasing for the
   Google Drive Markdown question, `[[Claude/Google Drive]]` (would skip).
8. **A dead hook.** `.rulesync/hooks.json` declares a `PostToolUse` formatter
   pointing at `.rulesync/hooks/format.sh`, which does not exist, and `hooks` is
   not in `rulesync.jsonc`'s `features`, so it would not generate anyway. Inert
   since [f18285e2 a bunch of rulesync skill updates](https://github.com/codekiln/logseq-encode-garden/commit/f18285e2).
9. **Whether a current tools page is worth having.** The stale tools table was
   dropped from the settings page; a current list would be useful, but as its own
   page rather than smuggled back in.
10. **`Logseq/Entity/Agent`** — still held from 2026-08-13. Creating the type
    sets a convention and 35 `Person/Steve Yegge/Agent/*` pages would become its
    instances.

## What produces no error here

The graph has no build and no test suite, so the work left undone is the work
nothing complains about. The declaration page's *What produces no error in a
graph* section is the standing list. Today added two more:

**An instrument can be right when captured and wrong when read.** `ListAgents`'
session field, correct at capture and silently aging. Work out *when* a field's
value was determined before trusting it.

**A file's silence is evidence of nothing.** An unset key and an unsupported key
are indistinguishable from a `settings.json` alone. Likewise a truncated fetch
and a genuine omission: two fetches of a published table came back truncated on
2026-08-18, and the right report was "could not confirm from the rendered page,"
not "the doc omits these."

**A standing mechanism beats a watching supervisor.** Twice today a correction of
mine arrived after the thing it was meant to prevent. What actually kept a
half-finished page out of a commit was the scribe's rule to stage named paths —
a rule that holds without anyone being awake.
