---
targets:
  - '*'
root: false
description: Standard file conventions and directory structure for logseq graphs
globs: []
cursor:
  alwaysApply: false
  description: Standard file conventions and directory structure for logseq graphs
---
## Logseq Directory Structure

- `logseq-graph` - the root of the logseq graph. In some projects, this is the root of the git repo. In others, the logseq root is a folder inside of the git root directory. The name of this is unique to the graph.
- `logseq-graph/pages/*.md` - All the pages in the graph that are not journal pages are stored here. 
  - Logseq will not create markdown files in subfolders of `pages/*/*.md`, but if a markdown file is placed in a subfolder of `pages`, logseq will be able to read and edit it. Logseq has a requirement that each page have a unique file name across the whole graph. If `pages/cars.md` exists, if a `cars.md` file is placed anywhere else in the repository, Logseq will display an error.  
  - logseq supports special hierarchies called "namespaces". A page with the title or "namespace" `[[Project/Tasks]]` is stored as `Project___Tasks.md` in `pages/`. Triple underscores delimit the hierarchical components.
- `logseq-graph/journals/YYYY_MM_DD.md` - Contains daily journal entries
- `logseq-graph/assets/` - Stores images, pdfs and other attachments that are referenced in markdown files via relative links.
- `logseq-graph/logseq/` - Configuration directory for the logseq graph. You typically shouldn't edit this.
- `.gitignore` - Standard Git ignore file (if using Git)
