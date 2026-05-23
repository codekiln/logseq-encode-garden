alias:: [[mise File Task Groups]]

- # [mise file task groups](https://mise.jdx.dev/tasks/file-tasks.html#task-grouping)
	- Mise file tasks can be grouped into folders:
		- ```
		  mise-tasks
		  ├── build
		  └── test
		      ├── _default
		      ├── integration
		      └── units
		  ```
	- After that, running the [[mise/tasks]] command will show the groups separated by `:`
		- ```
		  mise tasks
		  Name              Description Source
		  build                         ./mise-tasks/build
		  test                          ./mise-tasks/test/_default
		  test:integration              ./mise-tasks/test/integration
		  test:units                    ./mise-tasks/test/units
		  ```