alias:: [[admin:org]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # admin:org
	- **Official description:** Fully manage the organization and its teams, projects, and memberships.
	- **Subscopes:**
		- [[GitHub/Auth/OAuth/Scope/write:org]]
		- [[GitHub/Auth/OAuth/Scope/read:org]]
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s admin:org`
		- **gh minimum:** no
	- **Typical triggers:**
		- (enrich when needed)
	- **Related:** [[GitHub/Auth/OAuth]]
