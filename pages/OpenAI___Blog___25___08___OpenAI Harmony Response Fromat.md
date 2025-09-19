date-created:: [[2025/08]]

- # [OpenAI Harmony Response Format](https://cookbook.openai.com/articles/openai-harmony)
	- The [`gpt-oss` models](https://openai.com/open-models) were trained on the harmony response format for defining conversation structures, generating reasoning output and structuring function calls.
	- The format is designed to mimic the OpenAI Responses API, so if you have used that API before, this format should hopefully feel familiar to you.
	- ### [Roles](https://cookbook.openai.com/articles/openai-harmony#roles)  
	  
	  Every message that the model processes has a role associated with it. The model knows about five types of roles:
	  
	  | Role | Purpose |
	  | ---- | ---- | ---- |
	  | `system` | A system message is used to specify reasoning effort, meta information like knowledge cutoff and built-in tools |
	  | `developer` | The developer message is used to provide information about the instructions for the model (what is normally considered the “system prompt”) and available function tools |
	  | `user` | Typically representing the input to the model |
	  | `assistant` | Output by the model which can either be a tool call or a message output. The output might also be associated with a particular “channel” identifying what the intent of the message is. |
	  | `tool` | Messages representing the output of a tool call. The specific tool name will be used as the role inside a message. |
	  
	  These roles also represent the information hierarchy that the model applies in case there are any instruction conflicts: `system` > `developer` > `user` > `assistant` > `tool`
	-