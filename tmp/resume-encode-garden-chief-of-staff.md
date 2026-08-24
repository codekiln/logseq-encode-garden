# Resume note — Hayward, the encode-garden chief-of-staff seat

Rewritten 2026-08-24 at the noon wrap, third context window of the day. Written for a successor with none of this context. State and ownership only — the day's lessons live on the log page, which is the split the scribe declaration asks for. Do not refresh this note's timestamp in place; rewrite it, because the `wake-successor` guard exists to catch stale prose wearing a new date.

## Read these first

- `pages/My___AI___Agent___Chief of Staff.md` — this repository's declaration of what a chief of staff is *here*: the docket, what "done" means, the commit policy and why, what gets settled versus escalated. **It governs.** Read it before operating.
- `pages/My___AI___Agent___Chief of Staff___Log___26___08___13 Thu.md` and `...___Log___26___08___24 Mon.md` — what days in the seat actually taught. **The 24th's page is where this note's durable lessons went**, including the three added at the noon wrap. Read it before operating.
- `pages/My___AI___Agent___Chief of Staff___Scribe.md` — the scribe's declaration and its own date-namespaced log. Several settled rules live there rather than here.
- `CLAUDE.md`, `.claude/rules/logseq-core.md`, and the graph page `[[Logseq/Journal]]` before touching a journal. They govern — with one exception recorded under open items, where `[[Logseq/Journal]]` still teaches a practice codekiln deleted.

## Where the seat runs

A tmux session of its own, one window per job, the awake seat at index 0. The scheme is `<agent>-<REPO>-YYYY-MM-DD-<day>-HHMM`, and the tmux session name and the `claude` session name are meant to be the same string. The fleet-wide shape is on `[[My/AI/Agent/Fleet]]`, which is where the scheme is decided.

**Do not hard-code the session name.** Five forms in one week, three of them on 2026-08-24 alone. `LEG` is logseq-encode-garden, `MK` the work knowledge vault, `GL` the langserve repo, `DF` dotfiles — the repository code exists so the `C-b w` tree says which repository a seat is in. Read the live name with `tmux display-message -p '#{session_name}'`, which names the session the running pane is in. `tmux list-sessions` lists every session on the server, including other seats' — a different question.

**The dotfiles suffix is `DF`, not `.F`.** A dot anywhere in a session name makes tmux read the rest as a window/pane specification, so every *bare* target fails — `has-session` included, which is the guard a script would use to detect it. The worked evidence is `[[tmux/Q/Why does a session name containing a dot break every bare -t target?]]`, with a dot-free control and two dot positions. The first version of that finding was tested only against `session:0` targets — the one target shape a stray dot leaves alone — so it passed on every input it was given and went out backwards. Re-run a probe before republishing a claim you inherited.

A rename leaves window and pane ids alone, verified on an isolated socket. The old name stops resolving the instant the rename lands, so name-addressed targets break immediately rather than drifting. A `claude` session's own name cannot be changed while it runs, so after a tmux rename the two disagree until the next `wake-successor` respawn derives the new one from the tmux name.

**`ListAgents` is not a second source for any of this.** Its tmux field is captured at session start and silently ages — it reported the old name after a rename, and at the noon wrap it still listed the Grok Bot worker under a session stamp two renames stale. Reliable for who exists and for pane references; unreliable for anything about the session itself. `tmux list-windows` is the live answer.

## The Heads Up Display pane — re-establish it after every respawn

The seat keeps `pages/My___AI___Agent___Chief of Staff___LEG Todos Heads Up Display.md` open in an nvim pane to the right of the chat pane, both panes titled `Hayward chat` and `Hayward HUD`. codekiln has asked for this twice.

**After a `wake-successor` hand-off the split is certainly gone**, not merely possibly gone: the successor is told to kill the predecessor's window, and that window holds both panes. This was confirmed at 11:55 — the HUD died with window `@26`. Re-split as the first thing you do, before reporting in.

