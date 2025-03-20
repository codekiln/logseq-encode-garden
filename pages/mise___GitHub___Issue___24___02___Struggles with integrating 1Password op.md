# [Struggles with integrating 1Password's op · Issue #1617 · jdx/mise](https://github.com/jdx/mise/issues/1617)
	- References [[mise/GitHub/Discussion/24/01/Vaults and Secrets Management]] for broader discussion on secrets management
	- ## Summary
		- ### Core Challenge
			- [[op]] CLI integration with mise faces performance issues
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