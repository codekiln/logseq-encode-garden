logseq-entity:: [[Logseq/Entity/Question]]
- # Are `:cd` and `:pwd` built-in vim commands that do something different than the shell version of `cd` and `pwd`?
	- ## [[AI Answer]]
		- `:cd` and `:pwd` are Vim/Neovim built-in Ex commands. They read and change Neovim's own notion of a current working directory, not the working directory of the shell process that launched Neovim.
		- `:cd` sets that directory globally for the whole Neovim session by default. `:tcd` scopes the change to the current tab, and `:lcd` scopes it to the current window; both take priority over the global directory within their scope.
		- Changing Neovim's working directory does not run the shell's `cd`, so a terminal open in a different pane or a shell command run with `:!` still sees the directory the shell started in, unless that shell has its own `cd` run separately.
		- `:pwd` prints whichever directory currently applies to the active window: its `:lcd` value if set, otherwise its tab's `:tcd` value if set, otherwise the global `:cd` value.
