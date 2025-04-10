tags:: [[Py/asyncio]]

- # [FastAPI runs API calls in serial instead of parallel fashion](https://stackoverflow.com/questions/71516140/fastapi-runs-api-calls-in-serial-instead-of-parallel-fashion)
	- [[My Notes]]
	  id:: 67f7d1dd-fbf0-424f-9117-08f2a7015fdf
		- The original poster's example comes from the [[Py/asyncio]] docs, which is also explained in [[YouTube/Code Collider/24/03/How FastAPI Handles Requests Behind the Scenes]].
		- The top answer comes from [[StackOverflow/User/Chris]] and is voted up 270+ times, it's basically an [[Essay]] on how [[FastAPI]] is implemented with [[Py/asyncio]]. As people said in the comments, "Better answer than entire emojis-ridden FastApi documentation" See my formatting below.
		- I came here looking for an answer to what the limitations were for using [[FastAPI/BackgroundTasks]] vs when I should be managing my own [[Py/asyncio]] event loops, in particular, after reading [[FastAPI/Docs/Tutorial/Background Tasks]] here:
			- {{embed ((67f7c779-c56b-49b5-9314-09f1a4b72efa))}}
	- Top Answer from [[StackOverflow/User/Chris]]
		- ### Basic Answer
			- As per [FastAPI's docs](https://fastapi.tiangolo.com/async/#path-operation-functions):
				- > When you declare an endpoint with normal `def` instead of `async def`, it is run in an external threadpool that is then `await`ed, instead of being called directly (as it would **block** the server).
			- and:
				- > If you are using a third party library that communicates with something (a database, an API, the file system, etc.) and doesn't have support for using `await`, (this is currently the case for most database libraries), then declare your endpoints as normally, with just `def`.
				- > If your application (somehow) doesn't have to communicate with anything else and wait for it to respond, use `async def`.
				- > You can mix `def` and `async def` in your endpoints as much as you need and define each one using the best option for you. FastAPI will do the right thing with them.
			- Thus, a `def` (*synchronous*) endpoint in FastAPI will **still** run in the [`event loop`](https://docs.python.org/3/library/asyncio-eventloop.html), but instead of calling it *directly*, which would block the server, FastAPI will run it in a **separate thread** from an external threadpool and then `await` it (more details on the external threadpool are given later on); hence, FastAPI will still work *asynchronously*. In other words, the server will process requests to such endpoints *concurrently* (at the cost, though, of spawning a new thread or reusing an existing one from the threadpool, for every incoming request to such endpoints). Whereas, `async def` endpoints run **directly** in the `event loop`—which runs in a *single* thread, [typically the main thread](https://docs.python.org/3/library/asyncio-dev.html#concurrency-and-multithreading) of a process/worker, and here is created when calling [`uvicorn.run()`](https://github.com/encode/uvicorn/blob/a05ae6426cc8f224f4f1a995f46a901ab0f5644b/uvicorn/server.py#L60), or the equivalent method of some [other ASGI server](https://fastapi.tiangolo.com/deployment/manually/)—that is, the server will **also** process requests to such endpoints *concurrently*/*asynchronously*, **as long as there is** an `await` call to non-blocking operations inside such `async def` endpoints; usually, these are I/O-bound operations, such as *waiting* for (1) data from the client to be sent through the network, (2) contents of a file in the disk to be read, and (3) a database operation to finish.
			- **However**, if an endpoint defined with `async def` does not `await` for some [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutines) inside (i.e., a coroutine object is the result of calling an `async def` function), in order to give up time for other tasks in the `event loop` to run (e.g., requests to the same or other endpoints, background tasks, etc.), each request to such an endpoint will have to be completely finished (i.e., exit the endpoint), before returning control back to the `event loop` and allowing other tasks in the `event loop` to run (see [this answer](https://stackoverflow.com/a/78155528/17865804), if you would like to monitor all pending tasks in an `event loop`). In other words, in such cases, the server would be "blocked", and hence, any requests would be processed *sequentially*.
			- Having said that, you should still consider defining an endpoint with `async def`, if it **doesn't** execute any blocking operations inside that has to wait for them to respond (e.g., [`time.sleep()`](https://docs.python.org/3/library/time.html#time.sleep)), but is instead used to [return simple JSON data](https://stackoverflow.com/a/73974946/17865804), a simple [`HTMLResponse`](https://github.com/encode/starlette/blob/6f863b0d3b8e8f18d5df9e8cd2514f7085b874e1/starlette/responses.py#L165) or even a [`FileResponse`](https://github.com/encode/starlette/blob/827de43b97ad58c7b8daae12ad17c1848a4f1341/starlette/responses.py#L287) (in which case the file data will be read *asynchronously* and in chunks regardless, using `await anyio.open_file()`, as shown in [`FileResponse`](https://github.com/encode/starlette/blob/827de43b97ad58c7b8daae12ad17c1848a4f1341/starlette/responses.py#L287)), even if there is not an `await` call inside the endpoint in such cases, as FastAPI would likely perform better, when running such a simple endpoint *directly* in the `event loop` instead of a separate thread. If, however, you had to return some complex and large JSON data, either encoding them on your own within the endpoint, as shown in the linked answer earlier, or using Starlette's [`JSONResponse`](https://github.com/encode/starlette/blob/6f863b0d3b8e8f18d5df9e8cd2514f7085b874e1/starlette/responses.py#L173) or FastAPI's [`ORJSONResponse`](https://github.com/tiangolo/fastapi/blob/84f04cc8a048bd7cead9c1acff53d4479889c9c1/fastapi/responses.py#L36)/[`UJSONResponse`](https://github.com/tiangolo/fastapi/blob/84f04cc8a048bd7cead9c1acff53d4479889c9c1/fastapi/responses.py#L23) (see this [related answer](https://stackoverflow.com/a/74173023/17865804) as well), which, all these classes, would encode the data in a *synchronous* way, using `json.dumps()` and `orjson.dumps()`/`ujson.dumps()` respectively, in that case, you might consider having the endpoint defined with normal `def` (related answers could be found [here](https://stackoverflow.com/a/73580096/17865804) and [here](https://stackoverflow.com/a/73694164/17865804)). Alternatively, you could keep using an `async def` endpoint, but have such blocking operations inside (e.g., `orjson.dumps()` or `df.to_json()`) run in a separate thread/process, as described in the solutions provided later on (it would be a good practice to perform benchmark tests, similar to [this](https://stackoverflow.com/a/77941425/17865804), and compare the results to find the best-performing approach in your case).
			- **Note** that the same concept not only applies to endpoints, but also to functions that are used as [`StreamingResponse` generators](https://stackoverflow.com/a/75760884/17865804) (see [`StreamingResponse`](https://github.com/encode/starlette/blob/31164e346b9bd1ce17d968e1301c3bb2c23bb418/starlette/responses.py#L235) class implementation) or [`Background Tasks`](https://fastapi.tiangolo.com/tutorial/background-tasks/) (see [`BackgroundTask`](https://github.com/encode/starlette/blob/33f46a13625bcca4b7520e33be299a23b2e2b26c/starlette/background.py#L15) class implementation and [this answer](https://stackoverflow.com/a/76280152/17865804)), as well as [`Dependencies`](https://fastapi.tiangolo.com/async/#dependencies). That means FastAPI, behind the scenes, **will also** run such functions defined with normal `def` in a separate thread from the **same** external threadpool; whereas, if such functions were defined with `async def`, they would run *directly* in the `event loop`. In order to run an endpoint or a function described above in a separate thread and `await` it, FastAPI uses Starlette's asynchronous [`run_in_threadpool()`](https://github.com/encode/starlette/blob/b8ea367b4304a98653ec8ce9c794ad0ba6dcaf4b/starlette/concurrency.py#L35) function, which, under the hood, calls [`anyio.to_thread.run_sync()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.to_thread.run_sync). The default number of worker threads of that external threadpool is `40` and can be adjusted as required (have a look at [this answer](https://stackoverflow.com/a/77941425/17865804) for more details). Hence, after reading this answer to the end, you should be able to know when to define a FastAPI endpoint/`StreamingResponse` generator/`BackgroundTask`/Dependency with `def` or `async def`, as well as whether or not you should increase the number of threads of the external threadpool.
		- ### Python's   `async def`   function and   `await`
			- The keyword `await` (which only works within an `async def` function) passes function control back to the `event loop`. In other words, it suspends the execution of the surrounding coroutine, and tells the `event loop` to let some other task run, until that `await`ed task is completed. **Note** that just because you may define a custom function with `async def` and then `await` it inside your `async def` endpoint, it doesn't mean that your code will work *asynchronously*, if that custom function contains, for example, calls to `time.sleep()`, CPU-bound tasks, non-async I/O libraries, or any other blocking call that is incompatible with asynchronous Python code. In FastAPI, for example, when using the `async` methods of [`UploadFile`](https://fastapi.tiangolo.com/tutorial/request-files/#uploadfile), such as `await file.read()` and `await file.close()`, FastAPI/Starlette, behind the scenes, actually calls the corresponding *synchronous* [File methods](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects) in a separate thread from the external threadpool described earlier (using `run_in_threadpool()`) and `await`s it; otherwise, such methods/operations would block the `event loop`—you could find out more by looking at the [implementation of the `UploadFile` class](https://github.com/encode/starlette/blob/048643adc21e75b668567fc6bcdd3650b89044ea/starlette/datastructures.py#L426).
			- **Note** that `async` does not mean *parallel*, but *concurrently*. As mentioned earlier, asynchronous code with [`async` and `await` is many times summarized as using *coroutines*](https://fastapi.tiangolo.com/async/#coroutines). Coroutines are cooperative, meaning that at any given time, a program with coroutines is running **only** one of its coroutines, and this running coroutine suspends its execution only when it explicitly requests to be suspended.
			- As described [here](https://jwodder.github.io/kbits/posts/pyasync-fundam/):
			  
			  > Specifically, whenever execution of a currently-running coroutine reaches an `await` expression, the coroutine may be suspended, and another previously-suspended coroutine may resume execution if what it was suspended on has since returned a value. Suspension can also happen when an `async for` block requests the next value from an asynchronous iterator or when an `async with` block is entered or exited, as these operations use `await` under the hood.
			- If, however, a blocking I/O-bound or CPU-bound task was *directly* executed inside an `async def` function/endpoint, it would then **block the `event loop`**, and hence, the main thread would be blocked as well. Hence, a blocking operation such as `time.sleep()` in an `async def` endpoint would block the entire server (as in the example provided in your question). Thus, if your endpoint is not going to make any `async` calls, you could declare it with normal `def` instead, in which case, FastAPI would run it in a separate thread from the external threadpool and `await` it, as explained earlier (more solutions are given in the following sections).
			- Example:
				- ```python
				  @app.get("/ping")
				  def ping(request: Request):
				      #print(request.client)
				      print("Hello")
				      time.sleep(5)
				      print("bye")
				      return "pong"
				  ```
			- Otherwise, if the functions that you had to execute inside the endpoint are `async` functions that you had to `await`, you should define your endpoint with `async def`. To demonstrate this, the example below uses [`asyncio.sleep()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.sleep), which provides a **non-blocking** sleep operation. Calling it will suspend the execution of the surrounding coroutine (until the sleep operation is completed), thus allowing other tasks in the `event loop` to run.
				- ```python
				  import asyncio
				   
				  @app.get("/ping")
				  async def ping(request: Request):
				      #print(request.client)
				      print("Hello")
				      await asyncio.sleep(5)
				      print("bye")
				      return "pong"
				  ```
			- **Both** the endpoints above will print out the specified messages to the screen in the same order as mentioned in your question—if two requests arrived at (around) the same time—that is:
			  
			  ```
			  Hello
			  Hello
			  bye
			  bye
			  ```
		- ### Important Note
			- When using a web browser to call the same endpoint for the second (third, and so on) time, please remember to do that **from a tab that is isolated from the browser's main session**; otherwise, succeeding requests (i.e., coming after the first one) might be **blocked** by the browser (i.e., on **client side**), as the browser might be waiting for a response to the previous request from the server, before sending the next request. This is a common behaviour for the Chrome web browser at least, due to waiting to see the result of a request and check if the result can be cached, before requesting the same resource again (Also, **note** that [every browser has a specific limit for parallel connections](https://stackoverflow.com/a/79385086/17865804) to a given hostname).
			- You could confirm that by using `print(request.client)` inside the endpoint, where you would see that the `hostname` and `port` number are the same for all incoming requests—in case the requests were initiated from tabs opened in the same browser window/session; otherwise, the `port` number would normally be different for every request—and hence, those requests would be processed *sequentially* by the server, **because of the browser sending them sequentially** in the first place. To **overcome** this, you could either:
				- 1 - Reload the same tab (as is running), or
				- 2 - Open a new tab in an (isolated) Incognito Window, or
				- 3 - Use a different web browser/client to send the request, or
				- 4 - Use the `httpx` library to [make asynchronous HTTP requests](https://www.python-httpx.org/async/#making-async-requests), along with the [*awaitable*](https://docs.python.org/3/library/asyncio-task.html#awaitables) [`asyncio.gather()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather), which allows executing multiple asynchronous operations concurrently and then returns a list of results in the **same** order the awaitables (tasks) were passed to that function (have a look at [this answer](https://stackoverflow.com/a/74239367/17865804) for more details).
					- #### **Example**
						- ```python
						  import httpx
						  import asyncio
						  
						  URLS = ['http://127.0.0.1:8000/ping'] * 2
						  
						  async def send(url, client):
						      return await client.get(url, timeout=10)
						  
						  async def main():
						      async with httpx.AsyncClient() as client:
						          tasks = [send(url, client) for url in URLS]
						          responses = await asyncio.gather(*tasks)
						          print(*[r.json() for r in responses], sep='\n')
						  
						  asyncio.run(main())
						  ```
					- In case you had to call different endpoints that may take different time to process a request, and you would like to print the response out on client side as soon as it is returned from the server—instead of waiting for `asyncio.gather()` to gather the results of all tasks and print them out in the same order the tasks were passed to the `send()` function—you could replace the `send()` function of the example above with the one shown below:
						- ```python
						  async def send(url, client):
						      res = await client.get(url, timeout=10)
						      print(res.json())
						      return res
						  ```
		- ### Python's GIL and Blocking Operations inside Threads
			- Simply put, the Global Interpreter Lock (GIL) is a mutex (lock), ensuring that only one thread (per process) can hold the control of the Python interpreter (and run Python bytecode) at any point in time.
			- One might wonder that if a blocking operation inside a thread, such as `time.sleep()` within a `def` endpoint, blocks the calling thread, how is the GIL released, so that other threads get a chance to execute? The answer is because `time.sleep()` is not really a CPU-bound operation, but it "suspends execution of the calling thread for the given number of seconds"; hence, the thread is switched out of the CPU for `x` seconds, allowing other threads to switch in for execution. In other words, it does block the calling thread, but the calling process is still alive, so that other threads can still run within the process (obviously, in a single-threaded application, everything would be blocked). The state of the thread is stored, so that it can be restored and resume execution at a later point. That process of the CPU jumping from one thread of execution to another is called *context switching*.
			- Even if a CPU-bound operation (or an I/O-bound one that wouldn't voluntarily release the GIL) was executed inside a thread, and the GIL hadn't been released after `5ms` (or some other [configurable interval](https://docs.python.org/3/library/sys.html#sys.setswitchinterval)), Python would (automatically) tell the current thread to release the GIL. To find the default thread switch interval, use:
				- ```python
				  import sys
				  
				  print(sys.getswitchinterval())  # 0.005
				  ```
			- However, this automatic GIL release is best-effort, not guaranteed—see [this](https://stackoverflow.com/q/56692439/17865804), for instance.
		- ## `Async` / `await`   and Blocking I/O-bound or CPU-bound Operations
			- You should always aim at using `async` code, as it uses a single thread to execute tasks (i.e., there is only one thread that can take a lock on the interpreter), and thus, it can be more efficient than threading in I/O-bound scenarios, as it avoids the additional overhead of context switching. If, however, you are required to define a FastAPI endpoint (or a `StreamingResponse` generator, a background task, etc.) with `async def` (as you might need to `await` for coroutines inside), but also have to run some *synchronous* I/O-bound or CPU-bound task that would block the `event loop` (essentially, the entire server) and wouldn't let other requests to go through, for example:
				- ```python
				  @app.post("/ping")
				  async def ping(file: UploadFile = File(...)):
				    print("Hello")
				    try:
				        contents = await file.read()
				        res = cpu_bound_task(contents)  # this would block the event loop
				    finally:
				        await file.close()
				    print("bye")
				    return "pong"
				  ```
			- then:
				- 1 - You should check whether you could change your endpoint's definition to normal `def` instead of `async def`. **One way**, if the only method in your endpoint that had to be `await`ed was the one reading the file contents would be to declare the file contents parameter as `bytes`, i.e., `contents: bytes = File()`. Using that definition, FastAPI would read the file for you and you would receive the contents as `bytes`. Hence, there would be no need to use an `async def` endpoint with `await file.read()` inside. Please note that this approach (i.e., using `contents: bytes = File()`) should work fine for small files; however, for larger files, and always depending on your server's resources, this might cause issues, as the enitre file contents would be stored to memory (see the [documentation on `File` Parameters](https://fastapi.tiangolo.com/tutorial/request-files/#define-file-parameters)). Hence, if your system does not have enough RAM available to accommodate the accumulated data, your application may end up crashing—if, for instance, you have 8GB of RAM (the available RAM will always be less than the amount installed on your device, as other apps/services will be using it as well), you can't load a 50GB file.
					- **Alternatively**, you could use `file: UploadFile = File(...)` definition in your endpoint, but this time call the *synchronous* `.read()` method of the [`SpooledTemporaryFile`](https://docs.python.org/3/library/tempfile.html#tempfile.SpooledTemporaryFile) directly, which can be accessed through the `.file` attribute of the `UploadFile` object. In this way, you will be able to declare your endpoint with a normal `def` instead, and hence, each request will run in a separate thread from the external threadpool and then be `await`ed (as explained earlier). Example is given below. For more details on how to upload a `File`, as well as how FastAPI/Starlette uses the `SpooledTemporaryFile` behind the scenes when uploading a `File`, please have a look at [this answer](https://stackoverflow.com/a/70657621/17865804) and [this answer](https://stackoverflow.com/a/70667530/17865804).
						- ```python
						  @app.post("/ping")
						  def ping(file: UploadFile = File(...)):
						    print("Hello")
						    try:
						        contents = file.file.read()
						        res = cpu_bound_task(contents)
						    finally:
						        file.file.close()
						    print("bye")
						    return "pong"
						  ```
					- **Another way**, when you would like having the endpoint defined with normal `def`, as you might need to run blocking operations inside and would like having it run in a separate thread instead of calling it directly in the `event loop`, but at the same time you would have to `await` for coroutines inside, is to `await` such coroutines within an `async` dependency instead, as demonstrated in [this answer](https://stackoverflow.com/a/70659178/17865804), which will then return the result to the `def` endpoint.
				- 2 - Use FastAPI's (Starlette's) [`run_in_threadpool()`](https://github.com/encode/starlette/blob/b8ea367b4304a98653ec8ce9c794ad0ba6dcaf4b/starlette/concurrency.py#L35) function from the `concurrency` module—as [@tiangolo suggested](https://github.com/fastapi/fastapi/issues/1066#issuecomment-612940187)—which, as noted earlier, will run the function in a separate thread from an external threadpool to ensure that the main thread (where coroutines are run) does not get blocked. The `run_in_threadpool()` is an `await`able function, where its first parameter is a normal function, and the following parameters are passed to that function directly. It supports both *sequence* and *keyword* arguments.
					- ```python
					  from fastapi.concurrency import run_in_threadpool
					  
					  res = await run_in_threadpool(cpu_bound_task, contents)
					  ```
				- 3 - Alternatively, use `asyncio`'s [`loop.run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor)—after obtaining the running `event loop` using [`asyncio.get_running_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_running_loop)—to run the task, which, in this case, you can `await` for it to complete and return the result(s), before moving on to the next line of code. Passing `None` to the *executor* argument, the *default* executor will be used; which is a [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor):
					- ```python
					  import asyncio
					  
					  loop = asyncio.get_running_loop()
					  res = await loop.run_in_executor(None, cpu_bound_task, contents)
					  ```
					- or, if you would like to [pass keyword arguments](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-pass-keywords) instead, you could use a `lambda` expression (e.g., `lambda: cpu_bound_task(some_arg=contents)`), or, preferably, [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial), which is specifically recommended in the documentation for [`loop.run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor):
						- ```python
						  import asyncio
						  from functools import partial
						  
						  loop = asyncio.get_running_loop()
						  res = await loop.run_in_executor(None, partial(cpu_bound_task, some_arg=contents))
						  ```
					- In Python 3.9+, you could also use [`asyncio.to_thread()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.to_thread) to asynchronously run a synchronous function in a separate thread—which, essentially, uses `await loop.run_in_executor(None, func_call)` under the hood, as can been seen in the [implementation of `asyncio.to_thread()`](https://github.com/python/cpython/blob/c5660ae96f2ab5732c68c301ce9a63009f432d93/Lib/asyncio/threads.py#L12). The `to_thread()` function takes the name of a blocking function to execute, as well as any arguments (`*args` and/or `**kwargs`) to the function, and then returns a coroutine that can be `await`ed. Example:
					  
					  ```
					  import asyncio
					  
					  res = await asyncio.to_thread(cpu_bound_task, contents)
					  ```
					  
					  **Note** that as explained in [**this answer**](https://stackoverflow.com/a/77941425/17865804), passing `None` to the `executor` argument **does not** create a new `ThreadPoolExecutor` every time you call `await loop.run_in_executor(None, ...)`, but instead re-uses the *default* executor with the *default* number of worker threads (i.e., `min(32, os.cpu_count() + 4)`). Thus, depending on the requirements of your application, that number might not be enough. In that case, you should rather use a custom [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor). For instance:
						- ```python
						  import asyncio
						  import concurrent.futures
						  
						  loop = asyncio.get_running_loop()
						  with concurrent.futures.ThreadPoolExecutor() as pool:
						      res = await loop.run_in_executor(pool, cpu_bound_task, contents)
						  ```
					- I would strongly recommend having a look at the linked answer above to learn about the difference between using `run_in_threadpool()` and `run_in_executor()`, as well as how to create a re-usable custom `ThreadPoolExecutor` at the application startup, and adjust the number of maximum worker threads as needed.
				- 4 - `ThreadPoolExecutor` will successfully prevent the `event loop` from being blocked (and should be prefered for calling blocking I/O-bound tasks), but won't give you the **performance improvement** you would expect from running **code in parallel**; especially, when one needs to perform `CPU-bound` tasks, such as audio or image processing and machine learning (see [here](https://fastapi.tiangolo.com/async/#is-concurrency-better-than-parallelism)). It is thus preferable to **run CPU-bound tasks in a separate process**—using [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor), as shown below—which, again, you can integrate with `asyncio`, in order to `await` it to finish its work and return the result(s). As described [here](https://stackoverflow.com/q/15900366), it is important to protect the entry point of the program to avoid recursive spawning of subprocesses, etc. Basically, your code must be under [`if __name__ == '__main__'`](https://stackoverflow.com/questions/419163/what-does-if-name-main-do).
					- ```python
					  import concurrent.futures
					  
					  loop = asyncio.get_running_loop()
					  with concurrent.futures.ProcessPoolExecutor() as pool:
					      res = await loop.run_in_executor(pool, cpu_bound_task, contents)
					  ```
					- Again, I'd suggest having a look at the linked answer earlier on how to create a re-usable `ProcessPoolExecutor` at application startup—you should find [this answer](https://stackoverflow.com/a/77862153/17865804) helpful as well.
				- 5 - More solutions, as shown in [this answer](https://stackoverflow.com/a/70873984/17865804), include using `asyncio.create_task()` (if your task is actually `async def`, but you wouldn't like to `await` for it to complete) or [background tasks](https://stackoverflow.com/a/76280152/17865804), as well as spawning a new thread (using [`threading`](https://docs.python.org/3/library/threading.html)) or process (using [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html)) in the background instead of using [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html). Moreover, if you had to perform some **heavy background computation** task that wouldn't necessarily have to be run by the same process (for example, you don't need to share memory, variables, etc.), you could also benefit from using other bigger tools like [Celery](https://fastapi.tiangolo.com/tutorial/background-tasks/#caveat). Using `apscheduler`, as demonstrated in [this answer](https://stackoverflow.com/a/79031846/17865804), might be another option as well—always choose what suits you best.
				- 6 - Use **more** [server workers](https://fastapi.tiangolo.com/deployment/server-workers/) to take advantage of multi-core CPUs, in order to run multiple processes in parallel and be able to serve more requests. For example, `uvicorn main:app --workers 4`. When using 1 worker, only one process is run. When using multiple workers, this will spawn multiple processes (all single threaded). Each process has a separate GIL, as well as its own `event loop`, which runs in the main thread of each process and executes all tasks in its thread. That means, there is only one thread that can take a lock on the interpreter of each process; unless, of course, you employ additional threads, either outside or inside the `event loop`, e.g., when using `run_in_threadpool`, a custom `ThreadPoolExecutor` or defining endpoints/`StreamingResponse` generators/background tasks/dependencies with normal `def` instead of `async def`, as well as when calling `UploadFile`'s methods (see the first two paragraphs of this answer for more details).
					- **Note** that each worker ["has its own things, variables and memory"](https://fastapi.tiangolo.com/deployment/concepts/#memory-per-process). This means that `global` variables/objects, etc., won't be shared across the processes/workers. In this case, you should consider using a database storage, or Key-Value stores (Caches), as described [here](https://stackoverflow.com/a/71537393/17865804) and [here](https://stackoverflow.com/a/65699375/17865804). Additionally, note that "if you are consuming a large amount of memory in your code, **each process** will consume an equivalent amount of memory".