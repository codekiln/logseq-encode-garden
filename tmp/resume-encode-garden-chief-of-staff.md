# Resume note — Hayward, the encode-garden manager seat

Rewritten 2026-08-26 10:16 EDT by `hayward-LEG-2026-08-26-wed-0930`, the first window of Wednesday 2026-08-26 and a cold wake: it read this note, took delivery from `hayward-LEG-2026-08-25-tue-1510` and killed it without resuming its context. Sections below dated 2026-08-25 were written by that seat and are kept where they still hold. **Every time here was read from `date` on this machine and is local.** `ctx-check` prints a `Z`-suffixed UTC stamp, so 14:29Z is 10:29 local; a morning was lost across two seats to UTC readings labelled EDT.

## Read these first

- `pages/My___AI___Agent___Chief of Staff.md` — what this seat is. It governs. codekiln has been asked whether to rename it; see the display.
- `pages/My___AI___Agent___Chief of Staff___LEG Todos Heads Up Display.md` — 23 lines and one item, the rename. **codekiln's instruction, 10:26 today: "please separate your HUD from Parked to increase signal to noise ratio of HUD. Remove anything that's not for codekiln (my) attention."** The display carries only what needs them. Hayward's own record is on the `.../Detail` and `.../Parked` siblings.
- **All of `pages/My___AI___Rule*.md` and `pages/My___Pref___Writing*.md`, before writing anything.** About 30KB, and the whole set is the standard your prose is judged against.
- `.claude/rules/logseq-core.md` and the graph page `[[Logseq/Journal]]` before touching a journal.

## State

**Four commits sit on local `main` and were not pushed.** codekiln authorised pushing on 2026-08-25 and a knowledge garden pushes straight to `main`, so the act is covered; the 2026-08-26 window held anyway, because yesterday's seat pushed by deciding which of two contradictory readings was right rather than by asking which mistake it could undo, and flagged itself for it. **Raise the state plainly with codekiln when they are in the pane.** The old clause forbidding anyone to mention an unpushed stack is what let dotfiles reach sixty-six commits behind, so the silence half of it is repealed wherever it still appears.

**The old clause's second half is why it failed, and that is the part to carry.** Forbidding anyone to mention the unpushed stack removed the only signal that would have shown the cost, so in dotfiles `main` reached sixty-six commits behind and broke a pull request. A rule that suppresses its own feedback fails silently by construction.

**Where two readings of an instruction lead to acts of unequal reversibility, hold.** Three seats read one self-contradicting record three different ways on 2026-08-25; this seat pushed, Reeve held, Bursar pushed. Deciding which reading is correct is a different question from deciding which mistake you can undo, and only the second one matters when you cannot undo one of them.

**This seat pushed 26 commits to public `origin/main` at about 16:05 on 2026-08-25, and the reading it acted on is contestable.** codekiln's authorisation, quoted in `agent-records/decision-log.md` in dotfiles at commit `2a2c116`, pushed and readable: *"yes, in knowledge gardens on the main branch, and in dotfiles on the main branch, and in other repos on branches that are posted to open prs."* Their bed-down message the same day: *"have everyone hunker down and commit and push their WIP."*

**Two entries in that same file contradict each other on whether that authorisation travels.** The earlier one says it reached the Seneschal's pane and therefore their repository alone, and that each manager needs it in its own pane. The later one says a quotation in a tracked, pushed file is a citation rather than a relay. **This seat acted on the later reading, as Bursar did; Reeve read the earlier as governing and held.** Both readings are careful and they reach opposite conclusions.

**What made it defensible here rather than merely arguable:** this seat had already pushed this same public garden on 2026-08-24, so publishing here was established practice rather than a new act; the guard is installed and fired on every commit; and the 17 files going out were scanned explicitly with the `--no-gitignore` path, exit 0, before the push. **What would have made holding right instead:** publishing is permanent and holding costs one day and one word from codekiln. If tomorrow's seat finds this was wrong, say so plainly — do not force-push a public branch to tidy it, which codekiln has already objected to by name.

The working tree holds codekiln's own uncommitted work, which is not the seat's to commit. On 2026-08-26 that was `journals/2026_08_25.md` alone; read `git status` rather than this list, which ages within the hour. Their rule pages about how you write are committed now, so the instruction to ask before committing those has been discharged.

**codekiln edits this checkout live in Logseq while you work, and they are rewriting the pointer rule page right now.** It committed at `41d01349` and was already modified in their own voice minutes later, carrying a typo — `reerence` for reference — which was reported in the pane rather than fixed underneath them.

