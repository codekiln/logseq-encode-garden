# `langgraph_sdk.client.LangGraphClient.runs.stream` - from `langgraph_sdk.client.RunsClient` takes a `stream_mode` parameter
	- [[langgraph/sdk/schema/StreamMode]] `langgraph_sdk.schema.StreamMode`
		- ```python
		  StreamMode = Literal[
		      "values", "messages", "updates", "events", "debug", "custom", "messages-tuple"
		  ]
		  """
		  Defines the mode of streaming:
		  - "values": Stream only the values.
		  - "messages": Stream complete messages.
		  - "updates": Stream updates to the state.
		  - "events": Stream events occurring during execution.
		  - "debug": Stream detailed debug information.
		  - "custom": Stream custom events.
		  """
		  ```
	-