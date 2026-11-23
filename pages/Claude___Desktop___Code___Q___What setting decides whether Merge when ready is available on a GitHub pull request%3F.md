tags:: [[Claude/Desktop]], [[Claude/Code]], [[Q]]
logseq-entity:: [[Logseq/Entity/Question]]
title:: Claude/Desktop/Code/Q/What setting decides whether Merge when ready is available on a GitHub pull request?

- # What setting decides whether **Merge when ready** is available on a [[GitHub]] pull request in [[Claude/Desktop/Code]]?
	- ## [[AI Answer]]
		- **Short answer:** the per-repository GitHub setting **Allow auto-merge**, at **Settings → General → Pull Requests → Allow auto-merge** on GitHub. Only a repository admin can change it. **Merge when ready** in the PR menu of the Code tab is GitHub's auto-merge, so it is greyed out until that box is ticked, which is exactly what its tooltip says.
		- [[Answer/Official]] from [Managing auto-merge for pull requests in your repository](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-auto-merge-for-pull-requests-in-your-repository)
		- **The same flag through the API:** REST `allow_auto_merge` on the repository, and GraphQL `Repository.autoMergeAllowed`.
			- Check it: `gh api repos/OWNER/REPO --jq .allow_auto_merge`
			- Turn it on as an admin: `gh repo edit OWNER/REPO --enable-auto-merge`
		- **Other conditions, also from GitHub:**
			- Auto-merge works on public repositories on GitHub Free, and on private repositories only on paid plans (Pro, Team, Enterprise).
			- Once it is allowed, GitHub only accepts auto-merge on a PR that is still waiting on something, such as a required review or required status check from branch protection or a ruleset. If nothing blocks the PR, it can be merged straight away and there is nothing to wait for.
			- You need write access to the repository to turn auto-merge on for a PR.
		- **For codekiln's repos:** on [[2026-11-23 Mon]], `codekiln/logseq-encode-garden` already had `allow_auto_merge: true`, so the greyed-out option in the screenshot came from another repository where the box is not ticked.
		- **Unverified:** whether the Code tab caches the repository flag. If **Merge when ready** stays greyed out right after you tick the box, reopening the PR menu or restarting the session should load it again.
