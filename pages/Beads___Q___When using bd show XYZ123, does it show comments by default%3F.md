tags:: [[bd/show]]

- # When using `bd show XYZ123`, does it show comments by default?
	- `XYZ123` stands in for any [[bd]] issue id.
	- ## Answer
		- [[AI/Response]]
			- **Yes.** In the default human-readable output (no `--short`), `bd show` loads comments via `GetIssueComments` and, if there are any, prints a **COMMENTS** section (timestamp, author, rendered markdown body). If the issue has no comments, that section is omitted.
			- **`--short`** returns only a one-line summary and skips the comments block (and other detail sections).
			- **`--json`** includes comments in the structured payload (`IssueDetails.Comments`).
			- **`--thread`** is separate: it shows the full **conversation thread for messages**, not the default comments listing.
			- [Source: `cmd/bd/show.go` in steveyegge/beads](https://github.com/steveyegge/beads/blob/main/cmd/bd/show.go)
	- ## Related
		- [[bd]]