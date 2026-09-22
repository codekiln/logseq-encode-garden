# Trimesters and week navigation

## Trimester boundaries

- **Trimester 1** — January 1 through the day before Memorial Day, which is the last Monday in May.
- **Trimester 2** — Memorial Day through the day before Labor Day.
- **Trimester 3** — Labor Day, the first Monday in September, through December 31.

## Week numbering

Week `N` starts `N - 1` weeks after its trimester's start date. Weeks run Monday through Sunday.

## Navigation across a boundary

When a week is the first or last of its trimester, `prev::` and `next::` on the week page and on the week todos page point into the adjacent trimester rather than wrapping within the current one. The same applies to the day chain: `d1` of the first week of a trimester points back to `d7` of the last week of the previous trimester, and `d7` of the last week points forward to `d1` of the first week of the next.

Derive all of this from the `logseq-week-info-getter` subagent's report rather than computing the dates by hand.
