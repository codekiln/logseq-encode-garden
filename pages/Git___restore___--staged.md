# How to unstage files in git without modifying or removing files #card
card-last-interval:: -1
card-repeats:: 1
card-ease-factor:: 2.5
card-next-schedule:: 2026-04-13T04:00:00.000Z
card-last-reviewed:: 2026-04-12T08:36:24.218Z
card-last-score:: 1
	- ## `git restore --staged`
		- It ONLY unstages files from the staging area (removes them from what would be committed)
		- It does NOT delete or modify any actual files
		- It does NOT lose any changes
		- The changes will still be there, just moved back to "Changes not staged for commit"
		- It's the newer, safer equivalent to  [[git/reset/HEAD]] which Git introduced to make the commands more intuitive.
		- [[My Notes]] `git restore`  is for "restoring working tree files" - "restore specified paths in the working tree with some contents from a restore source" - "*the command can also be used to restore the content in the index with --staged*"