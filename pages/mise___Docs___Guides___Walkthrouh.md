tags:: [[Tutorial]]

- # DONE [Walkthrough | mise-en-place](https://mise.jdx.dev/walkthrough.html)
- ## [[mise/Config/mise.toml]]
	- commit it to the repo to share
	- use `mise.local.toml` to `.gitignore` for personal preferences
	- ### cascading or nested configurations for `mise.toml`
		- `mise` supports nested configuration files that cascade from broad to specific settings:
			- `~/.config/mise/config.toml` - Global settings for all projects
			- `~/work/mise.toml` - Work-specific settings
			- `~/work/project/mise.toml` - Project-specific settings
			- `~/work/project/mise.local.toml` - Project-specific settings that should not be shared
		- `mise` will use all the parent directories together to determine the set of tools—overriding configuration as it goes lower in the hierarchy.
	- #Tip - Use [[mise/config/ls]] to see the configuration files currently used by mise.
	- ### [[My Notes]] on `mise.toml`
		- [[2025-05-11 Sun]]
			- #### [[CLI command]] to find the currently active mise config #card
				- [[mise/config/ls]] - `mise config ls` - run this to find the currently active mise config
			- Here's a [[mise/Task]] definition for the mise config file which will  use [[mise/config/ls]] to find the currently active mise config and open it in preferred [[IDE]] - (Cursor, here)
				- ```toml
				  [tasks]
				  config = "cursor $(mise config ls | head -n1 | awk '{print $1}' | sed \"s|~|$HOME|\")"
				  ```
- ## Setting [[EnvVar]]s - [[mise/EnvVar]]s
	- #Example - note, this can also be added to [[mise/Config/mise.toml]]
		- ```
		  mise set MY_VAR=123
		  echo $MY_VAR
		  # 123
		  ```
	- Other #Examples of using this
		- Some examples on where this can be used:
		- Setting `NODE_ENV` for a Node.js project
		- Setting `DATABASE_URL` for a database connection
		- Setting `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` for AWS
		- Setting `RUST_TEST_THREADS=1` to run cargo tests in series
		- modify `PATH`
			- ```
			  [env]
			  _.path = "./node_modules/.bin"
			  ```
	- ### [[Lazy Eval]] (after "tools")
		- Environment variables typically are resolved before tools—that way you can configure tool installation with environment variables. However, sometimes you want to access environment variables produced by tools. To do that, turn the value into a map with `tools = true`:
			- ```
			  [env]
			  MY_VAR = { value = "tools path: {{env.PATH}}", tools = true }
			  _.path = { path = ["{{env.GEM_HOME}}/bin"], tools = true } # directives may also set tools = true
			  ```
	- ### Redactions - `redact = true`:
		- ```
		  [env]
		  SECRET = { value = "my_secret", redact = true }
		  _.file = { path = [".env.json"], redact = true }
		  ```
	- ### `env._` directives
		- > Since nested environment variables do not make sense, we make use of this fact by creating a key named "_" which is a TOML table for the configuration of these directives.
		- #### setting a dotenv file
			- here's how to set a dotenv file. here, `_` inside the `env` is a [[TOML/Table]]. Uses [[Rust/Lib/dotenvy]]
			- ```
			  [env]
			  _.file = '.env'
			  ```
			- Set [[mise/EnvVar/MISE_ENV_FILE]] to autoload dotenv files in any directory
		- #### `.env._.path` to specify `PATH`
			- an array
			- ```
			  [env]
			  _.path = [
			      # adds an absolute path
			      "~/.local/share/bin",
			      # adds paths relative to directory in which this file was found (see below for details), not PWD
			      "{{config_root}}/node_modules/.bin",
			      # adds paths relative to the exact file that this is found in (not PWD)
			      "tools/bin",
			  ]
			  ```
			- here, `{{config_root}}` is where `mise.toml` is, I think ... I'm not quite sure where `.config/mise` came from ...
				- > Adding a relative path like `tools/bin` or `./tools/bin` is similar to adding a path rooted at `{{config_root}}`, but behaves differently if your config file is nested in a subdirectory like `/path/to/project/.config/mise/config.toml`. Including `tools/bin` will add the path `/path/to/project/.config/mise/tools/bin`, whereas including `{{config_root}}/tools/bin` will add the path `/path/to/project/tools/bin`.
		- #### sourcing a file to get [[EnvVar]]s - #Cool
			- ```
			  [env]
			  _.source = "./script.sh"
			  ```
	- ### [[mise/Template]]
		- ```
		  [env]
		  LD_LIBRARY_PATH = "/some/path:{{env.LD_LIBRARY_PATH}}"
		  ```
	- using env vars in other env vars, aka [[Transclusion]]
		- ```toml
		  [env]
		  MY_PROJ_LIB = "{{config_root}}/lib"
		  LD_LIBRARY_PATH = "/some/path:{{env.MY_PROJ_LIB}}"
		  ```
