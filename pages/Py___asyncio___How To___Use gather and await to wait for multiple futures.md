tags:: [[Diataxis/How To]]

- # How to use [[Py/asyncio/gather]] and [[Py/asyncio/wait]] to await multiple futures
	- ## Overview
		- This guide shows you how to efficiently handle multiple coroutines in Python using `asyncio.gather` and `asyncio.wait`
		- For developers working with asynchronous code who need to manage multiple concurrent operations
		- Learn when to use each method based on your specific needs
	- ## Prerequisites
		- Basic understanding of Python's async/await syntax
		- Python 3.7 or later installed
		- Understanding of coroutines and futures
	- ## Steps
		- ### 1. Using asyncio.gather
			- Best for when you want to run multiple coroutines concurrently and collect all their results
			- Example:
				- ~~~python
				import asyncio
				
				async def fetch_data(id: int) -> dict:
				    await asyncio.sleep(1)  # Simulating API call
				    return {"id": id, "data": f"result_{id}"}
				
				async def main():
				    # Run three fetch operations concurrently
				    results = await asyncio.gather(
				        fetch_data(1),
				        fetch_data(2),
				        fetch_data(3)
				    )
				    print(results)  # [{"id": 1, ...}, {"id": 2, ...}, {"id": 3, ...}]
				
				asyncio.run(main())
				~~~
			- Key points about `gather`:
				- Returns results in the same order as the input coroutines
				- Waits for all coroutines to complete
				- Raises the first exception encountered (unless `return_exceptions=True`)
		- ### 2. Using asyncio.wait
			- Best for more fine-grained control over multiple coroutines
			- Example:
				- ~~~python
				import asyncio
				from asyncio import FIRST_COMPLETED
				
				async def process_data(id: int) -> str:
				    await asyncio.sleep(id)  # Different delays
				    return f"Task {id} completed"
				
				async def main():
				    # Create task objects
				    tasks = [
				        asyncio.create_task(process_data(i))
				        for i in range(1, 4)
				    ]
				    
				    # Wait for first task to complete
				    done, pending = await asyncio.wait(
				        tasks,
				        return_when=FIRST_COMPLETED
				    )
				    
				    # Process completed task
				    for task in done:
				        print(f"First result: {task.result()}")
				    
				    # Cancel remaining tasks
				    for task in pending:
				        task.cancel()
				
				asyncio.run(main())
				~~~
			- Key points about `wait`:
				- Returns two sets: `done` and `pending` tasks
				- Offers control over when to return using `return_when`:
					- `FIRST_COMPLETED`: Return when any task completes
					- `FIRST_EXCEPTION`: Return when any task raises an exception
					- `ALL_COMPLETED`: Return when all tasks complete (default)
		- ### 3. Choosing between gather and wait
			- Use `gather` when:
				- You need all results in a specific order
				- You want to handle all coroutines as a single unit
				- You want the results as a list instead of completed futures
			- Use `wait` when:
				- You need to process results as they complete
				- You want to implement timeouts
				- You need to cancel remaining tasks after some condition
	- ## Troubleshooting
		- Common issues with `gather`:
			- If an exception occurs, all tasks continue running by default
			- To handle exceptions individually, use `return_exceptions=True`
		- Common issues with `wait`:
			- Tasks not being cancelled properly
			- Make sure to explicitly cancel pending tasks if needed
			- Remember to handle exceptions from task.result()
	- ## Related
		- [[Py/asyncio/create_task]]
		- [[Py/asyncio/Task]]
		- [[Py/asyncio/Future]]
		- [[Py/asyncio/timeout]]