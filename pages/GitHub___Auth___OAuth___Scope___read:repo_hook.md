alias:: [[read:repo_hook]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # read:repo_hook
	- **Official description:** Grants read and ping access to hooks in public or private repositories.
	- **Parent scope:** [[GitHub/Auth/OAuth/Scope/admin:repo_hook]]
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s read:repo_hook`
		- **gh minimum:** no
	- **Typical triggers:**
		- (enrich when needed)
	- **Related:** [[GitHub/Auth/OAuth]]