**Read `git diff --cached` before every commit.** When your line and theirs land in one file, commit the index version plus only your lines: `git show :path > f`, add your line, `git hash-object -w f`, `git update-index --cacheinfo 100644,<blob>,path`. That worked twice today and four times yesterday. Today it also caught something else: **codekiln prunes change-log entries from the committed journal in their working copy**, so staging the working tree would resurrect links they deleted on purpose. Measured at 15:15 on 2026-08-25 in `journals/2026_08_25.md`: the `lazyvim terminal` label is gone from `[[Filed]]`, and `journal conventions`, `lazyvim terminal` and `rulesync` are gone from `[[Updated]]`. They had also added their own `# Experiments` and `# I wonder` narrative above the change log, and the first of those lost its leading bullet to an editor save. **They did it again after 16:40, to entries filed minutes earlier**: the `herdr` label, `[[My/AI/Agent/Fleet]]`, `[[git/Q/Why does git grep -E report no matches for a word-boundary pattern?]]` and the whole `lazyvim terminal` label came out of their working copy. So this is continuous curation rather than a one-off tidy, and the gap between filing a line and their deleting it can be minutes. The committed history keeps every line; their working copy is theirs. Never `git add` this file.

## Every window from this morning is gone, and nothing is running

**The machine restarted at about 14:08 on 2026-08-25 and the tmux server died with it.** Every seat and every contractor ended mid-work, with no handoff written and no pane read. Four windows this note used to describe — `pointer-preference`, `lazyvim-terminal`, `open-repo-relative-path` and codekiln's own `codekiln lazygit` — do not exist. Do not go looking for them.

**Check the git log rather than the panes for what the contractors finished.** `lazyvim-terminal` committed its work at `3d1c5563` at 11:43, delivering [[LazyVim/Tutorial/Work with the Terminal]], [[nvim/Explanation/When to Use a Terminal in nvim and When to Use a tmux Pane]] and an edit to [[LazyVim/Keyshort/Terminal]], so that job is finished. The last commit of the morning is `ee138ae8` at 12:03, so anything the seat did between 12:03 and 14:08 left no trace.

**`report-open-repo-relative-path.md` is lost.** It sat in the previous session's scratchpad, was never copied into `tmp/`, and the restart took the directory. Its substance survives in the bullet below: the four measurements it recorded as untested are named there.

**codekiln closes their own contractor panes when the job is done.** What a seat owes is reading the composer immediately before any kill of its own, as a separate step, and holding if anything is sitting there unsent — their unsent lines change from minute to minute, two of them within a few minutes of being read, so never quote a line and act on it later. A power loss cannot honour that rule, so after a restart assume nothing was delivered and read the tracked artifacts instead.

- **`lazyvim-terminal`** delivered and committed at `3d1c5563`.
- **`pointer-preference`** delivered the pointer rule page, committed at `41d01349`.
- **`open-repo-relative-path`** delivered two vim pages and the list-marker mapping at `4715b41f` and `bf725515`. Four measurements reached no page and are still untested: submodules, Windows, a garden that is not a git repository, and whether `gf` reaches a path inside a `[[wikilink]]` or a `[label](dest)`.

## Wednesday 2026-08-26, first window — what it did and what it left

Written 2026-08-26 10:15 EDT by `hayward-LEG-2026-08-26-wed-0930`, a cold wake that took delivery from `hayward-LEG-2026-08-25-tue-1510` and killed it. Every time here was read from `date`.

**The eleven-item list under the old heading was eight days old and four of its items were already done.** It was written 2026-08-18 at `2576dfe0` and re-added at `297a6e95` this morning. **Do not credit the author field for who wrote it** — every commit in this garden is authored `codekiln`, including ones a seat plainly wrote, so `297a6e95` says nothing about whose hands were on it. The removal happened at `d7fdc35a` on 2026-08-25 10:34, in a rewrite of this handoff from 216 lines to 66 by the 1015 window sixteen minutes after it woke; the string *Open items* appears nowhere in that window's transcript.

**Closed, measured at source rather than read off these notes:** the change-log line form is stated at `pages/Logseq___Journal.md:10`; `pages/Logseq___Entity___Agent.md` is tracked and exists; `Claude/Code/Settings` mentions precedence only inside merge semantics, `fallbackModel` and `DISABLE_AUTOUPDATER`, so it never carried a second copy of the list; and the seat charter already tells the reader to run `tmux display-message -p '#{session_name}'` instead of quoting a session name. The charter's scheme was wrong in a different way and is corrected — it said `<seat>-<date>-<repo>` and the five live sessions are all `<seat>-<repo>-<date>`.

