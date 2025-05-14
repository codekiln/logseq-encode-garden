tags:: [[Diataxis/Explanation]], [[Pytest/Fixture]]

- # Explanation: `yield` vs `return` in **async** `pytest` fixtures
	- This document focuses on *why* and *when* you choose one pattern over the other rather than *how* to write the code step-by-step.
	- ## Purpose
		- Async fixtures can either
			- **produce a value and stop**, or
			- **manage a resource whose lifetime spans the whole test**.
		- Choosing the wrong pattern causes resource leaks, flakey tests, or the dreaded *"coroutine was never awaited"* warnings.
	- ## The life-cycle principle
		- > **If your fixture *owns* something that must be cleaned up later, use `yield`.
		- If it merely hands back data, use `return`.**
		- The rule mirrors synchronous fixtures; `pytest` just happens to run the teardown code *after* the `await`-friendly `yield` section on the same event loop [official docs](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html#yield-fixtures).
	- ## When `return` is enough
		- A fixture gathers **pure data** (e.g., static config, sample JSON, calculated values).
		- Nothing needs disposal or rollback once the test is finished.
		- Example:
			- ~~~
			  @pytest_asyncio.fixture
			  async def static_payload() -> dict[str, str]:
			  return {"status": "ok"}           # no teardown needed
			  ~~~
	- ## When to prefer `yield`
		- The fixture **allocates or opens** anything that must be closed, cancelled, or rolled back:
			- database engines
			- HTTP clients
			- temporary queues or files
		- You need **guaranteed teardown**, even if the test crashes.
		- Example with an async context manager:
			- ~~~
			  import httpx
			  import pytest_asyncio
			  
			  @pytest_asyncio.fixture
			  async def http_client():
			  async with httpx.AsyncClient(base_url="http://test") as client:
			      yield client                  # pytest runs code _after_ the context exits
			  ~~~
		- Code after `yield` (or after `async with`) executes as teardown inside the running loop, so you can still `await` cleanup work safely — a detail confirmed in the `pytest-asyncio` fixture reference [docs](https://pytest-asyncio.readthedocs.io/en/stable/reference/fixtures/index.html).
	- ## Decision Table: yield vs return
		- | Situation                | Pattern      |
		  |-------------------------|-------------|
		  | Pure data, no teardown  | **`return`** |
		  | Resource with cleanup   | **`yield`**  |
	- ## How async generator fixtures work under the hood
		- `pytest` sees an **async generator** (`async def …` with `yield`).
		- It **awaits** the setup portion *before* `yield`.
		- The yielded value is injected into dependent fixtures or tests.
		- After the test finishes, `pytest` **resumes** the generator so that any code *after* `yield` (or the implicit `async with` close) runs as teardown on the same loop.
		- Because `pytest` controls the coroutine, you *never* call `await` on a fixture in the test body; you only await inside the fixture itself.  Accidentally returning a coroutine rather than its awaited result leads to "coroutine was never awaited" warnings, a common Stack Overflow pitfall [discussion](https://stackoverflow.com/questions/77285773/runtimewarning-coroutine-was-never-awaited-in-python-tests).
	- ## Composing fixtures (dependency injection)
		- ~~~python
		  @pytest_asyncio.fixture
		  async def db_engine() -> AsyncEngine:
		  engine = create_async_engine(DB_URL)
		  yield engine
		  await engine.dispose()
		  
		  @pytest_asyncio.fixture
		  async def db_session(db_engine):     # <-- no `await`
		  async with async_sessionmaker(db_engine)() as session:
		      yield session
		  ~~~
		- **No `await`** on `db_engine` in `db_session`. `pytest` injects the *resolved* engine.
		- Each fixture still awaits its own async work internally.
		- The dependency graph is resolved once; results are cached per scope [pytest docs](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html#the-scope-direction).
	- ## Teardown patterns and edge cases
		- **Multiple cleanup steps**: chain them after `yield` with `try/finally`.
		- **Dynamic teardown**: fall back to `request.addfinalizer()` only if you must register callbacks at runtime; otherwise, `yield` is clearer [discussion](https://stackoverflow.com/questions/78721505/choosing-between-yield-and-addfinalizer-in-pytest-fixtures-for-teardown).
	- ## Summary
		- **Use `return`** for read-only data.
		- **Use `yield`** for anything requiring teardown—mirrors synchronous etiquette.
		- Never `await` a fixture parameter; pytest already awaited it.
		- Put all async cleanup *after* `yield` or inside `async with`.
		- Understanding these patterns keeps async tests fast, leak-free, and readable.