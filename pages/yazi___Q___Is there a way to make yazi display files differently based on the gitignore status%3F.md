logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[yazi/Q/Does yazi have a git integration that copies a file path relative to the repository root? If so, what is the keyshort?]]

- # Is there a way to make [[yazi]] display files differently based on the [[gitignore]] status?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** Yes — via the official `git.yazi` plugin from the [yazi-rs/plugins](https://github.com/yazi-rs/plugins/tree/main/git.yazi) repository, which adds per-file git status badges including a distinct style for gitignored files.
			- **Install the plugin:**
				- ~~~sh
				  ya pkg add yazi-rs/plugins:git
				  ~~~
			- **Register fetchers in `~/.config/yazi/yazi.toml`:**
				- ~~~toml
				  [[plugin.prepend_fetchers]]
				  id    = "git"
				  url   = "*"
				  run   = "git"
				  group = "git"
				  
				  [[plugin.prepend_fetchers]]
				  id    = "git"
				  url   = "*/"
				  run   = "git"
				  group = "git"
				  ~~~
			- **Initialize in `~/.config/yazi/init.lua`:**
				- ~~~lua
				  require("git"):setup {
				      order = 1500,
				  }
				  ~~~
			- The plugin runs `git status --porcelain --ignored=matching` and displays a badge next to each file. Gitignored files get a **`darkgray`** foreground by default (via the `!!` porcelain prefix).
			- **Customize the ignored-file appearance** in `~/.config/yazi/theme.toml`:
				- ~~~toml
				  [git]
				  ignored      = { fg = "darkgray", dim = true }
				  ignored_sign = "!"
				  ~~~
			- **Caveat — fd hides gitignored files by default:** [[yazi]] uses `fd` for directory listing and `fd` itself respects `.gitignore`, so gitignored files won't appear in the listing at all unless you configure yazi to show them. There is no built-in `show_gitignored` toggle; the workaround is to pass `--no-ignore` to `fd` via manager config or to accept that the badge only shows up on files fd does list. See [issue #1655](https://github.com/sxyazi/yazi/issues/1655) for context (closed as not planned).
			- Sources: [git.yazi plugin README](https://github.com/yazi-rs/plugins/tree/main/git.yazi), [issue #1655](https://github.com/sxyazi/yazi/issues/1655)
