# DOING  solve #Error - "no precompiled python found for <REPONAME>, force mise to use a version with `mise settings set python.compile false`
	- ## DOING original error - while running [[mise/Task/LLM/copy_buffer_bundle]]
		- ```
		  mise run llm:copy_buffer_bundle                         
		  mise WARN  no precompiled python found for codekiln, force mise to use a precompiled version with `mise settings set python.compile false`
		  python-build: definition not found: codekiln
		  mise ERROR ~/Library/Caches/mise/python/pyenv/plugins/python-build/bin/python-build failed
		  python-build: definition not found: codekiln
		  mise ERROR failed to install core:python@codekiln
		  mise ERROR ~/Library/Caches/mise/python/pyenv/plugins/python-build/bin/python-build exited with non-zero status: exit code 2
		  mise ERROR Run with --verbose or MISE_VERBOSE=1 for more information
		  ```
		- ## research #C35S
			- ### Root Cause
				- Both tools use similar mechanisms to manage Python versions
				- Both modify PATH and use shims to intercept Python commands
				- When both are active, they conflict in reading `.python-version` files
			- ### Immediate Solutions
				- Option A: Disable Python compilation in mise
					- ```bash
					  mise settings set python.compile false
					  ```
				- Option B: Remove .python-version files and use mise's configuration
					- ```bash
					  rm .python-version
					  mise use python@<version>
					  ```
				- Option C: Configure mise to ignore [[Pyenv/.python-version]] files
					- Add to `~/.config/mise/config.toml`:
					- ```toml
					  [settings]
					  # idiomatic_version_file is true by default, so we only need to specify which tools to disable
					  idiomatic_version_file = true
					  # disable reading of .python-version files while still allowing other version files (e.g. .nvmrc)
					  # see: https://mise.jdx.dev/configuration.html
					  idiomatic_version_file_disable_tools = ['python']
					  ```
						- #[[Observation/My]] - *this technique could also be used to handle similar issues with [[nvm/.nvmrc]]*
			- ### Long-term Recommendations
				- Choose one tool as the primary Python version manager
					- If migrating to mise: Remove pyenv configuration from shell startup files
					- If keeping pyenv: Configure mise to ignore Python version management
				- For mise-managed projects
					- Use `mise.toml` for version configuration instead of `.python-version`
					- Consider running `mise sync python` to import existing pyenv installations
			- ### Prevention
				- Remove or comment out pyenv initialization in shell config files
				- Use mise's built-in Python version management features exclusively
	- ## DONE other observed behavior - `mise WARN  missing: python@codekiln`
	  collapsed:: true
		- in directories that use [[Pyenv/.python-version]], upon starting up a new shell, `mise` is repeatedly issuing a #Warning
			- ```
			  mise WARN  missing: python@codekiln
			  mise WARN  missing: python@codekiln
			  mise WARN  missing: python@codekiln
			  mise WARN  missing: python@codekiln
			  mise WARN  missing: python@codekiln
			  mise WARN  missing: python@codekiln
			  mise WARN  missing: python@codekiln
			  ```
		- ### Update - likely cause of repeated warnings was a mistaken entry in `.zshrc`
		  collapsed:: true
			- Somehow, my [[zsh/.zshrc]] ended up with this - probably because I needed more coffee when installing mise, LOL
				- ```
				  echo 'eval "$(mise activate zsh)"' >> ~/.zshrc
				  ```
				- As a result, my `.zshrc` was adding mise activate on every shell spawn - DOH!
				- after removing that, this behavior went away.
	-