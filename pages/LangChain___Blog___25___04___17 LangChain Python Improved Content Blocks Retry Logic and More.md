date-created:: [[2025-04-17 Thu]]
tags:: [[LangChain]], [[Blog]], [[Content-Blocks]], [[Retry-Logic]]

- # LangChain Python Updates: Improved Content Blocks, Retry Logic and More
	- [Original Announcement](https://changelog.langchain.com/announcements/langchain-python-updates-improved-contenet-blocks-retry-logic-and-more)
	- ## Standardized Multimodal Content Blocks
		- [Documentation](https://python.langchain.com/docs/how_to/multimodal_inputs/)
		- Example:
			- ```python
			  from langchain_core.messages import HumanMessage, AIMessage
			  from langchain_core.messages.content import ImageContent, TextContent
			  
			  # Create a message with both text and image content
			  message = HumanMessage(
			      content=[
			          TextContent(text="What's in this image?"),
			          ImageContent(
			              image_url="https://example.com/image.jpg",
			              image_path=None,
			              mime_type="image/jpeg"
			          )
			      ]
			  )
			  ```
	- ## ChatPromptTemplate with Arbitrary Content Blocks
		- [Documentation](https://python.langchain.com/docs/how_to/multimodal_prompts/)
		- Example:
			- ```python
			  from langchain_core.prompts import ChatPromptTemplate
			  from langchain_core.messages import HumanMessage
			  
			  # Create a template that can handle text and images
			  template = ChatPromptTemplate.from_messages([
			      ("human", [
			          {"type": "text", "text": "Describe this image:"},
			          {"type": "image_url", "image_url": "{image_url}"}
			      ])
			  ])
			  
			  # Format the template
			  messages = template.format_messages(
			      image_url="https://example.com/image.jpg"
			  )
			  ```
	- ## Custom [[Programming/Error Handling/Retry Logic/Exponential Backoff]] for Runnable.with_retry
		- [Documentation](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_retry)
		- Example:
			- ```python
			  from langchain_core.runnables import RunnableConfig
			  
			  # Configure custom retry parameters
			  chain_with_retries = chain.with_retry(
			      retry_patterns={
			          "ConnectionError": {
			              "max_attempts": 3,
			              "initial_delay": 1.0,
			              "max_delay": 60.0,
			              "exponential_base": 2.0,
			          }
			      }
			  )
			  ```