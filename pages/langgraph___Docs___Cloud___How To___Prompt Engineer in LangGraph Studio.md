# [Prompt Engineering in LangGraph Studio](https://langchain-ai.github.io/langgraph/cloud/how-tos/iterate_graph_studio/)
	- ## [[My Notes]]
	  id:: 67e5b7bc-41be-4c32-805b-45731ed912e6
		- Great way to let you customize the model and the LLM for each node!
			- {{embed ((67e5b74c-1671-4e93-9568-c6fa5bde68e3))}}
			- {{embed ((67e5b7e8-472e-420d-905c-4161ac34ea50))}}
	- ### Reference [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/iterate_graph_studio/#reference)
		- > When defining your configuration, you can use special metadata keys to instruct LangGraph Studio how to handle different fields.
		- #### `langgraph_nodes` [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/iterate_graph_studio/#langgraph_nodes)
			- **Description**: Specifies which graph nodes a configuration field is associated with.
			- **Value Type**: Array of strings, where each string is the name of a node in your graph.
			- **Usage Context**: Include in the `json_schema_extra` dictionary for Pydantic models or the `metadata["json_schema_extra"]` dictionary for dataclasses.
			- **Required**: No, but necessary if you want a field to be editable for specific nodes in the UI.
			- ##### #Example
				- ```python
				  system_prompt: str = Field(
				      default="You are a helpful AI assistant.",
				      json_schema_extra={"langgraph_nodes": ["call_model", "other_node"]},
				  )
				  ```
		- #### `langgraph_type` [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/iterate_graph_studio/#langgraph_type)
			- **Description**: Specifies the type of configuration field, which determines how it's handled in the UI.
			- **Value Type**: String
			- **Supported Values**:
			- `"prompt"`: Indicates the field contains prompt text that should be treated specially in the UI.
			- **Usage Context**: Include in the `json_schema_extra` dictionary for Pydantic models or the `metadata["json_schema_extra"]` dictionary for dataclasses.
			- **Required**: No, but helpful for prompt fields to enable special handling.
			- ##### #Example
				- ```python
				  system_prompt: str = Field(
				      default="You are a helpful AI assistant.",
				      json_schema_extra={
				          "langgraph_nodes": ["call_model"],
				          "langgraph_type": "prompt",
				      },
				  )
				  ```
	- ## Iterating on prompts [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/iterate_graph_studio/#iterating-on-prompts)
		- ### Node Configuration [¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/iterate_graph_studio/#node-configuration)
			- With this set up, running your graph and viewing in LangGraph Studio will result in the graph rendering like such.
			- **Note the configuration icon in the top right corner of the `call_model` node**:
			  id:: 67e5b74c-1671-4e93-9568-c6fa5bde68e3
				- ![little configure button!](https://langchain-ai.github.io/langgraph/cloud/how-tos/img/studio_graph_with_configuration.png)
			- Clicking this icon will open a modal where you can edit the configuration for all of the fields associated with the `call_model` node. From here, you can save your changes and apply them to the graph.
			- **Note that these values reflect the currently active assistant, and saving will update the assistant with the new values.**
			  id:: 67e5b7e8-472e-420d-905c-4161ac34ea50
				- ![pop-up configuration!](https://langchain-ai.github.io/langgraph/cloud/how-tos/img/studio_node_configuration.png)