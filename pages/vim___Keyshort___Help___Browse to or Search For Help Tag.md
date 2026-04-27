- [[vim]] [[Keyshort]] [[vim/Keyshort]]
	- ### How to browse directly to a known, named [[vim/help/Tag]], such as `add-local-help` [[card]]
	  card-last-interval:: 6.03
	  card-repeats:: 1
	  card-ease-factor:: 2.6
	  card-next-schedule:: 2026-05-03T09:33:44.103Z
	  card-last-reviewed:: 2026-04-27T09:33:44.103Z
	  card-last-score:: 5
		- [[Command]]: `:ta <subject>`
		- [[Examples]]
			- `:ta add-local-help` browses to the `add-local-help` subject in [[vim/help]]
		- mnemonic: ==ta== is short for **tag**
	- ### search for [[vim/help/Tag]]s that contain `write` [[card]]
	  card-last-interval:: 3.69
	  card-repeats:: 2
	  card-ease-factor:: 2.36
	  card-next-schedule:: 2026-05-01T02:45:36.725Z
	  card-last-reviewed:: 2026-04-27T10:45:36.726Z
	  card-last-score:: 3
		- [[Command]] `:ta /write` with the leading `/` searches for vim help tags that **contain** `write` (it doesn't need to appear at the beginning of the tag)
	- ### after searching for a [[vim/help/Tag]]s that contain `write`, browse to next and previous matches [[card]]
	  card-last-interval:: 4
	  card-repeats:: 2
	  card-ease-factor:: 2.46
	  card-next-schedule:: 2026-05-01T10:45:28.416Z
	  card-last-reviewed:: 2026-04-27T10:45:28.417Z
	  card-last-score:: 5
		- [[Command]]s `:tnext` and `:tprev` browse to next and previous vim help tag matches
			- also `:tn` and `:tp` or `[t` or `]t`