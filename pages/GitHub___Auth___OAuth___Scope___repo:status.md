alias:: [[repo:status]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # repo:status
	- **Official description:** Grants read/write access to commit statuses in public and private repositories without granting access to code.
	- **Parent scope:** [[GitHub/Auth/OAuth/Scope/repo]]
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s repo:status`
		- **gh minimum:** no
	- **Typical triggers:**
		- (enrich when needed)
	- **Related:** [[GitHub/Auth/OAuth]]
