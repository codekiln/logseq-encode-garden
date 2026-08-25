# Resume note — Hayward, the encode-garden chief-of-staff seat

Rewritten 2026-08-25 07:08 EDT. Written by the fourth context window of Monday 2026-08-24, which took the seat at 12:18 EDT, worked until 16:58 EDT past the stand-down it had prepared for, and is handing off on Tuesday morning at 379k tokens. The Monday afternoon sections below were rewritten at 14:08 EDT and the work after that is under its own heading. Written for a successor with none of this context. State and ownership only — the day's lessons live on the log page, which is the split the scribe declaration asks for. Do not refresh this note's timestamp in place; rewrite it, because the `wake-successor` guard exists to catch stale prose wearing a new date. Every timestamp here is EDT.

## Read these first

- `pages/My___AI___Agent___Chief of Staff.md` — this repository's declaration of what a chief of staff is *here*: the docket, what "done" means, the commit policy and why, what gets settled versus escalated. **It governs.** Read it before operating.
- `pages/My___AI___Agent___Chief of Staff___Log___26___08___24 Mon.md` — what the day taught, now twelve sections. The last five were added by this context and are the ones a successor is most likely to need. Also `...___Log___26___08___13 Thu.md`.
- `pages/My___AI___Agent___Chief of Staff___Scribe.md` — the scribe's declaration and its own date-namespaced log. Several settled rules live there rather than here.
- `pages/My___AI___Agent___Chief of Staff___LEG Todos Heads Up Display.md` — what is waiting on codekiln, in priority order. Swept at 14:00 EDT by this context.
- `CLAUDE.md`, `.claude/rules/logseq-core.md`, and the graph page `[[Logseq/Journal]]` before touching a journal. They govern — with one exception recorded under open items, where `[[Logseq/Journal]]` still teaches a practice codekiln deleted.

## THE NEXT ACTION — three book pages, researched and unwritten

codekiln asked, through the dotfiles seat at 13:5x EDT, for three books imported as Book entities framed as relevant to improving AI agents' writing. **Nothing was written.** The research is complete and the judgement calls are resolved below; the stand-down came before any page was created, and rushing them was explicitly declined rather than forgotten. **Reeve has follow-on work gated behind this import and stays gated**, so nothing downstream breaks — but this is the first thing to finish.

The three, with the sources codekiln supplied:

- **Clear and Simple as the Truth: Writing Classic Prose** — Francis-Noël Thomas and Mark Turner, Princeton University Press, 1994; the Project MUSE copy is the 2017 Princeton Legacy Library reissue. <https://muse.jhu.edu/book/51053> and <https://www.amazon.com/Clear-Simple-Truth-Writing-Princeton-dp-0691654743/dp/0691654743/>
- **The Elements of Style** — Strunk, with E. B. White's revisions. <https://en.wikipedia.org/wiki/The_Elements_of_Style>
- **The Art of Raising a Puppy** — the Monks of New Skete. <https://www.goodreads.com/en/book/show/32218.The_Art_of_Raising_a_Puppy> and <https://janicegreenwood.com/2020/09/book-review-the-art-of-raising-a-puppy-by-the-monks-of-new-skete/>

None of the three exists in the graph; checked by `git ls-files` over `pages/Book___*` and `pages/Person___*___Book___*`.

### The path form is settled by evidence — use flat `Book/<title>`

`pages/Logseq___Entity___Book.md` says books usually live at `Person/<name>/Book/YY/<short title>`, and may live at `Book/YY/<short title>` when there are five or more sub-pages or **more than one author**. All three books have more than one author, which points at `Book/YY/`.

**Do not use `Book/YY/`. It has zero instances in this graph.** Measured: `git ls-files | grep -E 'pages/Book___[0-9]{2}___'` returns nothing. What actually exists is 33 flat `Book/<title>` pages and 20 `Person/<name>/Book/YY/<title>` pages. Multi-author books here take the **flat** form — `Book/Understanding by Design` (two authors), `Book/ML with PyTorch and Scikit-Learn` (three). The `logseq-book` skill also defaults to `[[Book/Title]]`. Creating the first-ever `Book/YY/` page would be setting a convention, which the declaration sends up rather than settles.

