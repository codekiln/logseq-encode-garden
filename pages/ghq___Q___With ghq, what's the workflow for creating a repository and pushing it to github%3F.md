logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[ghq]], [[gh]]
- # With [[ghq]], what's the workflow for creating a repository and pushing it to github?
- ## Answer
	- [[AI/Response]]
		- **Short answer:** `ghq` handles the local repo location and layout; `gh` handles creating the GitHub remote. A common local-first workflow is:
		- `ghq create github.com/OWNER/REPO`
		- `cd "$(ghq list -p -e github.com/OWNER/REPO)"`
		- add files, then make an initial commit with normal `git add` / `git commit`
		- `gh repo create OWNER/REPO --private --source=. --remote=origin --push` (or `--public`)
		- **Why this works:** the `ghq` manual documents `ghq create <host>/<user>/<project>` for creating a new repository under the managed `ghq.root` directory structure. The `gh repo create` manual documents `--source` for creating a remote from an existing local repository and `--push` for pushing local commits to the new remote.
		- **If you have no commit yet:** create the repo locally with `ghq create`, add at least one commit, then run `gh repo create ... --source=. --push`; otherwise there is nothing meaningful to push.
		- **Alternative remote-first workflow:** if you prefer to create the GitHub repo first, run `gh repo create OWNER/REPO --private`, then `ghq get github.com/OWNER/REPO` (or the full repo URL) to clone it into your `ghq` layout.
		- **Visibility and remote name:** swap `--private` for `--public` or `--internal` as needed; `--remote=origin` is explicit but optional if `origin` is your normal choice.
		- [ghq manual page](https://man.freebsd.org/cgi/man.cgi?query=ghq&sektion=1&manpath=FreeBSD+13.2-RELEASE+and+Ports)
		- [GitHub CLI manual - gh repo create](https://cli.github.com/manual/gh_repo_create)
