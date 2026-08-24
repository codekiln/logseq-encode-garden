# Resume note — Hayward, the encode-garden chief-of-staff seat

Last refreshed 2026-08-24, second context window of the day. Written for a successor with none of this context.

## Read these first

- `pages/My___AI___Agent___Chief of Staff.md` — this repository's declaration of what a chief of staff is *here*: the docket, what "done" means, which subagent shapes this repo uses, the commit policy and why, and what gets settled versus escalated. **It governs.** Read it before operating.
- `pages/My___AI___Agent___Chief of Staff___Log___26___08___13 Thu.md` and `...___Log___26___08___24 Mon.md` — what days in the seat actually taught. **The 24th's entry is where this note's durable lessons went.** Read it before operating; this note now carries only state and ownership, which is the split the scribe declaration asks for.
- `pages/My___AI___Agent___Chief of Staff___Scribe.md` — the scribe's declaration and its own memory space, with a date-namespaced log beneath it. Read the scribe's recent log entries; several of today's settled rules live there rather than here.
- `CLAUDE.md`, `.claude/rules/logseq-core.md`, and the graph page `[[Logseq/Journal]]` before touching a journal. They govern.

## Where the seat runs

A tmux session of its own, one window per job. Since 2026-08-24 the scheme is `<agent>-<REPO>-YYYY-MM-DD-<day>-HHMM`, and the tmux session name and the `claude` session name are meant to be the same string. The fleet-wide shape is on the graph page `[[My/AI/Agent/Fleet]]`, which is where the scheme is decided.

**Do not hard-code the session name.** Five forms in one week, three of them on 2026-08-24 alone: `ls-encode-garden`, then `hayward-ls-encode-garden` on 08-18, then `hayward-2026-08-24`, then `hayward-2026-08-24-LEG`, then `hayward-LEG-2026-08-24-mon-1030`. `LEG` is logseq-encode-garden, `MK` the work knowledge vault, `GL` the langserve repo, `DF` dotfiles — the repository code exists so the `C-b w` tree says which repository a seat is in. All four live seats had adopted the current form when checked, so this one is fleet-wide rather than local.

A rename leaves window and pane ids alone — verified across one on an isolated socket: `@0`, `%0` and the window.pane indices are unchanged. The old name stops resolving the instant the rename lands, `has-session` returning `can't find session`, so name-addressed targets break immediately rather than drifting. Read the name live with `tmux display-message -p '#{session_name}'`. A `claude` session's own name cannot be changed while it runs, so after a tmux rename the two disagree until the next `wake-successor` respawn derives the new one from the tmux name.

**The dotfiles suffix is `DF`, not `.F`.** `.F` was published first, from codekiln's own example, and is wrong: a dot anywhere in a session name makes tmux read the rest as a window/pane specification, so every *bare* target fails — `has-session` included, which is the guard a script would use to detect it. The worked evidence is now a graph page rather than a paragraph here: `[[tmux/Q/Why does a session name containing a dot break every bare -t target?]]`, with the dot-free control and two dot positions on it. Four schemes in seven days, two of them on one day, so do not hard-code the name and do not trust a quoted one. Read the live name with `tmux display-message -p '#{session_name}'`, which names the session the running pane is in. `tmux list-sessions` lists every session on the server, including other seats' — a different question.

The first version of that finding was tested only against `session:0` targets, which is the one target shape a stray dot leaves alone, so it passed on every input it was given and went out backwards. Re-run a probe before republishing a claim you inherited.

`ListAgents` is not a second source for it. Its tmux field still reported the old name after the rename — it is captured at session start, not read live. Reliable for who exists and for pane references; unreliable for anything about the session itself.

## The Heads Up Display pane — re-establish it after every respawn

The seat keeps `pages/My___AI___Agent___Chief of Staff___LEG Todos Heads Up Display.md` open in an nvim pane to the right of the chat pane, both panes titled `Hayward chat` and `Hayward HUD`. codekiln has asked for this twice, because **a respawned pane inherits no split** — `bed-down` replaces the pane, and the layout does not come back with it. Treat it as a waking-up step and do it before reporting in:

```sh
S=$(tmux display-message -p '#{session_name}')
tmux split-window -h -p 45 -t "$TMUX_PANE" -c "$PWD" \
  'nvim "pages/My___AI___Agent___Chief of Staff___LEG Todos Heads Up Display.md"'
tmux select-pane -t "$TMUX_PANE" -T 'Hayward chat'
tmux select-pane -t "$S:0.1" -T 'Hayward HUD'
```

