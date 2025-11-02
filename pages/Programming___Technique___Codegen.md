alias:: [[Codegen]]
tags:: [[Term]]

- # Codegen
	- Short for "code generation," codegen is a programming technique where code is automatically generated from specifications, templates, or other structured data rather than being written manually.
	- ## Common Use Cases
		- Generating API client SDKs from [[OpenAPI]] specifications (e.g., [[StreamIO/GitHub/stream-py]] uses codegen to generate code from OpenAPI)
		- Creating boilerplate code from templates
		- Using [[AI/Coding]] tools and [[LLM]]s to generate code
		- Generating code from domain-specific languages (DSLs) or configuration files
	- ## Benefits
		- Reduces manual coding effort and potential errors
		- Ensures consistency across generated code
		- Allows maintaining a single source of truth (specification) that drives code generation
		- Enables cross-language code generation from the same specification (e.g., generating SDKs in multiple languages from one OpenAPI spec)
	- ## Related Concepts
		- Modern codegen and OpenAPI-driven SDKs are often preferred over forcing a single language across front-end and back-end boundaries (see [[Person/Gergely Orosz/Podcast/25/10/Python Go Rust Typescript AI Armin Ronacher]])