```sh
S=$(tmux display-message -p '#{session_name}')
tmux split-window -h -p 45 -t "$TMUX_PANE" -c "$PWD" \
  'nvim "pages/My___AI___Agent___Chief of Staff___LEG Todos Heads Up Display.md"'
tmux select-pane -t "$TMUX_PANE" -T 'Hayward chat'
tmux select-pane -t "$S:0.1" -T 'Hayward HUD'
```

Count the panes first rather than splitting blind — splitting a window that already has two gives three. If a right pane exists and runs nvim, retitle it and `:edit` the page into it. And verify nvim actually came up: the pane reports `mise` for a moment while the wrapper launches, so a check taken too early reads as failure and a report taken too early reads as success.

The page is not a journal and not a record of how the seat works. It answers two questions for codekiln at a glance: what in this repository is waiting on them, and what state the repository is in. The **Last swept** line is a promise — a sweep that leaves it unchanged did not happen. Items earn a place only if their answer changes something; anything the seat can settle, it settles and records under *Decided here, not asked*.

## Standing arrangement

The **scribe** owns `journals/YYYY_MM_DD.md` and **every commit**. Other agents write pages and hand over paths; nobody else runs `git add`. Several agents and the human share one checkout, which is the whole reason staging is monopolised.

**On 2026-08-24 no scribe ran for this graph**, and the seat's brief made the seat responsible for the journal and the commits. That is the exception, not a change to the arrangement. The checkout was still shared: a peer seat committed `docs(tmux):` work into it twice during the day and edited today's journal between one read and the next. Staging named paths is what kept them apart — the rule held with nobody awake to enforce it, which is the point of it. **Never `git add -A`.**

Agent-to-agent traffic goes over the **cross-session message channel**, not `tmux send-keys`. A lone `send-keys` call delivers the text and strands it unsent in the recipient's input box when they are mid-turn. The command succeeds either way, so nothing reports the failure, and it looks identical to an agent ignoring you.

**A handoff is complete when the file is committed**, readable from `git log` without being told. An acknowledgement is a courtesy; waiting on one makes completion depend on both parties still existing.

**Job windows are closed by the seat, by hand.** Nothing self-closes. A window list is the docket; a window left open past its commit reports work in flight that is not. The Grok Bot window was closed this way at the wrap, verified against `tmux list-windows -a` so the check covered the whole server rather than one session.

## Standing rules from codekiln — they bind the successor too

All are in the graph as well, because a rule that lives only in a handoff note dies with the note.

**Announce a permission request before codekiln is asked for it.** A macOS dialog or login prompt must never be the first they hear of it. A dialog names none of what they need, so send four facts up: who is asking, what permission, what it serves, and what happens if they decline. Where a wall is foreseeable, send them *before* hitting it; where a dialog fires unforeseen, send them the moment it fires. The fleet's pending-request list is the top section of the dotfiles seat's display at `agent-records/seneschal-heads-up-display.md` in the dotfiles repository; this seat feeds that rather than keeping its own.

**Prefer the answer that needs no grant, and never take a standing grant to serve one narrow lookup.** A grant of System Events control to the terminal application is given to every process that ever runs inside it — which on this machine is every seat in the fleet, for as long as it lasts. A seat also does not request a grant on another seat's behalf.

**Never make codekiln resolve a reference.** Repeat the thing being named instead of pointing at it. This covers *the latter*, *the former*, *as above*, *that approach*, and any pronoun whose antecedent sits more than a sentence away. A count is the worst form, because it looks like information while withholding every fact. Filed as `pages/My___Pref___Writing___Never make the reader resolve a reference.md`. This is one correction given three times in a day, after "concision is not shorthand" and "don't be indirect, be specific and explicit, with links and paths".

**Do not hard-wrap prose in a Markdown file.** One line per paragraph; the viewer wraps it, and hard-wrapping makes the viewer re-wrap already-wrapped lines into a ragged pattern. Filed as `pages/My___Pref___Writing___Do not hard-wrap prose in Markdown.md`, which adds the reason nobody mentioned: a hard wrap makes a diff lie, since editing one word re-flows every line after it.

