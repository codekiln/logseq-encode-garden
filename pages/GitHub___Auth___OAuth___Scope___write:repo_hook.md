alias:: [[write:repo_hook]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # write:repo_hook
	- **Official description:** Grants read, write, and ping access to hooks in public or private repositories.
	- **Parent scope:** [[GitHub/Auth/OAuth/Scope/admin:repo_hook]]
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s write:repo_hook`
		- **gh minimum:** no
	- **Typical triggers:**
		- (enrich when needed)
	- **Related:** [[GitHub/Auth/OAuth]]
