logseq-entity:: [[Logseq/Entity/Question]]

- # What is an octopus merge in [[git]]?
	- ## [[AI Answer]]
		- Short answer: yes — an **octopus merge** is a `git merge` that joins **more than two branches** into a single merge commit at once, instead of merging them one pair at a time.
		- It happens whenever `git merge` is given more than one branch argument, e.g. `git merge branch-a branch-b branch-c`. The resulting commit has more than two parents (one per merged branch), which is the "octopus" (many arms/tentacles) in the name.
		- Constraints:
			- It only works when the merge can be resolved automatically — if any branch has a real conflict against the current state, git refuses the octopus merge and asks you to merge the conflicting branches individually instead.
			- Because of that, it's mainly useful for combining several independent, non-conflicting topic branches (a common release-integration pattern), not for merges likely to have overlapping changes.
		- It is the default merge strategy git picks automatically when more than two branch tips are passed to `git merge`; it can also be requested explicitly with `-s octopus`.
