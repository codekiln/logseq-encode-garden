# TODO In LangGraph, is the entire graph a single [[LangChain/Runnable]], and if so, do I need to prefix the configurable if I want to use more than one model in the graph, for example, in different nodes?
	- It seems like each node assembles its own runnable independently, in which case I wouldn't necessarily have to prefix models in [[LangChain/chat_models/init_chat_model]] if I wanted to use just one model per node
	-
	-