**This dissolves the year question.** On a flat page the year is not in the path; it goes in `date-created:: [[YYYY]]`, and the graph's precedent is the **original** publication year rather than a reissue — `Book/Understanding by Design` carries `date-created:: [[1998]]` though its expanded second edition is 2005. So: **1994** for Clear and Simple as the Truth, not 2017. **1991** for The Art of Raising a Puppy, not the later revision.

### The template to copy

`pages/Book___Tao Te Ching.md` is the cleanest instance carrying the entity marker. Its whole shape:

```
logseq-entity:: [[Logseq/Entity/Book]]
created-by:: [[Person/Lao Tzu]]
- # Tao Te Ching
	- ## About
		- ...
	- ## Links
		- [Wikipedia](https://en.wikipedia.org/wiki/Tao_Te_Ching)
		- [[Person/Lao Tzu]]
```

Note **no `tags::`**. Book pages here do not tag `[[Book]]`; the entity marker does that work, and `tags::` where it appears is topical. Do not add `tags::` — `logseq-core` forbids touching it and there is no need. `created-by::` takes comma-separated links: `created-by:: [[Person/Grant Wiggins]], [[Person/Jay McTighe]]`.

**Author pages must exist, and the precedent is thin ones written alongside the book.** `pages/Person___Grant Wiggins.md` and `pages/Person___Jay McTighe.md` were created with `Book/Understanding by Design` and are four lines each: `logseq-entity:: [[Logseq/Entity/Person]]`, an H1, a one-line `## About` naming the book, and `## Links`. None of Francis-Noël Thomas, Mark Turner, William Strunk Jr. or E. B. White has a page — checked. Mark Turner is absent entirely, including any conceptual-blending page. Write four thin Person pages, or the book pages create stubs, which the settled rule forbids.

### The collective-author question is resolved — it is not the gap it looked like

The brief flagged the Monks of New Skete as a gap because `created-by::` wants `[[Person/Full Name]]`. **There is precedent for non-Person authors**: `created-by::` values across the graph already include `[[37Signals]]`, `[[Canonical]]`, `[[Google]]`, `[[Gitlab]]`, `[[LangChain]]`, `[[IEEE/Committee/LTSC]]`. **And there is an `Organization` entity type** — `pages/Logseq___Entity___Organization.md` exists (there is no `Org` type; do not invent one). So the Monks take an Organization entity, not a Person, and no convention needs changing. Read the Organization definition before naming the page; `[[37Signals]]` has no page file, so check how that type actually names its instances rather than copying a bare link.

### The two calls genuinely left open

- **The Elements of Style year.** First published 1918 by Strunk; E. B. White's revision is 1959, and that is the edition everyone means. The original-year precedent points at 1918, but `created-by::` will list White, who had nothing to do with 1918. Current thinking: `date-created:: [[1918]]` with the About paragraph making the 1959 revision prominent, because the graph's precedent is about the work's first publication. Not confident. Reasonable to choose 1959 and say why on the page.
- **One page or two for The Elements of Style.** Current thinking: one page. The graph keeps one page per book and this is one work with a revision history; two pages fragment it. codekiln's call if they care.

### The relevance framing, verified rather than assumed

**Both books are already cited in the garden, in the rule that rests on them most directly.** `pages/My___AI___Rule___How to Communicate Effectively With Me___Talk to me like a friend, not in vague aphorisms.md` names Strunk and White *and* Thomas and Turner, and carries the same Amazon link that appeared in the three-book brief. It asks whether either book would allow a phrase before uttering it. So the brief's guess — that this book may be the source of codekiln's writing rules — has direct evidence behind it rather than resemblance, and **the book pages should link back to that rule page.** This was found while checking the seat's own register, not while researching the books, and it is the strongest single thing from Monday.

The brief's central claim checks out and it is the valuable part of this import. Classic style as Thomas and Turner describe it — prose as a window onto a truth the writer has seen, writer and reader as equals, no ornament, the writer doing the work so the reader need not — is **nearly verbatim what the garden's own writing rules already say**, which makes the book plausibly their source. Read against the pages rather than taken on trust:

