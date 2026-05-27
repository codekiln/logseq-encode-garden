alias:: gh
tags:: [[CLI/Tool]]

- # `gh` command
	- [Manual | GitHub CLI](https://cli.github.com/manual/)
	- [announced in early 2020](https://github.blog/2020-02-12-supercharge-your-command-line-experience-github-cli-is-now-in-beta/)
	- ## [Installation](https://github.com/cli/cli#installation)
		- `brew install gh`
		- ### Authentication
			- `gh auth login` - quick start, global
			- [[GitHub/Auth/OAuth/Scope]] — OAuth scope catalog; add scopes with `gh auth refresh -h github.com -s <scope>` (e.g. [[GitHub/Auth/OAuth/Scope/workflow]])
			- [[GitHub/Auth/OAuth]] — normalization, `gh auth status`, minimum scopes `repo`, `read:org`, `gist`
			- [[GitHub/CLI/EnvVar/GH_TOKEN]]
				- `Alternatively, populate the GH_TOKEN environment variable with a GitHub API authentication token.`
				- See also [[GitHub/CLI/Q/Is it possible to scope gh CLI permissions by directory or repo]]
	- ## Extensions
		- [[GitHub/CLI/Extension]]
		-