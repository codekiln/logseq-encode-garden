alias:: [[Person/Tim Abell/GitHub/gitopolis]]
tags:: [[CLI/Tool]], [[Rust]]

- [timabell/gitopolis: Manage multiple git repositories - CLI tool - run commands, clone, and organize repos with tags](https://github.com/timabell/gitopolis?tab=readme-ov-file)
	- Example UI
		- ```
		  gitopolis --help
		  A CLI tool for managing multiple git repositories
		  License: A-GPL v3.0
		  Repo: https://github.com/rustworkshop/gitopolis
		  
		  Usage: gitopolis <COMMAND>
		  
		  Commands:
		    add     Add one or more git repos to manage
		    remove  Remove one or more git repos from gitopolis's list. Leaves actual repo on filesystem alone
		    list    Show list of repos gitopolis knows about. Use "long" to see tags and urls (tab separated format)
		    exec    Run any shell command. E.g. `gitopolis exec -- git pull`. Double-dash separator indicates end of gitopolis's arguments and prevents arguments to your commands being interpreted by gitopolis
		    tag     Add/remove repo tags. Use tags to organise repos and allow running commands against subsets of the repo list. Supports comma-separated tag lists (e.g., "tag1,tag2,tag3")
		    tags    List known tags. Use "long" to list repos per tag
		    clone   Clone repository from URL and add to gitopolis, or clone all configured repos from .gitopolis.toml. This command behaves in two very different ways depending on whether a remote url was provided: If URL is provided: clones from that URL, extracts repo name, adds to gitopolis (optionally with tags). If URL is omitted: clones all repos from .gitopolis.toml (filtered by --tag if specified) skipping existing folders. (Useful for setting up new machines/developers from an existing team configuration)
		    sync    Sync remotes between git repositories and .gitopolis.toml configuration
		    show    Show detailed information about a repository including tags and remotes
		    move    Move a repository to a new location, updating gitopolis configuration
		    help    Print this message or the help of the given subcommand(s)
		  
		  Options:
		    -h, --help     Print help
		    -V, --version  Print version
		  ```
	- See [[Person/Tim Abell/Blog/25/10/Using Gitopolis to Manage Multiple Git Repositories]] for impetus
		- [[tldr]]
			- like [[GitHub/Desktop]] but more systematic, for a collection of [[git/repo]]s
			- See [[Person/Tim Abell/GitHub/cloner]] for a quick way to use [[gh]] to get a config that looks like https://gist.githubusercontent.com/timabell/87add070a8a44db4985586efe380757d/raw/08be5b3c38190eeed4fda0060818fa39f3c67ee3/.gitopolis.toml from your github repos (public and private)