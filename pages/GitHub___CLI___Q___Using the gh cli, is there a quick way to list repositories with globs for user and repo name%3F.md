logseq-entity:: [[Logseq/Entity/question]]
via:: [[2026-04-03 Fri]]

- # Using the [[GitHub/CLI]] (`gh`), is there a quick way to list repositories with globs for user and repo name?
	- ## My Notes
		- This might be a place where [[gh/dash]] shines ... need to check that out.
	- ## Answer
		- [[AI/Response]]
			- [[gh/repo/list]]
				- **No built-in shell-style globs.** `gh repo list` accepts at most one `<owner>` (user or org) and has no flags to glob owners or repository names. You filter **after** listing or use **`gh search repos`** with GitHub’s search syntax (qualifiers and keywords), which is **not** the same as `*` / `?` filename globs.
				- **One owner, pattern-match names with `jq`:** list JSON and select with a regex (closest to a “repo name glob” in practice).
					- ~~~
					  gh repo list myorg --limit 1000 --json nameWithOwner \
					    -q '.[] | select(.nameWithOwner | test("^myorg/my-.*"; "i")) | .nameWithOwner'
					  ~~~
			- [[gh/repo/search]]
				- **Search across GitHub (or narrow by owner):** `gh search repos` uses the REST search API — combine `user:LOGIN`, `org:ORG`, or `--owner=…` with terms and `in:name` for name-oriented matches. See [GitHub CLI manual — `gh search repos`](https://cli.github.com/manual/gh_search_repos) and [Searching for repositories](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories).
			- [[gh/repo/list]] in loop or [[gh/api]] call
				- **Many owners:** loop over owners and run `gh repo list`, or drive [`gh api`](https://cli.github.com/manual/gh_api) / GraphQL if you need something `repo list` cannot express.