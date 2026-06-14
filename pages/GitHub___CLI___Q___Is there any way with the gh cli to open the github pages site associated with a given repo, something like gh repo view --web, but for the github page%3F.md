logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[GitHub/Pages]], [[GitHub/CLI/gh/browse]]
- # Is there any way with the gh cli to open the github pages site associated with a given repo, something like `gh repo view --web`, but for the github page?
	- ## [[AI Answer]]
		- [[AI/Response]]
		- **Short answer:** No built-in command exists, but you can get the Pages URL via `gh api` and pipe it to `open` (macOS) or `xdg-open` (Linux).
		- `gh browse` has flags like `--wiki`, `--settings`, and `--releases` but no `--pages` flag.
		- The GitHub Pages API endpoint returns a `html_url` field for enabled Pages sites:
			- ~~~bash
			  # Get the Pages URL for the current repo
			  gh api "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/pages" --jq '.html_url' | xargs open
			  ~~~
			- ~~~bash
			  # Or for a specific repo
			  gh api repos/{owner}/{repo}/pages --jq '.html_url' | xargs open
			  ~~~
		- If the repo does not have GitHub Pages enabled, the API returns a 404 error.
		- If the site uses a custom domain, `html_url` returns that custom domain rather than `<owner>.github.io/<repo>`.
		- A shell alias to wrap this:
			- ~~~bash
			  alias gh-pages-open='gh api "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/pages" --jq ".html_url" | xargs open'
			  ~~~
