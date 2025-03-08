alias:: [[Repomix/repomix.config.json]]

- # Repomix Config
	- The config file is in [[JSON5]] which means it can have [[Code/Comment]] in it
	- ## Config File Options
		- [[Repomix/Config/output/filePath]]
			- The name of the output file (default: `"repomix-output.txt"`)
		- [[Repomix/Config/output/style]]
			- The style of the output (`plain`, `xml`, `markdown`) (default: `"plain"`)
		- [[Repomix/Config/output/headerText]]
			- Custom text to include in the file header (default: `null`)
		- ### [[Repomix/Config/output/instructionFilePath]] - see [Custom Instruction](https://github.com/yamadashy/repomix/tree/main?tab=readme-ov-file#custom-instruction)
			- Path to **a file** containing **detailed custom instructions for the [[AI/LLM]] to include in the bundle** (default: `null`)
			- allows you to specify a separate file containing detailed instructions or context about your project. This allows AI systems to understand the specific context and requirements of your project.
			- #### #Example - this should likely be [[AI/Coding/v0/File/repo-overview]]
				- ```
				  # Coding Guidelines
				  
				  - Follow the Airbnb JavaScript Style Guide
				  - Suggest splitting files into smaller, focused units when appropriate
				  - Add comments for non-obvious logic. Keep all text in English
				  - All new features should have corresponding unit tests
				  
				  # Generate Comprehensive Output
				  
				  - Include all content without abbreviation, unless specified otherwise
				  - Optimize for handling large codebases while maintaining output quality
				  ```
			- #### [[My Notes]]
				- Perhaps a reference to
		- [[Repomix/Config/output/removeComments]]
			- Whether to remove comments from supported file types (default: `false`)
		- [[Repomix/Config/output/removeEmptyLines]]
			- Whether to remove empty lines from the output (default: `false`)
		- [[Repomix/Config/output/showLineNumbers]]
			- Whether to add line numbers to each line in the output (default: `false`)
		- [[Repomix/Config/output/copyToClipboard]]
			- Whether to copy the output to system clipboard in addition to saving the file (default: `false`)
		- [[Repomix/Config/output/topFilesLength]]
			- Number of top files to display in the summary. If set to 0, no summary will be displayed (default: `5`)
		- [[Repomix/Config/include]]
			- Patterns of files to include (using [glob patterns](https://github.com/mrmlnc/fast-glob?tab=readme-ov-file#pattern-syntax)) (default: `[]`)
		- [[Repomix/Config/ignore/useGitignore]]
			- Whether to use patterns from the project's `.gitignore` file (default: `true`)
		- [[Repomix/Config/ignore/useDefaultPatterns]]
			- Whether to use default ignore patterns (default: `true`)
			- see [defaultIgnore.ts](https://github.com/yamadashy/repomix/blob/main/src/config/defaultIgnore.ts) for more details.
		- [[Repomix/Config/ignore/customPatterns]]
			- Additional patterns to ignore (using [glob patterns](https://github.com/mrmlnc/fast-glob?tab=readme-ov-file#pattern-syntax)) (default: `[]`)
		- [[Repomix/Config/security/enableSecurityCheck]]
			- Whether to perform security checks on files (default: `true`)
	- ## #Example Configuration
		- ~~~json
		  {
		    "output": {
		      "filePath": "repomix-output.xml",
		      "style": "xml",
		      "parsableStyle": true,
		      "compress": false,
		      "headerText": "Custom header information for the packed file.",
		      "fileSummary": true,
		      "directoryStructure": true,
		      "removeComments": false,
		      "removeEmptyLines": false,
		      "showLineNumbers": false,
		      "copyToClipboard": true,
		      "topFilesLength": 5,
		      "includeEmptyDirectories": false,
		    },
		    "include": [
		      "**/*"
		    ],
		    "ignore": {
		      "useGitignore": true,
		      "useDefaultPatterns": true,
		      // Patterns can also be specified in .repomixignore
		      "customPatterns": [
		        "additional-folder",
		        "**/*.log"
		      ],
		    },
		    "security": {
		      "enableSecurityCheck": true
		    },
		    "tokenCount": {
		      "encoding": "o200k_base"
		    },
		  }
		  ~~~