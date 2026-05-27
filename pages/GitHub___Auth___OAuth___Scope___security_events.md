alias:: [[security_events]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # security_events
	- **Official description:** Grants read and write access to security events in the code scanning API without granting access to code.
	- **Parent scope:** [[GitHub/Auth/OAuth/Scope/repo]]
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s security_events`
		- **gh minimum:** no
	- **Typical triggers:**
		- (enrich when needed)
	- **Related:** [[GitHub/Auth/OAuth]]
