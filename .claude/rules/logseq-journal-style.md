---
paths:
  - journals/*.md
---
# Journal style (garden-first)

## Configuration order

1. If this garden defines the journal registry, read **`[[Logseq/Journal]]`** (`pages/Logseq___Journal.md`) and any linked pages under the **`Logseq/Journal/...`** namespace (for example **`[[Logseq/Journal/Section/Friction]]`**, **`[[Logseq/Journal/Section/Garddiff]]`**, **`[[Logseq/Journal/Editorial headings]]`**). Treat that material as **authoritative for section vocabulary, narrative patterns, and examples** when it conflicts with generic rules or commands.
2. If those pages are missing or silent on a point, follow **`logseq-journal-updates`**, the **`logseq-format-journal`** command, and **`logseq-flavored-markdown`**.

## Agent workflow

Mirror the entity workflow: load **`[[Logseq/Entity]]`** for entity policy; load **`[[Logseq/Journal]]`** before restructuring or extending a journal file.
