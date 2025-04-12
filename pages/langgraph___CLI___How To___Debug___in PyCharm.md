# How to create a [[PyCharm/Run Configuration]] to debug `langgraph dev`
	- ## [[see-also]]
		- [[langgraph/GitHub/Discussion/25/04/How to use langgraph dev in a PyCharm Debugger]]
			- **Run Configuration Type** - Python
			- **Virtual Environment** - Select your project's virtual environment
			- **Run Configuration Subtype** - `script`
			- **Script Path**: absolute path to the `langgraph` executable within the virtualenv, found with `which langgraph`
				- (anyone know how to make this more dynamic? just putting in `langgraph` yields `FileNotFoundError: [Errno 2] No such file or directory: 'langgraph'`
			- **Script Parameters**: `dev`
				- no need for `--debug-port`, which is for  [[Py/debugpy]]  instead of PyCharm's  [[pydevd]]