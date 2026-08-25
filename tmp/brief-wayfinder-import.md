# Brief — import the Latent Space /wayfinder interview

You are a contractor hired by Hayward, the manager seat for `logseq-encode-garden`. This brief is your whole task. You are engaged against this job, and you are done when it is delivered.

Read `CLAUDE.md`, `.claude/rules/logseq-core.md`, and every `pages/My___AI___Rule*.md` and `pages/My___Pref___Writing*.md` before you write a word into `pages/`. They govern, they are strict, and about 28KB of them is the standard your prose is judged against.

## What codekiln asked for, in their words

> can you please have hayward hire a contractor to import https://read.readwise.io/search/read/01m0gfjwrjsf18vzchms81ep69 and the doc it represents (use the readwise cli)

Both halves: the Reader entry with the highlights it carries, and the underlying source document.

## Already measured, so do not re-derive it

Hayward verified all of this before hiring you. Trust it, and say so if anything below fails to reproduce.

- **The CLI works and authentication is not interactive.** `readwise` is on PATH, version 0.5.9, installed globally by mise. `readwise reader-list-tags` returned data without prompting, so no browser handshake is waiting for you.
- **The two commands you need:** `readwise reader-get-document-details --document-id 01m0gfjwrjsf18vzchms81ep69 --json` returns the Markdown content, and `readwise reader-get-document-highlights --document-id 01m0gfjwrjsf18vzchms81ep69 --json` returns the highlights. Read `readwise --help` before inventing any other invocation.
- **The document.** Title `The /wayfinder Skill: Navigating the "Fog of War" of Planning`, author `Latent.Space`, Reader category `email`, about 12,095 characters of content.
- **The canonical source URL is `https://www.latent.space/p/wayfinder-skill`.** Hayward decoded this out of the newsletter's own base64 payload offline, with no network request, so it cost codekiln no tracked click.
- **It carries exactly 2 highlights and no notes and no tags.** One is the paragraph introducing /wayfinder and the "fog of war" quote; the other is Pocock on wanting an orchestrator layer for planning. Both are codekiln's own highlights and both belong on the page.
- **The email was sent 2026-08-20 17:00 local**, which is your candidate publication date. Confirm it from the document if the content states one.

## Where it lands, which Hayward has decided

Create one page at **`Latent Space/Blog/26/08/The wayfinder Skill: Navigating the "Fog of War" of Planning`**, on disk `pages/Latent Space___Blog___26___08___The wayfinder Skill: Navigating the "Fog of War" of Planning.md`.

**Drop the leading slash from `/wayfinder` in the page name.** A slash inside a Logseq page name creates a namespace segment, so `The /wayfinder Skill` would silently split the page under a namespace called `The `. Keep the real title, slash and all, in the H1 link text where it is prose rather than a path. `Claude/Code/Skill/Grill Me` already sets this precedent by naming the page `Grill Me` rather than `/grill-me`.

The namespace exists already — see `pages/Latent Space___Blog___25___03___Why MCP Won.md` and `pages/Latent Space___Blog___25___04___In the Matter of OpenAI vs LangGraph.md` for the house shape. Follow `pages/Logseq___Entity___Article.md`, which is the governing definition: `logseq-entity:: [[Logseq/Entity/Article]]`, `created-by::`, `date-created::` set to the publication date, the optional `readwise-link::` which is exactly what this import is for, an H1 of `- # [Title](url)`, and body sections chosen from Summary, Notes, Highlights and Links. Prefer a concise summary over pasting the full article.

**One judgment call is yours: who `created-by::` points at.** The byline is the publication, Latent.Space, and the piece is an interview whose substance is Matt Pocock's. `pages/Latent Space___Blog___25___03___Why MCP Won.md` uses `created-by:: [[@swyx]]`. Decide it, and say in your report which you chose and why.

## Deduplicate against these before creating anything

