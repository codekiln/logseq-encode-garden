logseq-entity:: [[Logseq/Entity/CLI/Command]]
tags:: [[mise/Commands]]

- # [mise settings](https://mise.jdx.dev/cli/settings.html) command
	- Show current settings
	- This is the contents of [[mise/Config/Global]]
	- Note that aliases are also stored in this file but managed separately with `mise tool-alias`
	- Usage: `mise settings [OPTIONS] [SETTING] [VALUE] [COMMAND]`
	- Commands:
		- add    Adds a setting to the configuration file
		- get    Show a current setting
		- ls     Show current settings [aliases: list]
		- set    Add/update a setting [aliases: create]
		- unset  Clears a setting [aliases: rm, remove, delete, del]
		- help   Print this message or the help of the given subcommand(s)
	- Arguments:
		- [SETTING]
			- Name of setting
		- [VALUE]
			- Setting value to set
	- Options:
		- -a, --all
			- List all settings
		- Standard / Global Options
			- -J, --json
				- Output in JSON format
			- -l, --local
				- Use the local config file instead of the global one
			- -T, --toml
				- Output in TOML format
			- --json-extended
				- Output in JSON format with sources
			- -C, --cd <DIR>
				- Change directory before running command
			- -E, --env <ENV>
				- Set the environment for loading `mise.<ENV>.toml`
			- -j, --jobs <JOBS>
				- How many jobs to run in parallel [default: 8]
				- [env: MISE_JOBS=]
			- -q, --quiet
				- Suppress non-error messages
			- -v, --verbose...
				- Show extra output (use -vv for even more)
			- -y, --yes
				- Answer yes to all confirmation prompts
			- --raw
				- Read/write directly to stdin/stdout/stderr instead of by line
			- --locked
				- Require lockfile URLs to be present during installation
				- Fails if tools don't have pre-resolved URLs in the lockfile for the current platform.
				- This prevents API calls to GitHub, aqua registry, etc.
				- Can also be enabled via MISE_LOCKED=1 or settings.locked=true
			- --silent
				- Suppress all task output and mise non-error messages
			- -h, --help
				- Print help (see a summary with '-h')
	- [[Examples]]
		- ```
		  # list all settings
		  $ mise settings
		  
		  # get the value of the setting "always_keep_download"
		  $ mise settings always_keep_download
		  
		  # set the value of the setting "always_keep_download" to "true"
		  $ mise settings always_keep_download=true
		  
		  # set the value of the setting "node.mirror_url" to "https://npm.taobao.org/mirrors/node"
		  $ mise settings node.mirror_url https://npm.taobao.org/mirrors/node
		  ```