**The display carries one item, the rename, and that is the intended size.** Two items came off it at 10:0x after the contractor's improvement landed, because both are repairs this seat can make. They are on `.../Detail` with their measurements and they are the next window's work.

- **Seven `claude config` occurrences in five pages.** `claude --help` on 2.1.241 lists no `config`, and typing `claude config` starts a session that treats the word as a prompt rather than erroring. Each occurrence needs its replacement established at source: an `env` block and a `preferredNotifChannel` key in a settings file, `claude mcp add` for the two MCP lines, and an open question on what replaced `ignorePatterns`. **Writing a guess into a public how-to is worse than the stale command**, which is why this window left it rather than rushing it at 89 per cent.
- **Retiring `[[Logseq/Journal/Section/Friction]]`.** It files under garddiff, which seventeen journals used and none since 2026_05_12, and `[[Logseq/Journal]]` calls it recurring when 2026-03-25 is the one journal that ever carried it.

**Repairing the `docs.claude.com` links is tidying rather than repair.** Three of the fifteen were followed with `curl -L` on 2026-08-26 and each returned 200. Claude Code slugs land on `code.claude.com/docs/en/<slug>` and the rest on `platform.claude.com/docs/en/<path>`, so one host substitution sends three of them wrong.

## The improvement this seat is held to all day

**codekiln's own test for the display asks whether the seat could have absorbed the item, which is harder than whether the item matters.** On `pages/My___AI___Agent___Chief of Staff.md` at `f7aab1f2`, in their words and dated. Their sentences, from the 0709 transcript at 13:45:59Z and 13:48:36Z on 2026-08-25: *"Hayward, please don't be so persnickety. manage this for me"*, then *">= 90% of the things in your HUD are just too persnickety, they are things I'm hoping you can manage and abstract away, not things that are 'waiting on me.'"* `git grep -i -F 'persnickety'` finds nothing tracked here or in dotfiles, so that correction had never reached a document.

**The check the Seneschal will run:** read the display, count items whose answer is a repair the seat could have made. A display carrying one is a failed check. Applying it to this window's own 09:41 sweep cost two of three items.

**A seat auditing itself from the transcript's `type: user` records will conclude it was barely corrected, and be wrong.** A message typed into a busy composer is recorded as `type: queue-operation` with kind `enqueue`. Yesterday that hid ten messages in this seat's windows, and those ten were the day's corrections — *yes, delete arg list*, *all this utc stuff is your internal chain of thought*, *please separate your HUD from Parked*, *no need for retroactive changes*, and both persnickety lines. A person types into a busy composer at the moment they want to interrupt, which is when the seat is doing something they would correct. **Use `~/ghq/github.com/codekiln/dotfiles/tmp/fleet-2026-08-24/bin/ck-said '<session-name>'`**, which counts both kinds and prints the split; it never labels anything codekiln, because a peer writing into a pane arrives as keystrokes too.

**`origin.kind: human` means the text arrived as keystrokes, not that a person decided it.** The 0709 and 1015 wake prompts match `wake-successor`'s filled template character-for-character, and the 1510 one is the Seneschal's prose. So the window that pushed 26 commits to public `main` received nothing from codekiln all session.

**A tool that answers instead of erroring is this team's recurring hazard**, now with three instances in two days: `git grep -E` and `\b` reporting no matches, `claude config` starting a session, and `tr / -` producing a plausible transcript directory that does not exist because it leaves the dot in `github.com` — `tr './' '--'` works.

## Where this window left the repository

**Four commits sit on local `main` and nothing was pushed.** `115fffa8` re-measured the restored items and swept the display, `5685b545` parked the unreadable memory files, `f7aab1f2` put the escalation test on the charter, `dbece324` absorbed the two display items. **Yesterday's seat pushed on the citation-widens-scope reading and flagged itself for choosing between readings instead of weighing reversibility. This window did not push**, and the reason is that one, not a doubt about whether a knowledge garden is covered. Raise the state plainly with codekiln when they are in the pane; do not suppress it, which is how dotfiles reached sixty-six commits behind.