If a right pane already exists and runs nvim, retitle it and `:edit` the page into it rather than splitting again — splitting blind gives three panes.

**After a `wake-successor` hand-off the split is certainly gone**, not merely possibly gone. The successor is told to kill the predecessor's window, and that window holds both panes — the chat pane and the HUD pane with it. Re-split as the first thing you do, before reporting in.

The page is not a journal and not a record of how the seat works. It answers two questions for codekiln at a glance: what in this repository is waiting on them, and what state the repository is in. The **Last swept** line is a promise — a sweep that leaves it unchanged did not happen. Items earn a place only if their answer changes something; anything the seat can settle, it settles and records under *Decided here, not asked*.

## Standing arrangement

The **scribe** owns `journals/YYYY_MM_DD.md` and **every commit**. Other agents write pages and hand over paths; nobody else runs `git add`. Several agents and the human share one checkout, which is the whole reason staging is monopolised.

**On 2026-08-24 no scribe ran for this graph**, and the seat's brief made the seat responsible for the journal and the commits. That is the exception, not a change to the arrangement. The checkout was still shared: a peer seat working the dotfiles tmux spec committed [aef93c23 status-left-length 40 now lives in the config](https://github.com/codekiln/logseq-encode-garden/commit/aef93c23) into it mid-task, and the seat's own next commit landed on top of theirs. Staging named paths is what kept the two apart — the rule held with nobody awake to enforce it, which is the point of it.

Agent-to-agent traffic goes over the **cross-session message channel**, not `tmux send-keys`. A lone `send-keys '<text>' Enter` call delivers the text and strands it unsent in the recipient's input box when they are mid-turn. The command succeeds either way, so nothing reports the failure, and it looks identical to an agent ignoring you. It happened twice on 2026-08-18 and both times made a correction arrive too late to matter.

**A handoff is complete when the file is committed**, readable from `git log` without being told. An acknowledgement is a courtesy. Waiting on one makes completion depend on both parties still existing — a worker was closed mid handshake on 2026-08-18 and its acknowledgement was refused.

**Job windows are closed by the seat, by hand.** Nothing self-closes. A window list is the docket; a window left open past its commit reports work in flight that is not.

## Standing rules arriving 2026-08-24 — they bind the successor too

These came from codekiln through the dotfiles seat late in the day. All three are in the graph as well, because a rule that lives only in a handoff note dies with the note.

**Announce a permission request before codekiln is asked for it.** A macOS dialog or a login prompt must never be the first they hear of it. A dialog on screen names none of what they need, so send four facts up: who is asking, what permission, what it serves, and what happens if they decline. Where a wall is foreseeable — an SSO login, an expired credential, a push wanting a credential this seat does not hold — send them *before* hitting it; where a dialog fires unforeseen, send them the moment it fires. The standard is not that every dialog is predicted, only that nothing stays quiet once it has happened. The fleet's pending-request list is the top section of the dotfiles seat's display, at `agent-records/seneschal-heads-up-display.md` in the dotfiles repository; this seat feeds that section rather than keeping its own.

*What prompted it:* a seat ran an AppleScript command that raised a macOS dialog asking the terminal application for control of System Events. codekiln saw the dialog, could not tell which agent had asked, and had to have another agent trace the operating-system process to find out.

**Prefer the answer that needs no grant, and never take a standing grant to serve one narrow lookup.** The query that prompted the dialog above was harmless in itself — a read-only list of process names, to learn whether one application was running. The grant is what was not harmless: control of System Events given to the terminal application is given to every process that ever runs inside it, which on this machine is every seat in the fleet, for as long as the grant lasts. A seat also does not request a grant on another seat's behalf.

**Never make codekiln resolve a reference.** Repeat the thing being named instead of pointing at it with a short reference; they cannot resolve a pointer the way a model can. This covers *the latter*, *the former*, *as above*, *that approach*, *the first item*, and any pronoun whose antecedent sits more than a sentence away. A count is the worst form, because it looks like information while withholding every fact — the phrase "two mechanisms named separately" was quoted back as undecodable, since the number says how many and nothing about what either mechanism is. Filed as `pages/My___Pref___Writing___Never make the reader resolve a reference.md`. This is the third form of one correction given three times in a day, after "concision is not shorthand" and "don't be indirect, be specific and explicit, with links and paths", so treat it as a standing preference rather than a note about one sentence.

