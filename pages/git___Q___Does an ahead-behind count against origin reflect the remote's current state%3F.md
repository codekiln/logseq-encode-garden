logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[git]], [[My/AI/Agent/Fleet]], [[My/AI/Agent/Chief of Staff]]

- # Does an ahead-behind count against origin reflect the remote's current state?
	- ## [[AI Answer]]
		- **Short answer: no.** `git status` and `git log @{u}..HEAD` compare HEAD against the *remote-tracking ref* — a local copy of where `origin/main` stood the last time this checkout fetched, pulled, or pushed. Neither touches the network. **Fetch first, then read the count.**
			- ~~~sh
			  git fetch origin
			  git rev-list --left-right --count origin/main...main   # behind  ahead
			  ~~~
		- ### What `ahead` actually means
			- `origin/main` is an ordinary ref under `.git/refs/remotes/`. Nothing updates it in the background — not `git log`, not `git status`, not `git branch -v`.
			- So "ahead by 6" reads as *ahead of what this checkout last saw*, and the sentence `git status` prints — `Your branch is ahead of 'origin/main' by 6 commits` — names a ref rather than a server, which is easy to read as a claim about the server.
			- A stale ref hides only the *behind* half. The ahead count stays correct, so the reading is not wrong in an obvious way; it is wrong by omission, which is why nothing about the output invites a second look.
		- ### Measured here
			- On [[2026/08/24]] in this graph's repository, before fetching:
				- ~~~sh
				  git log --oneline origin/main..main | wc -l   # 6
				  git log --oneline main..origin/main | wc -l   # 0
				  ~~~
			- After `git fetch origin`, with no local commit in between: still `6` ahead, now **`30` behind**. The remote-tracking ref had been standing since [[2026/08/17]] while other work was pushed to the same branch. A plain `git push` would have been rejected, and the six commits were only integrated by merging first.
		- ### Why it matters more with several agents in one repo
			- The single-author case tolerates it: a `git pull` before pushing repairs the picture, and a rejected push is a cheap error.
			- The [[My/AI/Agent/Fleet]] case does not. Several seats push to the same branch on the same day, so any count carried in a brief, a handoff doc, or a plan is a measurement with a timestamp on it, and it decays. A brief that says "six commits ahead" is reporting what one window saw at one moment.
			- The rule that follows: **fetch before trusting an ahead-behind count, and always before pushing to a repository another seat also touches.**
		- ### The wider shape of the error
			- The count is not a bad instrument. It answers exactly the question it was built for, and it answered that question correctly here — the mistake was a confident conclusion drawn from a partial read of evidence already in hand, where the missing half was one command away.
			- That is the same failure [[My/AI/Agent/Chief of Staff]] records under a check that reports a break where none exists: well-formed output carries no signal that it is a fragment. Work out what the instrument can see before building on what it says.
		- ### Sources
			- [git-status(1)](https://git-scm.com/docs/git-status) — the ahead/behind line is computed against the configured upstream ref; `git status` does not contact the remote.
			- [gitrevisions(7)](https://git-scm.com/docs/gitrevisions) — `@{u}` / `@{upstream}` names the remote-tracking branch, which is local.
