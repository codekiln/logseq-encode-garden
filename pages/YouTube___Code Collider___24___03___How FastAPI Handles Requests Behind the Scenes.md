# [How FastAPI Handles Requests Behind the Scenes - YouTube](https://www.youtube.com/watch?v=tGD3653BrZ8)
tags:: [[FastAPI]], [[Python]], [[Async Programming]], [[Web Development]]
- [[My Notes]]
- ## [[Video]]
	- {{video https://www.youtube.com/watch?v=tGD3653BrZ8}}
	- ### {{youtube-timestamp 0}} Introduction: Basic [[FastAPI]] Endpoint Example
		- Setting up a simple endpoint with:
			- Two print statements
			- 5-second delay between prints
			- Testing through FastAPI docs interface
		- #### Initial Test Results
			- Single request behavior:
				- Prints "hello"
				- Waits 5 seconds
				- Prints "bye"
	
	- ### {{youtube-timestamp 31}} [[Experiment/1]]: Sequential Request Handling
		- Testing multiple requests within 5-second window
		- #### Observations
			- Requests processed sequentially
			- Output pattern:
				- First request: hello → bye
				- Second request: hello → bye
			- [[Key Insight]]: FastAPI completes first request before processing second
	
	- ### {{youtube-timestamp 49}} [[Experiment/2]]: Using [[Async]] Operations
		- #### Implementation Changes
			- Replaced `time.sleep` with `asyncio.sleep`
		- #### Results
			- Different execution pattern:
				- Both "hello" prints appear first
				- Both "bye" prints appear later
			- [[Key Insight]]: FastAPI handled requests concurrently
	
	- ### {{youtube-timestamp 67}} [[Experiment/3]]: Non-Async Function
		- #### Implementation
			- Changed `async def` to regular `def`
		- #### Results
			- Parallel execution observed:
				- Both "hello" prints appear together
				- Both "bye" prints appear together
			- [[Key Insight]]: Requests handled in parallel
	
	- ### {{youtube-timestamp 101}} Understanding [[Blocking vs Non-blocking Operations]]
		- #### [[Non-blocking I/O]]: `asyncio.sleep`
			- Can be awaited
			- Function execution can pause
			- Event loop handles other tasks during pause
		- #### [[Blocking I/O]]: `time.sleep`
			- Cannot be awaited
			- Blocks event loop
			- No task switching possible
	
	- ### {{youtube-timestamp 147}} Summary of Request Handling Patterns
		- #### [[Pattern/1]]: Coroutine without Non-blocking I/O
			- Defined with `async def`
			- No non-blocking operations
			- Result: Sequential processing
		
		- #### [[Pattern/2]]: Coroutine with Non-blocking I/O
			- Defined with `async def`
			- Contains non-blocking operations
			- Result: Concurrent processing
		
		- #### [[Pattern/3]]: Normal Functions
			- Defined with regular `def`
			- Result: Parallel execution
	
	- ### {{youtube-timestamp 162}} [[FastAPI Architecture]] Deep Dive
		- #### Main Thread Behavior
			- Uvicorn starts main thread
			- Coroutines run in event loop
			- Event loop runs in main thread
		
		- #### [[Threading Model]]
			- Coroutines (`async def`): Run in main thread
			- Normal functions (`def`): Run in separate threads
	
	- ### {{youtube-timestamp 266}} [[Best Practices]]
		- #### When to Use `async def`
			- Non-blocking I/O operations
			- DB queries
			- External API requests
			- `asyncio.sleep`
		
		- #### When to Use Regular Functions
			- Blocking I/O operations
			- DB clients without await feature
			- `time.sleep`
			- Operations requiring separate threads