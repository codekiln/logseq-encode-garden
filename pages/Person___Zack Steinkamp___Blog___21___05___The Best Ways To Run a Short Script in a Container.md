created-by:: [[Person/Zack Steinkamp]]
date-created:: [[21/05]]
tags:: [[Blog/Post]]

- # [The Best Ways To Run a Short Script in a Container](https://steinkamp.us/posts/2021-05-10-script-in-container)
	- ## [[My Notes]]
		- [[Person/Zack Steinkamp]] describes two ways to run script/CLI-style tasks from the shell via [[Docker]] without maintaining a separate Dockerfile and compose/runner script for each task.
		- **containerscript**: Single Bash script that inlines the Dockerfile, build/run commands, and the script to run (see [Gist](https://gist.github.com/zsteinkamp/7235cebd34166a12ef0ba3bb1bae3758)).
		- **Turdokken**: Shebang-line tool; install in `$PATH` and use as shebang so scripts declare dependencies (e.g. `--install mysql-client`) and run in a container. Repo: [[GitHub/zsteinkamp/turdokken]].
	- ## `dockerscript`
		- One Bash script defines the Dockerfile, Docker build/run commands, and the script to run. Replace the `cmd()` function and adjust the `FROM` line or `RUN` commands for dependencies.
		- [[Example]] [[GitHub/Gist]]
			- [dockerscript - A single bash script that bootstraps a container, then runs itself inside that container. Use any "FROM" line. The only requirement is that /bin/bash is present. See also [Turdokken](https://github.com/zsteinkamp/turdokken).](https://gist.github.com/zsteinkamp/7235cebd34166a12ef0ba3bb1bae3758)
	- ## [[GitHub/zsteinkamp/turdokken]]
		- If one uses `turdokken` as the shebang, then scripts run in a container with declared dependencies.
		- Install Turdokken in `$PATH`; shebang must be `#!/usr/bin/env -S turdokken`.
		- Example script:
			- ~~~
			  #!/usr/bin/env -S turdokken --install mysql-client
			  
			  mysql --version
			  uname -a
			  echo $HOST_USERNAME
			  echo $@
			  ~~~
		- Running `./myscript.sh foo bar` runs the script inside a container that has `mysql-client` installed; Turdokken builds the image, runs the container, mounts the script, and invokes it with bash. You can mount local files for reading or modification.
		-