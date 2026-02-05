# How do I switch between [[tmux]] sessions?
	- ## Answer
		- ### Option 1: Switch from Within Tmux (Easiest)
			- Use the `switch-client` command:
				- ~~~
				  tmux switch-client -t session-name
				  ~~~
			- Or the shorter version:
				- ~~~
				  tmux switch -t GL
				  tmux switch -t logseq
				  tmux switch -t main-work-coding
				  ~~~
			- You can also use the built-in session switcher: `Prefix+s` (shows interactive list)
		- ### Option 2: Detach Then Attach
			- Detach from the current session:
				- ~~~
				  tmux detach
				  ~~~
			- Or press: `Prefix+d`
			- Then attach to another:
				- ~~~
				  tmux attach -t GL
				  tmux attach -t logseq
				  ~~~
		- ### Option 3: Direct Attach (From Outside Tmux)
			- If you're not in a tmux session:
				- ~~~
				  tmux attach -t session-name
				  ~~~
			- Or shorter:
				- ~~~
				  tmux a -t GL
				  ~~~
		- ### Quick List Your Sessions
			- ~~~
			  tmux list-sessions
			  ~~~
			- Or shorter:
				- ~~~
				  tmux ls
				  ~~~
	- ## Recommendation
		- Use `Prefix+s` for the nicest interactive experience — it shows all your sessions and windows in a tree view where you can navigate with arrow keys and press Enter to switch.
