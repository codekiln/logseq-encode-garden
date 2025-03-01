# [How do I prevent 'git diff' from using a pager? - Stack Overflow](https://stackoverflow.com/questions/2183900/how-do-i-prevent-git-diff-from-using-a-pager)
	- Make sure that you add  [[git/Flag/--no-pager]] or `-P` **before** your command, as in `git --no-pager log...`, ...
		- Or use [[git/EnvVar/GIT_PAGER]] or [[Linux/EnvVar/PAGER]] environment variables
		- or  [[git/Config/core.pager]] git config variable
		- #note consider setting [[git/Config/core.pager]] to use [[cat]] for AI coding
		  id:: 67c2dd1d-ac20-47e6-b5f8-cc816afb094f
			- `git config core.pager cat`
			- since it can be set at the repo level or globally with `--global`, and because it's easier than setting up environment variables for each the different types of AI coding processes
			- #Warning
				- > This would be terrible if you did  [[git/log]] in a repository with a large number of commits. Or worse, `git log -p` -- you'd get the entire set of commit diffs dumped into your terminal. #Quote from [[Person/Karen Etheridge]]