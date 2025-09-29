- # [JSONC | JSONC Specification](https://jsonc.org/)
	- ## About
	  id:: 67c822b0-3271-41da-a14f-4f023a1f4556
		- JSONC (JSON with Comments) is an extension of [[json]] that allows comments within JSON data. This specification defines the syntax and semantics of JSONC.
		- The JSONC format was informally introduced by Microsoft to be used for VS Code's configuration files (`settings.json`, `launch.json`, `tasks.json`, etc). Alongside the informal format, a publicly-available parser ([`jsonc-parser`](https://www.npmjs.com/package/jsonc-parser)) was supplied to parse those configuration files. The goal of this specification is to formalize the JSONC format as what [`jsonc-parser`](https://www.npmjs.com/package/jsonc-parser) considers valid while using its default configurations.
		- JSONC follows the same syntax rules as JSON with the addition of JavaScript style comments. Comments can be either single-line or multi-line.
	- ## Comparison with [[json/5]]
		- Both JSONC and [[json/5]] extend JSON to support comments, but they have different approaches:
			- **JSONC**: Minimal extension - adds only comments to standard JSON
			- **JSON5**: Comprehensive extension - adds comments, unquoted keys, trailing commas, and other JavaScript-like features
		- JSONC is more conservative and maintains closer compatibility with standard JSON
		- JSON5 is more permissive and allows more JavaScript-like syntax
	- ## #Example
		- ```jsonc
		  {
		    // This is a single-line comment
		    "name": "example",
		    "value": 42,
		    /* This is a 
		       multi-line comment */
		    "enabled": true
		  }
		  ```
	- ## Use Cases
		- Configuration files in development tools (especially VS Code)
		- Documentation within JSON data structures
		- Human-readable JSON files that benefit from explanatory comments
	- ## Related
		- [[json/5]] - Alternative JSON extension with broader syntax support
		- [[json]] - Standard JSON format
		- [jsonc-parser](https://www.npmjs.com/package/jsonc-parser) - Official parser implementation
