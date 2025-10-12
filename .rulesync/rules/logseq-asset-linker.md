---
root: false
targets:
  - '*'
description: ''
globs: []
---
# Constructing a Logseq Asset Link
This project rule is an extension to [logseq-flavored-markdown](mdc:.cursor/rules/logseq-flavored-markdown.mdc) which describes how to construct links to assets in the [assets](mdc:assets) directory and its subdirectories.

### **Description**  
This rule can help the user convert macOS file paths into relative Markdown links for Logseq, a knowledge management and note-taking application.  

Logseq uses a concept called **namespaces**. Namespaces are characters that allow for the addition of hierarchy in a file system.  

In Logseq, page titles that use namespaces (e.g., `[[Work/Projects/Logseq]]`) are converted to filenames by replacing the slashes (`/`) with double underscores (`__`), resulting in `Work__Projects__Logseq.md`.  

This translation allows Logseq to represent hierarchical namespaces logically within the app while storing all files in a single directory.  

Therefore, any namespace structure like `[[Parent/Child/Grandchild]]` becomes a single file named `Parent__Child__Grandchild.md`.  

---

### **Use Case 1: Path Name to Markdown Asset Link**  
When provided with a full file path to an asset, this GPT should:  
- Identify the Logseq folder within the path.  
- Format a relative link starting from a typical page location (`logseq/pages/`), assuming the page is located in `logseq/pages/somepage.md`.  
- Generate Markdown code that can be directly copied into Logseq, maintaining correct relative paths for seamless linking.  

The response should always be formatted as a code snippet for easy copying.  

#### **Example Interaction:**  
- **USER:** Can you give me the link for `/a/b/c/logseq/assets/Course-101/assignments/week3/notes/course101__assignment__03__notes.pdf`?  
- **GPT:**  
  ```markdown
  ![course101__assignment__03__notes.pdf](mdc:../assets/Course-101/assignments/week3/notes/course101__assignment__03__notes.pdf)
  ```  

---

### **Use Case 2: Logseq Namespace Name to Asset Path**  
This GPT should also be able to:  
- Turn a Logseq page reference from a namespaced name into a filename and an asset path.  
- For example, given a Logseq page like `[[A/B/C/D]]`, generate:  
  - A filename `A__B__C__D` of the appropriate type (e.g., png, pdf, etc.).  
  - The expected location of the asset as `../assets/A/B/C/D/A__B__C__D`.  
  - Replace all non-alphanumeric characters with underscores in filenames to ensure compatibility.  

#### **Example Interactions:**  
**Example 1:**  
- **USER:** Can you give me a PDF filename for `[[Course-101/homework/03/04 linear equations]]`?  
- **GPT:**  
  ```markdown
  Course-101__homework__03__04_linear_equations.pdf
  ```  

**Example 2:**  
- **USER:** Can you give me the asset path for `[[Course-101/homework/03/04 linear equations]]`?  
- **GPT:**  
  ```markdown
  ../assets/Course-101/homework/03/04/Course-101__homework__03__04_linear_equations.pdf
  ```  

**Example 3 (Longer Interaction):**  
- **USER:** Can you give me the link for `[[Projects/Research/Notes]]`?  
- **GPT:**  
  ```markdown
  [Notes](mdc:../assets/Projects/Research/Projects__Research__Notes)
  ```  
- **USER:** Can you make it a PDF link?  
- **GPT:**  
  ```markdown
  ![Notes](mdc:../assets/Projects/Research/Projects__Research__Notes.pdf)
  ```  
- **USER:** Can you link to the folder?  
- **GPT:**  
  ```markdown
  [assets in Projects/Research](mdc:../assets/Projects/Research)
  ```  

**Example 4:**  
- **USER:** Can you give me a PNG asset link for `[[Course-101/homework/03/04 linear equations]]`?  
- **GPT:**  
  ```markdown
  ![04_linear_equations.png](mdc:../assets/Course-101/homework/03/04/Course-101__homework__03__04_linear_equations.png)
  ```  

---

### **Updated Instructions for Handling File Links in Logseq**  
#### **1. File Links with `file:///` Scheme**  
When a user provides an absolute file path (e.g., `/Users/username/path/to/file.json`), generate a Markdown link formatted with the `file:///` protocol for direct access to the file.  

- **Example Input:**  
  `/Users/username/documents/projects/example-docs/example-docs_1234567890.json`  
- **Expected Output:**  
  ```markdown
  [example-docs_1234567890.json](mdc:file:/Users/username/documents/projects/example-docs/example-docs_1234567890.json)
  ```  

#### **2. Logseq Asset Links for Files**  
If the user specifies that a file is part of a Logseq project and requests a relative Logseq link, the output should:  
- Identify the file's location relative to the Logseq folder structure.  
- Assume the file is stored in a common root Logseq directory, typically either `logseq/assets/` or `logseq/pages/`.  
- Format the link relative to a typical Logseq page location (`logseq/pages/somepage.md`).  
- Use Markdown syntax for linking (e.g., `[name](mdc:relative/path/to/file)`).  

- **Example Input:**  
  `/Users/Myer/dev/clones/logseq/assets/Folder/File.ext`  
- **Expected Output:**  
  ```markdown
  [File.ext](mdc:../assets/Folder/File.ext)
  ```  

#### **3. Consistent Formatting for Logseq Namespaced Assets**  
For files that need to follow Logseq's **namespace conventions**, ensure you:  
- Replace `/` in the namespace with `__` (double underscores).  
- Ensure filenames are sanitized by replacing non-alphanumeric characters with underscores (`_`) for compatibility.  
- Generate paths that correspond to the Logseq folder structure.  

- **Example Input:**  
  Namespace: `[[Folder/Subfolder/File]]`  
- **Filename:**  
  `Folder__Subfolder__File.ext`  
- **Path:**  
  `../assets/Folder/Subfolder/Folder__Subfolder__File.ext`  

- **Example Output:**  
  ```markdown
  [File](mdc:../assets/Folder/Subfolder/Folder__Subfolder__File.ext)
  ```  

---

### **Key Rules and Best Practices**  
- **Absolute Paths for `file:///` Links:** Use the `file:///` scheme for direct file paths if explicitly requested.  
- **Relative Paths for Logseq Assets:** Always calculate relative paths for files in Logseq's `assets/` directory.  
- **Namespace Conversion:** For Logseq namespaces, convert slashes (`/`) to double underscores (`__`) in filenames.  
- **Filename Sanitization:** Replace non-alphanumeric characters with underscores (`_`) for compatibility.  
- **Markdown Link Syntax:** Always use Markdown formatting for links:  
  - `[name](mdc:relative/path)` for Logseq links.  
  - `[name](mdc:file:/absolute/path)` for direct file links.
