logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[GitHub/CLI/Q/Using the gh cli, is there a quick way to list repositories with globs for user and repo name?]]

- # What's the most idiomatic way to use `gh search repos` while also displaying primary language and number of stars in a table?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** use `--json fullName,language,stargazersCount` with `--template` and `gh`'s `tablerow`/`tablerender` extensions to [[Go/StdLib/text/template]] — no `jq` required.
			- ~~~bash
			  gh search repos "your query" \
			    --sort stars \
			    --limit 30 \
			    --json fullName,language,stargazersCount \
			    --template '{{tablerow "REPO" "LANGUAGE" "STARS"}}{{range .}}{{tablerow .fullName .language .stargazersCount}}{{end}}{{tablerender}}'
			  ~~~
			- `{{tablerender}}` at the end is required — omitting it skips column padding/alignment. `tablerow`/`tablerender` are `gh`-specific additions; run `gh help formatting` for the full reference.
			- **Field name gotchas** (REST search API naming differs from GraphQL):
				- `stargazersCount` (plural, with `s`) — not `stargazerCount`
				- `language` (plain string, `""` when undetected) — not `primaryLanguage`
				- `fullName` (`"owner/repo"`) — not `nameWithOwner`
			- **`--sort stars` is not the default** — without it results sort by best-match relevance.
			- **`--limit` caps at 100** per invocation; no native pagination beyond that.
			- `jq` alternative (useful for downstream processing or null-guarding):
				- ~~~bash
				  gh search repos "your query" --sort stars --limit 30 \
				    --json fullName,language,stargazersCount \
				    | jq -r '["REPO","LANGUAGE","STARS"],
				        (.[] | [.fullName, (if .language == "" then "(none)" else .language end), (.stargazersCount | tostring)])
				        | @tsv' \
				    | column -t
				  ~~~
			- See [gh search repos — GitHub CLI Manual](https://cli.github.com/manual/gh_search_repos) and [cli/cli discussion #8556](https://github.com/cli/cli/discussions/8556).