Run the `logseq-entity` and `logseq-link-hygiene` skills. These pages already exist and are the ones you will collide with or want to link:

- `pages/Person___Matt Pocock.md` — the hub page already exists, so do not create one.
- `pages/Claude___Code___Skill___Grill Me.md` — the article explicitly compares grill-me against wayfinder, so this is a real link, not a decorative one.
- `pages/Person___Matt Pocock___YouTube___26___06___Building Great Agent Skills: The Missing Manual.md`
- The `Latent Space/Pod` and `Latent Space/Blog` namespaces.

## The one thing you must bring back, because other work depends on it

codekiln's next step is a GitHub issue in another repository about adding Pocock's wayfinder skill. That issue gets written from your report, so it needs to stand on something you checked rather than on this brief.

**Verify at source that the document references Matt Pocock's wayfinder skill, and where.** Hayward already read the content and it does — 17 mentions, and the line `### Matt Pocock tells us about his /wayfinder skill, for greenfield projects or for when the way forward is unclear.` That sentence is the publication's own wording, quoted verbatim, so leave its pronoun alone if you carry it onto the page. Reproduce the finding yourself rather than quoting this brief. If it turns out to be a different skill or a different person, stop and say so.

Bring back, in your report:

1. **What wayfinder is**, in a few plain sentences — enough that someone who has not read the article can write an issue about adding it.
2. **The quotation that establishes it**, with enough surrounding text to be checkable.
3. **The GitHub URL for the wayfinder skill.** `pages/Claude___Code___Skill___Grill Me.md` links `https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md`, so the repository is `github.com/mattpocock/skills` and wayfinder is very likely a sibling under `skills/`. Establish the real path and say how you established it.

**Do not click the `substack.com/redirect/...` links to find it.** Every one carries codekiln's subscriber token, so following one registers a click on their account and leaks nothing useful to you. Go at `github.com/mattpocock/skills` directly.

## Standing rules for this engagement

- **Never touch `tags::` frontmatter** on any page. Not to add, not to fix, not to reorder.
- **Record the page in today's journal** under `[[Filed]]`, following `pages/Logseq___Journal.md`. Labels under `[[Filed]]` and `[[Updated]]` are alphabetized.
- **codekiln edits this checkout live in Logseq while you work, and they prune journal entries in their working copy.** Before any commit run `git diff --cached`. If your line and theirs land in the same file, commit the index version plus only your line: `git show :path > f`, add your line, `git hash-object -w f`, `git update-index --cacheinfo 100644,<blob>,path`. Then prove it byte-exact by removing exactly the line you inserted and testing the result equals the original. Do not `git add` a file codekiln has open changes in.
- **`git grep -E` with `\b` silently answers false in this repository.** A pattern holding `\b` matches nothing and exits 1, which looks identical to a genuine no-match. Use `git grep -P '\bword\b'` in single quotes, or `-F` for a fixed string, and run a positive control first. See `pages/git___Q___Why does git grep -E report no matches for a word-boundary pattern%3F.md`.
- **`tmp/` in this repository is tracked and the repository is public**, so anything you write here publishes. This brief is public and contains nothing that should not be.
- **Use targeted `git add`, never `git add -A`.** Conventional commit message with a gitmoji, imperative mood, matching the existing log.
- **Commit when you are done. Do not push. Do not mention the unpushed stack** in your report — not as an item, not as a question, not as a line.
- `--permission-mode auto` is already set on your process. It is not a decision for you.
- **codekiln takes they/them**, as does everyone else these documents name. Before you finish, run `grep -rniE '\b(he|him|his|she|her|hers)\b'` over what you wrote. Matt Pocock has not disclosed pronouns either, and an interview is easy to write in the wrong ones — this is the most likely place for you to slip.

## Report back

Write your report into the pane and stop. Cover: what you created, the `created-by::` call and why, the three wayfinder items above, and anything that failed to reproduce from the measured section. Hayward takes delivery by reading your pane.
