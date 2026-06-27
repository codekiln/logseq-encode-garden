alias:: [[GitHub Stars]], [[GitHub Stargazers]], [[Github/Star]]
see-also:: [[GitHub/Star/List]]
- # GitHub Star
	- A GitHub star is a repository-level bookmark, appreciation signal, and public popularity count. The count is exposed in GitHub's UI, search results, GraphQL field `stargazerCount`, REST field `stargazers_count`, and GitHub CLI field `stargazerCount`.
	- A repository's star count is often used as a quick maturity and attention signal: not proof of quality, but useful context alongside recency, issue activity, maintainers, release cadence, license, and fit for the problem.
	- Quick check:
		- ~~~sh
		  gh repo view OWNER/REPO --json stargazerCount --jq .stargazerCount
		  ~~~
	- The people behind the count are still called stargazers. On a public repository, their list is at `https://github.com/OWNER/REPO/stargazers`; the REST API exposes it through `GET /repos/{owner}/{repo}/stargazers`.
	- GitHub's API keeps a historical wrinkle: `watchers`, `watchers_count`, and `stargazers_count` refer to stars, while `subscribers_count` means notification watchers.
	- It includes [[GitHub/Star/List]]s, which help organize starred repositories.
	- ## Cultural history
		- Before 2012, GitHub "watching" mixed two behaviors that wanted to separate: remembering an interesting repository and receiving its notifications. GitHub split the ideas in August 2012, making stars the low-friction bookmark and watch the notification subscription.
		- The star count then became open source's most visible ambient applause meter. It compresses many meanings into one number: curiosity, admiration, intent to evaluate later, dependency trust, community momentum, and sometimes simple collecting.
		- That compression made stars useful and dangerous. Developers routinely glance at star counts when comparing projects, but a high count can reflect fashion, age, visibility, or a viral README as much as maintenance quality.
		- The count also became part of repository presentation. Many READMEs now include badges, "star us" calls to action, or star-growth charts that show adoption over time. The growth curve tells a different story than the total: a slow long tail, a launch spike, a conference bump, a Hacker News wave, or a sudden AI-era rediscovery.
		- Star-history charts turned the count into a tiny cultural graph: projects can show when attention arrived, compare themselves to adjacent tools, and make momentum visible to maintainers, funders, and users.
		- The same visibility made stars gameable. Bought or fake stars are the shadow side of any public popularity metric: useful for discovery, tempting for theater. A star count is a clue, not a verdict.
	- ## Sources
		- GitHub Docs, "Saving repositories with stars": [https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars)
		- GitHub Docs, "REST API endpoints for starring": [https://docs.github.com/en/rest/activity/starring](https://docs.github.com/en/rest/activity/starring)
		- GitHub CLI Manual, `gh repo view`: [https://cli.github.com/manual/gh_repo_view](https://cli.github.com/manual/gh_repo_view)
		- Wired, "GitHub Changes Make It Easier to Track Your Favorite Projects": [https://www.wired.com/2012/08/github-changes-make-it-easier-to-track-your-favorite-projects/](https://www.wired.com/2012/08/github-changes-make-it-easier-to-track-your-favorite-projects/)
		- Hudson Borges and Marco Tulio Valente, "What's in a GitHub Star? Understanding Repository Starring Practices in a Social Coding Platform": [https://arxiv.org/abs/1811.07643](https://arxiv.org/abs/1811.07643)
		- Star History: [https://star-history.com/](https://star-history.com/)
		- Hao He et al., "4.5 Million (Suspected) Fake Stars in GitHub": [https://arxiv.org/abs/2412.13459](https://arxiv.org/abs/2412.13459)
