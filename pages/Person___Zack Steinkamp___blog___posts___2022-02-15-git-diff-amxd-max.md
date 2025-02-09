tags:: [[c74/M4L]]

- # [Making 'git diff' Work For .amxd](https://steinkamp.us/posts/2022-02-15-git-diff-amxd-max)
	- id:: 67a8be1a-780f-4c61-82e5-c04cfae63cc6
	  > `.amxd` files are basically JSON, but with a non-JSON file header. This binary part at the beginning makes git fall back to binary file mode when trying to show diffs. Usualy that's not very helpful.
	- `echo '*.amxd binary diff=amxd' > ~/.gitattributes`
	- `git config --global core.attributesfile ~/.gitattributes`
	- then, in `~/.gitconfig`
		- ```
		  [diff "amxd"]
		    textconv = awk '(NR>1)'
		    binary = true
		  ```
	- > In this case, we're using `awk` to suppress printing the first line. That's good enough for my uses, but if you are an `awk` wizard and you want to use a tool like `jq` to work with the JSON data, perhaps you can suppress everything to the initial `{` on that first line.