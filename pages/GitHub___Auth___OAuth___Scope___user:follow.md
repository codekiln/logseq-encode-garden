alias:: [[user:follow]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # user:follow
	- **Official description:** Grants access to follow or unfollow other users.
	- **Parent scope:** [[GitHub/Auth/OAuth/Scope/user]]
	- **Implied by:** [[GitHub/Auth/OAuth/Scope/user]] (normalized away if both requested)
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s user:follow`
		- **gh minimum:** no
	- **Typical triggers:**
		- (enrich when needed)
	- **Related:** [[GitHub/Auth/OAuth]]
