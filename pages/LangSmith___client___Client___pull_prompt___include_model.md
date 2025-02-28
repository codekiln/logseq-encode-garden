tags:: @Langchain, @langsmith-py-sdk, @langsmith
# [Client.pull_prompt() — 🦜️🛠️ LangSmith documentation](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client#langsmith.client.Client.pull_prompt)
	- `pull_prompt(prompt_identifier: str, *, include_model: bool | None = False) → Any`
	- ## Overview
		- The `pull_prompt` method is a core functionality of the LangSmith Client that allows you to retrieve prompts stored in LangSmith PromptHub.
		- This method enables seamless integration between your code and prompts managed in LangSmith, facilitating prompt versioning, sharing, and reuse.
	- ## Parameters
		- ### `prompt_identifier: str`
			- A string that uniquely identifies the prompt to retrieve
			- Can be in several formats:
				- Simple name for your own private prompts: `"joke-generator"`
				- With author handle for public prompts: `"username/prompt-name"`
				- With version tag or commit hash: `"joke-generator:v1"` or `"joke-generator:12344e88"`
		- ### `include_model: bool | None = False`
			- When set to `True`, returns the prompt bundled with its associated model configuration
			- When `False` (default), returns only the prompt template
	- ## Model Identification Implications
		- ### How `include_model=True` Works
			- When a prompt is stored with an associated model in PromptHub, setting `include_model=True` will:
				- Return a `RunnableSequence` that combines both the prompt template and the model
				- Automatically configure the appropriate model with the settings stored in PromptHub
				- Enable direct invocation without needing to manually set up the model
			- Example:
				- ```python
				  from langsmith import Client
				  
				  client = Client()
				  # Returns a RunnableSequence of prompt + model
				  chain = client.pull_prompt("structured-output-prompt", include_model=True)
				  # Can be directly invoked
				  result = chain.invoke({"input": "data to process"})
				  ```
		- ### Environment Requirements
			- When using `include_model=True`, you must have:
				- The appropriate model provider package installed (e.g., `langchain_openai`)
				- Required environment variables set (e.g., `OPENAI_API_KEY`)
				- Access permissions to the model specified in the prompt
	- ## Relationship to LangSmith PromptHub
		- ### PromptHub Integration
			- PromptHub serves as a central repository for storing, versioning, and sharing prompts
			- `pull_prompt` is the primary method to retrieve prompts from PromptHub programmatically
			- Enables collaboration across teams by providing access to shared prompt resources
		- ### Versioning Capabilities
			- Supports retrieving specific versions of prompts using tags or commit hashes
			- Facilitates reproducibility by allowing exact prompt versions to be referenced
			- Enables A/B testing by comparing different prompt versions
	- ## Structured Output Applications
		- ### Optimizing for Structured Responses
			- Particularly valuable when working with prompts designed for structured output
			- When combined with `include_model=True`, can pull prompts specifically tuned for:
				- JSON output formatting
				- Schema validation
				- Consistent response structures
		- ### Example with Structured Output
			- ```python
			  from langsmith import Client
			  
			  client = Client()
			  # Pull a prompt designed for structured JSON output with its model
			  structured_chain = client.pull_prompt("json-extractor", include_model=True)
			  
			  # The model is already configured with the right parameters for structured output
			  # such as response_format={"type": "json_object"} for OpenAI models
			  result = structured_chain.invoke({"text": "Extract entities from this text..."})
			  # result will be properly structured according to the prompt's design
			  ```
	- ## Best Practices
		- ### When to Use `include_model=True`
			- When you want to use the exact model configuration stored with the prompt
			- When sharing prompts across a team to ensure consistent model settings
			- When the prompt has been optimized for a specific model
		- ### When to Use `include_model=False`
			- When you want to use your own model configuration
			- When you need to customize model parameters for your specific use case
			- When you want to use the prompt with a different model than originally specified
	- ## Related Methods
		- ### Other PromptHub Interactions
			- `push_prompt()` - Store a prompt in PromptHub
			- `list_prompts()` - List available prompts
			- `delete_prompt()` - Remove a prompt from PromptHub
			- `like_prompt()` / `unlike_prompt()` - Interact with community prompts