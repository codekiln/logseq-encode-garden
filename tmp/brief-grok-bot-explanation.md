# Brief — a Diátaxis explanation of "Grok Bot"

You are a worker in the `logseq-encode-garden` seat (Hayward). This brief is your whole task. Read `CLAUDE.md` and `.claude/rules/logseq-core.md` before you write anything into `pages/`; they govern and they are strict.

## What codekiln wants

They have an email from Dov saying "Grok Bot" is now included in their Cursor Teams plan. They want one page that answers three questions:

1. What it is.
2. Whether it needs extra billing on top of the Cursor Teams plan.
3. How it might be used.

Diátaxis **explanation**, not a tutorial and not a how-to: understanding-oriented prose that leaves the reader able to reason about the thing, rather than steps to follow. The garden has a `diataxis-docs` skill — load it.

## Settle the name before the page has a title

codekiln uses voice input and product names arrive mis-transcribed. Do not write a page called "Grok Bot" until you have established that something by that name exists.

The groundwork is done, so start from here rather than repeating it:

- **The garden already documents `BugBot`** — Cursor's own v1.0 changelog, 4 June 2025, quoted on `pages/CursorAI___v___1___0.md`: an automatic PR reviewer that comments on GitHub PRs with a "Fix in Cursor" button, documented at `docs.cursor.com/bugbot`. Note Cursor's own capitalisation, `BugBot`, and that the docs URL is lowercase.
- **xAI's model is `Grok`**, and Cursor does offer third-party models, so a Grok-powered review bot is not impossible.
- **The graph has no `Grok` page and no xAI namespace at all.** So if the subject really is xAI's Grok, you are creating a namespace, which is a convention call — do not invent one. Report back instead.

Three outcomes and what each means: it is BugBot mis-transcribed, and the page is about BugBot under the garden's attested spelling; it is genuinely a distinct Grok-based product, and you have a sourced name for it; or you cannot tell, in which case **stop and report rather than picking the likelier one**. Verifying the premise before building on it is the rule that made an earlier task today cost nothing.

## The billing answer is the one with money attached

This is the part codekiln will act on, so it gets the strictest standard. Source it or mark it unknown.

- Do not infer inclusion from a marketing sentence. "Included for teams" in a launch post is not the same as a line on the pricing page, and the two have disagreed before.
- If Cursor's pricing and docs do not answer whether it costs extra on a Teams plan, the correct page says so, and says who would know — the pricing page as of the date you read it, the docs, or Cursor support. A confident guess here is worse than a clean "not stated".
- Date every pricing claim. Pricing pages change and an undated claim rots invisibly.

## The primary source is an email you do not have

Dov's email is what prompted this and neither you nor I can read it. If the page turns on something only that email says — a plan tier, a bundled entitlement, a product name that appears nowhere public — **stop and report to the dotfiles seat, `.files-cos-2026-08-24-mon-1106`, over the cross-session message channel.** They will ask codekiln to paste it. Nobody goes looking through their mail.

**Do not paste the email's contents into this repository if it does reach you.** `tmp/` here is tracked and published, unlike the other repos the fleet works in — this brief is public. An email from a named third party does not go into a public garden.

## Where the page goes, and the conventions that will trip you

- **The namespace is `CursorAI`, not `Cursor`.** Every one of the ~40 existing pages uses it. This is the single most likely thing to get wrong.
- Explanation pages in this graph are filed as `<Topic>/Explanation/<Title>` — on disk `CursorAI___Explanation___<Title>.md`, triple underscores for the slashes. See `pages/herdr___Explanation___Where Input Box Text Comes From.md` and `pages/Pytest___asyncio___Explanation___yield vs return in async pytest fixtures.md` for the shape.
- Tag it `[[Diataxis/Explanation]]`. **Never touch a `tags::` line on a page you did not create.**
- **Resolve every wikilink against the live graph before you write it.** A near-miss title creates a silent empty page rather than an error, and 622 page files here are already under 80 bytes. Grep for the title and for `alias::` lines containing it; the `logseq-link-hygiene` skill runs the check. Absence of a `.md` file does not mean absence of a page.
- LFM, strictly: every line starts with a bullet including headings (`- # Title`), TAB indentation for nesting, no blank lines, `~~~` code fences inside bullets, no ordered lists.
- Markdown prose in any `.md` file outside `pages/` goes one line per paragraph. Do not hard-wrap — see `pages/My___Pref___Writing___Do not hard-wrap prose in Markdown.md`.
- Write so codekiln never has to resolve a reference: name the thing again instead of pointing back at it, and never let a count stand in for the facts it counts — `pages/My___Pref___Writing___Never make the reader resolve a reference.md`.

## Finishing

You write the page. **You do not commit it**, and you do not run `git add` — several agents and codekiln share this one checkout, and a stray `git add` stages someone else's half-written work. Hand the file paths back to whoever holds the seat when you are done.

Record the change in today's journal only if you are asked to; the seat is handling the journal today. Say plainly what you could not source rather than smoothing it over — an unsourced billing claim is the one outcome that costs codekiln money.
