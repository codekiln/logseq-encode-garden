- [[vim]] [[Keyshort]] [[vim/Keyshort]]
	- ### How to browse directly to a known, named [[vim/help/Tag]], such as `add-local-help` [[card]]
	  card-last-interval:: 11.2
	  card-repeats:: 3
	  card-ease-factor:: 2.8
	  card-next-schedule:: 2026-07-05T11:39:33.136Z
	  card-last-reviewed:: 2026-06-24T07:39:33.136Z
	  card-last-score:: 5
		- [[Command]]: `:ta <subject>`
		- [[Examples]]
			- `:ta add-local-help` browses to the `add-local-help` subject in [[vim/help]]
		- mnemonic: ==ta== is short for **tag**
	- ### search for [[vim/help/Tag]]s that contain `write` [[card]]
	  card-last-interval:: 17.31
	  card-repeats:: 4
	  card-ease-factor:: 2.08
	  card-next-schedule:: 2026-07-11T13:02:28.491Z
	  card-last-reviewed:: 2026-06-24T06:02:28.491Z
	  card-last-score:: 3
		- [[Command]] `:ta /write` with the leading `/` searches for vim help tags that **contain** `write` (it doesn't need to appear at the beginning of the tag)
	- ### after searching for a [[vim/help/Tag]]s that contain `write`, browse to next and previous matches [[card]]
	  card-last-interval:: 4
	  card-repeats:: 2
	  card-ease-factor:: 2.32
	  card-next-schedule:: 2026-06-28T07:32:10.403Z
	  card-last-reviewed:: 2026-06-24T07:32:10.403Z
	  card-last-score:: 3
		- [[Command]]s `:tnext` and `:tprev` browse to next and previous vim help tag matches
			- also `:tn` and `:tp` or `[t` or `]t`