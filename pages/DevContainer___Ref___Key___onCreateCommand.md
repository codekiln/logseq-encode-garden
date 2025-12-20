- # Key: onCreateCommand
	- ## Description
		- A command that runs when the dev container is created (after the container image is built or pulled, and the container is created and started)
		- Runs only once per container creation, not on every container start
	- ## Type
		- `string` or `array` of strings
	- ## Usage
		- Useful for one-time setup tasks like configuring Git safe directories
		- Example:
			- ~~~
			  "onCreateCommand": "git config --global --add safe.directory ${containerWorkspaceFolder}"
			  ~~~
		- Can also be an array of commands:
			- ~~~
			  "onCreateCommand": [
			    "command1",
			    "command2"
			  ]
			  ~~~
	- ## Context
		- This is a lifecycle hook that runs during container initialization
		- Different from `postCreateCommand` which runs after the container is created and the workspace is opened
		- Different from `postStartCommand` which runs every time the container starts
	- ## Common Use Cases
		- Configuring Git safe directories
		- Setting up global Git configuration
		- Installing dependencies that don't need to be in the image
	- ## Related
		- [[DevContainer/Ref/Variable/containerWorkspaceFolder]] - Variable commonly used with this key
		- [[DevContainer/Ref/Key]] - Index of all keys

