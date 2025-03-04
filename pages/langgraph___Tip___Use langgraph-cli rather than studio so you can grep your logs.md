# Use [[langgraph/CLI]] rather than [[langgraph/Studio]] in order to be able to grep the logs
	- For some reason, LangGraph Studio doesn't let you search over all the logs. As a result, debugging issues is tedious.
	- A #Workaround is to launch `langgraph build` and `langgraph up` from the #CLI - but [[LangGraph Assistants]] and the "manage configuration" won't work
	-