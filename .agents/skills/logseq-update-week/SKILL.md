---
name: logseq-update-week
description: >-
  Set up a full week of Logseq pages in a trimester-numbered garden: the week
  page, the week todos page, seven day pages, and the refreshed
  Logseq/Template/Today/Link page, all wired with prev/next navigation that
  crosses trimester boundaries. Use when the user asks to set up the week, run
  the weekly page setup, create this or next week's pages, or repair week
  navigation under `pages/YYYY___tT___wWW*.md`. Do not use for journal pages
  under `journals/`.
metadata:
  short-description: 'Create the week, todos and day pages for a trimester week'
---
# Weekly page setup

Creates the complete structure for a week. Run with no arguments for the current week.

## Get the dates first

Run the `logseq-week-info-getter` subagent and take from it:

- **year** — four digits
- **trimester** — 1, 2 or 3
- **week** — the week number within that trimester
- **day** — the days in the week, Monday through Sunday

Trimester boundaries and the prev/next rules across them are in [references/trimester-and-navigation.md](./references/trimester-and-navigation.md). Read it whenever the week sits at the start or end of a trimester.

## Files to write

In `pages/`, with `tT` the trimester number and `wWW` the zero-padded week number (trimester 3, week 6 gives `t3` and `w06`):

- `YYYY___tT___wWW.md` — week page
- `YYYY___tT___wWW___Todos.md` — week todos
- `YYYY___tT___wWW___d1.md` through `d7.md` — Monday through Sunday

Then update `pages/Logseq___Template___Today___Link.md` with this week's day links.

The frontmatter and body for each of those page types is in [references/page-templates.md](./references/page-templates.md). Read it before writing any of the files.

## Navigation

Every page carries `up::`, `prev::` and `next::`. Day pages chain across week boundaries: `d1` points back to the previous week's `d7`, and `d7` points forward to the next week's `d1`. Week pages and todos pages chain to their neighbors the same way, including across a trimester boundary.

Day pages start minimal — the heading and an empty agenda. Weather and schedule go in only when the week overview page supplies them.

All files follow the `logseq-core` rule for LFM structure and the triple-underscore namespace convention (detail: skill `logseq-lfm`).