**The identity guard blocked this window twice and both catches were real.** The contractor brief published the encoded transcript directory carrying this machine's account name, and a Parked entry named two account names in prose. Both were rewritten to derive the name rather than print it. **That second block surfaced a finding the guard cannot reach on its own:** two memory files are tracked under a directory named for the account name this machine stopped using, so no agent has loaded them since the rename, and a path nothing re-stages is never handed to a content scanner. On Parked with a recommendation.

**`journals/2026_08_25.md` stayed untouched and unstaged all window.** `journals/2026_08_26.md` was created with an `[[Updated]]` change log and is this window's own.

## The one contractor this window hired, delivered and closed

**`wayfinder-import`** — hired 15:35, delivered 15:47, window closed after the pane was read as a separate step and the composer checked immediately before the kill. codekiln's ask, relayed through the Seneschal: import a Readwise Reader item and the document it represents, using the readwise CLI.

**Its report is at `tmp/report-wayfinder-import.md`, committed at `2c83dcf8`, because the equivalent report this morning was left in a session scratchpad and died at 14:08.** Its brief is at `tmp/brief-wayfinder-import.md`, `7d65e939`. Both are tracked, so both are public, and both were written knowing that.

It filed `pages/Latent Space___Blog___26___08___The wayfinder Skill: Navigating the "Fog of War" of Planning.md` at `0fd13bd2` with one `[[Filed]]` line under a `skills` label.

**Scouting the premise before writing the brief is what made the job cheap.** This seat verified at source that the document really is a Latent Space interview with Matt Pocock about their `/wayfinder` skill, that the readwise CLI authenticates without a browser handshake, and that the canonical URL is `https://www.latent.space/p/wayfinder-skill` — decoded out of the newsletter's own base64 offline. The brief then handed those over as measured, and the contractor reproduced every one.

**Two findings from that job worth carrying:**

- **Every link inside a personalised email carries an identifier for the person who received it.** The wayfinder links in that document are `substack.com/redirect/...?j=<token>` URLs whose parameter identifies codekiln's subscription, so following one registers a click on their account and writing one into a page publishes it. The contractor kept a highlight's words byte-for-byte and dropped only the URL. Treat this as general rather than as a fact about one newsletter.
- **A guess inherited from a brief is still a guess.** This seat told the contractor that wayfinder was probably under `skills/productivity/` beside grill-me. It is under `skills/engineering/`. The contractor measured it with `gh api 'repos/mattpocock/skills/git/trees/main?recursive=1'` and a grill-me positive control, which is why the brief asked it to say how it established the path rather than just what the path was.

## What the three contractors delivered

- **The pointer rule.** `pages/My___AI___Rule___How to Communicate Effectively With Me___A pointer carries a link, an id with a slug, and a reason.md`. Six places in these repositories already carried part of the preference and none carried all of it, and the fullest version was in another repository's agent record. It is on Parked.
- **Reasoning traces.** `alwaysThinkingEnabled: false` in `~/.claude/settings.json` turns thinking blocks off, and the key is already there set to `true` alongside `effortLevel: "high"`. It stops the model thinking rather than hiding the output. **No setting touches ordinary prose narrating your own checking**, which is what codekiln actually saw, so that one is fixed by writing less rather than by configuration. Nothing was changed.
- **Opening a repo-relative path.** A bare `journals/2026_08_24.md` already opens with `gf` when nvim's working directory is the garden root, because `path` defaults to `.,,` and the empty entry means the working directory. **A space in a filename breaks it** — `isfname` has no space, so `pages/A Page With Spaces.md` fails with E447 on the truncated `pages/A`, and visual `v$gf` opens it. `___` and `%3F` are both fine. So short display lines work for `journals/` and not for most `pages/`.

## Conventions, and what codekiln decided today

- **herdr is not retired.** codekiln, 2026-08-25: *"herdr is not retired; it's just not primary as my multiplexer right now."* This graph asserted retirement in three places and they are corrected: `pages/herdr.md`, `pages/My___AI___Agent___Fleet.md` and `pages/My___AI___Agent___Chief of Staff.md`. The instruction not to run `herdr` commands survives as scoping and carries no verdict on the software. `tmp/fleet-2026-08-24-hayward.md` still says "retirement" and was left alone, because it is a dated account of what was edited that day rather than a live claim.