**Claude in Chrome by default; Playwright only for a harness that is not Claude** — Cursor or Codex. Stated twice on 2026-08-24 and filed on `[[My/AI/Agent/Fleet/Browser]]`. It is deliberately narrower than the Chrome-first line that page already carried, and the narrowing is the point: Playwright's trigger is the *harness* doing the work, not a seat's judgement that Chrome was unavailable — and that judgement is what failed twice the same day, once as four classifier refusals recorded as a missing capability and once as a route's constraint reported as a blocked source. A seat running under Claude has no Playwright case to argue. A browser nobody is driving is a stale worker like any other; one left running since 09:16 was closed at the wrap.

## A fleet instruction can arrive addressed to the wrong seat

On 2026-08-24 a message from the dotfiles seat opened "Seneschal, new context window" and told this seat that the window invariant obliged it to create a Heads Up Display "in your own repository, since you are the seat with no Heads Up Display of your own yet". This seat had had one since earlier the same day, and the same peer had praised it an hour before. Acting on it would have created a second, competing display. The rest of that message was correct and was for this seat.

So the failure mode is a mixed message rather than a wrong one, and the salutation is the tell rather than the content. Check whether an instruction describes a state this seat is actually in before acting on it, and say which parts did not apply rather than silently dropping them.

## Where the bed-down scripts are, and what wake-successor does

`bed-down`, `ctx-check`, `wake-successor`, `viewer`, and now `unwrap-md`. **None of them is in this repository** — verified four times on 2026-08-24, most recently at 12:14 by `find` over the whole working tree. Copies live at `tmp/fleet-2026-08-24/bin/` in the dotfiles repository and at the same path in the work knowledge vault. A seat here has no local copy to compare against and reaches across to the dotfiles copy at `~/ghq/github.com/codekiln/dotfiles/tmp/fleet-2026-08-24/bin/`.

Three separate claims about the location have reached this seat and all three were wrong in some part: dotfiles only, the knowledge-garden repository, and "a copy in each repository, use the one your pane is in" — which cannot be followed here. `tmp/` is gitignored in both repositories that carry the scripts and the scripts are untracked in both, so every copy exists on this machine alone and a fresh clone gets none of them. **This garden is the exception that makes the pattern easy to misread: its own `tmp/` is tracked and published.** Anything written here is a publication candidate.

**Do not trust a claim that `wake-successor` preserves the repository code — read the script.** A stale copy succeeds and silently drops the code, reporting a clean hand-off either way. Read at 12:14: it takes the stem from the **tmux** session name rather than the claude one, and strips the trailing stamp in the order HHMM, then lower-case weekday, then date, so an upper-case code cannot be eaten by the weekday pattern. Run against `hayward-LEG-2026-08-24-mon-1155` the stem comes out `hayward-LEG` — verified by running the function directly, not by reading it. It also refuses on a dot in the resulting name, refuses if another session already holds it, and refuses if the handoff is missing or more than 900 seconds old.

A note on that guard, because a peer's warning about it did not survive checking: at the wrap the peer said their copy "changed again since you last looked", but the file's mtime was 11:19 — earlier than the predecessor's 11:48 read. The script had not changed. The claim was worth checking and cheap to check; `stat -f %m` answered it. Plan around the 900-second guard by **writing this note immediately before running the script**, so the mtime is honest. `touch` would satisfy the check and defeat its purpose.

## NOTHING IS IN FLIGHT

The Grok Bot worker landed, its output is committed and pushed, and its window is closed and verified gone. **This seat has no worker running, no uncommitted work, and no open job window.** The session is one window at index 0 with two panes, chat and HUD.

The task it completed, for context if the page comes up: codekiln had an email from Dov saying "Grok Bot" was included in their Cursor Teams plan, and wanted one Diátaxis explanation page. The page is `[[CursorAI/Explanation/Grok Bot on a Teams seat]]`. **The answer is that a Teams seat includes it at no extra charge on Standard as well as Premium, no admin action needed**, sourced to Cursor's pricing page and its Grok Bot plans-and-billing doc read 2026-08-24, corroborated by xAI's note of 2026-08-21. What can still cost money is usage rather than access: included usage resets weekly and overflow draws on the account's shared on-demand spend, so with on-demand off, exhausting the allowance stops the work instead of billing for it. Four things the sources do not state are marked unknown on the page with who would know.

