alias:: [[mise/Lockfile]]

- [mise.lock Lockfile | mise-en-place](https://mise.jdx.dev/dev-tools/mise-lock.html)
	- `mise.lock` is a lockfile that pins exact versions and checksums of tools for reproducible environments. Lockfiles are not created automatically—you must run `mise lock` to generate them. Once a lockfile exists, mise will keep it updated as tools are installed or upgraded.