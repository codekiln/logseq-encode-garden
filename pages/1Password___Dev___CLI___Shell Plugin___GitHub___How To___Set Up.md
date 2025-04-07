alias:: [[1Password/Dev/How To/Set up the 1Password GitHub Shell Plugin]]

- # [How to set up the 1Password GitHub shell plugin](https://developer.1password.com/docs/cli/shell-plugins/github/) for authenticating the [[GitHub/CLI]] with a [[GitHub Fine-Grained Access Token]]
	- [[My Notes]]
		- Takes about 5 min depending how many of the prerequisites are already met
		- I didn't realize this before, but the process of initializing the plugin in your [[zsh/.zshrc]] or your [[Shell/Config/dotfile]] will set it up so that it uses [[op/run]]. It's pretty slick.
		- The linked instructions above are sufficient and also flexible
			- for example, they enable using more than one github account and using different tokens for each - [learn how to set up your plugin to use multiple accounts](https://developer.1password.com/docs/cli/shell-plugins/multiple-accounts/)
		- Basic process
			- `$ op plugin init gh`
			- Locate the token
				- `? Locate your GitHub Personal Access Token: Search in 1Password...` select, hit enter
				- `? Locate your GitHub Personal Access Token: Expand search...` select, hit enter
					- you'll see a bunch of options. This is a [[Curses]]-style interface and you can start typing the name of your item in 1Password to locate the token
			- If necessary, rename certain fields of the 1Password item to match expectations of the plugin
				- ```
				  op: The "<1PASSWORD_NAME_FOR_GH_TOKEN>" item does not follow required item structure for credential type Personal Access Token:
				      token              Token used to authenticate to GitHub.
				      host (optional)    The GitHub host to authenticate to. Defaults to 'github.com'.
				  
				  To continue, you'll have to update the field names. This can be done interactively. Proceed? [Y/n] y
				  ? op: Select the field to be renamed to "token": credential
				  
				  ? op: Select the field to be renamed to "host": hostname
				  
				  ```
			- Conclusion and setting up [[Shell/alias]] for [[gh]]
				- ```
				  Your 1Password item has been successfully updated. It can now be used with GitHub CLI.
				  ? Configure when the chosen credential(s) will be used to authenticate: Prompt me for each new terminal session
				  
				  The last step is to set up an alias for gh.
				  You can do so by running the following command:
				  
				    echo "source /Users/Me/.config/op/plugins.sh" >> ~/.zshrc && source ~/.zshrc
				  
				  Afterwards, run any gh command to see it in action!
				  ```
	- ## Prerequisites
		- [[1Password/Desktop]] installed and authenticated
		- [[1Password/Dev/CLI]] installed and activated in desktop
		- [[GitHub/Auth/How To/Create a Fine Grained Personal Access Token]] done and stored in 1Password
	-
		-