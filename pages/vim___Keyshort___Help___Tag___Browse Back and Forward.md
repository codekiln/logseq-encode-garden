- [[vim]] [[Keyshort]] [[vim/Keyshort]]
	- **how to browse backwards and forwards in help tags in vim** [[card]]
	  card-last-interval:: 4
	  card-repeats:: 2
	  card-ease-factor:: 2.08
	  card-next-schedule:: 2026-06-30T07:50:55.349Z
	  card-last-reviewed:: 2026-06-26T07:50:55.350Z
	  card-last-score:: 3
		- **shortcut**: `CTRL-O` backwards, `CTRL-I` forwards
			- `CTRL-O` go to the Older help tag
			- `CTRL-I` and then `<TAB>` go to the Newer help tag
		- `:help jump-motions`
		- [[My Notes]]
			- I formerly had vim `CTRL-T` marked here with `CTRL-O` as going to older help tag. When I `:helpgrep CTRL-T` I end up seeing that `CTRL-T` is "pervious match" and `CTRL-G` is "next match" with the [[Mnemonic]] that `T` is above `G` on a normal keyboard (and T would be up in the page AKA previous while G would be *down* on the page AKA *next*)
			- [[2026-06-24 Wed]] confused this with `:tn` and `:tp`. The fact that there's two different sets of shortcuts - one for "historical navigation order" and the other for "next and previou search order" is somehow unintuitive to me, even though browsers also separate these sets of actions.
			-