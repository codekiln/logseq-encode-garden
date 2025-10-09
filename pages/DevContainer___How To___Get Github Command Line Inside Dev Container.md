- [GitHub CLI on devcontainer - DEV Community](https://dev.to/r7kamura/github-cli-on-devcontainer-3od7) - how to get [[GitHub/CLI]] in a [[DevContainer]]
	- To use the [GitHub CLI](https://cli.github.com/) (a.k.a. `gh`)  on devcontainer, you need to pass credentials for that.
	  
	  If you run `gh auth login` on the host side, the credentials will be stored at `~/.config/gh/hosts.yml`, so mounting it on the container side will work.
	  
	  Maybe it can be difficult to include this setting in `docker-compose.yml` since it is the developer's preference whether to use `gh` and devcontainer or not. In such case, it would be nice to add that setting to `docker-compose.override.yml`, and ignore these files from Git.
	  
	  ```
	  # docker-compose.override.yml
	  services:
	    rails:
	      volumes:
	        - ~/.config/gh/hosts.yml:/root/.config/gh/hosts.yml
	  ```
	  
	  ```
	  # .gitignore or .git/info/exclude
	  docker-compose.override.yml
	  .devcontainer/devcontainer.json
	  ```
	  
	  Normally, `docker-compose` command will automatically merge `docker-compose.override.yml` into `docker-compose.yml`, but in this case you need to specify it explicitly as follows:
	  
	  ```
	  # .devcontainer/devcontainer.json
	  {
	    "name": "Rails",
	    "dockerComposeFile": [
	      "../docker-compose.yml",
	      "../docker-compose.override.yml"
	    ],
	    "service": "rails",
	    "workspaceFolder": "/workspace",
	    "runServices": ["rails"]
	  }
	  ```