- ## [[mise/Task]]s
	- tasks can be defined in [[mise/Config/mise.toml]]
	  collapsed:: true
		- ```toml
		  [tasks]
		  build = "npm run build"
		  test = "npm run test"
		  ```
	- or in your project dir, apparently one can put `mise-tasks/build.sh` and `mise run build` will work just as well
	- collapsed:: true
	  > [[mise/run]] sets up the "mise environment" before running task.
		- ir you activate mise, you don't need to worry about this, but if not, `mise run X` will set up env vars first.
	- ### Task Usage Spec
	  collapsed:: true
		- [[Observation/My]] mise has what appears to be its own language for describing a custom way to invoke a command. much as one can use a makefile, using mise, one can make `mise-tasks/gree` with a shell script like this, and it will set up tab complete and make it so certain CLI arguments are actually created as [[EnvVar]]s.
		- ```sh
		  #!/usr/bin/env bash
		  set -e
		  
		  #MISE description="Greet a user with a message"
		  #USAGE flag "-g --greeting <greeting>" help="The greeting word to use" {
		  #USAGE   choices "hi" "hello" "hey"
		  #USAGE }
		  #USAGE flag "-u --user <user>" help="The user to greet"
		  #USAGE flag "--dir <dir>" help="The directory to greet from" default="."
		  #USAGE complete "dir" run="find . -maxdepth 1 -type d"
		  #USAGE arg "<message>" help="Greeting message"
		  
		  echo "all available options are in the env with the prefix 'usage_'"
		  env | grep usage_
		  
		  echo "$usage_greeting, $usage_user! Your message is: $usage_message"
		  ```
		- Now, `mise run greet --user jdx -g "hey" "How are you?"` will result in `usage_user` env var being set to `jdx` and `usage_greeting` being set to "hey"
		- ```
		  > mise run greet --help
		  [greet] ERROR Usage: greet [FLAGS] <message>
		  
		  Arguments:
		    <message>
		      Greeting message
		  
		  Flags:
		    -g --greeting <greeting>
		      The greeting word to use
		      [possible values: hi, hello, hey]
		    -u --user <user>
		      The user to greet
		    --dir <dir>
		      The directory to greet from
		  ```
		- example run
		  collapsed:: true
			- ```
			  mise run greet --user me -g "hey" "how are you"
			  [greet] $ ~/Documents/GitHub/logseq-encode-garden/mise-tasks/greet --user me -g hey how are you
			  all available options are in the env with the prefix 'usage_'
			  usage_user=me
			  usage_greeting=hey
			  usage_message=how are you
			  usage_dir=.
			  hey, me! Your message is: how are you
			  ```
		- In my testing, the tab completion did not play well with [[Zsh/OhMyZsh]] autocompletions
- ## [Common Commands](https://mise.jdx.dev/walkthrough.html#common-commands) [[mise/Commands]]
  collapsed:: true
	- [[mise/completion]] - Set up completions for your shell
	- [[mise/config]] aka [[mise/cfg]] - A bunch of commands for working with `mise.toml` files via the CLI
	- [[mise/exec]] aka [[mise/x]] - Execute a command in the mise environment without activating mise
	- [[mise/generate]] aka [[mise/g]] - Generates things like git hooks, task documentation, GitHub actions, and more for your project
	- [[mise/install]] aka [[mise/i]] - Install tools
	- [[mise/link]] - Symlink a tool installed by some other means into mise
	- [[mise/ls-remote]] - List all available versions of a tool
	- [[mise/ls]] - Lists information about installed/active tools
	- [[mise/outdated]] - Informs you of any tools with newer versions available
	- [[mise/plugin]] - Plugins can extend mise with new functionality like extra tools or environment variable management
	  collapsed:: true
		- Commonly, these are simply asdf/vfox plugins
	- [[mise/run]] aka [[mise/r]] - Run a task defined in `mise.toml` or `mise-tasks`
	- [[mise/self-update]] - Update mise to the latest version
	  collapsed:: true
		- Don't use this if you installed mise via a package manager
	- [[mise/settings]] - CLI access to get/set configuration settings
	- [[mise/uninstall]] aka [[mise/rm]] - Uninstall a tool
	- [[mise/upgrade]] aka [[mise/up]] - Upgrade tool versions
	- [[mise/use]] aka [[mise/u]] - Install and activate tools
	- [[mise/watch]] aka [[mise/w]] - Watch for changes in a project and run tasks when they occur
	-