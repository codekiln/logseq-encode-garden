logseq-entity:: [[Logseq/Entity/Question]]

- # Is there a [[Claude Code]] CLI slash command to see a diff of changed files, and why doesn't `/diff` show the diff content?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Claude Code Commands Reference](https://code.claude.com/docs/en/commands.md)
		- **Short answer:** `/diff` exists; the "New file not yet staged" message for untracked files is a side effect of the **Current** tab being `git diff HEAD` under the hood, not intentional concealment — `git` has no index entry to diff an untracked file against.
		- Per the official reference, `/diff` has two kinds of tabs: **Current** (`git diff HEAD`, all uncommitted changes) and **per-turn** (`T1`, `T2`, …, individual Claude turns). The docs describe switching between them but don't specify the per-turn tabs' data source.
		- Unconfirmed in official docs (seen on a third-party blog): per-turn tabs may reconstruct edits from the conversation record rather than from `git`, which would let them show new-file content without staging first. Worth testing empirically — arrow to a turn tab (e.g. `T6`) for an untracked file instead of Current.
		- Running `git add <file>` stages an untracked file; after that, the Current tab shows its full diff and line counts.
		- The Current tab shows content normally for already-tracked, modified files — the missing-content behavior is specific to untracked new files there.
		- Other ways to view diffs in the CLI:
			- The per-turn tabs (`T1`, `T2`, …) in `/diff`
			- IDE integrations (e.g. JetBrains) rendering Claude Code diffs natively
			- `/code-review`, which shows diffs alongside review feedback
		- A [feature request to stage untracked files from within `/diff`](https://github.com/anthropics/claude-code/issues/60425) was filed and closed as not planned.
