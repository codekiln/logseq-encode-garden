# Hayward — report, 2026-08-24

Seat: chief of staff, `logseq-encode-garden`. tmux session `hayward-2026-08-24`. Nothing was sent to codekiln.

## 1. The six held commits — pushed

The brief's premise was stale. `main` was six ahead of a remote-tracking ref that had been standing since 2026-08-17; after `git fetch origin` it was **six ahead and thirty behind**. A plain push would have been rejected.

I did not re-open the push decision. I merged `origin/main` into `main`, resolved the single conflict, and pushed.

- Conflict: add/add on `journals/2026_08_17.md` — both sides created the file independently. Resolved as a union, keeping this seat's narrative blocks and the "Nine Characters of Identity" heading, and adding origin's `gh` group under `[[Filed]]` and `[[GitHub/CLI/Extension]]` under `[[Updated]]`. Also gave origin's first line the leading `- ` it was missing; a bare `# [[Filed]]` is not valid LFM.
- Pushed `2ba1de8d..efef7c68`.
- Safety ref `backup/hayward-pre-rebase-2026-08-24` at `82e07b26`, local only, to be dropped at end of day.

## 2. The harness change — recorded in the garden

Pushed as `efef7c68..88c08ede`, five commits.

Filed:

- `pages/My___AI___Agent___Fleet.md` — the five tmux levels and what each is for, the spawn recipe, and what the fleet expects of a seat.
- `pages/My___AI___Agent___Fleet___Bed Down.md` — the 200k ceiling with its measurements (358k–484k last week, 641k under herdr), what `ctx-check` and `bed-down` each do, the fifteen-minute handoff guard, and the scripts' staging path named as staging.
- `pages/tmux___Q___Why does a tmux -t =session target fail in zsh%3F.md`
- `pages/git___Q___Does an ahead-behind count against origin reflect the remote's current state%3F.md` — added at Seneschal's request, from first-hand evidence gathered here.

Updated: `pages/My___AI___Agent___Chief of Staff.md` (the seat name moved from window `0` of `ls-encode-garden` up to the session, `hayward-2026-08-24`), `pages/herdr.md` (retirement), `pages/tmux___Option___status-left-length.md`, `journals/2026_08_24.md`.

## 3. Two things in the brief that did not survive checking

**`status-left-length 40` is not in `~/.config/tmux/tmux.conf`.** The live global value is `40`, but that file sets no status option at all — its stated intention is to stay close to stock tmux, and it holds only terminal features, passthrough, and `update-environment`. The `40` is a runtime `set -g`, which is server-global and outlives every session **but not the server**. On the next `kill-server` or reboot the cap silently returns to `10` and long session names start being cut again. This is the same origin already documented for `status-left` and `status-right` on this server.

*Closed the same day, not by me.* The seat working `tmux-status-left-spec` added `set -g status-left-length 40` to the chezmoi source for the tmux config and updated the page (`aef93c23`), with an isolated-socket probe and a `-f /dev/null` negative control. The finding stands as measured at 09:18; the page now records the fix rather than the gap.

**An ahead-behind count is not a fact about the remote.** Covered above and filed as a Q page. The mechanism worth carrying: the count answers the question it was built for, and a stale remote-tracking ref hides only the *behind* half, so the output looks complete.

## 3b. A third convention claim that does not hold in this repo

`fleet-conventions.md` says `tmp/` is gitignored, and reasons from that: that a `git add -f` on a `tmp/` file bypasses the pre-commit identity guard, and that working notes may live there safely.

**In this repo `tmp/` is not ignored.** `.gitignore` has no `tmp` rule, `git check-ignore` returns nothing, and two resume docs are already tracked there and public on GitHub. So the bypass the convention warns about does not exist here — but neither does the privacy it assumes. Anything written to `tmp/` in this garden is a candidate for publication, and should be treated as such. This report was scanned for credential-shaped strings before being committed.

## 3c. This working copy is shared, and "clean" is a snapshot

While I was committing the browser page, another seat committed `aef93c23` into **this same checkout** — my commit's parent turned out to be theirs rather than mine. Nothing broke, because I stage named paths; a `git add -A` at that moment would have swept up whatever they had in flight.

So the three facts I reported — default branch, in sync, tree clean — were true when read and can be falsified by a peer seconds later. They describe a moment, not a state that holds. The same is true of any such report from a seat sharing a checkout.

## 3d. One thing I got wrong, caught before close

I wrote five topic-led narrative blocks into today's journal with editorial headings — "Depth Over Detection", "Ahead of What, Exactly", and so on — following `[[Logseq/Journal]]` and `[[Logseq/Journal/Editorial headings]]`, which instruct exactly that.

The seat's own resume note records that codekiln deleted all three such blocks from the 2026-08-18 journal himself, and that headings should name the finding rather than allude to it. Checked against the journals: 08-16, 08-18 and 08-19 are change log only. The one journal carrying an editorial heading is 08-17 — this seat's own, from last week.

Today's journal is now change log only, grouped under `agents` / `git` / `tmux` and `agents` / `herdr` / `tmux`, matching 08-18. One page heading was reworded from a metaphor to the finding it names.

The underlying problem is filed as open item 11 in the resume note: the two graph pages still teach the deleted practice, so the next agent reading them reproduces this. Fixing them is a convention change and codekiln's call, so it is recorded and not acted on.

