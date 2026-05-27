alias:: [[user]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # user
	- **Official description:** Grants read/write access to profile info (includes `user:email` and `user:follow` when scopes are normalized).
	- **Subscopes:**
		- [[GitHub/Auth/OAuth/Scope/read:user]]
		- [[GitHub/Auth/OAuth/Scope/user:email]]
		- [[GitHub/Auth/OAuth/Scope/user:follow]]
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s user`
		- **gh minimum:** no
	- **Typical triggers:**
		- (enrich when needed)
	- **Related:** [[GitHub/Auth/OAuth]]
