alias:: [[admin:repo_hook]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # admin:repo_hook
	- **Official description:** Grants read, write, ping, and delete access to repository hooks; use to limit access to hooks only (`repo` / `public_repo` already include hooks).
	- **Subscopes:**
		- [[GitHub/Auth/OAuth/Scope/write:repo_hook]]
		- [[GitHub/Auth/OAuth/Scope/read:repo_hook]]
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s admin:repo_hook`
		- **gh minimum:** no
	- **Typical triggers:**
		- (enrich when needed)
	- **Related:** [[GitHub/Auth/OAuth]]