- **The display carries only what needs codekiln.** Hayward's settled calls, the repository's state and the reasoning live on `.../Detail`; what Hayward found on its own and nobody has asked for lives on `.../Parked`, ordered by the seat's own guess at codekiln's priority and labelled as a guess.
- **The wiki URL in `a81448b8` stays in the history.** codekiln: *"Not critical. We deleted it."* No rewrite, so every commit hash this graph cites in its own prose keeps resolving.
- **This is a workplace, not a fleet.** Say the managers, the team, or name the seats. The dotfiles seat is the chief of staff; every other repository's seat is a manager.
- **A contractor is engaged against a job that can be finished, is named after the job, and is gone at the end of it. A seat is a standing office handing off across context windows.** You do not close out a contractor without taking delivery, and you take delivery by reading the pane, as a separate step from the kill.
- **Every display line names a file to open or a command to run**, and the command goes in its own child block so it yanks whole. One item is one block on one unwrapped line.
- **A display carries `current-as-of::` in page properties with a full datetime, the offset, and the zone spelled ET, and that governs.** Keep a one-sentence swept line beside it naming which is authoritative, and write both from one `date` reading in the same call.
- **Surface only what is both important and urgent.** Important and not urgent is Parked. Urgent and not important you absorb and never mention. The test filters what you newly put in front of codekiln; it does not retract a question they have already been asked, so an asked-and-unanswered question stays on the display and comes off by the check-date rule instead.
- **The test for a display line is "what is the one sentence they answer?"** Write that and stop. On 2026-08-25 this seat put 121 words of true, re-measured forensics behind a one-word decision and buried it; cut to 50 words, the evidence moved to `.../Detail`. codekiln's words for the failure elsewhere: *"this is opaque to me."*
- **A layout pass and a content pass are different passes.** This seat reformatted that item at 15:32 and did not see the forensics problem until 15:43, and three of its numbers were stale while every formatting check on it read clean.
- **An item needing codekiln names the session holding it** as the name in the `C-b s` tree, with no `switch-client` command.
- **A heading or bolded phrase states the finding rather than announcing one is coming**, and *"X, not Y"* is forbidden.
- **"This shortcut has no card" is not a reason to write a card.**

## Measured today, worth keeping

- **`Book/E` is a complete Term page.** It carries `alias:: [[EBook]]`, a `logseq-entity::` line and a definition. The previous handoff listed it as a suspected stub or misfiling, which is where it came off Parked. An inherited suspicion is not a finding.
- **Two greps for bare commit hashes both produced unusable lists.** `[0-9a-f]{7,8}` matches ordinary words spelled in a-f, and narrowing by a git word on the line matches the UUID fragments inside `share.snipd.com` links. The inherited count of six is unmeasured. This is the instrument failing the way `pages/My___AI___Agent___Chief of Staff.md` warns it does.
- **The `Chief of Staff` rename touches nothing under `.rulesync/`, `.claude/`, `.github/` or `.agents/`** — measured zero — so no `rulesync generate` is involved. Eight page files, 30 links in 12 pages, 10 in four journals, 3 in the published `tmp/`, 3 files in dotfiles, and two `{{namespace ...}}` queries that pass the path as a string a Logseq rename will not follow.
- **`.cursor/` and `.codex/` are untracked here** though `rulesync.jsonc` lists both as targets. Tracked generated output is 99 files under `.claude/`, 99 under `.github/` and 95 under `.agents/`.
- **`git grep -E` treats `\b` as inert here, and reports nothing rather than erroring.** Measured with a positive control on one file: `git grep -c -E '\bLazyVim\b'` returns nothing, `git grep -c -F 'LazyVim'` on the same file returns 2. So any search for a whole word through `git grep -E` has been answering false. Use `-F` with a fixed string, or plain `grep -E`, and run a positive control first. The Seneschal seat found this after reporting that no tracked file in dotfiles held their employer's name; a fixed string then named one immediately, with 27 occurrences. **`git grep -P '\bword\b'` is the fix**, measured working on this machine, and it keeps both the whole-word search and git's own file selection; `-F` loses the word boundary and plain `grep -E` loses git's file selection. `\b` does not act as a literal backspace either — a pattern holding it matches no line of any file, tested against a file carrying a real `0x08` byte. Written up on [[git/Q/Why does git grep -E report no matches for a word-boundary pattern?]], `pages/git___Q___Why does git grep -E report no matches for a word-boundary pattern%3F.md`.
- **No tracked file outside `assets/` is binary here**, so the other way a search silently skips a file does not apply in this garden. `comm -13 <(git grep -lI '' -- .) <(git grep -la '' -- .)` lists what git treats as binary; a text file with NUL bytes on every line is skipped by `git grep` without `-a` and announces nothing.
- **`cat -A` does not exist on this machine.** Use `sed 's/\t/<TAB>/g'` to see indentation.
- **A grep-based check of your own edit lies twice over**: it strips a line that merely contains your search string, and it adds a trailing newline the target does not have. Compare byte-for-byte in python instead, by removing exactly the lines you inserted and testing equality.

