---
targets:
  - '*'
description: Normalize GitHub and GitLab project links to Person/<Name>/<SCM>/<ProjectName> style
argument-hint: "Optional file path or glob (default: changed files in pages/ and journals/)"
---
# Normalize SCM Project Links

Normalize GitHub/GitLab project links to the canonical style:

- `[[Person/<Name>/GitHub/<ProjectName>]]`
- `[[Person/<Name>/GitLab/<ProjectName>]]`

Examples: `[[Person/Simon Willison/GitHub/showboat]]`, `[[Person/Jane Doe/GitLab/internal-platform]]`.

## Disallowed styles (rewrite these)

- `[[GitHub/<owner>/<project>]]`
- `[[GitLab/<owner>/<project>]]`
- `[[GitHub/<project>]]`
- `[[GitLab/<project>]]`
- Any other non-canonical GitHub/GitLab namespace link.

## Workflow

1. Identify candidate links in target files:
   - `[[GitHub/<owner>/<project>]]`
   - `[[GitLab/<owner>/<project>]]`
   - Any other non-canonical GitHub/GitLab namespace links
2. Resolve the canonical person page name for `<owner>` or known person identity:
   - Search existing person pages first (deduplication and canonical naming).
   - If needed for the task, create/update person page according to existing person-page rules.
3. Rewrite links to canonical format:
   - `[[Person/<Canonical Name>/GitHub/<project>]]`
   - `[[Person/<Canonical Name>/GitLab/<project>]]`
4. Preserve all surrounding content and meaning; only change link namespace format.
5. Report files changed and unresolved links (if any).

## Notes

- Prefer existing canonical person page names over guessed names.
- If owner-person mapping is ambiguous, pause and ask for confirmation.

## Related

- command: `logseq-person` (router) and skill `logseq-entity` — see `[[Logseq/Entity/Person]]` for person hub naming and deduplication. If a person page does not exist and the task requires references, create/update the person **hub** first per that entity definition.
- naming/path rules: `logseq-core` rule and `logseq-lfm` skill (file-name ↔ link translation).
