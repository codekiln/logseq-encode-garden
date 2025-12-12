# `rust-script`
	- ## What **rust-script** Is
		- **rust-script** is a lightweight tool that allows you to run **single-file Rust programs** as scripts—similar to how you might use Python, Ruby, or Node.js—without manually creating a full Cargo project.
		- You can write Rust in a single `.rs` file with special "script headers," and run it directly with:
		- ~~~bash
		  rust-script my_script.rs
		  ~~~
		- It handles:
			- On-demand compilation
			- Dependency resolution via Cargo
			- Caching for fast re-runs
			- Optional shebang execution (`#!/usr/bin/env rust-script`)
	- ## Why People Use rust-script
		- **rust-script makes Rust feel like a scripting language** while preserving full Rust performance and tooling.
		- Use cases include:
			- Utility scripts
			- Build scripts and automation
			- Prototyping Rust code
			- Teaching and examples
			- Quick CLIs without scaffolding
		- Compared with writing a whole Cargo project, it's dramatically quicker for small tasks.
	- ## Key Features
		- ### 1. **Single-file executables**
			- Write a script like:
			- ~~~rust
			  fn main() {
			    println!("Hello, world!");
			  }
			  ~~~
			- Run with:
			- ~~~bash
			  rust-script hello.rs
			  ~~~
		- ### 2. **Inline dependencies**
			- Add dependencies right in the file (much like Rust's `cargo-script` used to allow):
			- ~~~rust
			  //! cargo-deps: reqwest = "0.11", tokio = { version = "1", features = ["full"] }
			  
			  #[tokio::main]
			  async fn main() {
			    let body = reqwest::get("https://example.com").await.unwrap().text().await.unwrap();
			    println!("{body}");
			  }
			  ~~~
			- rust-script reads these headers, generates a temporary Cargo project, compiles it, and caches it.
		- ### 3. **Shebang support**
			- You can make Rust scripts directly executable on Unix-like systems:
			- ~~~rust
			  #!/usr/bin/env rust-script
			  fn main() {
			    println!("Hello from a shebang!");
			  }
			  ~~~
			- Run directly:
			- ~~~bash
			  ./myscript
			  ~~~
		- ### 4. **Cargo-like experience, minimal ceremony**
			- It automatically:
				- Creates an implicit Cargo manifest
				- Pulls dependencies
				- Compiles and caches binaries
			- You stay focused on the code.
		- ### 5. **Fast re-runs via caching**
			- The first run compiles; subsequent runs are nearly instant unless the script changes.
	- ## How rust-script Compares to Alternatives
		- **rust-script**: Easiest for single-file scripts with inline deps; very ergonomic.
		- **cargo-script**: Similar predecessor; rust-script is generally more up-to-date and idiomatic.
		- **cargo + `fn main`**: Standard approach, but requires project scaffolding.
		- **EvCxR** (Jupyter/REPL): Great for interactive experimentation; slower for scripting.
		- **shebang with `cargo run`**: Possible but much heavier.
		- rust-script strikes the balance between **real Rust** and **script-like workflows**.
	- ## Installation
		- [[cargo/install]] is used to install binary crates (executables) globally, not libraries. Libraries are added as dependencies in `Cargo.toml`.
		- ~~~bash
		  cargo install rust-script
		  ~~~
	- ## Execution model
		- When invoked:
			- It parses script headers (dependencies, features, edition).
			- Generates a temporary Cargo project under the hood.
			- Compiles and caches the executable.
			- Runs the compiled binary.
		- The cache invalidates when:
			- The script contents change
			- The inline dependency list changes
			- Toolchain changes
	- ## Limitations
		- Not ideal for multi-file projects
		- Compilation is still Rust-fast (but not Python-fast)
		- Inline dependency parsing has some constraints (header comment formats)
		- Requires Cargo and the Rust toolchain
	- ## Quick Example
		- `echo.rs`:
		- ~~~rust
		  //! cargo-deps: clap = "4"
		  
		  use clap::Parser;
		  
		  #[derive(Parser)]
		  struct Args {
		    message: String,
		  }
		  
		  fn main() {
		    let args = Args::parse();
		    println!("You said: {}", args.message);
		  }
		  ~~~
		- Run:
		- ~~~bash
		  rust-script echo.rs "hello"
		  ~~~
	- If you'd like, I can also prepare:
		- A cheat sheet
		- A comparison to Python / Node scripting workflows
		- A template for a reusable internal tool script
		- Examples for specific tasks (file I/O, HTTP, concurrency)