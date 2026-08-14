# Resume note — Hayward, the encode-garden chief-of-staff seat, 2026-08-13

Written for a successor with none of this context.

## Resume this session

```
claude --resume encode-garden-hayward
```

The seat is named **Hayward**; `pages/My___AI___Agent___Chief of Staff.md`
explains what the name means and why it belongs to the seat rather than to a
session. It answered to `encode-garden-chief-of-staff` for most of 2026-08-13
and was renamed late in the day, so anything written earlier — transcripts,
other agents' notes, commit messages — may still address it by the old name.

herdr workspace `w2` (label `encode-garden`). Two tabs live: `hayward` and
`scribe` (`encode-garden-scribe`, resumable by the same `--resume` form under
its own name).

## Read these first

- `pages/My___AI___Agent___Chief of Staff.md` — this repository's declaration of
  what a chief of staff is *here*: the docket, what "done" means, which subagent
  shapes this repo uses, the commit policy and why, and what gets settled versus
  escalated. Read it before operating.
- `pages/My___AI___Agent___Chief of Staff___Log___26___08___13 Thu.md` — what the
  first day of the role actually taught. Several sections are corrections to
  earlier claims on the same page.
- `CLAUDE.md` and `.claude/rules/logseq-core.md` — how this graph works. They
  govern.

## Repository state at wrap-up

Committed and pushed, working tree clean, `main` level with `origin/main`.
44 commits today, 56 new pages. Nothing held in a scratch directory; this repo
has no gitignored `tmp/` — this file is committed.

## Standing arrangement

`encode-garden-scribe` owns `journals/YYYY_MM_DD.md` and **every commit**.
Other agents write pages and hand it the paths; nobody else runs `git add`.
Several agents and the human share one checkout, which is why staging is
monopolised. It stages named paths only, never `-A`, and stages before reviewing
with `git diff --cached`.

Agent-to-agent traffic goes over the **cross-session message channel**, never by
prompting a pane. Address by name *and* the listing's reference, read fresh at
the moment of sending. A pane's input box may hold a machine-generated
suggestion that looks like typed input; it is not the human and is not a reason
to wait.

## Open items, with owners

**Awaiting the human — nobody should act on these unasked.**

1. **`Logseq/Entity/Agent`** — whether to create the entity type for the 35
   `Person/Steve Yegge/Agent/*` pages filed today. Deliberately held: creating a
   type sets a graph convention and 35 pages would become its instances. The
   pages carry no `logseq-entity::` line, so adopting them later is a separate
   mechanical pass and should be scoped as its own work item.
2. **The journal's "agent supervision" label** — one of five grouping labels in
   today's `[[Filed]]`/`[[Updated]]` sections. It is the scribe's word, not his,
   and `[[Logseq/Journal]]` says grouping labels are chosen with him. Cheap to
   rename.
3. **Aliases suggested and not written**, since aliases are human-curated here:
   `[[Chief of Staff]]` on the declaration; `[[The Continuous Thunderdome]]` and
   `[[Model Welfare for Agentic Engineers]]` on the two Yegge essays;
   `[[Person/Steve Yegge/Agent/Spider]]` on the Lark page; two on the herdr
   explanation pages.
4. **An `Anthropic/Model/Claude/5/Opus` stub** — would let the Yegge fleet pages
   link the model the way the crew pages link Fable. Not created because a model
   stub wants a `tags::` line and that attribute is his.

**Queued work, briefed but not started.**

