tags:: [[Idea/My]]

- # Aichat -
	- [[My Notes]]
		- [[2025-05-08 Thu]]
			- Aichat would be a meta-library that would serve as an interface to connect collections of small AI applications written in various agentic AI libraries to a delivery mechanism that is a chat provider. It would abstract out the connections between between libraries for chat back-ends and libraries for AI back-ends so that any AI back-end can be used with any chat back-end.
			- This library is motivated by experience building [[AI/Apps]] that connect [[langgraph]] applications for [[StreamIO/Chat]] delivery.
				- StreamIO is a composable communication infrastructure platform, that is, an in-app communications SDK provider. It is a service that has a well-defined API for how to make a chat application (see [Backend - Python Chat Messaging Docs](https://getstream.io/chat/docs/python/?language=python); they also have over a dozen SDKs in different languages).
					- It was designed in the era before AI was really popular, so it was designed to solve a different problem than most AI apps. There are many competitors to StreamIO, but it's the one I'm most familiar with. It's important to note that StreamIO isn't just about chat. It is a [[CPaaS]], and it offers SDKs for real time multi-channel video, audio and notifications alongside its chat-centric features.
				- [langgraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/) is one of many frameworks for agentic AI apps. There are many competitors there, too.
			- So I'm going to articulate this idea in terms of StreamIO Chat, and LangGraph.
				- I want to use the