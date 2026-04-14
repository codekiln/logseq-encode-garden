---
paths:
  - '{journals,pages}/*.md'
---
# Person entities (router)

- **Authoritative SOP:** `[[Logseq/Entity/person]]` — how we recognize person **hub** pages (`[[Person/Full Name]]` only), namespace vs entity type, `logseq-entity::`, aliases, dedup, and SCM child pages.
- **Workflow:** Use the **logseq-entity** skill: read `[[Logseq/Entity]]` and the person type page, dedupe before creating, then create or update pages per that SOP (fallback: `.rulesync/config/logseq-entity.md` section **person**).
- **This rule file** stays short; do not reintroduce legacy `[[People/...]]` title or alias patterns here or in new pages.
- **Search before create:** `rg` / glob on `pages/Person___*.md`, name variants, and `alias::` lines; one hub per human; canonical link text must match the real page title.
- **Tags:** Never modify, add, or remove **`tags::`** on existing pages unless a separate human instruction explicitly overrides garden tagging rules.
- **Journal:** When filing a new person hub from a session, follow `logseq-journal-updates` (link under `[[Filed]]`, etc.).
