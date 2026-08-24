# Hayward — report, 2026-08-24

Seat: chief of staff, `logseq-encode-garden`. tmux session `hayward-2026-08-24`.
Nothing was sent to Myer.

## 1. The six held commits — pushed

The brief's premise was stale. `main` was six ahead of a remote-tracking ref that had
been standing since 2026-08-17; after `git fetch origin` it was **six ahead and thirty
behind**. A plain push would have been rejected.

I did not re-open the push decision. I merged `origin/main` into `main`, resolved the
single conflict, and pushed.

- Conflict: add/add on `journals/2026_08_17.md` — both sides created the file
  independently. Resolved as a union, keeping this seat's narrative blocks and the
  "Nine Characters of Identity" heading, and adding origin's `gh` group under `[[Filed]]`
  and `[[GitHub/CLI/Extension]]` under `[[Updated]]`. Also gave origin's first line the
  leading `- ` it was missing; a bare `# [[Filed]]` is not valid LFM.
- Pushed `2ba1de8d..efef7c68`.
- Safety ref `backup/hayward-pre-rebase-2026-08-24` at `82e07b26`, local only, to be
  dropped at end of day.

## 2. The harness change — recorded in the garden

Pushed as `efef7c68..88c08ede`, five commits.

Filed:

- `pages/My___AI___Agent___Fleet.md` — the five tmux levels and what each is for, the
  spawn recipe, and what the fleet expects of a seat.
- `pages/My___AI___Agent___Fleet___Bed Down.md` — the 200k ceiling with its measurements
  (358k–484k last week, 641k under herdr), what `ctx-check` and `bed-down` each do, the
  fifteen-minute handoff guard, and the scripts' staging path named as staging.
- `pages/tmux___Q___Why does a tmux -t =session target fail in zsh%3F.md`
- `pages/git___Q___Does an ahead-behind count against origin reflect the remote's current state%3F.md`
  — added at Seneschal's request, from first-hand evidence gathered here.

Updated: `pages/My___AI___Agent___Chief of Staff.md` (the seat name moved from window `0`
of `ls-encode-garden` up to the session, `hayward-2026-08-24`), `pages/herdr.md`
(retirement), `pages/tmux___Option___status-left-length.md`, `journals/2026_08_24.md`.

## 3. Two things in the brief that did not survive checking

**`status-left-length 40` is not in `~/.config/tmux/tmux.conf`.** The live global value is
`40`, but that file sets no status option at all — its stated intention is to stay close to
stock tmux, and it holds only terminal features, passthrough, and `update-environment`. The
`40` is a runtime `set -g`, which is server-global and outlives every session **but not the
server**. On the next `kill-server` or reboot the cap silently returns to `10` and long
session names start being cut again. This is the same origin already documented for
`status-left` and `status-right` on this server.

*Open item, not mine to close:* making it survive needs one line in the tmux config, which
is a dotfiles change and goes through OpenSpec. Recorded on the page; not acted on.

**An ahead-behind count is not a fact about the remote.** Covered above and filed as a Q
page. The mechanism worth carrying: the count answers the question it was built for, and a
stale remote-tracking ref hides only the *behind* half, so the output looks complete.

## 3b. A third convention claim that does not hold in this repo

`fleet-conventions.md` says `tmp/` is gitignored, and reasons from that: that a `git add -f`
on a `tmp/` file bypasses the pre-commit identity guard, and that working notes may live
there safely.

**In this repo `tmp/` is not ignored.** `.gitignore` has no `tmp` rule, `git check-ignore`
returns nothing, and two resume docs are already tracked there and public on GitHub. So the
bypass the convention warns about does not exist here — but neither does the privacy it
assumes. Anything written to `tmp/` in this garden is a candidate for publication, and
should be treated as such. This report was scanned for credential-shaped strings before
being committed.

## 4. Decisions taken alone

- Merge rather than rebase: this repo's history already carries `Merge branch 'main'`
  commits, and a merge meant one conflict resolution instead of six.
- Union on the journal conflict rather than picking a side.
- New pages under `My/AI/Agent/Fleet` as a sibling of `My/AI/Agent/Chief of Staff`, since
  the hierarchy belongs to the fleet rather than to any one seat.
- Every wikilink resolved against the live graph before linking. The only unresolved
  targets in what I wrote are established logical pages already used across the graph
  (`[[Zsh]]` 20 refs, `[[Bash]]` 11, `[[Person/codekiln]]` 22, date pages); no new stub
  was created.

## 5. Next

- `backup/hayward-pre-rebase-2026-08-24` dropped after confirming every commit on it is
  reachable from `origin/main`.
- The tmux config line above, if and when someone takes it through OpenSpec in dotfiles.
