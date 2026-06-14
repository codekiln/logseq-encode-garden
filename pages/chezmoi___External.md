alias:: [[chezmoi/Externals]], [[chezmoi external]]
tags:: [[chezmoi/Docs]]

- # [chezmoi External Files](https://www.chezmoi.io/user-guide/include-files-from-elsewhere/)
	- chezmoi can manage files that come from external sources (git repos, archives, single files) via `.chezmoiexternal.toml` files
	- ## git-repo type
		- Clones a git repo to a target directory and keeps it updated
		- Declared in a `.chezmoiexternal.toml` file placed in the **parent** of the desired target directory in the chezmoi source
		- ```toml
		  ["<dirname>"]
		    type = "git-repo"
		    url = "https://github.com/user/repo.git"
		    refreshPeriod = "168h"
		  ```
		- `refreshPeriod` controls how often `chezmoi update` runs `git fetch` — `"168h"` = weekly
		- To pin to a specific commit or tag, add `exact = true` and `ref = "<tag-or-sha>"`
	- ## Usage in this dotfiles repo
		- [[oh-my-tmux]] is managed this way
			- Source: `chezmoi/dot_local/share/tmux/.chezmoiexternal.toml`
			- Clones to: `~/.local/share/oh-my-tmux/`
			- See [[oh-my-tmux/Installation]] for the full setup
	- ## Chezmoi symlinks
		- Use a `symlink_<name>` file in the chezmoi source to create a symlink at the target path
		- File contents = the symlink target (can be relative or absolute)
		- Example: `chezmoi/dot_config/tmux/symlink_tmux.conf` containing `../../.local/share/oh-my-tmux/.tmux.conf`
		  creates `~/.config/tmux/tmux.conf → ../../.local/share/oh-my-tmux/.tmux.conf`
