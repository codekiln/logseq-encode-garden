# Editing journal request blocks

## The marker is the first token after the bullet

A request block looks like this, with real tab characters for indentation:

```
			- TODO please create [[Logseq/Entity/Series]]. A Series should be …
			  id:: 6aafa689-7002-4ba2-851f-01dd79dfe4f4
```

Flipping the marker replaces `TODO` with `DOING`, and later `DOING` with `DONE`. The bullet, the tab depth and every character after the marker stay as they are.

Match on the block's own text rather than a line number — the journal may have grown since it was read. A targeted edit on the unique request text is safer than a line-addressed `sed`.

## An `id::` line belongs to the block above it

A block ref like `((6ab187ef-6ec3-45f8-8758-d6810702ef29))` resolves through the `id::` line sitting under its block, indented two spaces past the bullet. Keep the pair together, and leave the id in place even when the request reaches `DONE` — [[Person/codekiln]] and other pages link to finished requests.

## Multi-line requests

A request can run several lines, with continuation lines indented under the bullet. Only the first line carries the marker. Leave the continuation lines untouched.

## What never changes

- The wording of a request. The text is [[Person/codekiln]]'s.
- The order of blocks, or their nesting depth.
- Anything outside the Ghost Gardener heading — narrative blocks, `[[My Thoughts]]`, other headings.
- `tags::` frontmatter, anywhere.

## Nested subtasks

```
	- TODO look up the last videos watched in readwise reader and import …
		- TODO import Jev and link to [Jev + Claude Code …](https://read.readwise.io/…)
			- TODO import Ray Amjad as person reference and this as youtube within it
```

Work the leaves first. A parent reaches `DONE` once all of its children are `DONE`; while any child is open, the parent sits at `DOING`.

## Stalled requests

A request you cannot finish stays at `DOING`, with the reason given in chat. Written explanation of why an agent stopped belongs in the conversation, away from the journal.
