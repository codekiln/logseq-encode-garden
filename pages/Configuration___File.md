tags:: [[Term]]
alias:: [[Configuration File]], [[.conf file]]

- # Configuration File
	- ## [[Unix/Convention]]s
		- ### [[dotfiles]] conventions - `~/.<app>.conf`
		  collapsed:: true
			- traditional behavior
				- Historically:
				- Config lived directly in `$HOME`
				- Files were prefixed with `.` to keep them hidden
				- Example:
					- ```
					  ~/.tmux.conf
					  ~/.vimrc
					  ~/.gitconfig
					  ```
			- The “dot hides files” behavior:
				- Originated in early [[Unix]] (1970s)
				- Was implemented in the [[ls]] [[CLI/Tool]]
				- Is now standard in all Unix-like systems:
					- [[Linux]]
					- [[MacOS]] (Darwin/BSD)
					- [[BSD]]
					- [[Solaris]]
		- ### [[XDG]] conventions - `~/.config/<app>/<app>.conf`
		  collapsed:: true
			- XDG moved config files into [[dot/config]] (or the value of [[XDG/EnvVar/XDG_CONFIG_HOME]]
				- ```
				  ~/.config/<application>/
				  ```
			- Since:
			- The directory itself (`.config`) is already hidden
			- Each application gets its own subdirectory
			- In this case ==There’s **no need** to hide the filename itself.==
			- So instead of:
				- ```
				  ~/.tmux.conf
				  ```
			- You get:
				- ```
				  ~/.config/tmux/tmux.conf
				  ```
		- ### [[Local/File]] or [[Local/Override]] files
		  collapsed:: true
			- The `.local` suffix is a long-standing Unix convention meaning:
			  
			  > “Local customizations layered on top of upstream defaults.”
			- You’ll see similar patterns in:
				- `/etc/foo.conf` + `/etc/foo.conf.local`
				- `/etc/profile` + `/etc/profile.local`
				- `/etc/apache2/apache2.conf` + `/etc/apache2/conf.d/*.conf`
				- vim: `vimrc` + `vimrc.local`
			- zsh frameworks with `*.local` overrides
			- It’s a **layering strategy**, not a standard.
-