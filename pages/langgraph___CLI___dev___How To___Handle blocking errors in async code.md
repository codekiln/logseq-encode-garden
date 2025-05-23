# How to handle langgraph's blocking error
	- ## sample error 1 - "LangGraph dev identified a synchronous blocking call in your code"
		- ```
		  Heads up! LangGraph dev identified a synchronous blocking call in your code. When running in an ASGI web server, blocking calls can degrade performance for everyone since they tie up the event loop.
		  Here are your options to fix this:
		  1. Best approach: Convert any blocking code to use async/await patterns
		     For example, use 'await aiohttp.get()' instead of 'requests.get()'
		  2. Quick fix: Move blocking operations to a separate thread
		     Example: 'await asyncio.to_thread(your_blocking_function)'
		  3. Override (if you can't change the code):
		     - For development: Run 'langgraph dev --allow-blocking'
		     - For deployment: Set 'BG_JOB_ISOLATED_LOOPS=true' environment variable
		  These blocking operations can prevent health checks and slow down other runs in your deployment. Following these recommendations will help keep your LangGraph application running smoothly!
		  ```
	- ## Sub-optimal workarounds
		- For development: Run 'langgraph dev --allow-blocking'
		- For deployment: Set 'BG_JOB_ISOLATED_LOOPS=true' environment variable [[langgraph/CLI/EnvVar/BG_JOB_ISOLATED_LOOPS]]
	- ## Better workarounds
		- search your code for synchronous clients and replace them with async clients
	- ## Resources
		- [blockbuster causes blocking error via tiktoken in async context with latest langgraph-api · Issue #4218 · langchain-ai/langgraph](https://github.com/langchain-ai/langgraph/issues/4218)
			- References workarounds; recommendation from