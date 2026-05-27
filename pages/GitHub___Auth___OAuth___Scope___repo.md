alias:: [[repo]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]], [[GitHub/Repo]]

- # repo
	- **Official description:** Grants full access to public and private repositories including read and write access to code, commit statuses, repository invitations, collaborators, deployment statuses, and repository webhooks. Also grants managing organization-owned resources (projects, invitations, team memberships, webhooks) and user-owned projects.
	- **Subscopes:**
		- [[GitHub/Auth/OAuth/Scope/repo:status]]
		- [[GitHub/Auth/OAuth/Scope/repo_deployment]]
		- [[GitHub/Auth/OAuth/Scope/public_repo]]
		- [[GitHub/Auth/OAuth/Scope/repo:invite]]
		- [[GitHub/Auth/OAuth/Scope/security_events]]
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s repo` (usually already present after login)
		- **gh minimum:** cannot remove with `--remove-scopes`
	- **Typical triggers:**
		- Default scope for most `gh` operations on private repositories (issues, PRs, pushes via gh-assisted auth)
		- Required baseline alongside [[GitHub/Auth/OAuth/Scope/read:org]] and [[GitHub/Auth/OAuth/Scope/gist]] for stored `gh` credentials
	- **Related:** [[GitHub/Auth/OAuth]], [[GitHub/Repo]]
