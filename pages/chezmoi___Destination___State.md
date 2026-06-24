logseq-entity:: [[Logseq/Entity/Card]]
alias:: [[chezmoi/Concept/Destination/State]]
tags:: [[chezmoi/Concept]]

- # What does the [[Term]] *Destination State* mean in [[chezmoi]]? [[card]]
  card-last-interval:: 4.28
  card-repeats:: 2
  card-ease-factor:: 2.7
  card-next-schedule:: 2026-06-28T13:24:03.087Z
  card-last-reviewed:: 2026-06-24T07:24:03.087Z
  card-last-score:: 5
	- [[My Answer]]
		- In Chezmoi, the **destination state** means "for each of the [[chezmoi/Target]]s, what is is the state of that file currently in the [[Home/Dir]]?
		- The [[dotfiles repo]] [[Declares]] how the [[dotfiles]] managed by chezmoi should control the [[Home/Dir]] dotfiles. Destination State is how chezmoi references the "runtime" or "actual" state vs the declared state in the repo.
	- [[Their Answer]]
		- The *destination state* is the current state of all the [[chezmoi/Target]]s in the [[chezmoi/Destination/Directory]].