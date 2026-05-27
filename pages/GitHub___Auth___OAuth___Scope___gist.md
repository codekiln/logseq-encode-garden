alias:: [[gist]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]]

- # gist
	- **Official description:** Grants write access to gists.
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s gist` (usually already present after login)
		- **gh minimum:** cannot remove with `--remove-scopes`
	- **Typical triggers:**
		- `gh gist create` and other gist write operations
		- Part of the default minimum scope set for [[GitHub/CLI]] stored credentials
	- **Related:** [[GitHub/CLI/How to/Create a Gist on GitHub from the command line]], [[GitHub/Auth/OAuth]]