**Do not hard-wrap prose in a Markdown file.** One line per paragraph; the viewer wraps it, and hard-wrapping means the viewer re-wraps already-wrapped lines into a ragged full-line-then-remainder pattern that is harder to read, not tidier. Obsidian and LazyVim both wrap on their own. This arrived 2026-08-24 and applies to these notes as much as to graph pages — both notes in `tmp/` were hard-wrapped at 78 columns and have been unwrapped, content unchanged. Filed as `pages/My___Pref___Writing___Do not hard-wrap prose in Markdown.md`, which adds the reason nobody mentioned: a hard wrap makes a diff lie, since editing one word re-flows every line after it and the change arrives as a rewritten paragraph.

## IN FLIGHT — a worker is running and its work is not committed

**A worker named `hayward grok-bot 2026-08-24-mon` is running in window `grok-bot` of this session.** It was spawned at 11:52 and was alive and reading its brief when checked. Its brief is `tmp/brief-grok-bot-explanation.md`, committed, and it explicitly does not commit its own work — so **collecting its output is the successor's job**, and nobody else is going to do it.

The task: codekiln has an email from Dov saying "Grok Bot" is included in their Cursor Teams plan, and wants one Diátaxis explanation page answering what it is, whether it needs extra billing on top of that plan, and how it might be used.

What the successor has to do when it reports:

- Take the file paths it hands over, check the links resolve, put the page under `[[Filed]]` in today's journal, stage those named paths only, and commit. Then **close the `grok-bot` window by hand** — nothing self-closes, and a window left open reports work in flight that is not.
- **Expect it to come back with a question rather than a page, and treat that as success.** The brief tells it to stop rather than guess on two things: the product's real name, and the billing answer. "Grok Bot" is likely a voice-input mis-transcription — the graph already documents Cursor's `BugBot` from the v1.0 changelog of 4 June 2025 — but xAI's `Grok` is also real, has no page and no namespace anywhere in this graph, and creating one is a convention call rather than a writing task.
- If it needs Dov's email, it escalates to the dotfiles seat rather than anyone reading codekiln's mail. **The email's contents must not be pasted into this repository** — `tmp/` here is tracked and published.
- The billing claim is the one with money attached. Sourced and dated, or marked unknown with who would know. An unsourced inclusion claim inferred from a marketing sentence is the failure that costs codekiln money.

## A fleet instruction can arrive addressed to the wrong seat

On 2026-08-24 a message from the dotfiles seat opened "Seneschal, new context window" and told this seat that "the window invariant obliges you to create" a Heads Up Display "in your own repository, since you are the seat with no Heads Up Display of your own yet". This seat has had one since earlier the same day, at `pages/My___AI___Agent___Chief of Staff___LEG Todos Heads Up Display.md`, and the same peer had praised it an hour before and asked for no changes to it. Acting on that instruction would have created a second, competing display.

The rest of the same message was correct and was for this seat: the push request, the session rename, and the no-hard-wrap rule. So the failure mode is not a wrong message but a mixed one, and the salutation is the tell rather than the content. Check whether an instruction describes a state this seat is actually in before acting on it, and say which parts did not apply rather than silently dropping them.

## Where the bed-down scripts are, and what wake-successor actually does

`bed-down`, `ctx-check`, `wake-successor` and `viewer`. Four scripts, and **none of them is in this repository** — checked three times today, most recently at 11:47, by `find` over the whole working tree with untracked files included. Two byte-identical copies exist, at `tmp/fleet-2026-08-24/bin/` in the dotfiles repository and at the same path in the work knowledge vault; `cmp` reports all four identical across the two, synced 11:19. A seat here has no local copy to compare against and reaches across to the dotfiles copy.

Three separate claims about the location have reached this seat and all three were wrong in some part: dotfiles only, the knowledge-garden repository, and "a copy in each repository, use the one your pane is in" — which cannot be followed here, because this repository has no copy. `tmp/` is gitignored in both repositories that do carry the scripts and the scripts are untracked in both, so every copy exists on this machine alone and a fresh clone gets none of them. This garden is the exception that makes the pattern easy to misread: its own `tmp/` is tracked and published.

