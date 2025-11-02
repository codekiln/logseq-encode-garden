alias:: [[Context Local]], [[Context Locals]]
tags:: [[Term]]

- # [[Programming/Language/Feature/Context/Local]]
	- A language feature that provides storage that flows with the logical flow of execution, allowing information (like correlation IDs, tracing data) to be carried through async/await or promise chains without being explicitly passed at each step.
	- ## Definition
		- Similar to thread-local storage, but with a much narrower scope that follows the logical flow of execution rather than the thread
		- Enables automatic propagation of context information (correlation IDs, tracing data, etc.) through async operations
		- Essential for maintaining context when stack frames are lost in async/await or promise-based code
	- ## The Problem It Solves
		- **Stack frames** implicitly carry information—correlation IDs, tracing context, etc. sit in the stack and can be accessed by walking up the stack
		- When using **async/await or promises**, the stack context is lost because execution is chained across promises rather than following a linear stack
		- This makes it very hard to carry information through all potential paths that a promise chain might take
		- Example: A correlation ID that should be attached to every log event and error event becomes difficult to propagate through promise chains
	- ## Language Implementations
		- **.NET**: Called "execution context"
		- **JavaScript (Node.js)**: Evolved from domains → Async Hooks → Async Local Storage (backend only; browsers still don't have it)
		- **Other languages**: Known as "context locals" in some ecosystems
	- ## Use Cases
		- **OpenTelemetry tracing**: Ensuring tracing context flows through async operations
		- **Correlation IDs**: Propagating request correlation IDs through log events and error events
		- **Request context**: Maintaining request-level context in async code
	- ## Related
		- [[Programming/Language/Feature/Async/Await]]
		- [[Person/Gergely Orosz/Podcast/25/10/Python Go Rust Typescript AI Armin Ronacher]]

