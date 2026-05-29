logseq-entity:: [[Logseq/Entity/CLI/Command]]
see-also:: [[GitHub/CLI]]
- # [gh browse](https://cli.github.com/manual/gh_browse)
	- **Usage:** `gh browse [<number> | <path>] [flags]`
	- Open the repository in the web browser.
		- When given a number, opens the corresponding issue or pull request.
		- When given a path, opens that file or directory in the source code browser.
	- ## Options
		- `-b`, `--branch <string>` — select another branch
		- `--commit` — open the last commit
		- `-n`, `--no-browser` — print the destination URL instead of opening the browser
		- `-p`, `--projects` — open repository projects tab
		- `-r`, `--releases` — open repository releases tab
		- `-s`, `--settings` — open repository settings
		- `-w`, `--wiki` — open repository wiki
	- ## Notes
		- There is no `--pages` flag; to open a repo's [[GitHub/Pages]] site use `gh api` — see [[GitHub/CLI/Q/Is there any way with the gh cli to open the github pages site associated with a given repo, something like gh repo view --web, but for the github page?]]
