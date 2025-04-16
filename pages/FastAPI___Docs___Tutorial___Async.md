# [Concurrency and async / await - FastAPI](https://fastapi.tiangolo.com/async/)
	- ### async and await
		- > I created another library on top of AnyIO, as a thin layer on top, to improve a bit the type annotations and get better **autocompletion**, **inline errors**, etc. It also has a friendly introduction and tutorial to help you **understand** and write **your own async code**:  [[Asyncer]] [Asyncer](https://asyncer.tiangolo.com/). It would be particularly useful if you need to **combine async code with regular** (blocking/synchronous) code.
	- ### [[FastAPI/Docs/Tutorial/Async/Very Technical Details]] [here](https://fastapi.tiangolo.com/async/#very-technical-details)
		- > When you declare a *path operation function* with normal `def` instead of `async def`, it is run in an external threadpool that is then awaited, instead of being called directly (as it would block the server).
		-