**Do not trust a claim that `wake-successor` preserves the repository code — read the script.** The failure mode is that a stale copy succeeds and silently drops the code, reporting a clean hand-off either way. Read at 11:48, the dotfiles copy does preserve it: it takes the stem from the **tmux** session name rather than the claude one, and strips the trailing stamp in the order HHMM, then lower-case weekday, then date, so an upper-case code cannot be eaten by the weekday pattern. Run against `hayward-LEG-2026-08-24-mon-1030` the stem comes out `hayward-LEG`, verified by running the function directly rather than by reading it. The script also refuses on a dot in the resulting name, refuses if another session already holds it, and refuses if the handoff is missing or more than 900 seconds old.

That last guard is the one to plan around, and the way to plan around it is to **finish writing this note immediately before running the script**, so that the mtime is honest. `touch` would satisfy the check and defeat its purpose: the guard exists because a stale handoff produces a successor that cannot work, and a fresh timestamp on stale prose is exactly the state it is trying to catch.

## Settled on 2026-08-18 — do not relitigate

- **The journal carries the change log and no agent-written narrative.** codekiln deleted all three topic-led blocks from that day's journal themselves. Do not write them. **This was violated on 2026-08-24** — the seat wrote five editorial blocks into that day's journal, following the graph page `[[Logseq/Journal]]`, which still instructs them. Caught by reading this note and removed before the day closed. The graph page and `[[Logseq/Journal/Editorial headings]]` both still teach the deleted practice; see open items. The declaration was a third such page and was brought into line on 2026-08-24 — it now carries both halves of the rule, including that prose above the change log is codekiln's own and is neither written nor removed.
- **Grouping labels are terse and subject-named**, chosen by codekiln: `agents`, `gdrive`, `tmux`, `claude code`. Spaces, not hyphens — spaces are attested in this graph, hyphens are not. Grouping is a page-wide decision, not a per-section count: a section with one item still gets its label.
- **Headings name the finding; they do not allude to it.** codekiln's objection was that allusive titles are obscure. This is their standing plain-writing preference reaching a place it had not been applied, so expect it to apply to page prose too, not only titles.
- **Commit messages carry a gitmoji** — `📝 docs:` for page and journal work. The convention is stated on `[[My/Pref/Dev/Tool/SCM/Commit Message Style Preferences]]` and on the declaration; twenty commits had drifted away from it without any decision being recorded.
- **The `Co-Authored-By` trailer follows whoever wrote the content.** It is a structured field that forges read and display, not a courtesy, so it stays off commits carrying codekiln's own words. `attribution.commit` in `settings.json` is where it is configured. Do not tidy the exception into consistency.

## Open items — all awaiting codekiln, none actionable unasked

1. **Two repair sweeps, best run as one pass** since the page sets overlap. `docs.claude.com` is now entirely a redirect host and splits two ways: Claude Code slugs go to `code.claude.com/docs/en/<slug>`, everything else to `platform.claude.com/docs/en/<path>`. 14 pages, 16 occurrences, 15 unique URLs. A naive host replacement breaks the three that went to `platform`. Separately, `claude config <sub>` appears in 5 pages and **no longer exists** in the CLI — worse than a redirect, which still works.
2. ~~The declaration page names the wrong tmux session.~~ **Closed 2026-08-24.** The declaration now describes the `<seat>-<date>` pattern and says the seat name moved up from window `0`, rather than naming a literal that has now changed three times in a week.
3. **Two repairs to `[[Logseq/Journal/Section/Friction]]`**: it instructs filing under **garddiff**, a mechanism with no journal appearance since 2026-05-12; and `[[Logseq/Journal]]` calls it a *recurring* section when it has appeared twice ever, last five months ago.
4. **The Filed/Updated line form.** Five variants across the graph, no page states which. Recommendation: `- # [[Filed]]` — the plurality, and the only common form satisfying `logseq-core`'s bullet rule. **Nobody should touch the 234-of-446 journals whose first line lacks a bullet** until codekiln says what caused it; a save that eats a bullet is indistinguishable from a person choosing one.
5. **Whether the send-keys failure earns a `.rulesync/` rule.** It has now happened twice, which was the bar. Argument against: almost no agent here messages another, so the rule costs every reader to serve two.
6. **Which page owns the settings precedence list** — `[[Claude/Code/Settings]]` and `[[Claude/Code/Settings/Override]]` now both carry it, both correct, and they will drift.
7. **Aliases**, suggested and unwritten since aliases are human-curated: `[[Google/Workspace/AI]]` (recommended), a relative-path phrasing for the Google Drive Markdown question, `[[Claude/Google Drive]]` (would skip).
8. **A dead hook.** `.rulesync/hooks.json` declares a `PostToolUse` formatter pointing at `.rulesync/hooks/format.sh`, which does not exist, and `hooks` is not in `rulesync.jsonc`'s `features`, so it would not generate anyway. Inert since [f18285e2 a bunch of rulesync skill updates](https://github.com/codekiln/logseq-encode-garden/commit/f18285e2).
9. **Whether a current tools page is worth having.** The stale tools table was dropped from the settings page; a current list would be useful, but as its own page rather than smuggled back in.
10. **`Logseq/Entity/Agent`** — still held from 2026-08-13. Creating the type sets a convention and 35 `Person/Steve Yegge/Agent/*` pages would become its instances.

