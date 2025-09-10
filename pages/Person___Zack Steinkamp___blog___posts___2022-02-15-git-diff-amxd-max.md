tags:: [[c74/M4L]]
created-by:: [[Person/Zack Steinkamp]]

- # [Making 'git diff' Work For .amxd](https://steinkamp.us/posts/2022-02-15-git-diff-amxd-max)
	- [[My Notes]]
		- See also the source material at [steinkamp.us/pages/posts/2022-02-15-git-diff-amxd-max.md at main · zsteinkamp/steinkamp.us · GitHub](https://github.com/zsteinkamp/steinkamp.us/blob/main/pages/posts/2022-02-15-git-diff-amxd-max.md)
	- #Quotes
		- Here's a quick tip if you're using git for revision control in developing Max/MSP or Max For Live devices.
		- Perhaps you have been here?
		- ```bash
		  $ git diff
		  diff --git a/cool.amxd b/cool.amxd
		  index c7a9b88..afdafb1 100644
		  Binary files a/cool.amxd and b/cool.amxd differ
		  ```
		- `.amxd` files are basically JSON, but with a non-JSON file header. This binary part at the beginning makes git fall back to binary file mode when trying to show diffs. Usualy that's not very helpful.
		  
		  There's just a bit of configuration to make the `git diff` output more helpful. Here's what to do:
		- 1. Create a global `.gitattributes` file in your home directory. This will will map the `.amxd` file extension to a named file type that we will use later. Run this command to create the file with the correct contents:
		- ```bash
		  echo '*.amxd binary diff=amxd' > ~/.gitattributes
		  ```
		- 2. Now tell git where to find the new global `.gitattributes` file. Run this command:
		- ```bash
		  git config --global core.attributesfile ~/.gitattributes
		  ```
		- 3. The final step is to tell git how to convert the 'binary' file to text when displaying a diff. Add this content to your `~/.gitconfig` file:
		- ```config
		  [diff "amxd"]
		    textconv = awk '(NR>1)'
		    binary = true
		  ```
		- 3. The final step is to tell git how to convert the 'binary' file to text when displaying a diff. Add this content to your `~/.gitconfig` file:
		- ```config
		  [diff "amxd"]
		    textconv = awk '(NR>1)'
		    binary = true
		  ```
		- In this case, we're using `awk` to suppress printing the first line. That's good enough for my uses, but if you are an `awk` wizard and you want to use a tool like `jq` to work with the JSON data, perhaps you can suppress everything to the initial `{` on that first line.