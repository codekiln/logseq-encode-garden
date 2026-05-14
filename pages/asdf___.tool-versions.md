- `.tool-versions` asdf [config file](https://asdf-vm.com/manage/configuration.html#tool-versions)
	- can be in the home directory to express global dependencies, or it can be in a project to express project dependencies.
	- Edit the file directly or use `asdf set` which updates it.
	- ```
	  ruby 2.5.3 # This is a comment
	  # This is another comment
	  nodejs 10.15.0
	  # fallbacks
	  python 3.7.2 2.7.15 system
	  ```