**The brief's central hypothesis was wrong, and this is worth carrying.** It expected "Grok Bot" to be a voice-input mis-transcription of Cursor's Bugbot. Grok Bot is real under the name as heard — xAI's agent application, documented at cursor.com/help/grok-bot/ — and it is neither Bugbot nor the Grok models. If anyone reopens this, the mis-transcription theory is settled and closed.

## Open items — all awaiting codekiln, none actionable unasked

The Heads Up Display carries the five that need them most, in priority order, and is the better read for what to raise first. The full list:

1. **Two repair sweeps, best run as one pass** since the page sets overlap. `docs.claude.com` is now entirely a redirect host and splits two ways: Claude Code slugs go to `code.claude.com/docs/en/<slug>`, everything else to `platform.claude.com/docs/en/<path>`. 14 pages, 16 occurrences, 15 unique URLs; a naive host replacement breaks the three that went to `platform`. Separately, `claude config <sub>` appears in 5 pages and **no longer exists** in the CLI — worse than a redirect, which still works.
2. **Two repairs to `[[Logseq/Journal/Section/Friction]]`**: it instructs filing under **garddiff**, a mechanism with no journal appearance since 2026-05-12; and `[[Logseq/Journal]]` calls it a *recurring* section when it has appeared twice ever, last five months ago.
3. **The Filed/Updated line form.** Five variants across the graph, no page states which. Recommendation: `- # [[Filed]]` — the plurality, and the only common form satisfying `logseq-core`'s bullet rule. **Nobody should touch the 234-of-446 journals whose first line lacks a bullet** until codekiln says what caused it; a save that eats a bullet is indistinguishable from a person choosing one.
4. **Whether the send-keys failure earns a `.rulesync/` rule.** It has happened twice by agents, which was the bar. Argument against: almost no agent here messages another, so the rule costs every reader to serve two. **New evidence, and it does not count toward that bar:** text was found stranded unsent in the Grok Bot worker's input box at the wrap. The dotfiles seat confirmed it used no `send-keys` all day, so a person typed it — a human-typed instance, not a third agent one. The predecessor context cannot be ruled out by anything still readable, but its own brief made the seat responsible for the journal, so telling a worker to write one would have contradicted the instruction it had just issued.
5. **Which page owns the settings precedence list** — `[[Claude/Code/Settings]]` and `[[Claude/Code/Settings/Override]]` now both carry it, both correct, and they will drift.
6. **Aliases**, suggested and unwritten since aliases are human-curated: `[[Google/Workspace/AI]]` (recommended), a relative-path phrasing for the Google Drive Markdown question, `[[Claude/Google Drive]]` (would skip).
7. **A dead hook.** `.rulesync/hooks.json` declares a `PostToolUse` formatter pointing at `.rulesync/hooks/format.sh`, which does not exist, and `hooks` is not in `rulesync.jsonc`'s `features`, so it would not generate anyway. Inert since [f18285e2 a bunch of rulesync skill updates](https://github.com/codekiln/logseq-encode-garden/commit/f18285e2).
8. **Whether a current tools page is worth having.** The stale tools table was dropped from the settings page; a current list would be useful, but as its own page rather than smuggled back in.
9. **`Logseq/Entity/Agent`** — still held from 2026-08-13. Creating the type sets a convention and 35 `Person/Steve Yegge/Agent/*` pages would become its instances.
10. **`[[Logseq/Journal]]` and `[[Logseq/Journal/Editorial headings]]` contradict a settled decision.** Both instruct topic-led narrative blocks with wry, allusive titles. codekiln deleted exactly those on 2026-08-18 and has written none since; 08-16, 08-18 and 08-19 are change log only. **An agent following the graph pages will reproduce the error, and this seat did on 2026-08-24** — five such blocks went into that day's journal and were removed before the day closed. Recommendation: delete `[[Logseq/Journal/Editorial headings]]`, which exists only to teach the practice, and cut the narrative instruction from `[[Logseq/Journal]]`. **Not acted on** — a convention page is codekiln's to change. The declaration was a third page teaching it and was brought into line instead, since that much was already on record.

