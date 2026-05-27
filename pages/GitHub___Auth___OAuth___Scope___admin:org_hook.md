alias:: [[admin:org_hook]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # admin:org_hook
	- **Official description:** Grants read, write, ping, and delete access to organization hooks (OAuth tokens only on hooks created by the same OAuth app).
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s admin:org_hook`
		- **gh minimum:** no
	- **Typical triggers:**
		- (enrich when needed)
	- **Related:** [[GitHub/Auth/OAuth]]