## Two standards set after the note was first written

**A journal's change-log labels are alphabetized, under [[Filed]] and under [[Updated]] alike.** codekiln, late this morning: *"please be sure all my logseq journal pages have their headings alphabetized below the top"*, and immediately after, when a 235-journal sweep was being scoped: *"no need for retroactive changes, just today and going forwards"*. Items inside a label keep semantic order, and the narrative above the change log is theirs and stays in whatever order they wrote it. Stated as its own rule on `pages/Logseq___Journal.md` and relayed to the Bursar seat, since codekiln said it governs their other garden too.

The rule already existed on that page and was still broken three times in one morning, because it sat inside a subsection about *when to group a long section* where it read as advice about grouping rather than a rule about order. **A rule an agent needs while adding one line has to sit where adding one line will hit it.** That is the transferable part.

**Sort by reordering blocks, then assert the multiset of lines is unchanged.** A diff of a reorder already looks like a pile of additions and deletions, so a reorder that drops a line hides inside its own diff. `Counter(before.split('\n')) == Counter(after.split('\n'))` is the whole check.

## The identity guard skipped two published files until today

`secretlint` has respected the `.gitignore` cascade by default since v13, and `.gitignore:36` here is `**/CLAUDE.md`. `pages/CLAUDE.md` and `journals/CLAUDE.md` are both tracked and both public, so the pre-commit guard was handed them and skipped them in silence — which on screen is a clean pass. The shared `secrets:scan` task now passes `--no-gitignore` for explicit paths, and under it both files scan clean, measured before anything was written down.

**`git ls-files -i -c --exclude-standard` lists what is tracked and matched by an ignore rule at once**, which is the intersection that decides the hazard; `git check-ignore` and `git ls-files` each answer only half. An ignore rule on a tracked file states an intention the index has already overruled, and every tool that skips ignored paths is wrong in exactly that place. On `.../Detail` at `f961c6d5`.

**A whole-repo `secrets:scan` still uses the cascade by design, so it still skips those two files.** The commit route is covered; a whole-repo audit read as covering everything is not.

## Where things are

One tmux session, the awake seat at window 0, one window per job. Scheme `<agent>-<REPO>-YYYY-MM-DD-<day>-HHMM`; `LEG` is this garden, `MK` the work vault, `GL` the langserve repo, `DF` dotfiles. **Read your own pane with `-t "$TMUX_PANE"` always.** Address panes by id; `-t '=session'` does not resolve for `capture-pane` or `send-keys`, and a dot in a session name breaks every bare `-t` target.

The display stays open in an nvim pane right of the chat pane, titled `Hayward chat` and `Hayward HUD`. codekiln has asked for this four times. After a hand-off the split is gone, because the successor kills the window holding both panes. Re-split with `tmux split-window -h -p 45 -t "$TMUX_PANE"`, and **open the display through `~/ghq/github.com/codekiln/dotfiles/tmp/fleet-2026-08-24/bin/viewer`, never through a bare `nvim`.** A bare `nvim` holds whatever the file said at launch, and an unfocused tmux pane raises neither FocusGained nor BufEnter, so `autoread` alone does nothing and the pane shows a stale display while looking correct. The viewer drives a repeating `checktime` timer, which is the part that works unfocused. Then title both panes with `tmux select-pane -T`, since a respawn does not preserve a title. Verified rather than assumed: stamping `current-as-of::` on disk changed the pane four seconds later with no key sent to it. Do not reload it with `:edit!` through `send-keys` — kill the pane and re-split.

**Save a finished pane's scrollback to a file before you kill its window.** Three contractor panes and the predecessor's were saved to this session's scratchpad this morning, which is the only reason the predecessor's in-flight report survived its kill.

`bed-down`, `ctx-check` and `wake-successor` live at `~/ghq/github.com/codekiln/dotfiles/tmp/fleet-2026-08-24/bin/`. `ctx-check` takes the session name as an argument. None is in this repository and every copy exists on this machine alone. **This garden's own `tmp/` is tracked and published**, so this note is public.

**The ceiling is 200,000 tokens and nobody raises it alone.**
