tags:: [[Py/Lib/getstream]], [[StreamIO/Lib/Py/getstream]]
created-by:: [[Person/Tommaso Barbuglik]]

- # [GetStream/stream-py: Official Python API Client for Stream Chat and Video](https://github.com/GetStream/stream-py)
	- ## [[My Notes]]
		- [[2025-05-12 Mon]]
		  id:: 68220306-c9aa-4177-ba2e-7f0e9ef730ac
			- This appears to be a universal API for Chat, Video and Feeds for python, which is a departure from their previous strategy which had [[StreamIO/GitHub/stream-chat-python]] for chat and different libraries for feeds and video.
			- It appears that they have  something called #OpenAI realtime integration (not sure what that means): `uv add 'getstream[openai-realtime]'`.
				- TODO why would they make integration that's specific to one provider?
			- They are using [[uv]] for their dev.
			- Apparently they are using [[Programming/Technique/Codegen]] to generate this from [[OpenAPI]]
			-
	-