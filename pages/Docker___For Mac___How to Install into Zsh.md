tags:: [[Diataxis/How To]], [[zsh]]

- # DONE How do I get Docker to show up in the Zsh shell after Docker for Mac is installed / updated?
- [[Feb 2nd, 2025]]
	- ## Summary
		- The easiest way to solve this is to go to [[Docker/For Mac/Settings/Advanced]]
			- note that there is NOT a scroll bar, but you need to use the scroll wheel with your mouse in the left sidebar; it's a UI made by back-end developers
		- Then select System, which adds /usr/local/bin [[Docker/CLI]] tools to [[Shell/PATH]]
		- note that while this is working for me right now, [this stackoverflow user claimed that after a subsequent docker update](https://stackoverflow.com/a/78228559/78202), the permissions weren't retained, so they ended up creating a [[zsh/.zshrc]] entry for [[Docker]]
- [[Feb 1st, 2025]]
	- [[zsh]] didn't find it
		- ```
		  docker --version
		  zsh: command not found: docker
		  ```
		- [macos - Docker command not found when running on Mac - Stack Overflow](https://stackoverflow.com/questions/64009138/docker-command-not-found-when-running-on-mac)
		  collapsed:: true
			- top answer
				- > you need to add the `docker` command to your PATH manually. It can be done through profile file. As ZSH is now a default shell on MacOS, it would go to [[zsh/.zprofile]] `~/.zprofile` file:
					- ```
					  # Add Docker Desktop for Mac (docker)
					  export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin/"
					  ```
			- comment 1
				- > Note that recent versions of docker install the CLI in `$HOME/.docker/bin`, and these are just symlinks to the bins in `/Applications/Docker.app/Contents/Resources/bin/`
				- so in theory, I could use `$HOME/.docker/bin` instead...
					- ```
					  ls $HOME/.docker/bin/
					  com.docker.cli                docker-credential-ecr-login   kubectl
					  docker                        docker-credential-osxkeychain kubectl.docker
					  docker-compose                docker-index
					  docker-credential-desktop     hub-tool
					  ```
			- DONE When should I use [[zsh/.zprofile]] vs [[zsh]] #Q
				- **`.zprofile`**:
					- Loaded for **login shells** (i.e., when you log into a system via SSH or TTY).
					- It is equivalent to [[Bash/.bash_profile]].
						- **Bash login shells** use:
							- `.bash_profile` (preferred)
							- If `.bash_profile` is missing, it falls back to `.profile`
							- If neither exists, it may use `/etc/profile`
					- Ideal for environment variables (`export PATH=...`), session-wide settings, and commands that should run **only once** at login.
				- **`.zshrc`**:
					- Loaded for **interactive shells** (i.e., every new terminal session).
					- Equivalent to `.bashrc` in [[Bash/.bashrc]].
					- Used for **shell configuration**, such as aliases, functions, key bindings, and prompt settings.
		- [[Docker/Forum]] [Docker:command not found after installing Docker desktop on Mac - Docker Desktop - Docker Community Forums](https://forums.docker.com/t/docker-command-not-found-after-installing-docker-desktop-on-mac/93837/5) OP [[2020/05]]
		  collapsed:: true
			- comment from [[2023/04]]
				- > Interesting, looks like somehow the settings now install docker as USER instead of SYSTEM so the executables are not included in your PATH by default. I recently moved between Macs and was caught offguard by this change.
				- ![image](https://global.discourse-cdn.com/docker/optimized/3X/a/e/ae44f6a29d23e64133ab6f8aeec18cf549c470d1_2_690x397.png)
				-
					- (original [image](https://global.discourse-cdn.com/docker/original/3X/a/e/ae44f6a29d23e64133ab6f8aeec18cf549c470d1.png))
			- A few comments from later, even the last six months; most users flip to system
			- one comment from [[2025/01]]
				- > Flipping between also worked for me in 2025. This is even after attempting to manually edit my [[zsh/.zshrc]] and bashrc files.
		- [[Docker/Docs/Desktop/Setup/Install/Mac Permission Requirements]]
			- [Understand permission requirements for Docker Desktop on Mac | Docker Docs](https://docs.docker.com/desktop/setup/install/mac-permission-requirements/#installing-symlinks)
				- With version 4.18 and later, **you can choose whether to install symlinks either in `/usr/local/bin` or `$HOME/.docker/bin` during installation of Docker Desktop**.
				- If `/usr/local/bin` is chosen, and this location is not writable by unprivileged users, Docker Desktop requires authorization to confirm this choice before the symlinks to Docker binaries are created in `/usr/local/bin`. If `$HOME/.docker/bin` is chosen, authorization is not required, but then you must [manually add `$HOME/.docker/bin`](https://docs.docker.com/desktop/settings-and-maintenance/settings/#advanced) to their PATH.
			-
-