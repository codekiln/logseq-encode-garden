- `XDG_CONFIG_HOME` is an environment variable defined by the **XDG Base Directory Specification**. It tells applications where to store **user-specific configuration files**.
- ### Default behavior
- If `XDG_CONFIG_HOME` is **not set**, programs fall back to:
	- ```
	  ~/.config
	  ```
	  So:
	  
	  ```
	  $XDG_CONFIG_HOME/tmux
	  ```
	  
	  usually means:
	  
	  ```
	  ~/.config/tmux
	  ```
	  
	  ---
- ### Why it exists
  
  The XDG spec standardizes where apps put:
- config files
- data files
- cache files
  
  Instead of cluttering `$HOME` with dotfiles like:
  
  ```
  ~/.tmux.conf
  ~/.gitconfig
  ~/.config
  ~/.somethingelse
  ```
  
  apps can use:
  
  ```
  ~/.config/<app>/
  ```
  
  This makes configuration:
- more organized
- easier to back up
- easier to redirect (e.g., in containers or custom setups)
  
  ---
- ### How to check yours
  
  ```
  echo $XDG_CONFIG_HOME
  ```
  
  If it prints nothing, it means you’re using the default `~/.config`.