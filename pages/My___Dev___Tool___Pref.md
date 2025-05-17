alias:: [[My Dev Tool Preferences]]

- # My #[[Dev]] #[[Tool]] #Preferences (at the moment)
	- always use established, documented best practices
	- use [[mise]] for managing environments and tools
		- [[Secrets Management]]
			- use [[1Password/Dev/op/run]] and put [[1Password Secret References]] in [[.env]] or [[mise/Config/mise.toml]]
		- [[Python]]
			- use [[pyproject.toml]]
			- [[Package Manager]]
				- [[uv]] - current top preference
				- [[Poetry]] - secondary preference
			- use latest "bugfix" python version, AKA "pre-prerelease", e.g. [[Python 3.13]] [at the moment](https://devguide.python.org/versions/)
			- use [[Py/asyncio]] and related
			- [[Software/Testing]]
				- use [[Pytest]]
					- use [[Pytest/Fixture]]s
					- separate integration from unit tests by folder, for example:
						- ```
						  my-package/
						    my_package/
						      my_module.py
						    tests/
						      conftest.py
						      integration/
						        my_package/
						          test_my_module.py
						      unit/
						        my_package/
						          test_my_module.py
						  
						  ```
			- [[Linting]], [[Programming/Language/Formatter]]
				- [[Ruff]] for both, using [[Py/Lib/black]] and [[Py/Lib/isort]] under the hood
			- [[Server/Side]]
				- [[FastAPI]] - For most things powered by APIs
				- [[Django]] - For exceptional scenarios - monoliths and getting things done with the greatest modularity and "opinionated batteries included"
		- [[NodeJS]]
			- prefer to use the latest [[NodeJS/LTS]] version
			- prefer [[Typescript]]
			- [[Client/Side]]
				- [[React]] - current top preference
				- [[VueJS]] - secondary preference
		- [[Documentation]]
			- utilize [[Logseq]] sub-folder with [[Markdown]] inside a [[GitHub/Repo]]
		-