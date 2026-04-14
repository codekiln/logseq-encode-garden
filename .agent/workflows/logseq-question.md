---
description: >-
  Log a question in the knowledge garden under a logical namespace, record it in
  today's journal, and attempt to research and answer it
trigger: /logseq-question
turbo: true
---
# Workflow: /logseq-question

# Log a Question in the Knowledge Garden

This Rulesync slash command is a **thin entrypoint**. Run skill **logseq-question** by reading and following, in order:

1. `.rulesync/skills/logseq-question/SKILL.md` — scope, relation to **logseq-entity**, and pointer to the full workflow.
2. `.rulesync/skills/logseq-question/references/question-workflow.md` — variables, conventions, Steps 0–5, report, and related rules.

**Question** instances are defined on **`[[Logseq/Entity/question]]`** and share dedup/configuration with skill **logseq-entity**; do not treat this command file as the source of truth for entity semantics.

// turbo
