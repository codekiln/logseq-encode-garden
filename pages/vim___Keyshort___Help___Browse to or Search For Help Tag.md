- [[vim]] [[Keyshort]] [[vim/Keyshort]]
	- ### How to browse directly to a known, named [[vim/help/Tag]], such as `add-local-help` [[card]]
	  card-last-interval:: 4.14
	  card-repeats:: 2
	  card-ease-factor:: 2.7
	  card-next-schedule:: 2026-06-22T10:26:28.690Z
	  card-last-reviewed:: 2026-06-18T07:26:28.692Z
	  card-last-score:: 5
		- [[Command]]: `:ta <subject>`
		- [[Examples]]
			- `:ta add-local-help` browses to the `add-local-help` subject in [[vim/help]]
		- mnemonic: ==ta== is short for **tag**
	- ### search for [[vim/help/Tag]]s that contain `write` [[card]]
	  card-last-interval:: 8.88
	  card-repeats:: 3
	  card-ease-factor:: 2.22
	  card-next-schedule:: 2026-05-22T05:37:27.648Z
	  card-last-reviewed:: 2026-05-13T08:37:27.648Z
	  card-last-score:: 3
		- [[Command]] `:ta /write` with the leading `/` searches for vim help tags that **contain** `write` (it doesn't need to appear at the beginning of the tag)
	- ### after searching for a [[vim/help/Tag]]s that contain `write`, browse to next and previous matches [[card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.46
	  card-next-schedule:: 2026-06-19T04:00:00.000Z
	  card-last-reviewed:: 2026-06-18T08:26:57.908Z
	  card-last-score:: 1
		- [[Command]]s `:tnext` and `:tprev` browse to next and previous vim help tag matches
			- also `:tn` and `:tp` or `[t` or `]t`