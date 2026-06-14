logseq-entity:: [[Logseq/Entity/Question]]
- # Using ghq, what's the easiest way to cd to the local repo if it exists? [[card]]
	- ## [[AI Answer]]
		- [[AI/Response]]
		- Short answer: pipe `ghq list --full-path` through `grep` to get the path, then `cd` to it.
		- ~~~bash
		  cd "$(ghq list --full-path | grep -m 1 <repo-name>)"
		  ~~~
		- For exact owner/repo matching, `ghq list` output is in `owner/repo` form — combine with `ghq root` or use `--full-path`:
		- ~~~bash
		  # Exact owner/repo, full path
		  cd "$(ghq list --full-path | grep -m 1 owner/repo)"
		  ~~~
		- To guard against the repo not existing locally (silent no-op instead of a `cd` error):
		- ~~~bash
		  dir="$(ghq list --full-path | grep -m 1 owner/repo)" && [ -d "$dir" ] && cd "$dir"
		  ~~~
		- For interactive fuzzy selection across all local repos, pair with [[fzf]]:
		- ~~~bash
		  cd "$(ghq list --full-path | fzf)"
		  ~~~
		- Note: `ghq look <repo>` (older versions) opened a sub-shell instead of a true `cd`; `ghq list --full-path | grep` is the idiomatic replacement.
