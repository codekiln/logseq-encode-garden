logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[rulesync/gitignore]], [[rulesync/Ignore]]

- # Why does `git check-ignore` report nothing for a tracked file?
- ## Answer
	- [[AI/Response]]
		- **Because a tracked file is not being ignored, whatever `.gitignore` says about its path.** `git check-ignore` answers "is git ignoring this path right now", and tracked files are exempt from ignore rules, so the pattern that matches the path is never reported. `--no-index` switches the question to "does a pattern match this path", which is the question an audit is actually asking.
		- Measured in a throwaway repository with `**/CLAUDE.md` in `.gitignore` and `sub/CLAUDE.md` force-added and committed:
		- | Command | Output | Exit |
		  |---|---|---|
		  | `git check-ignore -v sub/CLAUDE.md` | none | `1` |
		  | `git check-ignore -v --no-index sub/CLAUDE.md` | `.gitignore:1:**/CLAUDE.md` | `0` |
		  | `git check-ignore -v CLAUDE.md` (untracked, same pattern) | `.gitignore:1:**/CLAUDE.md` | `0` |
		- **Exit `1` with no output is what makes this costly.** It is the same result the command gives for a path no pattern matches, so a script or a reader treats "tracked, therefore exempt" and "no rule covers this" as one answer. The untracked row shows the pattern is real and the command can see it.
		- ### When to use which
			- **Auditing whether a rule covers a path** — use `--no-index`. This is the case whenever the question is about `.gitignore` itself, including whether a repository's ignore file and its tracked contents disagree.
			- **Asking why a file is not showing up in `git status`** — the plain form is right, because that is a question about the file's current state.
			- **Asking whether a directory's contents are published** — neither form answers it. `git ls-files <dir>` does, because it lists what is actually tracked.
		- ### The separate trap with the same symptom
			- A directory pattern given without its trailing slash can also report nothing. That is a different cause from the tracked-file exemption, and a path can hit both at once, so ruling out one does not rule out the other.