# Logseq Asset Linker
	- ## GitHub Link
		- [GitHub - logseq-asset-linker.mdc](https://github.com/codekiln/logseq-encode-garden/blob/main/.cursor/rules/logseq-asset-linker.mdc)
	- ## Rule Contents
		- ### Description
			- This rule helps convert file paths into relative Markdown links for Logseq
			- Logseq uses **namespaces** to add hierarchy in the file system
			- In Logseq, page titles with namespaces (e.g., `[[Work/Projects/Logseq]]`) become filenames with double underscores (`Work__Projects__Logseq.md`)
			- This allows Logseq to show hierarchical namespaces while storing files in a single directory
			- Example: `[[Parent/Child/Grandchild]]` becomes `Parent__Child__Grandchild.md`
		- ### Use Case 1: Path Name to Markdown Asset Link
			- When given a full file path to an asset, this rule will:
				- 1. Find the Logseq folder in the path
				- 2. Format a relative link from `logseq/pages/`
				- 3. Generate copyable Markdown code
			- #### Example
				- Input: `/a/b/c/logseq/assets/Course-101/assignments/week3/notes/course101__assignment__03__notes.pdf`
				- Output:
					- ~~~markdown
					  ![course101__assignment__03__notes.pdf](../assets/Course-101/assignments/week3/notes/course101__assignment__03__notes.pdf)
					  ~~~
		- ### Use Case 2: Namespace Name to Asset Path
			- This rule converts Logseq page references to filenames and paths
			- Given `[[A/B/C/D]]`, it generates:
				- Filename: `A__B__C__D` with appropriate extension
				- Asset path: `../assets/A/B/C/D/A__B__C__D`
				- Sanitized filenames for compatibility
			- #### Examples
				- Example 1:
					- Input: `[[Course-101/homework/03/04 linear equations]]`
					- Output (PDF filename):
						- ~~~markdown
						  Course-101__homework__03__04_linear_equations.pdf
						  ~~~
				- Example 2:
					- Input: `[[Course-101/homework/03/04 linear equations]]`
					- Output (asset path):
						- ~~~markdown
						  ../assets/Course-101/homework/03/04/Course-101__homework__03__04_linear_equations.pdf
						  ~~~
				- Example 3:
					- Input: `[[Projects/Research/Notes]]`
					- Basic link:
						- ~~~markdown
						  [Notes](../assets/Projects/Research/Projects__Research__Notes)
						  ~~~
					- PDF link:
						- ~~~markdown
						  ![Notes](../assets/Projects/Research/Projects__Research__Notes.pdf)
						  ~~~
					- Folder link:
						- ~~~markdown
						  [assets in Projects/Research](../assets/Projects/Research/)
						  ~~~
				- Example 4:
					- Input: `[[Course-101/homework/03/04 linear equations]]`
					- PNG asset link:
						- ~~~markdown
						  ![04_linear_equations.png](../assets/Course-101/homework/03/04/Course-101__homework__03__04_linear_equations.png)
						  ~~~
		- ### File Link Handling Instructions
			- #### 1. File Links with `file:///` Scheme
				- For absolute paths, use `file:///` protocol
				- Example:
					- Input: `/Users/username/documents/projects/example-docs/example-docs_1234567890.json`
					- Output:
						- ~~~markdown
						  [example-docs_1234567890.json](file:///Users/username/documents/projects/example-docs/example-docs_1234567890.json)
						  ~~~
			- #### 2. Logseq Asset Links
				- For files in Logseq projects:
					- Use relative paths from `logseq/pages/`
					- Assume common root directories (`assets/` or `pages/`)
					- Use proper Markdown link syntax
				- Example:
					- Input: `/Users/username/dev/clones/logseq/assets/Folder/File.ext`
					- Output:
						- ~~~markdown
						  [File.ext](../assets/Folder/File.ext)
						  ~~~
			- #### 3. Namespaced Assets Format
				- Replace `/` with `__` in namespaces
				- Sanitize filenames (replace non-alphanumeric with `_`)
				- Follow Logseq folder structure
				- Example:
					- Input namespace: `[[Folder/Subfolder/File]]`
					- Filename: `Folder__Subfolder__File.ext`
					- Path: `../assets/Folder/Subfolder/Folder__Subfolder__File.ext`
					- Output:
						- ~~~markdown
						  [File](../assets/Folder/Subfolder/Folder__Subfolder__File.ext)
						  ~~~
		- ### Key Rules and Best Practices
			- Use `file:///` scheme for direct file paths when requested
			- Use relative paths for Logseq assets
			- Convert slashes to double underscores in namespaces
			- Sanitize filenames for compatibility
			- Use proper Markdown link syntax:
				- `[name](relative/path)` for Logseq links
				- `[name](file:///absolute/path)` for direct file links