tags:: [[c74/M4L]]

- # [Making 'git diff' Work For .amxd](https://steinkamp.us/posts/2022-02-15-git-diff-amxd-max)
	- `echo '*.amxd binary diff=amxd' > ~/.gitattributes`
	- `git config --global core.attributesfile ~/.gitattributes`
	- then, in `~/.gitconfig`
		- ```
		  [diff "amxd"]
		    textconv = awk '(NR>1)'
		    binary = true
		  ```
	-