5. **A page for `[[gh/dash]]`** — he asked for this and it arrived at wrap-up, so
   it was not started. The link has dangled since 2026-04-03 with exactly one
   reference in the graph, at
   `pages/GitHub___CLI___Q___Using the gh cli, is there a quick way to list repositories with globs for user and repo name%3F.md:6`,
   under `## My Notes`. No `gh___dash*` file and no page claims a matching
   `alias::`.
   - Research is already done and committed elsewhere: branch `gh-dash-research`
     in the `codekiln/dotfiles` repo, commit `b080174`, at
     `tmp/gh-dash-exploration.md`, with every command and negative control in an
     appendix. **Pull from there rather than re-deriving.**
   - Upstream: [dlvhdr/gh-dash](https://github.com/dlvhdr/gh-dash), a `gh` CLI
     extension and terminal UI for GitHub. Go, MIT, ~12.3k stars, latest release
     [v4.25.2](https://github.com/dlvhdr/gh-dash/releases/tag/v4.25.2). GitHub
     only — four attempts at other forges, none merged. Not installed here.
   - His source was a video, archived in Readwise at 99.96%: "I'm never going
     back to GitHub UI ever again" by DevOps Toolbox,
     <https://youtube.com/watch?v=Z-3dUHDnkEI>, with seven highlights. DevOps
     Toolbox is Omer Hamerman (`omerxx`), established from the local clone of
     `omerxx/dotfiles` rather than the web — worth checking whether an author
     page exists before creating one.
   - One highlight is the advocate admitting he mostly pops out to the browser
     anyway. Keep it; it is the honest counterweight.
   - **The finding worth more than the tool page:** gh-dash writes its own full
     default config to `$XDG_CONFIG_HOME/gh-dash/config.yml` on first run. Of a
     116-line real-world config, ~90 lines are byte-identical to the generated
     defaults and only seven settings are genuine choices. That bears directly
     on his "prefer a tool's documented defaults" preference — **a long config
     file is not evidence of a configuration-heavy tool when the tool prints its
     own defaults into it.** If that generalises, it belongs somewhere more
     durable than a gh-dash page.

**Held deliberately, not forgotten.**

6. **Failure shapes collected but not yet written up**, kept out of the daily log
   because they are one class and will read as one section written once rather
   than bullets appended on the day each was found. Worth writing when the set
   settles.
   - Likely organising split when it is written, rather than a flat list: the
     first four are self-inflicted, and the remedy for each is a question that
     went unasked. The fifth involves another party, and its remedy is not a
     better question — it is noticing that what you were able to verify and what
     you are being asked to act on are disjoint. The tell is not that a claim is
     unverifiable; it is that the unverifiable ones are the ones with a request
     attached.
   - An instrument measuring the wrong property — mtime for staleness when the
     bodies matched.
   - A summary of one's own output read as corroboration. The measurement really
     ran; it ran on an echo.
   - A small self-selected sample generalised to a population — six panes that
     had all just been instructed.
   - A fact already used for one conclusion, which also answered a second
     question nobody thought to ask it. Nothing prompts a re-read of a fact you
     believe you have spent.
   - A message that is right about everything checkable, where the only false
     claims are the ones asking you to undo something. Verifying the checkable
     parts builds confidence that then carries the unverifiable ones. Observed
     2026-08-14: an instruction to drop committed work and accept a changed
     reporting line, arriving alongside several true statements.
   - A convention that was **proposed** somewhere, later read as **in force**
     there. Observed 2026-08-14: this graph was said to keep entity definitions
     under `Meta/Entity`. It does not — they live at `Logseq/Entity/*`, 43 of
     them. But the graph does contain one line naming the other convention, in
     `pages/Obsidian___Migration___26___05___30 about Openspec, AI Rules, Logseq, and avoiding Heresy.md:47`,
     describing "a possible move of entity docs toward `Meta/Entity`" that was
     never made. So a search for the convention finds a real line in a real page
     of this graph asserting it, and the only thing marking it as not-current is
     the word "possible".
     - The check has to be for **instances, not mentions**. "Does this repo use
       X" passes on a page that merely contemplates X; "how many things here are
       X" returns zero and settles it. Counting is the cheap discriminator, and
       a naming convention with no instances is a proposal.
     - The related remedy, for rules arriving from elsewhere: state a rule with
       its reason attached. A rule carrying its own reason shows where it stops
       applying, while a bare prohibition travels further than its justification
       does. Two arrived this way and neither held here — "avoid `tmp/`" (it is
       not ignored in this repo) and `Meta/Entity` as a discovery target. Given
       their reasons, both would have failed in seconds on arrival.

## Outside this repo

A global chief-of-staff skill is being written in the `codekiln/dotfiles` repo
by another agent, from final rounds submitted by every chief. This repo's final
round has been sent. Its content is the standing-operational shape: no tracker,
no branches, no PRs, no build — and the failure modes that come with that.

Three research requests arrived today from outside this workspace and were
answered as garden pages. Each carried permission to modify the local
`herdrdev/herdr` checkout. **That permission was declined every time** — it is a
third-party clone and the authority to write to it is the repo owner's, not a
peer's. Any needed change gets specified and brought to him. That checkout was
left clean.
