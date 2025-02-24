- [Getting Started | mise-en-place](https://mise.jdx.dev/getting-started.html)
- ## #Install
	- #brew
		- `brew install mise`
- ## `exec` and `run`
	- `mise` can be used to install and run [tools](https://mise.jdx.dev/dev-tools/), launch [tasks](https://mise.jdx.dev/tasks/), and manage [environment variables](https://mise.jdx.dev/environments/).
	- ```
	  $ mise exec python@3 -- python
	  mise hint use multiple versions simultaneously with mise use python@3.12 python@3.11
	  mise hint installing precompiled python from astral-sh/python-build-standalone
	  if you experience issues with this python (e.g.: running poetry), switch to python-build by running mise settings python.compile=1
	  mise python@3.13.2 ✓ installed                                                                                                                                                 mise WARN  missing: node@18.20.7
	  Python 3.13.2 (main, Feb 12 2025, 14:59:08) [Clang 19.1.6 ] on darwin
	  Type "help", "copyright", "credits" or "license" for more information.
	  >>> exit()
	  
	  $ mise exec node@22 -- node -v
	  v22.14.0
	  ```
	- [`mise x|exec`](https://mise.jdx.dev/cli/exec.html) is a powerful way to load the current `mise` context (tools & environment variables) without modifying your shell session or running ad-hoc commands with mise tools set. Installing [`tools`](https://mise.jdx.dev/dev-tools/) is as simple as running [`mise use|u`](https://mise.jdx.dev/cli/use.html).
	- ### set a global default in the mise config
		- ```
		  $ mise use --global node@22   
		  mise ~/.config/mise/config.toml tools: node@22.14.0
		  mise exec -- node my-script.js
		  # run my-script.js with node 22...
		  ```
	- ### [[mise/run]]
		- Another useful command is [`mise r|run`](https://mise.jdx.dev/cli/run.html) which allows you to run a [`mise task`](https://mise.jdx.dev/tasks/) or a script with the `mise` context.
		- #Tip
			- You can set a shell alias in your shell's rc file like `alias x="mise x --"` to save some keystrokes.
- ## [Activate mise](https://mise.jdx.dev/getting-started.html#activate-mise)
	- #Zsh - `echo 'eval "$(mise activate zsh)"' >> ~/.zshrc`
		- #note - I got `mise WARN  missing: python@3.12.1` the first time, then I did `RUST_BACKTRACE=1 mise exec python@3.12.1 -- python` and it worked thereafter
	-