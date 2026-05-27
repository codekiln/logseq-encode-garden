alias:: [[workflow]]
see-also:: [[GitHub/Auth/OAuth/Scope]], [[GitHub/CLI]], [[GitHub/Action]]

- # workflow
	- **Official description:** Grants the ability to add and update GitHub Actions workflow files. Workflow files can be committed without this scope if the same file (same path and contents) already exists on another branch in the same repository. Workflow runs may expose `GITHUB_TOKEN` with a different permission set.
	- **gh CLI**
		- **Request:** `gh auth refresh -h github.com -s workflow`
		- **gh minimum:** no
	- **Typical triggers:**
		- Push or commit changes under `.github/workflows/` when using [[GitHub/CLI]] or git over HTTPS with credentials from `gh auth login`
		- API or CLI operations that create or update workflow YAML without an existing identical file on another branch
		- Error messages asking for the `workflow` scope when publishing Actions definitions
	- **Related:** [[GitHub/Action]], [[GitHub/CLI/EnvVar/GH_TOKEN]], [[GitHub/Auth/OAuth]]
