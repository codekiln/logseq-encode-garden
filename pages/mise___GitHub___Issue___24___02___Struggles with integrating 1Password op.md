created-by:: [[Person/Randy Syring]]

- # [Struggles with integrating 1Password's op · Issue #1617 · jdx/mise](https://github.com/jdx/mise/issues/1617)
	- References [[mise/GitHub/Discussion/24/01/Vaults and Secrets Management]] for broader discussion on secrets management
	- most of the discussion here is actually **about how to load secrets from 1password into the environment** upon changing directories, which is **not** what I'm interested in
	- The poster [[Person/Randy Syring]] works for a software firm called [level12](https://www.level12.io/), and as of [[2025/01]] they ended up building and using an in-house but [[Open Source]] solution, [[level12/GitHub/env-config]].
		- ((67dfd3a1-5848-4bef-a0b3-fbca1ff319e6))
			- This doesn't seem like what I'm looking for. I don't want to put secrets in my environment. I want secrets to be used at runtime.
	- ## Summary
		- ### Core Challenge
			- [[1Password/Dev/op]] CLI integration with mise faces performance issues
			- Takes ~1 second to resolve secrets, which is problematic when run on every prompt
		- ### Current Working Solution with [[direnv]]
			- Configuration using two files:
				- ~~~toml
				  # .mise.toml
				  [env]
				  TF_VAR_wasabi_access_key = 'op://private/aws/access-key'
				  TF_VAR_wasabi_secret_key = 'op://private/aws/secret-key'
				  ~~~
				- ~~~bash
				  # .envrc
				  direnv_load op run --no-masking -- direnv dump
				  watch_file .mise.toml
				  ~~~
		- ### Attempted Solutions
			- #### 1. Using `_.source` in mise
				- Approach:
					- ~~~toml
					  [env]
					  TF_VAR_wasabi_access_key = 'op://private/aws/access-key'
					  TF_VAR_wasabi_secret_key = 'op://private/aws/secret-key'
					  _.source = 'op-run.sh'
					  ~~~
				- Issue: Gets executed on every prompt
			- #### 2. Lua Plugin POC
				- Created `mise_env.lua` hook
				- Successfully modified environment vars
				- Same issue: Executes on every prompt
		- ### Key Problems
			- Environment variables not getting removed when leaving directory
			- Multiple executions per prompt
			- No caching mechanism like [[direnv]] has
		- ### Potential Solutions Discussed
			- [[@jdx]] noted:
				- Shell environment variables persist between prompts
				- Only need to track sources, not values
			- Suggestion for `mise refresh` command for manual re-resolution
		- ### Current Status
			- Issue moved to discussion for further exploration
			- [[direnv]] remains the recommended approach for now