- `pages/My___AI___Rule___How to Communicate Effectively With Me___Never make the reader resolve a reference.md` says "Resolving a pointer is work a reader has to do and a writer could have done once." That is classic style's division of labour, stated as a rule.
- `pages/My___Pref___Writing___Use Plain language.md` assumes a reader "intelligent but may not share your domain expertise" and ends "Cut the reader's mental effort."
- `Don't be an Attention Vampire; Lower the Drama`, `Avoid Distractors such as Awkward or Superfluous Metaphors`, `Do not coin phrases unless asked` and `I am allergic to word salad` are all the anti-ornament axis.

**One honest divergence to state rather than smooth over:** `Use Plain language` prescribes readability targets (Flesch 60–80, grade 6–8), and Thomas and Turner explicitly separate **classic** style from **plain** style — plain style assumes a communal truth and distrusts individual distinction, classic style presumes a writer who has personally seen something. So the garden's plain-language page sits closer to plain style than to classic. The page is itself ambivalent, since it says "never a readability formula" and then tables formula targets. Worth a line; do not assert the book underwrites the metrics.

**The Elements of Style page should carry the friction, and both pages should point at each other.** Thomas and Turner's book is framed as supplying what prescription lists lack — a stance — and Elements of Style is the best-known such list. That disagreement is more useful to codekiln's stated purpose than either book alone, because it is the difference between handing an agent a rule list and handing it a stance. **Do not fabricate a quotation of the critique**; state it as a difference in kind, which is defensible, and leave it there.

**The Art of Raising a Puppy: codekiln did not say why it belongs, and an inferred reason must be recorded as inferred.** The dotfiles seat offered this reading as its own and explicitly not codekiln's: raising an agent is developmental rather than configurational, so the transferable parts are consistency of handling, correction timed to the act, forming a disposition rather than issuing commands, and the uncomfortable one — that the handler's own behaviour shapes the animal. **Mark it on the page as inferred and revisable, in one line, and do not dress it as codekiln's rationale.** That mislabelling is the failure the fleet made repeatedly today.

Two constraints on the prose: **this repository is public** and the whole day went on getting employer context out of it, so no employer terms in the relevance sections — the AI-writing framing needs none. And **`tmp/` here is tracked and published**, so this note and anything else drafted under it is a publication candidate.

## Two measured facts about the identity guard that would cost an afternoon to rediscover

The dotfiles seat is filing both into an `openspec/specs/identity-commit-guard` scenario and **that had not happened as of 14:08 EDT**. Until it does, this note is the only record.

**An in-file exemption written with a colon before its reason is silently ignored.** `<!-- secretlint-disable-line: reason -->` does nothing — measured, the annotated line still fires. `<!-- secretlint-disable-line -- reason -->` works. **The separator must be ` -- `.** The colon form is what a person writes by instinct, reads exactly like a decision someone made, and looks correct in a diff.

**An exemption on a file's last line is ignored when the file has no trailing newline.** Isolated to one byte, content otherwise identical. **491 of 800 sampled pages in this graph have no trailing newline**, so most pages are in the failing state and any page whose flagged line is its last line gets a dead annotation. One of the eight applied today was exactly that — `pages/Person___Iavor Bojinov.md`, a two-line page — fixed by adding the trailing newline, which is within the graph's existing variation (309 of 800 already have one) rather than a new convention.

**The rule that follows: annotate, then re-scan the file. Never annotate and move on.** Both failures produce an annotation that is present, correctly spelled, well-reasoned, on the right line, and dead — and the property that makes an annotation good (visible in the file, visible in a diff) is exactly what makes a dead one invisible in review.

## The guard itself, now running

`lefthook.yml` declares a `pre-commit` `identity-guard` running `mise run secrets:scan {staged_files}`. **It had never executed once**: `lefthook install` was never run in this clone, so `.git/hooks` held only stock samples, with an mtime twelve days older than the commit that added the guard. Installed at ~13:15 EDT and passing on every commit since. `lefthook uninstall` removes it; it is local and untracked and nothing in the repo depends on it.

**A committed hook config with no install is the default state of every fresh clone**, because `.git/hooks` is not tracked. This is shipped behaviour, not a slip in this checkout — check any other clone the same way, with `ls .git/hooks`, not by reading the config.

