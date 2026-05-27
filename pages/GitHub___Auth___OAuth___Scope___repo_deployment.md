alias:: [[repo_deployment]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # repo_deployment
	- **Official description:** Grants access to deployment statuses for public and private repositories without granting access to code.
	- **Parent scope:** [[GitHub/Auth/OAuth/Scope/repo]]
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s repo_deployment`
		- **gh minimum:** no
	- **Typical triggers:**
		- (enrich when needed)
	- **Related:** [[GitHub/Auth/OAuth]]
