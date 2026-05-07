logseq-entity:: [[Logseq/Entity/Article]]
created-by:: [[Person/Chris Krycho]]
source-link:: https://v5.chriskrycho.com/essays/jj-init/
date-created:: [[2024/02/02]]
see-also:: [[jj-vcs]]
- # [jj init](https://v5.chriskrycho.com/essays/jj-init/)
	- Author: **[[Person/Chris Krycho]]** — *Sympolymathesy* (first published 2024-02-02; article metadata shows a 2024-09-09 revision).
	- ## Summary
		- Introductory essay on [[jj-vcs]] (Jujutsu / `jj`): motivation (Git’s CLI and mental-model pain), what Jujutsu combines from Mercurial-style changes vs revisions, Pijul/Darcs-style first-class conflicts, and a usable UI — plus near-zero migration cost on existing Git repos (`brew install jj`, then `jj git init` / `jj git clone`).
		- Walks through revsets, the default `jj log` view vs `git log`, `jj describe` and `jj new` as alternatives to commit-centric workflows, and why treating **changes** as primary shifts day-to-day ergonomics.
	- ## Notes
		- Frames `jj` as a serious Git frontend today and an evolving native DVCS over time (native backend still immature when written).
		- Useful alongside upstream docs on [revsets](https://github.com/jj-vcs/jj/blob/main/docs/revsets.md) and the project tutorial.
	- ## Links
		- [[jj-vcs]]
