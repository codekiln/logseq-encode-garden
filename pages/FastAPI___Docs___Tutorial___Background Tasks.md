tags:: [[Diataxis/Tutorial]], [[FastAPI/background_tasks]]

- # [Background Tasks Tutorial](https://fastapi.tiangolo.com/tutorial/background-tasks/)
	- ## Overview
		- Background tasks are operations that need to happen after returning a response to the client
		- Common use cases:
			- Email notifications
			- Processing data
			- Writing logs
	- ## Core Concepts
		- ### Task Execution Model
			- From [[starlette/background/BackgroundTask]] [Starlette Docs](https://www.starlette.io/background/):
				- Tasks run in the same process and event loop as your FastAPI app
				- Tasks execute in order they were added
				- Tasks only start after response is sent
				- If a task fails, remaining tasks in that request won't run
		- ### Request Independence
			- Each HTTP request gets its own `BackgroundTasks` instance
			- Tasks from different requests are isolated
			- Failure in one request's tasks won't affect other requests
		- ### Threading and AsyncIO
			- Async functions run directly on the event loop
			- Sync functions run in a thread pool to avoid blocking
			- Default thread pool is limited (typically 40 threads)
	- ## Using Background Tasks
		- ### Basic Example
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
		- ### With Dependency Injection
			- ```python
			  from typing import Annotated
			  from fastapi import BackgroundTasks, Depends, FastAPI
			  
			  app = FastAPI()
			  
			  def write_log(message: str):
			      with open("log.txt", mode="a") as log:
			          log.write(message)
			  
			  def get_query(background_tasks: BackgroundTasks, q: str | None = None):
			      if q:
			          message = f"found query: {q}\n"
			          background_tasks.add_task(write_log, message)
			      return q
			  
			  @app.post("/send-notification/{email}")
			  async def send_notification(
			      email: str, 
			      background_tasks: BackgroundTasks, 
			      q: Annotated[str, Depends(get_query)]
			  ):
			      message = f"message to {email}\n"
			      background_tasks.add_task(write_log, message)
			      return {"message": "Message sent"}
			  ```
	- ## Error Handling
		- ### Best Practices
			- Use try/except in background tasks
			- Log errors appropriately
			- Remember errors won't affect the HTTP response
			- Example:
				- ```python
				  def background_job():
				      try:
				          # ... do work ...
				      except Exception as e:
				          logger.error(f"Background task failed: {e}")
				  ```
	- ## When to Use What
		- ### Use BackgroundTasks for
			- Small, quick tasks
			- Tasks needing access to FastAPI app variables
			- Simple operations like:
				- Sending emails
				- Writing logs
				- Basic API calls
		- ### Use [[Celery]] or Similar for
			- Heavy computation
			- Tasks needing multiple processes
			- Tasks needing multiple servers
			- When you need a message queue (RabbitMQ/Redis)
	- ## Technical Details
		- From the tutorial:
			- FastAPI imports `BackgroundTasks` from Starlette
			- Recommended to use `BackgroundTasks` (plural) over `BackgroundTask`
			- > "By only using `BackgroundTasks` (and not `BackgroundTask`), it's then possible to use it as a *path operation function* parameter and have FastAPI handle the rest for you"
		- From [[starlette/background/BackgroundTask]] [Starlette Docs](https://www.starlette.io/background/):
			- Tasks run in order
				- > The tasks are executed in order. In case one of the tasks raises an exception, the following tasks will not get the opportunity to be executed.
			- Tasks run after response is sent
			- Multiple tasks supported via `add_task`