---
# note that this is not currently supported by rulesync; 
# see [Feature request: for claude code slash commands, support passing through claude-code-specific yaml markdown frontmatter keys to the generated command markdown files · Issue #413 · dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync/issues/413)
argument-hint: [logseq-namespaced-page-name]
description: Given namespaced Logseq page name, return the filename
targets: ["*"]
---

# Get Page File

Follow the `Workflow` to implement the `LOGSEQ_NAMESPACED_PAGE_NAME` then `Report` the completed work.

## Variables

LOGSEQ_NAMESPACED_PAGE_NAME: $ARGUMENTS

## Workflow

- If no `LOGSEQ_NAMESPACED_PAGE_NAME` is provided, STOP immediately and ask the user to provide it.
- Starting from the logseq project root (the directory with `journals/`, `logseq/`, `pages/`)
  - Search `./pages/*.md` for a page, assuming that `/` in `LOGSEQ_NAMESPACED_PAGE_NAME` translates to `___` in the file name

## Report

The report block should be in yaml with an all caps key. One of the below blocks should be the entire report.

### IF page is found
EXISTS: true
FILENAME: pages/the___full___filename.md

### ELSE IF page not found and similar pages exist
EXISTS: false
POSSIBLY_RELATED_FILENAMES: 
  - pages/close___match___page.md
  - pagtes/another___close___match___page.md

### ELSE
EXISTS: false