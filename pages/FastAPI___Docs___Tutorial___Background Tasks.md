tags:: [[Diataxis/Tutorial]], [[FastAPI/background_tasks]]

- # [Background Tasks Tutorial](https://fastapi.tiangolo.com/tutorial/background-tasks/)
	- useful for operations that need to happen that **shouldn't block returning a request to a client**
	- ### #Example of using [[FastAPI/background_tasks/add_task]] - `add_task(func, *args, **kwargs)`
		- ```python
		  from fastapi import BackgroundTasks, FastAPI
		  
		  app = FastAPI()
		  
		  
		  def write_notification(email: str, message=""):
		      with open("log.txt", mode="w") as email_file:
		          content = f"notification for {email}: {message}"
		          email_file.write(content)
		  
		  
		  @app.post("/send-notification/{email}")
		  async def send_notification(email: str, background_tasks: BackgroundTasks):
		      background_tasks.add_task(write_notification, email, message="some notification")
		      return {"message": "Notification sent in the background"}
		  ```
	- ### [[Dependency/Injection]] with `BackgroundTasks` - [[FastAPI/Docs/Tutorial/Background Tasks/Dependency Injection]] - [link](https://fastapi.tiangolo.com/tutorial/background-tasks/#dependency-injection)
		- #### What is Dependency Injection?
			- Think of it as FastAPI's way of automatically providing things your endpoint needs
			- Instead of creating these things inside your function, you just say what you need and FastAPI handles the rest
		- #### How BackgroundTasks Works with Dependencies
			- You can use `BackgroundTasks` at different levels in your code:
				- In your main endpoint function (called a *path operation function*)
				- In helper functions (called dependencies or dependables)
				- In functions that help your helper functions (called sub-dependencies)
			- FastAPI is smart enough to:
				- Keep track of all background tasks you create at any level
				- Run them all together after sending the response
				- Handle all the complexity for you
		- #### Explained #Example - [[FastAPI/Depends]] and [[FastAPI/BackgroundTasks]]
			- ```python
			  from typing import Annotated
			  
			  from fastapi import BackgroundTasks, Depends, FastAPI
			  
			  app = FastAPI()
			  
			  # Simple function that writes to a log file
			  def write_log(message: str):
			      with open("log.txt", mode="a") as log:
			          log.write(message)
			  
			  # Helper function (dependency) that processes queries
			  def get_query(background_tasks: BackgroundTasks, q: str | None = None):
			      if q:
			          message = f"found query: {q}\n"
			          background_tasks.add_task(write_log, message)  # Schedule log writing for later
			      return q
			  
			  # Main endpoint function
			  @app.post("/send-notification/{email}")
			  async def send_notification(
			      email: str, background_tasks: BackgroundTasks, q: Annotated[str, Depends(get_query)]
			  ):
			      message = f"message to {email}\n"
			      background_tasks.add_task(write_log, message)  # Schedule another log write
			      return {"message": "Message sent"}
			  ```
				- ##### How This Example Works
					- When someone makes a request:
						- 1. FastAPI sees you need `get_query` and runs it first
							- *in particular, see* `Annotated[str, Depends(get_query)]`
							- 2. inside of `get_query` (which runs prior to invocation of the endpoint), the logic here dictates that if there was a query parameter, it **schedules** a log write
						- 3. Then the `send_notification` function runs and **schedules another** log write - it has its own `add_task(write_log, message)`
						- 4. FastAPI sends the response back **immediately**
						- 5. The response is sent in a way that's async with respect to all the scheduled log writes
			- ### Understanding [[FastAPI/BackgroundTasks]] - Technical Deep Dive
				- #### Where it comes from
					- FastAPI's `BackgroundTasks` is built on top of [[starlette/background/BackgroundTask]]
					- FastAPI uses the plural form (`Tasks` instead of `Task`) to make it more powerful
				- #### Why use BackgroundTasks instead of BackgroundTask?
					- `BackgroundTasks` is designed to work seamlessly with FastAPI's dependency system
					- It can be used directly as a parameter in your endpoint functions
					- FastAPI **automatically manages its lifecycle for you**
				- #### Simple Example Showing the Difference
					- Using raw Starlette `BackgroundTask` and `BackgroundTasks`:
						- ```python
						  from starlette.background import BackgroundTask, BackgroundTasks
						  from starlette.responses import JSONResponse
						  from fastapi import FastAPI
						  
						  app = FastAPI()
						  
						  async def write_log(message: str):
						      with open("log.txt", "a") as f:
						          f.write(message)
						  
						  @app.post("/starlette-way")
						  async def starlette_way():
						      # For a single task, use BackgroundTask
						      single_task = BackgroundTask(write_log, "single task message")
						      
						      # For multiple tasks, use BackgroundTasks
						      multiple_tasks = BackgroundTasks()
						      multiple_tasks.add_task(write_log, "first message")
						      multiple_tasks.add_task(write_log, "second message")
						      
						      # Must explicitly attach tasks to response
						      # Can only attach to specific response types like JSONResponse
						      return JSONResponse(
						          {"message": "Tasks scheduled"}, 
						          background=multiple_tasks  # or single_task
						      )
						  ```
					- Using FastAPI's `BackgroundTasks`:
						- ```python
						  from fastapi import FastAPI, BackgroundTasks
						  
						  app = FastAPI()
						  
						  async def write_log(message: str):
						      with open("log.txt", "a") as f:
						          f.write(message)
						  
						  # FastAPI manages the BackgroundTasks instance for you
						  @app.post("/fastapi-way")
						  async def fastapi_way(background_tasks: BackgroundTasks):
						      # Just add tasks - FastAPI handles the rest
						      background_tasks.add_task(write_log, "first message")
						      background_tasks.add_task(write_log, "second message")
						      
						      # Works with any response type
						      return {"message": "Tasks scheduled"}
						  
						  # Easy to share tasks between functions
						  def log_something(background_tasks: BackgroundTasks):
						      background_tasks.add_task(write_log, "shared task")
						  
						  @app.post("/shared")
						  async def shared_example(background_tasks: BackgroundTasks):
						      log_something(background_tasks)  # Same instance is shared
						      background_tasks.add_task(write_log, "main task")
						      return {"message": "Tasks scheduled"}
						  ```
				- #### Important Notes about Background Tasks
					- From [[starlette/background/BackgroundTask]] [Starlette Docs](https://www.starlette.io/background/):
						- Tasks run in order they were added
							- > The tasks are executed in order. In case one of the tasks raises an exception, the following tasks will not get the opportunity to be executed.
						- Tasks run after response is sent
						- Multiple tasks supported via `add_task`
					- #### Concurrency and Task Execution Details
						- In-Process Nature
							- Tasks run in the same process as your FastAPI app
							- Share the same event loop as your application
							- Not run in separate threads by default
						- Request Independence
							- Each HTTP request gets its own `BackgroundTasks` instance
							- Tasks from different requests are independent
							- If Request A's tasks fail, Request B's tasks are unaffected
						- When to Use What
							- Use `BackgroundTasks` for:
								- Small, quick tasks
								- Tasks that need access to your FastAPI app's variables
								- Simple background operations like sending emails
							- Use Celery or similar for:
								- Heavy computation
								- Tasks that need to run across multiple processes
								- Tasks that need to run across multiple servers
								- When you need a proper job queue (RabbitMQ/Redis)
				- #### Technical Details from [[FastAPI/Docs/Tutorial/Background Tasks]] [FastAPI Background Tasks Tutorial](https://fastapi.tiangolo.com/tutorial/background-tasks/)
					- FastAPI imports `BackgroundTasks` directly from Starlette for convenience
					- It's recommended to use `BackgroundTasks` (plural) instead of `BackgroundTask` (singular)
						- > "By only using `BackgroundTasks` (and not `BackgroundTask`), it's then possible to use it as a *path operation function* parameter and have FastAPI handle the rest for you"
					- For heavy background computation, consider using tools like [[Celery]]:
						- When you need to run tasks across multiple processes
						- When you need to run tasks across multiple servers
						- When you need a message/job queue manager (like RabbitMQ or Redis)
					- Use `BackgroundTasks` when:
						- You need to access variables from the same FastAPI app
						- You need to perform small background tasks (like sending emails)
				- #### Key Benefits of using FastAPI's BackgroundTasks
					- 1. Simpler Integration with FastAPI
						- From [[FastAPI/Docs/Tutorial/Background Tasks]]:
							- No need to import from Starlette directly
							- Works with any response type
							- No manual response wrapping needed
					- 2. Works with FastAPI's dependency injection system
						- From [[FastAPI/Docs/Tutorial/Background Tasks/Dependency Injection]] [here](https://fastapi.tiangolo.com/tutorial/background-tasks/#dependency-injection):
							- Can be used at multiple levels:
								- In path operation functions
								- In dependencies (dependables)
								- In sub-dependencies
							- FastAPI reuses the same object across all levels
							- All background tasks are merged and run together
					- 3. Maintains all Starlette features
						- From [[starlette/background/BackgroundTask]] [Starlette Docs](https://www.starlette.io/background/):
							- Tasks run in order
								- > The tasks are executed in order. In case one of the tasks raises an exception, the following tasks will not get the opportunity to be executed.
									- For [[Error/Handling]], see [[StackOverflow/23/01/How to handle exceptions in background tasks in FastAPI and Starlette]] [here](https://stackoverflow.com/a/75146315/78202)
							- Tasks run after response is sent
							- Multiple tasks supported via `add_task`