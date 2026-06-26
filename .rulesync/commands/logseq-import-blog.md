---
targets:
  - '*'
description: Import a blog post, article, or essay as an Article entity by applying the logseq-entity skill and the graph's Logseq/Entity/Article entity definition
argument-hint: Source URL (optional); article source and namespace can be prompted if omitted
---
# Import Blog Post, Article, or Essay as an Article Entity

Use this command to import a blog post, article, essay, or similar web-published writing into the Logseq garden. The authoritative workflow is the **logseq-entity** skill plus the graph page **[[Logseq/Entity/Article]]**.

This command is only a routing guide. Do not maintain a separate Blog/Article/Essay import workflow here; update **[[Logseq/Entity/Article]]** when the garden's Article entity definition changes.

## Required Inputs

- `{url}` - Optional source URL. If omitted, ask for the article URL or pasted source material.
- Article title, byline/creator, publication date, source URL, and page namespace are inferred from the source when possible.

## Workflow

1. Load the **logseq-entity** skill and its required references:
   - `.rulesync/skills/logseq-entity/SKILL.md`
   - `.rulesync/skills/logseq-entity/references/configuration-contract.md`
   - `.rulesync/skills/logseq-entity/references/logseq-entity-type-pages.md`
2. Load the graph configuration in skill order:
   - **[[Logseq/Entity]]**
   - **[[Logseq/Entity/Article]]**
   - **[[Logseq/Frontmatter]]**
3. Fetch or inspect the source enough to identify:
   - title
   - author, company, or organization that wrote the piece
   - publication date
   - source URL
   - publication/site when useful
4. Deduplicate using **[[Logseq/Entity/Article]]**:
   - exact source URL
   - exact title
   - normalized title words under likely author, publication, Blog, Article, and Essay namespaces
   - byline plus distinctive title phrase
5. Choose the page namespace according to **[[Logseq/Entity/Article]]** and nearby garden precedent.
   - Existing author or publication namespaces are preferred.
   - `Blog`, `Article`, and `Essay` path segments are organizational; the entity type is still marked with `logseq-entity:: [[Logseq/Entity/Article]]`.
6. Create or update the page using Logseq Flavored Markdown:
   - set `logseq-entity:: [[Logseq/Entity/Article]]`
   - set `created-by::` to the person, company, or organization that wrote the piece when known
   - set `date-created::` to the publication date when known
   - set `source-link::` to the original source URL
   - optionally set `readwise-link:: <URL>` when a Readwise Reader URL is available
   - first body block is `- # [Article Title](source URL)`
7. Link from the creator page when the creator page already exists or was created as part of the entity workflow.
8. Complete the logseq-entity journal requirement:
   - new graph pages under **[[Filed]]**
   - existing graph pages materially edited under **[[Updated]]**
   - no duplicate page link across Filed and Updated for the same day

## Report

After completing the import, report:

- page link and filename
- creator linked through `created-by::`
- whether a creator page was updated
- journal links added under **[[Filed]]** and **[[Updated]]**