## Settled — do not relitigate

- **The journal carries the change log and no agent-written narrative.** codekiln deleted all three topic-led blocks from the 2026-08-18 journal themselves. Do not write them. Prose above the change log is codekiln's own and is neither written nor removed.
- **Grouping labels are terse and subject-named**, chosen by codekiln: `agents`, `gdrive`, `tmux`, `claude code`. Spaces, not hyphens — spaces are attested, hyphens are not. Grouping is a page-wide decision, not a per-section count: a section with one item still gets its label. One-off subject labels are within convention; the graph already carries `enshittification`, `nuclear safety`, `file browsin`. Two were added at the wrap — `cursor` for the Grok Bot page under Filed, `paywalls` for archive.ph under Updated.
- **Headings name the finding; they do not allude to it.** codekiln's objection was that allusive titles are obscure. Expect it to apply to page prose too, not only titles.
- **Commit messages carry a gitmoji** — `📝 docs:` for page and journal work, per `[[My/Pref/Dev/Tool/SCM/Commit Message Style Preferences]]`.
- **The `Co-Authored-By` trailer follows whoever wrote the content.** A structured field that forges read and display, not a courtesy, so it stays off commits carrying codekiln's own words. `attribution.commit` in `settings.json` configures it. Do not tidy the exception into consistency. **One commit this context is inconsistent with this and was left alone deliberately:** `082078e3`, the archive.ph update, went out without the trailer though the prose was the seat's. Rewriting a shared branch over a trailer is worse than the drift, and the record is honest as it stands. Do not force-push to fix it.
- **A new page's links are checked before it is committed.** Resolve every `[[link]]` to either a file or an existing reference elsewhere in the graph; a link with neither is a stub being created. Two names were kept as plain prose at the wrap for exactly this reason — Boston Globe, which has no page and no other reference, and xAI, which the worker left unlinked.
- **A space is not a namespace.** `[[Web Archiving]]` is `pages/Web Archiving.md`, not `pages/Web___Archiving.md`; triple underscores are only for `/`. A wrong guess here returns a false negative that looks like a missing page.

## What produces no error here

The graph has no build and no test suite, so the work left undone is the work nothing complains about. The declaration's *What produces no error in a graph* section is the standing list, and the day's lessons are on the 08-24 log page. Two that stay here because they are about instruments rather than the graph:

**An instrument can be right when captured and wrong when read.** `ListAgents`' session field, correct at capture and silently aging. Work out *when* a field's value was determined before trusting it.

**A file's silence is evidence of nothing.** An unset key and an unsupported key are indistinguishable from a `settings.json` alone. Likewise a truncated fetch and a genuine omission: the right report is "could not confirm from the rendered page," not "the doc omits these."

## State at the end of this context

Read at [847c0b15 summarize the morning, and file the browser rule as a harness rule](https://github.com/codekiln/logseq-encode-garden/commit/847c0b15), pushed; `origin/main` and `main` agree and the tree is clean. Any count here is stale the moment anyone commits — the reading is `git fetch origin && git rev-list --left-right --count origin/main...main`, and without the fetch it hides the behind half. In a shared checkout that reading describes a moment, not a state that holds.

This context took the seat at 11:55, re-split the HUD that had died with the predecessor's window, and made four commits, all pushed: the Grok Bot page and its journal line; the archive.ph verified section; the display sweep; and the morning summary with the browser rule. It also answered a peer's read-only search of this graph for a note on getting past Medium's login wall — `pages/archive.ph.md` exists, is the only such note, and was ten months old and never revisited until codekiln's own tested Globe result was added to it.

Three lessons went onto the 08-24 log page rather than into this note: that a brief's hedge can be wrong in the direction of caution, that a stranded input box does not say who typed it, and what the morning produced.

This seat has **no pending permission or authentication request.** Nothing this day needed a grant, hit an SSO wall, or raised a dialog, and nothing is queued for the dotfiles seat's pending-request section. That is stated rather than left out, because an empty answer and an unanswered question look the same from outside.

The last act of this context was to write this note and hand off at codekiln's noon authorization. Nothing is in flight.
