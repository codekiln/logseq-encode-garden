alias:: [[Microsoft/GitHub/poml]]
tags:: [[Diataxis/Explanation]]
- # [POML (Prompt Orchestration Markup Language)](https://github.com/microsoft/poml)
	- ## Overview
		- POML is a markup language designed to enhance prompt engineering for Large Language Models (LLMs)
		- Created by Microsoft and hosted on GitHub
		- Brings structure and maintainability to prompt development
		- Addresses challenges in prompt engineering like complex data integration and format sensitivity
	- ## Context
		- Prompt engineering has evolved from simple text prompts to complex, multi-part instructions
		- Developers face challenges with:
			- Complex data integration from multiple sources
			- Format sensitivity where small changes break prompts
			- Difficulty maintaining and reusing prompt components
			- Lack of separation between content and presentation
		- POML addresses these challenges by providing a structured markup approach similar to how HTML structures web content
	- ## Key Principles
		- **Structured Markup**: Uses HTML-like syntax with semantic components
		- **Separation of Concerns**: Content separated from presentation through CSS-like styling
		- **Modularity**: Promotes reusable, component-based prompt design
		- **Data Integration**: Built-in support for diverse data types and external sources
		- **Developer-Friendly**: Familiar syntax and tooling for developers
	- ## Mechanism
		- ### Markup Components
			- Semantic elements like `<role>`, `<task>`, and `<example>`
			- Custom components for specific prompt patterns
			- Hierarchical structure for complex prompts
		- ### Data Handling
			- Supports embedding diverse data types
			- Can reference external sources like text files, spreadsheets, and images
			- Specialized components for different data formats
		- ### Styling System
			- CSS-like styling that separates content from presentation
			- Dynamic styling modifications without changing core prompt logic
			- Consistent formatting across prompts
		- ### Templating Engine
			- Variables using `{{ }}` syntax
			- Loops with `for` statements
			- Conditionals with `if` statements
			- Variable definitions with `<let>` tags
	- ## Examples
		- Basic POML structure with templating:
			- ~~~xml
			  <role>Assistant</role>
			  <task>Summarize the following text</task>
			  <let name="items" value="['apple', 'banana', 'cherry']" />
			  <if condition="{{ items.length > 0 }}">
			    <for item in items>
			      - {{ item }}
			    </for>
			  </if>
			  ~~~
		- Integration with external data:
			- ~~~xml
			  <role>Data Analyst</role>
			  <data source="spreadsheet.csv" format="table" />
			  <task>Analyze trends in the provided data</task>
			  ~~~
	- ## Development Toolkit
		- Visual Studio Code extension with:
			- Syntax highlighting
			- Auto-completion
			- Interactive testing
		- SDKs available for:
			- Node.js
			- Python
		- Built-in validation and error checking
	- ## Misconceptions
		- POML replaces plain text prompts → **False**. POML compiles down to text but provides structure during development
		- Only useful for complex prompts → **False**. Even simple prompts benefit from structure and reusability
		- Requires learning a new programming language → **False**. Uses familiar HTML/CSS-like syntax that developers already know
		- Only works with specific LLMs → **False**. POML is LLM-agnostic and compiles to plain text prompts
	- ## Related
		- [[rulesync]] - Tool that could benefit from POML's templating and include capabilities
		- [[Person/Kazuki Yamada]] - Creator of rulesync who discussed POML integration
		- [[Prompt Engineering]]
		- [[LLM]]
		- [[Microsoft]]
