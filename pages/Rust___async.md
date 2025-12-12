- # Rust async
	- Here's a clean, Rust-native explanation of the selected line and the constructs involved.
	- ## 🔍 The selected line
		- ~~~rust
		  let _cleanup = runtime.block_on(async { client.delete_project(project_id).await });
		  ~~~
		- This combines **four** concepts:
			- **`async { ... }` block**
			- **`.await` operator**
			- **A future value**
			- **A synchronous executor call (`block_on`)**
		- Let's break those down.
	- ## 1. `async { ... }` — an async block expression
		- `async { ... }` is an **expression** that returns a *future* — specifically an *anonymous type that implements `Future<Output = T>`*.
		- Inside an async block, you can use `await`, but the block itself **does not run** until something *polls* the future (usually an executor).
		- It is similar to:
			- ~~~rust
			  async fn foo() -> T { ... }
			  ~~~
			- but inline.
		- Other Rust constructs that work the same way (i.e., block forms that produce values) include:
			- `unsafe { ... }`
			- `const { ... }`
			- `try { ... }` (unstable; returns `Result`)
			- `loop { ... }`, `if { ... }`, etc., because *blocks are expressions*
		- Rust's rule: **Blocks are expressions that evaluate to the last expression inside.**
		- So the async block:
			- ~~~rust
			  async {
			    client.delete_project(project_id).await
			  }
			  ~~~
			- produces a future whose output type is whatever `.await` returns — here likely `Result<(), SomeError>` or whatever the API defines.
	- ## 2. What is `.await`?
		- `.await` is **neither a method nor a property** — it is a **postfix operator built into the language parser**, like `?`.
		- It transforms a `Future<Output = T>` into a `T`, *but only inside an async context*.
		- If you want an analogy:
			- It is like Python `await f()`, **but syntactically resembles a field access** (`obj.field`).
			- Under the hood, it compiles down to state-machine code that polls the future and suspends.
		- Its "type"?
			- The expression:
				- ~~~rust
				  some_future.await
				  ~~~
				- has the type **`T`**, where the original future was `Future<Output = T>`.
	- ## 3. The sequence of evaluation
		- Your full line:
			- ~~~rust
			  let _cleanup = runtime.block_on(async { client.delete_project(project_id).await });
			  ~~~
			- ⚙️ *Steps:*
				- `async { ... }` creates a future of type `impl Future<Output = DeleteResult>`.
				- `runtime.block_on(...)` takes that future and **runs it to completion**, turning async → sync.
				- The result of the `.await` inside is returned out of the async block.
				- That value becomes `_cleanup`.
	- ## 4. Are there other parts of Rust with similar syntax?
		- Yes — Rust has several "block operators" and "postfix operators":
			- ### **Block expressions:**
				- `async { … }` — future-producing
				- `unsafe { … }` — unsafe block
				- `try { … }` — result-producing block (unstable)
				- `const { … }` — const-evaluated block (stable)
				- `{ … }` plain blocks
			- ### **Postfix operators (built-in, not methods):**
				- `.await`
				- `?`
				- Array indexing (`arr[idx]`)
				- Deref and reference are prefix/suffix but part of expression syntax, not methods.
		- These are all *language-level constructs*, unlike Python where most constructs desugar into method calls.
	- ## Quick mental model
		- **`async { ... }`** → "Create a future value."
		- **`.await`** → "Extract the future's output; pause until ready."
		- **`block_on(fut)`** → "Drive the future to completion from sync code."
		- You can think of `.await` like Python `await`, **but it is not a function or property — it is language syntax.**
