alias:: [[read:user]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # read:user
	- **Official description:** Grants read access to a user's profile data.
	- **Parent scope:** [[GitHub/Auth/OAuth/Scope/user]]
	- **Implied by:** [[GitHub/Auth/OAuth/Scope/user]] (normalized away if both requested)
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s read:user`
		- **gh minimum:** no
	- **Typical triggers:**
		- (enrich when needed)
	- **Related:** [[GitHub/Auth/OAuth]]
