# Resume note — encode-garden chief of staff, 2026-08-13

Written for a successor with none of this context.

## Resume this session

```
claude --resume encode-garden-chief-of-staff
```

herdr workspace `w2` (label `encode-garden`). Two tabs were live at wrap-up:
`chief-of-staff` and `scribe` (`encode-garden-scribe`, resumable by the same
`--resume` form under its own name).

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

6. **Four failure shapes from today**, kept out of the day's log because they are
   one class and will read as one section written once rather than four bullets
   appended separately: an instrument measuring the wrong property; a summary of
   one's own output read as corroboration; a small self-selected sample
   generalised to a population; and a fact already used for one conclusion that
   also answered a second question nobody asked it. Worth writing on a later day.

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
