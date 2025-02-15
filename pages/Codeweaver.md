created-by:: [[Person/Carlos Tarjano]]

- [[GitHub/tesserato/CodeWeaver]] [tesserato/CodeWeaver: Weave your codebase into a single, navigable Markdown document](https://github.com/tesserato/CodeWeaver/tree/main)
- #Blog [Launching CodeWeaver](https://tesserato.web.app/posts/2025-02-12-CodeWeaver-launch/index.html)
	- # Usage
	  [](https://github.com/tesserato/CodeWeaver/tree/main#usage)
	- ## For help, run
	- ```
	  codeweaver -h
	  ```
	- ## For actual usage, run
	  ```
	  codeweaver [options]
	  ```
	- **Options:**
	- | Option | Description | Default Value |
	  | ---- | ---- | ---- |
	  | `-dir <directory>` | The root directory to scan and document. | Current directory (`.`) |
	  | `-output <filename>` | The name of the output Markdown file. | `codebase.md` |
	  | `-ignore "<regex patterns>"` | Comma-separated list of regular expression patterns for paths to exclude. | `\.git.*` |
	  | `-included-paths-file <filename>` | File to save the list of paths that were included in the documentation. | None |
	  | `-excluded-paths-file <filename>` | File to save the list of paths that were excluded from the documentation. | None |
	  | `-help` | Display this help message and exit. |  |