---
paths:
  - journals/*.md
  - pages/*.md
---
# Logseq SCM Project Link Style

Use this rule to enforce canonical SCM project link namespaces.

## Required Style

For repository/project page links, use:

- `[[Person/<Name>/GitHub/<ProjectName>]]`
- `[[Person/<Name>/GitLab/<ProjectName>]]`

Examples:

- `[[Person/Simon Willison/GitHub/showboat]]`
- `[[Person/Simon Willison/GitHub/rodney]]`
- `[[Person/Jane Doe/GitLab/internal-platform]]`

## Disallowed Styles

Do not introduce or keep generic SCM path styles such as:

- `[[GitHub/<owner>/<project>]]`
- `[[GitLab/<owner>/<project>]]`
- `[[GitHub/<project>]]`
- `[[GitLab/<project>]]`

## Enforcement Guidance

1. When adding or editing GitHub/GitLab project references, rewrite them to the canonical person-first namespace.
2. If the person page exists, use that exact canonical person name in links.
3. If the person page does not exist and the task requires creating references, create/update the person page first using existing person-page conventions.
4. For legacy content updates, normalize existing non-canonical SCM links to this style.

## Related

- command: `logseq-normalize-scm-project-links` - Normalize GitHub/GitLab project links in a file or across changed files
- rule: `logseq-person` - Person page deduplication and canonical person naming
- rule: `logseq-page-naming-reference` - Namespace/file naming rules
