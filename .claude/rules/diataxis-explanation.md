# Diataxis Explanation / Concept (Logseq)

This rule points agents at the **knowledge graph** for understanding-oriented (“explanation” / “concept”) pages. Full template and naming policy live in Logseq, not in a long duplicated checklist here.

<rule>
name: diataxis_explanation_format
description: Diataxis-style explanation pages in Logseq — load Logseq/Entity/concept and Diataxis hub pages first
filters:
  - type: file_path
    pattern: ".*Concept.*\\.md$|.*Explanation.*\\.md$|Programming___Language___Func\\.md$|Programming___Language___Concept___Object-Oriented\\.md$|Logseq___Entity___concept\\.md$"

actions:
  - type: suggest
    message: |
      # Diataxis explanation / concept documentation in this garden

      ## Authority order

      1. Read **`[[Logseq/Entity/concept]]`** in the graph (`pages/Logseq___Entity___concept.md`) for **instance SOP**: frontmatter (`logseq-entity::`, optional `see-also::`, `via::`), when to use concept vs term entities, and recommended body sections.
      2. Read **`[[Diataxis/Explanation]]`** (aliases **`[[Diataxis/Concept]]`**) for Diataxis vocabulary in this graph.
      3. Read **`[[Logseq/Entity]]`** for shared entity conventions (`see-also::` vs `## Related`, `via::`, etc.).

      ## Shape (summary)

      - **Understanding-oriented**: why and how ideas fit together—not primarily a how-to, tutorial, or reference table.
      - **Logseq Flavored Markdown**: bullets, headings as bullets, tab nesting, no blank lines between bullets.
      - **Tags**: include **`[[Diataxis/Concept]]`** (or **`[[Diataxis/Explanation]]`**, same cluster via alias) when adding tags to new concept-shaped pages; **never remove** existing `tags::` without explicit author instruction.
      - **Related graph pages**: use **`see-also::`** in frontmatter (strongest tie first); avoid a **`## Related`** section that only lists internal links unless the author asks.

      ## Rulesync note

      Edit **`.rulesync/rules/diataxis-explanation.md`** (this file) to change agent guidance; run **`rulesync generate`**. Do not hand-edit generated outputs under `.codex/`, `.cursor/rules`, etc.

examples:
  - input: |
      Creating or expanding a concept page in pages/*.md
    output: "Load Logseq/Entity/concept and Diataxis/Explanation before applying structure; use see-also:: and LFM per type page"

metadata:
  priority: high
  version: 2.0
  related_rules: ["logseq-flavored-markdown"]
</rule>

## Maintainer note

Long-form Diataxis templates previously embedded in this rule now live on **`[[Logseq/Entity/concept]]`** so the ontology and agent instructions stay aligned.
