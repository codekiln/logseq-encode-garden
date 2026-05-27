alias:: [[user:email]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # user:email
	- **Official description:** Grants read access to a user's email addresses.
	- **Parent scope:** [[GitHub/Auth/OAuth/Scope/user]]
	- **Implied by:** [[GitHub/Auth/OAuth/Scope/user]] (normalized away if both requested)
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s user:email`
		- **gh minimum:** no
	- **Typical triggers:**
		- (enrich when needed)
	- **Related:** [[GitHub/Auth/OAuth]]
