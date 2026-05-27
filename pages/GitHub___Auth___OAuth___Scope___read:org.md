alias:: [[read:org]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # read:org
	- **Official description:** Read-only access to organization membership, organization projects, and team membership.
	- **Parent scope:** [[GitHub/Auth/OAuth/Scope/admin:org]]
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s read:org` (usually already present after login)
		- **gh minimum:** cannot remove with `--remove-scopes`
	- **Typical triggers:**
		- Listing organizations and teams visible to the authenticated user
		- `gh` commands that resolve org context without needing [[GitHub/Auth/OAuth/Scope/write:org]] or [[GitHub/Auth/OAuth/Scope/admin:org]]
	- **Related:** [[GitHub/Auth/OAuth/Scope/write:org]], [[GitHub/Auth/OAuth]]