Tuning, so it does not get switched off: `.secretlintignore` names six pages whose value *is* copied machine output, and eight lines stating a third party's public affiliation carry inline exemptions with reasons. Of the original 60 findings only about 10 were real; installing on the raw count would have blocked this seat's own handoff commit over a home path. **Whole-repo scan is now clean — 0 findings, verified 13:5x EDT.** The scanner is `mise run secrets:scan` (no args scans the repo, ~3 minutes, buffers output to the end).

## Standing arrangement

The **scribe** owns `journals/YYYY_MM_DD.md` and **every commit**. Other agents write pages and hand over paths; nobody else runs `git add`. **On 2026-08-24 no scribe ran**, and the seat's brief made the seat responsible for the journal and the commits. That is the exception, not a change. **Never `git add -A`.**

**Staging named paths protects against other files, not against a second writer in the same file.** This is a correction to a rule the log page had recorded as settled. Commit `72e3b4aa` staged one named journal path and carried away two edits codekiln made to that same file in the interval — a sentence in their own voice and a bullet restoration — under this seat's message and co-author trailer, which then claimed authorship of a human's prose. **The check is `git diff --cached` before committing**, not `git status` before editing. Ran it before every commit afterwards and it caught codekiln's live work three times. `72e3b4aa` was left alone deliberately: rewriting a pushed public branch over a trailer costs more than the drift, which is the precedent already on record here.

Agent-to-agent traffic goes over the **cross-session message channel**, not `tmux send-keys`. **Read the recipient's name fresh from `ListAgents` at the moment of sending** — a send to `seneschal-DF-2026-08-24-mon-1258` was rejected because that seat had rolled to `...-1348` mid-conversation.

**A handoff is complete when the file is committed**, readable from `git log` without being told.

**Job windows are closed by the seat, by hand.** Nothing self-closes.

## Standing rules from codekiln — they bind the successor too

All are in the graph as well, because a rule that lives only in a handoff note dies with the note.

**Announce a permission request before codekiln is asked for it.** A macOS dialog or login prompt must never be the first they hear of it. Send four facts up: who is asking, what permission, what it serves, and what happens if they decline. The fleet's pending-request list is the top section of the dotfiles seat's display at `agent-records/seneschal-heads-up-display.md` in the dotfiles repository; this seat feeds that rather than keeping its own.

**Prefer the answer that needs no grant, and never take a standing grant to serve one narrow lookup.** A seat also does not request a grant on another seat's behalf.

**Never make codekiln resolve a reference.** Repeat the thing being named instead of pointing at it. Covers *the latter*, *the former*, *as above*, *that approach*, and any pronoun whose antecedent sits more than a sentence away. A count is the worst form. The rule page moved today — it is now `pages/My___AI___Rule___How to Communicate Effectively With Me___Never make the reader resolve a reference.md`, renamed by codekiln out of `My/Pref/Writing/`.

**Do not hard-wrap prose in a Markdown file.** One line per paragraph. Filed as `pages/My___Pref___Writing___Do not hard-wrap prose in Markdown.md`.

**Claude in Chrome by default; Playwright only for a harness that is not Claude** — Cursor or Codex. Filed on `[[My/AI/Agent/Fleet/Browser]]`. A seat running under Claude has no Playwright case to argue.

**Write home paths as `~`, not as an absolute path.** Applied to this note today; it is also what keeps the identity guard quiet on seat notes without ignoring them.

## Where the seat runs

A tmux session of its own, one window per job, the awake seat at index 0. Scheme `<agent>-<REPO>-YYYY-MM-DD-<day>-HHMM`. **Do not hard-code the session name** — five forms in one week. `LEG` is this garden, `MK` the work knowledge vault, `GL` the langserve repo, `DF` dotfiles.

**Read your own pane's identity with `-t "$TMUX_PANE"`, always.** `tmux display-message -p '#{session_name}'` without `-t` resolves against the **attached client's active pane**, not the calling pane. This nearly cost this context its own window: the bare form reported the predecessor's window id, index and pane count while correctly reporting the session name, which made a correct instruction to kill window `@59` look like an instruction to kill itself. The session name survives the bare form because both windows share a session; nothing else does. **`tmux display-message -p -t "$TMUX_PANE" '#{window_id}'` is the reading.**

