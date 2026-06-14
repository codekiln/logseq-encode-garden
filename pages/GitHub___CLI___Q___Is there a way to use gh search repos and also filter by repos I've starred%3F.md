logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[GitHub/CLI/Q/What's the most idiomatic way to use gh search repos while also displaying primary language and number of stars in a table?]]

- # Is there a way to use `gh search repos` and also filter by repos I've starred?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** No — `gh search repos` uses the GitHub search API which has no "starred by me" qualifier. Use `gh api /user/starred` instead.
			- `gh search repos` flags include `--owner`, `--language`, `--stars`, `--topic`, etc., but there is no `--starred` flag and the underlying GitHub search API does not expose a "repos I've starred" filter.
			- **Alternative: `gh api /user/starred`**
				- ~~~bash
				  gh api /user/starred --paginate \
				    --jq '.[] | [.full_name, .language, (.stargazers_count | tostring)] | @tsv' \
				  | column -t
				  ~~~
				- This hits the [REST `GET /user/starred`](https://docs.github.com/en/rest/activity/starring?apiVersion=2022-11-28#list-repositories-starred-by-the-authenticated-user) endpoint, which returns all repos you have starred (paginated).
				- `--paginate` fetches all pages automatically; omit it to get only the first 30.
			- **Combining both** — if you want to search within your starred repos by keyword, there is no single command. The closest workaround is:
				- ~~~bash
				  gh api /user/starred --paginate --jq '.[].full_name' \
				  | grep -i "keyword"
				  ~~~
			- See [gh api — GitHub CLI Manual](https://cli.github.com/manual/gh_api) and [GitHub REST docs: List repositories starred by the authenticated user](https://docs.github.com/en/rest/activity/starring?apiVersion=2022-11-28#list-repositories-starred-by-the-authenticated-user).
