---
targets:
  - '*'
description: Person entities — router to Logseq/Entity/Person
---
# Person entities (command)

- **Documentation:** `[[Logseq/Entity/Person]]` — person **hub** pages, `logseq-entity::`, no `[[People/...]]`, namespace vs entity type, dedup, SCM children as [[Logseq/Entity/Software/Project]] when the child is a repo hub.
- **Process:** Run the **logseq-entity** skill: load entity registry + person entity definition, search `pages/Person___*.md`, classify existing/similar/new/blocked, then create or edit per the entity definition.
- **Do not** add `[[People/Full Name]]` aliases or titles; optional `alias::` only for real alternates listed on the type page.
