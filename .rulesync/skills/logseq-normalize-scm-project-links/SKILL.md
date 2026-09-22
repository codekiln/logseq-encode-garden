---
name: logseq-normalize-scm-project-links
description: >-
  Rewrite GitHub and GitLab project wikilinks in the garden to the
  `Person/<Name>/GitHub/<Project>` form, resolving each owner to an existing
  person page rather than guessing a name. Use when a page or journal carries
  `[[GitHub/owner/project]]`, `[[GitLab/project]]` or another off-standard SCM
  namespace link, or when the user asks to normalize, clean up or standardize
  repo links. Do not use for link targets that are not repositories — see
  skill `logseq-link-hygiene` for wikilink resolution generally.
targets: ["*"]
codexcli:
  short-description: Rewrite GitHub/GitLab wikilinks to Person/<Name>/<SCM>/<Project>
---

# Normalize SCM project links

The standard form is `[[Person/<Name>/GitHub/<Project>]]` or `[[Person/<Name>/GitLab/<Project>]]`, as in `[[Person/Simon Willison/GitHub/showboat]]`.

Rewrite these:

- `[[GitHub/<owner>/<project>]]`
- `[[GitLab/<owner>/<project>]]`
- `[[GitHub/<project>]]`, `[[GitLab/<project>]]`
- any other GitHub or GitLab namespace link that does not sit under a person

## Workflow

Default scope is the changed files under `pages/` and `journals/`; the user may give a path or glob instead.

1. Find the candidate links in scope.
2. Resolve `<owner>` to a person page. Search `pages/Person___*.md` first — an existing page name always wins over a name derived from the owner handle. When the owner-to-person mapping is ambiguous, stop and ask.
3. When the task needs a person page that does not exist, create the person **hub** first per `[[Logseq/Entity/Person]]` and the `logseq-entity` skill. A repo hub filed as a child of that person is a `[[Logseq/Entity/Software/Project]]`.
4. Rewrite the link namespace and nothing else. Surrounding text, link text and meaning stay as they are.
5. Report the files changed and any link left unresolved.

## Related

- skill: `logseq-entity` — person hubs, dedup, `[[Logseq/Entity/Person]]`
- rule: `logseq-core` — file name and link name translation (detail: skill `logseq-lfm`)