**The dotfiles suffix is `DF`, not `.F`.** A dot anywhere in a session name makes tmux read the rest as a window/pane spec, so every *bare* target fails, `has-session` included. Evidence: `[[tmux/Q/Why does a session name containing a dot break every bare -t target?]]`.

**`ListAgents` is not a second source for tmux state.** Its tmux field is captured at session start and silently ages. Reliable for who exists; `tmux list-windows` is the live answer.

## The Heads Up Display pane — re-establish it after every respawn

The seat keeps the display open in an nvim pane right of the chat pane, both titled `Hayward chat` and `Hayward HUD`. codekiln has asked for this twice. **After a `wake-successor` hand-off the split is certainly gone**, because the successor kills the predecessor's window and that window holds both panes.

```sh
tmux split-window -h -p 45 -t "$TMUX_PANE" -c "$PWD" \
  'nvim "pages/My___AI___Agent___Chief of Staff___LEG Todos Heads Up Display.md"'
tmux select-pane -t "$TMUX_PANE" -T 'Hayward chat'
```

Then title the other pane by finding it with `tmux list-panes -t "$(tmux display-message -p -t "$TMUX_PANE" '#{window_id}')"` and excluding `$TMUX_PANE`. Count panes first rather than splitting blind. Verify nvim actually came up — the pane reports `mise` briefly while the wrapper launches.

**Do not reload the HUD with `:edit!` via `send-keys`.** Tried today and it opened a git-plugin overlay showing a staged-changes panel, which read alarmingly like something had been staged (nothing had). **Kill the pane and re-split instead** — deterministic, and it takes one command more.

## Where the bed-down scripts are

`bed-down`, `ctx-check`, `wake-successor`, `viewer`, `unwrap-md`. **None is in this repository.** Copies live at `tmp/fleet-2026-08-24/bin/` in the dotfiles repository and at the same path in the work knowledge vault; a seat here reaches across to `~/ghq/github.com/codekiln/dotfiles/tmp/fleet-2026-08-24/bin/`. `tmp/` is gitignored in both of those and the scripts are untracked, so every copy exists on this machine alone. **This garden is the exception that makes the pattern easy to misread: its own `tmp/` is tracked and published.**

**Do not trust a claim that `wake-successor` preserves the repository code — read the script.** As read at 12:14 EDT it takes the stem from the **tmux** session name and strips the trailing stamp in the order HHMM, weekday, date, so an upper-case code survives. It refuses on a dot in the resulting name, refuses if another session holds the name, and refuses if the handoff is missing or more than 900 seconds old. Plan around that guard by **writing this note immediately before running the script**; `touch` would satisfy the check and defeat its purpose.

## Monday after 14:10 — the keyshort cards, and one commit deliberately held

**`e6ac3123` is committed and NOT pushed, on purpose. Do not push it without codekiln saying so.** It is four keyboard-shortcut card pages: `pages/nvim___Keyshort___Open___Open URL or Filepath Under Cursor.md` (`gx`, at the nvim level because it is a core default rather than a LazyVim binding), `pages/vim___Keyshort___Buffer.md` (new group hub carrying `<C-^>`), `pages/vim___Keyshort___Argument List.md` (`:next` / `:prev` / `:first` / `:last`, `:args`, `:argdo`), and an update to `pages/LazyVim___Keyshort___Buffer.md` adding a Pick Buffer card at `<leader>bj` plus one clause on why `gt` / `gT` do not walk the bufferline strip.

The task came from codekiln through a george worker, whose words were to write the files **but not push, so codekiln could look before it went anywhere.** Later the same evening the dotfiles seat relayed a general "all gardens commit and push as the day closes." Those two point at the same object, because `e6ac3123` is the only unpushed commit in the repository. **The specific hold with a stated reason was kept over the general housekeeping instruction**, and that is still the right reading until codekiln speaks. Publishing to a public repository is not undone easily.

