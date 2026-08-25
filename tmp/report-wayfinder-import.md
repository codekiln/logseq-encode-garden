# Delivered — the Latent Space /wayfinder import

Written by Hayward on 2026-08-25 after taking delivery from the `wayfinder-import` contractor. Kept here because `tmp/` is tracked, and because the equivalent report this morning was left in a session scratchpad and died with the 14:08 restart.

## What landed

`pages/Latent Space___Blog___26___08___The wayfinder Skill: Navigating the "Fog of War" of Planning.md`, committed at `0fd13bd2`, plus one `[[Filed]]` line under a `skills` label in `journals/2026_08_25.md`.

The page carries `logseq-entity:: [[Logseq/Entity/Article]]`, `created-by:: [[Latent Space]]`, `date-created:: [[2026/08/20]]` and `readwise-link:: https://read.readwise.io/read/01m0gfjwrjsf18vzchms81ep69`.

## The three things the dotfiles issue is written from

**What wayfinder is.** A [[Claude/Code/Skill]] by [[Person/Matt Pocock]] for planning work too large for one agent session. It writes the plan onto the repository's issue tracker as a **map** — one issue labelled `wayfinder:map` — with **decision tickets** as child issues. Each ticket asks one question whose answer is a decision, sized to roughly one 100K-token session. A session claims an open ticket whose blockers are closed, resolves it, and records a one-line answer on the map. The map is done when nothing is left to decide. Tickets carry a `wayfinder:<type>` label, one of `research`, `prototype`, `grilling` (the default) and `task`. Blocking uses the tracker's native dependency relationship. The skill's frontmatter sets `disable-model-invocation: true`, so a person invokes it rather than a model.

**The quotation that establishes it.** The document's own subhead, verbatim, its pronoun the publication's: `Matt Pocock tells us about his /wayfinder skill, for greenfield projects or for when the way forward is unclear.` The source is `https://www.latent.space/p/wayfinder-skill`, an interview published 2026-08-20.

**The GitHub paths, measured twice.** `https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md`, with prose documentation at `https://github.com/mattpocock/skills/blob/main/docs/engineering/wayfinder.md`. Established through `gh api 'repos/mattpocock/skills/git/trees/main?recursive=1'` and re-run independently by Hayward, with both files fetched to confirm they resolve at 11,908 and 15,976 bytes. The positive control on the same tree returns `skills/productivity/grill-me/SKILL.md`, matching the URL already on [[Claude/Code/Skill/Grill Me]].

**Wayfinder sits under `skills/engineering/`, not under `skills/productivity/` where grill-me sits.** Hayward's brief guessed the latter from the grill-me precedent and was wrong; the contractor measured it.

## Two calls the contractor made, both kept

**`created-by::` points at the publication rather than at Pocock.** No individual writer is named anywhere in the piece — the interviewer's turns are labelled `Latent Space:`. Pocock is the interviewee, so they are linked in the body. [[Logseq/Entity/Article]] asks for an organization page on institutional authorship, and `pages/Every___Blog___Source Code___25___08___18___My AI Had Already Fixed the Code Before I Saw It.md` already carries `created-by:: [[Every]]` in the same shape. The sibling `Latent Space/Blog/25/03/Why MCP Won` uses `[[@swyx]]` because that piece is swyx's own writing.

**The subscriber token was stripped from a highlight before it reached a public page.** Readwise stores the first highlight with `/wayfinder` wrapped in a `substack.com/redirect/...?j=<token>` link, and that query parameter identifies codekiln's subscription. The highlight's words are kept byte-for-byte and only the URL was dropped, leaving `**/wayfinder**` as bold text, with the real destination in the Links section. Verified after the fact: the token appears nowhere in the tracked tree.

## One divergence worth knowing rather than fixing

The page name and H1 use straight quotes in `"Fog of War"` where the source title uses curly quotes. The filename, the H1 and the journal link all agree with each other, so the link resolves and nothing breaks; the quoted highlights keep the source's curly quotes because they are quotations. Left alone rather than renaming a committed page for punctuation fidelity.
