# How to unstage files in git without modifying or removing files #card
	- ## `git restore --staged`
		- It ONLY unstages files from the staging area (removes them from what would be committed)
		- It does NOT delete or modify any actual files
		- It does NOT lose any changes
		- The changes will still be there, just moved back to "Changes not staged for commit"
		- It's the newer, safer equivalent to  [[git/reset/HEAD]] which Git introduced to make the commands more intuitive.