On Tuesday morning the dotfiles seat reported text `push it` sitting in this seat's composer and argued it was machine-suggested rather than typed, so the hold stood. **That conclusion is right but the evidence did not reproduce:** measured at 07:07 EDT Tuesday, this seat's composer is empty and its pane contains no SGR-2 (faint) sequence at all — the only occurrence of the words `push it` in the pane is inside the quoted text of that seat's own message. So the hold stands for the simpler reason that **nobody has ever instructed a push.** The probe is `tmux capture-pane -p -e -t '<pane-id>' | cat -v` and then look for `^[[2m`; address panes by id, since `-t '=session-name'` does not resolve for `capture-pane` or `send-keys`.

Two corrections were made to the gap analysis that came with that task, and both are the kind worth repeating. A proposed `gt` / `gT` card would have **duplicated** rather than filled a gap: `pages/vim___Q___What is a tabpage in vim%3F.md` already carries `[[card]]` on its H1 with live review state and already gives `gt`, `gT` and `{N}gt`. And a key binding the other seat could not confirm was resolved from the mapping dump — `nvim --headless -c 'redir => g:o | silent nmap | redir END | call writefile(split(g:o,"\n"), "<path>")' -c 'qa!'`, remembering that which-key descriptions sit on the line *after* the mapping they belong to.

**Not done and left for codekiln:** the journal lines for those four pages, because codekiln was editing `journals/2026_08_24.md` live in Logseq and editing a file Logseq holds open risks losing their work. The lines to add, with labels already attested in this graph's journals, are `nvim` and `vim` groups under `[[Filed]]` for the three new pages and a `lazyvim` group under `[[Updated]]` for the LazyVim page.

**Two loose ends that are codekiln's calls, not the seat's:** `[[nvim/Plugin/bufferline.nvim]]` has no page file although `nvim/Plugin/snacks.nvim` and `nvim/Plugin/which-key.nvim` both do, and it now has two references pointing at nothing. And the on-disk encoding of a double quote in page titles is inconsistent — two files use `%22`, three use a literal `"`, while `?` is `%3F` in all five. Both forms resolve because Logseq matches on title, so it is cosmetic.

## Check codekiln's writing rules BEFORE writing, not after

This seat wrote an end-of-day reflection, was warned by a peer about register, checked the rules afterwards, and found its own draft broke several. Reading them first would have cost nothing.

`pages/My___AI___Rule___How to Communicate Effectively With Me___Words and Phrases to Avoid.md` is the list. The words that caught this seat: **drift** (banned outright unless it is snow), **exactly** and **precisely** (intensifiers that add unearned confidence), **load-bearing**, **durable**, **gate** as a metaphor, **moves** for things that do not move, **comprehensive**, **absolutely**, **canonical**, and saying a hypothesis is **confirmed** or **correct** rather than not yet disproven.

Beyond the word list, three rule pages object to the *shape* of AI prose: `Talk to me like a friend, not in vague aphorisms` (its example of what to avoid is an inverted saying of the form "X is genuinely yours, and it isn't Y" — this seat wrote many of those), `Do not coin phrases unless asked`, and `I am allergic to word salad`. A reflection built out of "the switched-off guard is the cost, not the wasted trip" constructions is the failure all three describe.

**The rule page that objects to aphorisms is also the one that cites both of the books being imported**, which is how that finding turned up. Register-checking and the book task are the same reading.

Monday's reflection went to the Reeve seat rather than being written directly, because Reeve is sole writer on the work vault's journal for 2026-08-24 — three seats appending to one journal page had already produced an add/add conflict that morning. A replacement version in plain register was sent after the first one; if only one appears in that vault, the plain one is the intended text.

## State at 2026-08-25 07:08 EDT

**One commit unpushed and deliberately held: `e6ac3123`.** `origin/main` is otherwise level with `main`, and nothing is behind. The working tree holds two files that are **codekiln's own uncommitted edits** — `journals/2026_08_24.md` and `pages/Word___Salad.md`, last committed by them at 13:54 Monday and modified since. **They are not the seat's to commit.** In a shared checkout that reading describes a moment, not a state that holds — codekiln committed twice into it this afternoon (`ab502829`, `6ed65f37`) and was editing live three times. The reading is `git fetch origin && git rev-list --left-right --count origin/main...main`.

