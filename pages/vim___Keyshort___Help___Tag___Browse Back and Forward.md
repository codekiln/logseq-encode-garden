- [[vim]] [[Keyshort]] [[vim/Keyshort]]
	- **how to browse backwards and forwards in help tags in vim** [[card]]
	  card-last-interval:: 3.45
	  card-repeats:: 1
	  card-ease-factor:: 2.36
	  card-next-schedule:: 2026-04-30T19:57:45.200Z
	  card-last-reviewed:: 2026-04-27T09:57:45.200Z
	  card-last-score:: 3
		- **shortcut**: `CTRL-O` backwards, `CTRL-I` forwards
			- `CTRL-O` go to the Older help tag
			- `CTRL-I` and then `<TAB>` go to the Newer help tag
		- `:help jump-motions`
		- [[My Notes]]
			- I formerly had vim `CTRL-T` marked here with `CTRL-O` as going to older help tag. When I `:helpgrep CTRL-T` I end up seeing that `CTRL-T` is "pervious match" and `CTRL-G` is "next match" with the [[Mnemonic]] that `T` is above `G` on a normal keyboard (and T would be up in the page AKA previous while G would be *down* on the page AKA *next*)
			-