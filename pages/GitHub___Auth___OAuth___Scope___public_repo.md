alias:: [[public_repo]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # public_repo
	- **Official description:** Limits access to public repositories: code, commit statuses, projects, collaborators, deployment statuses; required to star public repositories.
	- **Parent scope:** [[GitHub/Auth/OAuth/Scope/repo]]
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s public_repo`
		- **gh minimum:** no
	- **Typical triggers:**
		- (enrich when needed)
	- **Related:** [[GitHub/Auth/OAuth]]
