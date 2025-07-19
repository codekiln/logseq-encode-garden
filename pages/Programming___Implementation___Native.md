alias:: [[Native Implementation]]

- # Native Implementation vs Wrapper Rendering Explanation
	- ## Overview
		- A **native implementation** means a system reimplements functionality entirely within its own runtime and toolchain, without calling out to a foreign environment or tool—such as JavaScript engines or CLI wrappers.
	- ## Context
		- Many languages and platforms add support for complex tools like diagram rendering, image processing, or parsers by wrapping existing tools written in another language.
		- The term "native implementation" arises when there's a desire to avoid such wrappers and instead build or port the feature into the host environment directly.
		- Mermaid rendering provides a concrete example: it's originally implemented in JavaScript, but other languages often want to render Mermaid diagrams without relying on JavaScript or Node.js.
	- ## Key Principles
		- **Same-Language Execution** – Native implementations execute entirely within the host language’s runtime (e.g. Python, Rust, Go).
		- **No Foreign Process Calls** – Native implementations do not shell out to tools like `mmdc`, embed a browser, or depend on headless Node-based infrastructure.
		- **Self-Sufficiency** – All logic for parsing, layout, and rendering is reimplemented or directly handled by the host language’s libraries.
	- ## Mechanism
		- ### Native Implementation
			- Reimplement the tool’s grammar, parsers, and layout engines.
			- Use native graphics libraries to generate output (SVG, PNG, etc.).
			- Avoid runtime dependencies on external toolchains.
		- ### Wrapper-Based Approach
			- Generate intermediate output (e.g., Mermaid `.mmd` text).
			- Invoke a command-line tool like `mmdc` or spin up a headless browser.
			- Capture and return rendered output from the subprocess.
	- ## Examples
		- ~~~python
		  # Wrapper example (Python calling mmdc CLI)
		  import subprocess, tempfile
		  diagram = "graph TD; A-->B;"
		  with tempfile.NamedTemporaryFile(suffix=".mmd", delete=False) as f:
		      f.write(diagram.encode())
		  subprocess.run(["mmdc", "-i", f.name, "-o", "out.svg"])
		  ~~~
		- ~~~rust
		  // Hypothetical native Rust Mermaid renderer
		  let graph = mermaid_rs::parse("graph TD; A-->B;")?;
		  let svg   = mermaid_rs::render(graph);
		  std::fs::write("out.svg", svg)?;
		  ~~~
	- ## Misconceptions
		- **“Embedding a tool makes it native.”** Embedding Node.js still relies on external execution and does not count as native.
		- **“Code generation is enough.”** Generating Mermaid syntax (`.mmd`) is not rendering; native refers to processing and rendering the diagram.
	- ## Related
		- [[Mermaid/mmdc]]
			- [Mermaid CLI (`mmdc`) GitHub](https://github.com/mermaid-js/mermaid-cli)
			- [MermaidJS Documentation](https://mermaid.js.org/)