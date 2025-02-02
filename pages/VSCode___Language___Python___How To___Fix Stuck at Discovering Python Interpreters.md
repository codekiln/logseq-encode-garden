- log [[2024/Trimester/t3/w17/d3]] - [[Wed, 2024/12/25]] - debugging [[VSCode/Language/Python]] and [[VSCode/Extension/Python]] - [[VSCode/Proj/24t3/LearnVSCode/03 Basic Python]]
	- 13:12 - I debugged this for over two hours today while working through ((676c263c-2b13-40b2-8626-d83b0ac63c04))
	- I got stuck on configuring the interpreter after installing [[VSCode/Extension/Python]]. I tried everything. Here's what worked.
	- ## Problem Summary
		- When I upgraded from [[Macbook/Myron]] to [[Macbook/Myriad]], going from [[Chips/amd/intel64]] to [[Chips/arm/M2]], I had a bunch of old virtualenvs that pointed to versions of python that were broken on my machine. In addition, I had many old projects that used outdated, broken versions of python on my machine.
		- When VSCode's python extensions start up, they try to introspect into the environment to see what virtualenvs are available. In order to support the widest market, the startup script searches for all the known and supported kinds of virtual environments. Unfortunately, it appears that if **even one of the versions of python or one of the [[Python/Virtualenv]]s errors out during VS Code's startup, it breaks the whole environment discovery process**.
		- This is not generally well-known in the VS Code community, as far as I can tell. The only reason I figured this out was because of a [comment that LazarusX left on the vscode-python github issue here](https://github.com/microsoft/vscode-python/issues/23303#issuecomment-2090639469):
			- > It's migrated from my last machine, and only used a few years ago. **I have no idea why it's scanned as a potential environment**. However, IMO, there could be enhancement for this situation, because **a broken environment should not block the entire interpreter discovery process**. I also believe there is sort of regression here, because the extension used to work fine in spite of the broken environment.
		- ### Solution Summary
	- ## Key Technique - trace logs in the output panel of VS Code
		- I saw that the VS Code team was very active about responding to bug reports, but they always needed a user to get the trace or debug python logs. This technique helped me figure out what my problem was.
			- ### #VSCode #Keyshort to open the output view in the View menu > Output #card
			  card-last-interval:: 375.25
			  card-repeats:: 7
			  card-ease-factor:: 2.48
			  card-next-schedule:: 2026-01-27T14:58:46.021Z
			  card-last-reviewed:: 2025-01-17T08:58:46.021Z
			  card-last-score:: 5
				- `Shift Cmd U`
				- ![image.png](../assets/image_1735150607578_0.png){:height 352, :width 264}
				- [[Mnemonic]]s:
					- O**U**TPUT
					- If something went wrong, you're going to need to do a **U** Turn and look at the output logs
			- ### Select the Python menu in the View > Output window to view [[VSCode/Language/Python]] logs
				- ![image.png](../assets/image_1735150704242_0.png){:height 507, :width 154}{:height 507, :width 154}
				- AFAICT there isn't a keyboard shortcut for this step.
			- ### Select the Settings Cog logo in the right menu portion of the Output View and select `trace`
				- ![image.png](../assets/image_1735150851803_0.png){:height 323, :width 194}
			-
	- ## Steps Taken
		- ### Uninstall any unneeded [[VSCode/Extension]]s including all python and jupyter extensions such as [[VSCode/Extension/Python]]
			- ```
			    414  code --list-extensions --show-versions\n
			    415  code --uninstall-extension vue.volar
			    416  code --list-extensions --show-versions\n
			  ```
		- ### Destroy [[Pyenv/virtualenv]] associated with the project I was working on; [[GitP/acolyte]]
			- I removed `.python-version` files and also removed the pyenv virtualenv
			- ```
			    424  pyenv virtualenv-delete gitp-acolyte
			    425  ls -la
			    426  rm -rf .python-version
			    427  rm -rf gitp-acolyte/.python-version
			  ```
		- ### Reset [[Poetry]]
			- ### Reinstall Poetry using the official installer
				- [Poetry Installation](https://python-poetry.org/docs/main/#installing-with-the-official-installer)
				- ```
				    432  curl -sSL https://install.python-poetry.org | python3 -
				  ```
				- Note that this script installs it into a virtualenv located in `~/Library/Application Support/pypoetry` (where the config also is; see below)
			- ### Install [[Poetry/Shell/Zsh/OhMyZsh]] integration with [[Zsh/OhMyZsh]]
				- ```
				    438  vim ~/.zshrc # I had to add
				    439  . ~/.zshrc
				    440  poetry --version
				    441  mkdir $ZSH_CUSTOM/plugins/poetry
				    442  poetry completions zsh > $ZSH_CUSTOM/plugins/poetry/_poetry\n
				    443  vim ~/.zshrc
				    444  . ~/.zsrhc
				  ```
			- ### Reset Poetry Config
				- I had blindly tried many different [[Poetry/Configuration]]s ([poetry configurations](https://python-poetry.org/docs/main/configuration/)) while trying to debug this issue:
					- ```
					  (gitp-acolyte)  ✘ Me@Home  ~/dev/gitpa/gitp-acolyte  ↱ cc/04-host-n-dist/03-ai-ep-yml  history | grep "poetry config"
					    112  poetry config virtualenvs.prefer-active-python true\n
					    385  poetry config virtualenvs.in-project true
					    395  poetry config virtualenvs.in-project false
					    447  poetry config virtualenvs.prefer-active-python true
					    456  poetry config --list
					  ```
						- note that `poetry config virtualenvs.in-project` set to both `true` and `false` were advocated for here
							- [python - VSCode doesn't show poetry virtualenvs in select interpreter option - Stack Overflow](https://stackoverflow.com/questions/59882884/vscode-doesnt-show-poetry-virtualenvs-in-select-interpreter-option) (asked 4 years ago, 188 votes up)
						- I tried `virtualenvs.prefer-active-python true` because of this confusing page in the [[Pyenv/Docs/Managing-Environments]]:
							- [Managing environments | Documentation | Poetry - Python dependency management and packaging made easy](https://python-poetry.org/docs/managing-environments/)
								- > **If you use a tool like [pyenv](https://github.com/pyenv/pyenv) to manage different Python versions**, you can set the experimental `virtualenvs.prefer-active-python` option to `true`. Poetry will then try to find the current `python` of your shell.
								- > For instance, if your project requires a newer Python than is available with your system, a standard workflow would be:
									- > `pyenv install 3.9.8`
									- > `pyenv local 3.9.8`
									- > `poetry install`
							- Ok, that definitely makes it seem like that's a good way to go for pyenv. However, what this actually does is not intuitive. And I ended up seeing some people who actually removed the configuration to solve it (which would have removed the default value of false)
								- [`poetry env info` does not respect `virtualenvs.prefer-active-python = true` setting · Issue #5947 · python-poetry/poetry](https://github.com/python-poetry/poetry/issues/5947) [[GitHub/python-poetry/poetry/Issue]]
									- Note, after all the steps below, my results were different from the OP here in that they were the same whether I ran `poetry run poetry env info` or if I ran `poetry env info`
										- ```
										  (gitp-acolyte)  Me@Home  ~/dev/gitpa/gitp-acolyte  ↱ cc/04-host-n-dist/03-ai-ep-yml  poetry run poetry env info                            
										  
										  Virtualenv
										  Python:         3.13.1
										  Implementation: CPython
										  Path:           /Users/Me/.pyenv/versions/3.13.1/envs/gitp-acolyte
										  Executable:     /Users/Me/.pyenv/versions/3.13.1/envs/gitp-acolyte/bin/python
										  Valid:          True
										  
										  Base
										  Platform:   darwin
										  OS:         posix
										  Python:     3.13.1
										  Path:       /Users/Me/.pyenv/versions/3.13.1
										  Executable: /Users/Me/.pyenv/versions/3.13.1/bin/python3.13
										  (gitp-acolyte)  Me@Home  ~/dev/gitpa/gitp-acolyte  ↱ cc/04-host-n-dist/03-ai-ep-yml  poetry env info                      
										  
										  Virtualenv
										  Python:         3.13.1
										  Implementation: CPython
										  Path:           /Users/Me/.pyenv/versions/3.13.1/envs/gitp-acolyte
										  Executable:     /Users/Me/.pyenv/versions/3.13.1/envs/gitp-acolyte/bin/python
										  Valid:          True
										  
										  Base
										  Platform:   darwin
										  OS:         posix
										  Python:     3.13.1
										  Path:       /Users/Me/.pyenv/versions/3.13.1
										  Executable: /Users/Me/.pyenv/versions/3.13.1/bin/python3.13
										  ```
				- These configurations are stored in a toml file; [see Configuration | Poetry](https://python-poetry.org/docs/main/configuration/)
					- > This file can typically be found in one of the following directories:
					    * macOS: `~/Library/Application Support/pypoetry`
				- I read many articles and forum posts about using poetry with pyenv, and they all seemed to give contradictory advice. But the thing that ended up working for me was removing the customizations to the config that I did by removing this dir. In particular, I removed these customizations because
					- ```
					  (gitp-acolyte)  Me@Home  ~/dev/gitpa/gitp-acolyte  ↱ cc/04-host-n-dist/03-ai-ep-yml  history | grep "pypoetry"     
					    176  emulate bash -c '. /Users/Me/Library/Caches/pypoetry/virtualenvs/gitp-acolyte-kfI6rJB7-py3.13/bin/activate'
					    361  emulate bash -c '. /Users/Me/Library/Caches/pypoetry/virtualenvs/gitp-acolyte-kfI6rJB7-py3.13/bin/activate'
					    458  ls ~/Library/Application Support/pypoetry
					    459  ls "~/Library/Application Support/pypoetry"
					    460  ls ~/Library/Application\ Support/pypoetry
					    461  vim ~/Library/Application\ Support/pypoetry
					    462  rm -rf ~/Library/Application\ Support/pypoetry/config.toml
					  ```
				- These changes stuck (after the below)...
					- ```
					  (gitp-acolyte)  Me@Home  ~/dev/gitpa/gitp-acolyte  ↱ cc/04-host-n-dist/03-ai-ep-yml  ls -la ~/Library/Application\ Support/pypoetry/
					  total 8
					  drwxr-xr-x@   4 Me  staff   128 Dec 25 12:48 .
					  drwxr-xr-x  179 Me  staff  5728 Dec 13 07:24 ..
					  -rw-r--r--@   1 Me  staff     5 Dec 25 12:29 VERSION
					  drwxr-xr-x@   7 Me  staff   224 Dec 25 12:29 venv
					  ```
		- ### Recreate the [[GitP/acolyte]] [[Pyenv/virtualenv]] and specify the pyenv global version to be 3.13.1
			- ```
			    449  pyenv virtualenv 3.13.1 gitp-acolyte
			    452  pyenv local gitp-acolyte
			    453  pyenv which python
			    469  pyenv global 3.13.1
			  ```
		- ### Uninstall all unneeded python versions with [[Pyenv]] and their [[Pyenv/virtualenv]]s
			- The first part of the solution was to uninstall all old virtual environments and old versions of python.
			- ```shell
			  #!/bin/bash
			  
			  # Get list of virtualenvs in ~/.virtualenvs
			  old_virtualenvs=$(ls ~/.virtualenvs)
			  
			  # Get list of pyenv-managed virtualenvs
			  pyenv_virtualenvs=$(pyenv virtualenvs --bare)
			  
			  # Loop through each virtualenv in ~/.virtualenvs
			  for env in $old_virtualenvs; do
			      # Check if it's managed by pyenv-virtualenv
			      if ! echo "$pyenv_virtualenvs" | grep -q "^$env$"; then
			          echo "Deleting unused virtualenv: $env"
			          rm -rf ~/.virtualenvs/"$env"
			      fi
			  done
			  
			  ```
			- ```
			    473  pyenv versions
			    474  pyenv uninstall 3.5.6
			    475  pyenv uninstall 3.6.7
			    476  pyenv versions
			    477  pyenv uninstall 3.7.1
			    478  pyenv versions
			    479  pyenv uninstall 3.9.6
			    480  pyenv uninstall 3.12.0
			    481  pyenv versions
			    482  ls -la /Users/Me/.pyenv/versions/
			    483  ls -la ~/.virtualenvs/
			    485  touch scripts/clean_virtualenvs.sh
			    486  chmod +x scripts/clean_virtualenvs.sh
			    487  vscr scripts/clean_virtualenvs.sh
			    488  ./scripts/clean_virtualenvs.sh
			    490  ls -la /Users/Me/.virtualenvs/
			    491  rm -rf ~/.virtualenvs/2023-11-26\ Sun\ Chiaroscurro\ Project
			    493  pwd
			    494  poetry install
			    495  poetry env info --path
			    496  poetry env info --executable | pbcopy
			  ```
		- ### Reinitialize [[Poetry]] inside [[GitP/acolyte]]
			- 494  poetry install
		- ### Start VS Code and reinstall [[VSCode/Extension/Python]]; associate it with the pyenv virtualenv that poetry install installed to
			- 495  poetry env info --path
			   496  poetry env info --executable | pbcopy
			- now I did `Cmd Shift P` in #VSCode and did `Python: Select Interpreter` and then entered in the path to the virtualenv. It started working.
			-