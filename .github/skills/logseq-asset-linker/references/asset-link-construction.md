# Constructing a Logseq Asset Link

This is an extension to the LFM formatting rules describing how to construct links to assets in the `assets/` directory and its subdirectories.

### Description

Convert macOS file paths into relative Markdown links for Logseq.

Logseq uses **namespaces**: page titles that use namespaces (e.g., `[[Work/Projects/Logseq]]`) are converted to filenames by replacing slashes (`/`) with double underscores (`__`), resulting in `Work__Projects__Logseq.md`. Any namespace structure like `[[Parent/Child/Grandchild]]` becomes a single file named `Parent__Child__Grandchild.md`.

> Note on underscores: **asset filenames** derived from namespaces use **double** underscores (`__`) as in this rule's examples. Page files on disk use **triple** underscores (`___`). Keep them distinct.

### Use Case 1: Path Name to Markdown Asset Link

Given a full file path to an asset:
- Identify the Logseq folder within the path.
- Format a relative link starting from a typical page location (`logseq/pages/`), assuming the page is `logseq/pages/somepage.md`.
- Generate Markdown that can be directly copied into Logseq with correct relative paths.
- Always format the response as a code snippet.

#### Example
- **USER:** Can you give me the link for `/a/b/c/logseq/assets/Course-101/assignments/week3/notes/course101__assignment__03__notes.pdf`?
  ```markdown
  ![course101__assignment__03__notes.pdf](../assets/Course-101/assignments/week3/notes/course101__assignment__03__notes.pdf)
  ```

### Use Case 2: Logseq Namespace Name to Asset Path

- Turn a Logseq page reference from a namespaced name into a filename and an asset path.
- Given `[[A/B/C/D]]`, generate filename `A__B__C__D` of the appropriate type (png, pdf, etc.) and expected location `../assets/A/B/C/D/A__B__C__D`.
- Replace all non-alphanumeric characters with underscores in filenames.

#### Examples
- PDF filename for `[[Course-101/homework/03/04 linear equations]]`:
  ```markdown
  Course-101__homework__03__04_linear_equations.pdf
  ```
- Asset path for the same:
  ```markdown
  ../assets/Course-101/homework/03/04/Course-101__homework__03__04_linear_equations.pdf
  ```
- Link for `[[Projects/Research/Notes]]`:
  ```markdown
  [Notes](../assets/Projects/Research/Projects__Research__Notes)
  ```
- As a PDF link:
  ```markdown
  ![Notes](../assets/Projects/Research/Projects__Research__Notes.pdf)
  ```
- As a folder link:
  ```markdown
  [assets in Projects/Research](../assets/Projects/Research)
  ```
- PNG asset link for `[[Course-101/homework/03/04 linear equations]]`:
  ```markdown
  ![04_linear_equations.png](../assets/Course-101/homework/03/04/Course-101__homework__03__04_linear_equations.png)
  ```

### Handling File Links

#### 1. File Links with `file:///` Scheme
When a user provides an absolute file path (e.g., `/Users/username/path/to/file.json`), generate a Markdown link with the `file:///` protocol for direct access.
- Input: `/Users/username/documents/projects/example-docs/example-docs_1234567890.json`
  ```markdown
  [example-docs_1234567890.json](file:/Users/username/documents/projects/example-docs/example-docs_1234567890.json)
  ```

#### 2. Logseq Asset Links for Files
If a file is part of a Logseq project and a relative link is requested:
- Identify the file's location relative to the Logseq folder structure (typically `logseq/assets/` or `logseq/pages/`).
- Format relative to a typical page location (`logseq/pages/somepage.md`).
- Use Markdown syntax `[name](relative/path/to/file)`.
- Input: `/Users/Myer/dev/clones/logseq/assets/Folder/File.ext`
  ```markdown
  [File.ext](../assets/Folder/File.ext)
  ```

#### 3. Consistent Formatting for Namespaced Assets
- Replace `/` in the namespace with `__` (double underscores).
- Sanitize filenames by replacing non-alphanumeric characters with `_`.
- Generate paths corresponding to the Logseq folder structure.
- Input namespace `[[Folder/Subfolder/File]]` → filename `Folder__Subfolder__File.ext`, path `../assets/Folder/Subfolder/Folder__Subfolder__File.ext`:
  ```markdown
  [File](../assets/Folder/Subfolder/Folder__Subfolder__File.ext)
  ```

### Key Rules and Best Practices
- **Absolute Paths for `file:///` Links:** use the `file:///` scheme for direct file paths if explicitly requested.
- **Relative Paths for Logseq Assets:** always calculate relative paths for files in `assets/`.
- **Namespace Conversion:** convert `/` to `__` in asset filenames.
- **Filename Sanitization:** replace non-alphanumeric characters with `_`.
- **Markdown Link Syntax:** `[name](relative/path)` for Logseq links; `[name](file:/absolute/path)` for direct file links.
