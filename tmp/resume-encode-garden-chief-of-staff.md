# Resume note — Hayward, the encode-garden chief-of-staff seat

Last refreshed 2026-08-24. Written for a successor with none of this context.

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

A tmux session of its own, one window per job. As of 2026-08-24 the session is
named `<seat>-<date>` — `hayward-2026-08-24` — so the seat name sits at session
level rather than on window `0`. The fleet-wide shape is on the graph page
`[[My/AI/Agent/Fleet]]`; the seat's own declaration carries it too.

**Do not hard-code the session name.** It was `ls-encode-garden`, became
`hayward-ls-encode-garden` mid-day on 2026-08-18 under a `<seat>-<repo>` sweep,
became `<seat>-<date>` on 2026-08-24, and gained a repo suffix the same afternoon:
**`hayward-2026-08-24-LEG`**. `LEG` is logseq-encode-garden, `MK` the work
knowledge vault, `GL` the langserve repo, `DF` dotfiles — the suffix exists so the
`C-b w` tree says which repository a seat is in.

**The dotfiles suffix is `DF`, not `.F`.** `.F` was published first, from codekiln's
own example, and is wrong: a dot in a session name makes tmux read everything after
it as a pane specification, so every *bare* session target fails. Verified here on
an isolated socket (`tmux -L dottest`, never the default one — `kill-server` on the
default socket would take every seat's session down):

```
tmux -L dottest new-session -d -s 'hay-.F'
tmux -L dottest has-session  -t '=hay-.F'   # can't find pane: F   exit 1
tmux -L dottest list-windows -t '=hay-.F'   # can't find pane: F
tmux -L dottest new-window   -t '=hay-.F'   # can't specify pane here
tmux -L dottest has-session  -t '=hay-.F:'  # exit 0 — trailing colon disambiguates
tmux -L dottest list-panes   -t '=hay-.F:0' # exit 0 — explicit window also works
tmux -L dottest has-session  -t '=hay-DF'   # exit 0 — control, clean
```

`has-session` exiting 1 is the worst of it: a script cannot even test whether the
session exists, and the failure reads as a missing session rather than a bad name.
A convention that works only if you remember a trailing colon is a trap. Four schemes in seven days, two of
them on one day. The claude session name is untouched by these renames, so peer
addressing is unaffected. Read the live name with
`tmux display-message -p '#{session_name}'`, which names the session the running
pane is in. `tmux list-sessions` lists every session on the server, including
other seats' — it answers a different question.

`ListAgents` is not a second source for it. Its tmux field still reported the old
name after the rename — it is captured at session start, not read live. Reliable
for who exists and for pane references; unreliable for anything about the session
itself.

## The Heads Up Display pane — re-establish it after every respawn

The seat keeps `pages/My___AI___Agent___Chief of Staff___LEG Todos Heads Up Display.md`
open in an nvim pane to the right of the chat pane, both panes titled `Hayward chat`
and `Hayward HUD`. codekiln has asked for this twice, because **a respawned pane
inherits no split** — `bed-down` replaces the pane, and the layout does not come
back with it. Treat it as a waking-up step and do it before reporting in:

```sh
S=$(tmux display-message -p '#{session_name}')
tmux split-window -h -p 45 -t "$TMUX_PANE" -c "$PWD" \
  'nvim "pages/My___AI___Agent___Chief of Staff___LEG Todos Heads Up Display.md"'
tmux select-pane -t "$TMUX_PANE" -T 'Hayward chat'
tmux select-pane -t "$S:0.1" -T 'Hayward HUD'
```

If a right pane already exists and runs nvim, retitle it and `:edit` the page into
it rather than splitting again — splitting blind gives three panes.

The page is not a journal and not a record of how the seat works. It answers two
questions for codekiln at a glance: what in this repository is waiting on him, and
what state the repository is in. The **Last swept** line is a promise — a sweep
that leaves it unchanged did not happen. Items earn a place only if his answer
changes something; anything the seat can settle, it settles and records under
*Decided here, not asked*.

## Standing arrangement

The **scribe** owns `journals/YYYY_MM_DD.md` and **every commit**. Other agents
write pages and hand over paths; nobody else runs `git add`. Several agents and
the human share one checkout, which is the whole reason staging is monopolised.

**On 2026-08-24 no scribe ran for this graph**, and the seat's brief made the
seat responsible for the journal and the commits. That is the exception, not a
change to the arrangement. The checkout was still shared: a peer seat working the
dotfiles tmux spec committed `aef93c23` into it mid-task, and the seat's own next
commit landed on top of theirs. Staging named paths is what kept the two apart —
the rule held with nobody awake to enforce it, which is the point of it.

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
  write them. **This was violated on 2026-08-24** — the seat wrote five editorial
  blocks into that day's journal, following the graph page `[[Logseq/Journal]]`,
  which still instructs them. Caught by reading this note and removed before the
  day closed. The graph page and `[[Logseq/Journal/Editorial headings]]` both
  still teach the deleted practice; see open items.
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
2. ~~The declaration page names the wrong tmux session.~~ **Closed 2026-08-24.**
   The declaration now describes the `<seat>-<date>` pattern and says the seat
   name moved up from window `0`, rather than naming a literal that has now
   changed three times in a week.
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

11. **`[[Logseq/Journal]]` and `[[Logseq/Journal/Editorial headings]]` contradict a
    settled decision.** Both instruct topic-led narrative blocks with wry,
    allusive, magazine-style titles. codekiln deleted exactly those on 2026-08-18
    and has written none since; 2026-08-16, 08-18 and 08-19 are change log only.
    An agent following the graph pages will reproduce the error, and this seat did
    on 2026-08-24. Recommendation: the pages should record what the journals
    actually do. **Not acted on** — a convention page is codekiln's to change, and
    `[[Logseq/Journal/Editorial headings]]` exists only to teach the practice, so
    the fix is a deletion rather than an edit.

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

**A governing page can be out of date, and it still reads as governing.** The
graph page said write editorial narrative; the human's own edits said the
opposite, and the edits were four months newer than nothing — the page carried no
date at all. When a page and an observed human action disagree, the action wins,
and the disagreement is worth filing rather than silently obeying one side. Both
were checked here by reading the last four journals rather than by reasoning about
which source ought to govern.

**A capability recorded as absent decays, and bedding down is a retry.** On
2026-08-24 a peer seat met four classifier denials on `claude --chrome`, recorded
the capability as unavailable, and after bedding down ran the identical command
successfully on the first try. The fleet had meanwhile reported a *source* as
blocked when only one *route* to it was. Write an absence the way you would write
a count: what was tried, when, and what the failure looked like — a successor
cannot otherwise tell a standing limitation from a transient refusal, and has no
reason to retest it. `[[My/AI/Agent/Fleet/Browser]]` carries the worked shape.

**A test can confirm a claim on the only inputs that could not falsify it.** The
`.F` suffix was tested with targets that named a window explicitly — `session:0` —
which is precisely the one case where a trailing dot is harmless, so the test passed
on every input it was given and the claim went out. The falsifier was already
stated; it just was not run. This is the same failure as reading an ahead-behind
count without fetching, and as recording a capability absent after four denials:
evidence that was one command away, not evidence that was unavailable. When a rule
holds on every sample tried, find the sample that would break it before writing it
down.