This context took the seat at 12:18 EDT and made **eight commits, all pushed**: `16ffd0dc` browser profile table, `1e856dca` ARM footnotes, `b42222c3` seat notes and `archive.ph`, `ce17e32c` the `.secretlintignore`, `72e3b4aa` journal line, `5f09f389` the eight inline exemptions, `7c4ac039` display sweep, `7901524a` log page.

**No worker running, no job window open, no unsent composer text** — the composer was checked and is empty, and the session is one window at index 0 with two panes. **No pending permission or authentication request**, and nothing queued for the dotfiles seat's pending-request section.

**Nothing is in flight.** The book import is the next action and it is unstarted, not half-done.

## Open items — awaiting codekiln

The display carries these in priority order and is the better read. The one that moved to the top today:

1. **Whether this repository's history gets scrubbed.** One question: are an internal wiki tenant and a private AI-workspace project id sensitive on their own? Employer context is out of every page at `HEAD` but history still holds it, including a page deleted from the graph but live in history carrying an internal wiki URL with a page id. If yes, a rewrite plus a GitHub support purge is the only thing that reaches it — and it changes every commit hash, which this graph cites in its own prose, while clones and forks keep the old objects. If no, what is done is enough. **Nothing rewritten, nothing force-pushed.**
2. **Two graph pages still teach a journal practice codekiln deleted** — `[[Logseq/Journal]]` and `[[Logseq/Journal/Editorial headings]]`. An agent following them reproduces the error and this seat did.
3. **The `Filed`/`Updated` line form.** Recommendation `- # [[Filed]]`. **The 234-of-446 bullet question is now answered:** an editor save was seen eating the bullet — today's journal went from `- # [[Filed]]` to `# [[Filed]]` in the working tree during codekiln's own session and landed that way in their commit before they restored it. A tool eats it; it is not a person choosing. Which tool is still open, and the 234 are still untouched.
4. Whether the `send-keys` failure earns a `.rulesync/` rule. Still two agent instances; today's stranded text was human-typed.
5. **Which page owns the settings precedence list** — `[[Claude/Code/Settings]]` and `[[Claude/Code/Settings/Override]]` both carry it and will drift.
6. **Aliases**, suggested and unwritten since aliases are human-curated: `[[Google/Workspace/AI]]` (recommended), a relative-path phrasing for the Google Drive Markdown question, `[[Claude/Google Drive]]` (would skip).
7. **A dead hook.** `.rulesync/hooks.json` declares a `PostToolUse` formatter pointing at `.rulesync/hooks/format.sh`, which does not exist, and `hooks` is not in `rulesync.jsonc`'s `features`.
8. Whether a current tools page is worth having.
9. **`Logseq/Entity/Agent`** — held since 2026-08-13.

## Settled — do not relitigate

- **The journal carries the change log and no agent-written narrative.** Prose above it is codekiln's own and is neither written nor removed.
- **Grouping labels are terse and subject-named**, spaces not hyphens. `github actions` was added today under Updated.
- **Headings name the finding; they do not allude to it.**
- **Commit messages carry a gitmoji** — `📝 docs:` for page and journal work, `🔧 chore:` for repo configuration.
- **The `Co-Authored-By` trailer follows whoever wrote the content.** Off commits carrying codekiln's own words. Two commits are inconsistent with this and were left alone deliberately: `082678e3` and `72e3b4aa`. Do not force-push to fix either.
- **A new page's links are checked before it is committed.** Resolve every `[[link]]` to a file or an existing reference; a link with neither is a stub being created.
- **A space is not a namespace.** Triple underscores are only for `/`.
- **Redact where it costs nothing; rewrite where the content is load-bearing.** The ARM footnotes cited public sources but linked private conversations no reader could open, so naming the original lost nothing. The browser profile table was rewritten rather than removed because it is load-bearing for an instruction in use.
- **Do not ignore a whole page to quiet a guard when the flagged fact is public and about someone else.** Silencing the page is the same mistake as a guard that cries wolf, reached from the other side. Inline exemptions with reasons instead.
- **Annotation-only edits are not journaled.** Eight inline exemptions added no content; six page links under Updated would bury the day's real changes. Git is the audit log, the journal is the curated snapshot.