## 3e. The browser page, corrected the same day

The page first said no invocation was verified. That was true when written and wrong within the hour: `claude --chrome -n '<name>' --permission-mode auto '<brief-pointer>'` reaches an SSO-gated source with no login handshake, no debugging port, and without disturbing the running browser — demonstrated against a protected Splunk index.

The page now leads with that as the **first** route and demotes Playwright to the fallback. The one-process-per-profile-directory constraint stays, relabelled as a fact about the Playwright route rather than about the source; two seats had reported a source blocked when only that route was.

Which profile `claude --chrome` attaches to is recorded as **unsettled**. A session that answers proves a session works, not which profile it holds, and the page asserts neither way.

Added with it: an absence is a dated claim like any other. A seat recorded `--chrome` unavailable after four classifier denials; the identical command worked first try after bedding down. So bedding down is itself a retry, and an absence should be written the way a count is — what was tried, when, and what the failure looked like.

## 4. Decisions taken alone

- Merge rather than rebase: this repo's history already carries `Merge branch 'main'` commits, and a merge meant one conflict resolution instead of six.
- Union on the journal conflict rather than picking a side.
- New pages under `My/AI/Agent/Fleet` as a sibling of `My/AI/Agent/Chief of Staff`, since the hierarchy belongs to the fleet rather than to any one seat.
- Raw email addresses left out of the browser page. This repo is public, neither address appears anywhere else in it, and the profile *directory* name is the whole handle an agent needs — the addresses would have been a new publication for no operational gain.
- No browser work taken. There was none to do here, and taking some to test an invocation would have contended for `Default` against codekiln's own open window.
- Every wikilink resolved against the live graph before linking. The only unresolved targets in what I wrote are established logical pages already used across the graph (`[[Zsh]]` 20 refs, `[[Bash]]` 11, `[[Person/codekiln]]` 22, date pages); no new stub was created. `[[Chrome]]` was caught and de-linked before commit — it had no page and no other user in the graph, so it would have been one.

## 5. Second context window — graph work the day's findings had earned

The day's findings were sitting in `tmp/` notes rather than in the graph. Three went in, and one of them was wrong on the way.

**The dot-in-a-session-name finding was re-run before publishing, and needed to be.** The `.F`-versus-`DF` claim had been tested only against targets naming a window explicitly, `session:0` — the single target shape a stray dot leaves alone — so it passed on every input it was given. Re-run on an isolated socket with a dot-free control and two dot positions, the mechanism is broader than the note said: a dot *anywhere* in the name is read as a separator, `has-session` fails the same as the rest, and the message moves with the dot (`hay-.F` reports a missing pane, `hay-D.F` a missing window named `hay-D`), so two instances of one fault do not look alike. Filed as `[[tmux/Q/Why does a session name containing a dot break every bare -t target?]]` with the table on it, and pointed at from `[[tmux/session/Name]]` and `[[My/AI/Agent/Fleet]]`.

**Two claims on `[[My/AI/Agent/Fleet]]` were corrected.** The session scheme now carries the repository suffix and the no-dot constraint. The `tmp/` line now asks the reader to run `git check-ignore` per checkout instead of asserting an answer that is false here — section 3b's finding, which had reached the report and the display but not the page that states the convention.

**The declaration was a third page teaching the deleted journal practice.** Section 3d named `[[Logseq/Journal]]` and `[[Logseq/Journal/Editorial headings]]`; the seat's own declaration instructed it in two places as well, which is the page the next occupant reads first. That the journal carries the change log and no agent narrative was settled on 08-18 and recorded, so the declaration was brought into line rather than escalated — with both halves, including that prose above the change log is codekiln's own and is neither written nor removed. The two pages that *state* the convention are untouched and remain the open item.

Also filed: the chief-of-staff log page for the day, which is where the durable lessons moved to. The resume note had been carrying them, and the scribe declaration is explicit that the note holds state while the log space holds what outlasts it.

Swept the Heads Up Display. Its own state line had quoted an ahead-count that the commit writing it invalidated, which is the graph's recurring error in miniature; it now names the command rather than a reading.

Three commits, pushed. `9e8d0aae..def9594a`.

## 6. Decisions taken alone, this context

- Corrected the declaration rather than escalating it, on the grounds that the underlying decision was already on record and only the convention pages are codekiln's to change.
- Left the 24 slash-form date links on pages written today alone. `[[Logseq/Date]]` calls `[[YYYY/MM/DD]]` acceptable and merely not preferred for new writes, so rewriting committed ones is churn. New writing uses the journal form, `[[YYYY-MM-DD Ddd]]`, which is the form that actually reaches the day's journal.
- Left the peer seat's `tmux/Option/pane-border-*` pages alone despite their carrying the same date form. They are that seat's work in a shared checkout.
- Fixed two faults in the resume note itself: it misgendered codekiln twice, and it carried a bare SHA against the rule it states two sections earlier.

## 7. Next

- `backup/hayward-pre-rebase-2026-08-24` is gone; nothing references it.
- The tmux config line above, if and when someone takes it through OpenSpec in dotfiles.
- Waiting on codekiln: the two convention pages, and the nine other items on the display.
