tags:: [[JS/Library]], [[Linter]], [[Diataxis/Explanation]]

- # BiomeJS Conceptual Overview
	- ## Overview
		- BiomeJS is a comprehensive web development toolchain that combines formatting, linting, and code analysis into a single, fast tool
		- Built with Rust for performance, designed as a unified replacement for multiple tools like ESLint, Prettier, and other JavaScript tooling
		- Aims to be "one toolchain for your web project" with a focus on speed, simplicity, and scalability
	- ## Context
		- JavaScript ecosystem traditionally requires multiple tools: ESLint for linting, Prettier for formatting, various plugins for different file types
		- This fragmentation leads to:
			- Configuration complexity across multiple tools
			- Performance overhead from running separate processes
			- Inconsistent behavior between tools
			- Maintenance burden of keeping tools compatible
		- BiomeJS emerged to consolidate these tools into a single, performant solution
		- Inspired by rust-analyzer's architecture for language tooling
	- ## Key Principles
		- **Unified Toolchain** - Single tool handles formatting, linting, and code analysis
		- **Performance First** - Built in Rust, approximately 35x faster than Prettier
		- **Zero Configuration** - Works out of the box with sensible defaults
		- **Compatibility** - 97% compatible with Prettier, includes 360+ rules from ESLint ecosystem
		- **Scalability** - Designed to handle projects of any size efficiently
		- **Actionable Diagnostics** - Provides detailed, contextual error messages
	- ## Mechanism
		- ### Architecture
			- Built in Rust for native performance
			- Single binary handles multiple operations
			- Inspired by rust-analyzer's innovative language tooling approach
			- Can process multiple file types through unified API
		- ### Operations
			- **Formatting**: Reformats code to consistent style (97% Prettier-compatible)
			- **Linting**: Checks code against 360+ rules from ESLint and TypeScript ESLint
			- **Check**: Single command (`biome check`) runs all operations together
		- ### Supported Languages
			- JavaScript, TypeScript, JSX, TSX
			- JSON
			- HTML, CSS
			- GraphQL
	- ## Examples
		- ### Basic Usage
			- ~~~bash
			  # Format files
			  biome format ./src

			  # Lint files
			  biome lint ./src

			  # Run all checks at once
			  biome check ./src
			  ~~~
		- ### Configuration
			- Zero configuration required to start
			- Optional `biome.json` for customization:
				- ~~~json
				  {
				    "formatter": {
				      "indentStyle": "space",
				      "indentSize": 2
				    },
				    "linter": {
				      "rules": {
				        "recommended": true
				      }
				    }
				  }
				  ~~~
		- ### Editor Integration
			- Available as VS Code extension
			- Supports real-time formatting and linting
			- Provides instant feedback in editor
	- ## Misconceptions
		- **BiomeJS is just a faster Prettier** → False. It's a complete toolchain that also includes comprehensive linting (360+ rules) and other development tools
		- **You need extensive configuration to use it** → False. BiomeJS works with zero configuration, though it can be customized when needed
		- **It only works with JavaScript** → False. Supports JavaScript, TypeScript, JSON, HTML, CSS, GraphQL, and their variants (JSX, TSX)
		- **It's incompatible with existing setups** → Mostly false. 97% Prettier compatibility and includes ESLint rule equivalents
	- ## Related
		- [[GitHub/dyoshikawa/rulesync]] - Uses BiomeJS in its development environment
		- [[ESLint]] - Traditional JavaScript linter that BiomeJS aims to replace
		- [[Prettier]] - Code formatter that BiomeJS is 97% compatible with
		- [[Rust]] - Programming language BiomeJS is built with for performance
		- [BiomeJS Official Site](https://biomejs.dev)