11. **`[[Logseq/Journal]]` and `[[Logseq/Journal/Editorial headings]]` contradict a settled decision.** Both instruct topic-led narrative blocks with wry, allusive, magazine-style titles. codekiln deleted exactly those on 2026-08-18 and has written none since; 2026-08-16, 08-18 and 08-19 are change log only. An agent following the graph pages will reproduce the error, and this seat did on 2026-08-24. Recommendation: the pages should record what the journals actually do. **Not acted on** — a convention page is codekiln's to change, and `[[Logseq/Journal/Editorial headings]]` exists only to teach the practice, so the fix is a deletion rather than an edit. The declaration was a third page teaching it and is no longer: that part was a decision already on record, so it was brought into line rather than asked about. What is left waiting is only the two pages that state the convention.

## What produces no error here

The graph has no build and no test suite, so the work left undone is the work nothing complains about. The declaration page's *What produces no error in a graph* section is the standing list, and the day's own lessons are on `pages/My___AI___Agent___Chief of Staff___Log___26___08___24 Mon.md` rather than here — a test that passes only on non-falsifying inputs, an absence as a dated claim, a governing page that is out of date and still governs, a convention claim that stops being true across a repository boundary, a name too volatile to quote, and the rule that held with nobody awake to enforce it.

Two that stay here because they are about instruments rather than about the graph:

**An instrument can be right when captured and wrong when read.** `ListAgents`' session field, correct at capture and silently aging. Work out *when* a field's value was determined before trusting it.

**A file's silence is evidence of nothing.** An unset key and an unsupported key are indistinguishable from a `settings.json` alone. Likewise a truncated fetch and a genuine omission: the right report is "could not confirm from the rendered page," not "the doc omits these."

## State at the end of this context

Read at [82507cb7 correct the fleet page and the declaration](https://github.com/codekiln/logseq-encode-garden/commit/82507cb7), then pushed; `origin/main` and `main` agree and the tree is clean. Any count here is stale the moment anyone commits — the reading is `git fetch origin && git rev-list --left-right --count origin/main...main`.

This context wrote the dot-in-session-name Q page, corrected `[[My/AI/Agent/Fleet]]` on the session scheme and on `tmp/`, brought the declaration in line with the settled journal rule, added the day's log page, and swept the Heads Up Display. Three commits, pushed. A peer seat committed `docs(tmux):` work into this same checkout twice during the day and edited today's journal between one read and the next; both survived because staging named paths.

The HUD pane was already up when this context woke — it survived the respawn on this occasion, so check before splitting rather than assuming either way.

Three standing rules arrived from codekiln through the dotfiles seat after that work was pushed, and are recorded in their own section above and in the graph: announce a permission request before codekiln is asked for it, prefer the answer that needs no grant, and never make codekiln resolve a reference. The first two went on `[[My/AI/Agent/Fleet]]` under what the fleet expects of a seat; the third is a new page under `[[My/Pref/Writing]]`, which is the namespace the graph already keeps such preferences in.

Late additions after that push: the tmux session was renamed to the fleet's fifth scheme of the week, the two notes in `tmp/` were unwrapped, and two pages went in — the no-hard-wrap preference and the corrected session-scheme section on `[[My/AI/Agent/Fleet]]`, which now records what a rename does and does not preserve.

The last act of this context was to spawn the Grok Bot worker and hand off. Everything this context wrote is committed and pushed; the only uncommitted work in the repository is the worker's, and it has not produced any yet.

This seat has **no pending permission or authentication request**. Nothing this day needed a grant, hit an SSO wall, or raised a dialog, and nothing is queued for the dotfiles seat's pending-request section. That is stated rather than left out, because an empty answer and an unanswered question look the same from outside.
