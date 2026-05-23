tags:: [[Question]]
logseq-entity:: [[Logseq/Entity/question]], [[Logseq/Entity/Card]] 
see-also:: [[git/How To/Discard Changes to Working Dir]], [[git/reset]]

- # What's the [[git]] command that will remove untracked and unignored files to bring it up to HEAD? [[card]]
	- ## Answer
		- [[My Answer]]
			- Step 1 - [[git/reset/--hard]] `HEAD` discards tracked changes
			- Step 2 - [[git/clean]] `git clean -df` to delete untracked files and directories
		- [[AI/Response]]
			- **Untracked, non-ignored files only:** use [[git/clean/--directory]]  and [[git/clean/--force]] as `git clean -df` to delete untracked files and directories. Git skips paths matched by [[git/.gitignore]], so ignored files stay. Preview first with [[git/clean/--dry-run]] as `git clean -dfn`
			- **Full working tree match to HEAD:** run `git reset --hard HEAD` to discard changes to tracked files (staged and unstaged), then `git clean -fd` for untracked non-ignored paths. One-liner: `git reset --hard HEAD && git clean -fd`.
			- **Avoid `-x` unless you mean it:** `git clean -fdx` also removes ignored files (build output, local env files, etc.) — that is broader than "unignored" untracked files.
			- [git-clean documentation](https://git-scm.com/docs/git-clean)
			- [git-reset documentation](https://git-scm.com/docs/git-reset)