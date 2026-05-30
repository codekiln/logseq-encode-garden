---
name: logseq-ai-model
description: >-
  Reference or document AI models in the garden using provider namespaces and
  singular naming. Use when mentioning a model in passing/changelogs, creating a
  model stub, or authoring a detailed model page with features, benchmarks,
  tiers, access, and specs. Covers OpenAI/Anthropic/Google/DeepSeek/xAI model
  link formats and model-code aliases. Do not use for general entity creation
  (logseq-entity) or non-model pages.
---
# Logseq AI model pages

Extends naming conventions (singular page names; see `logseq-core`) for AI models.

## Quick reference (mention / changelog / stub)

- Provider namespaces: `[[OpenAI/Model/...]]`, `[[Anthropic/Model/...]]`, `[[Google/AI/Model/...]]`, `[[DeepSeek/Model/...]]`, `[[xAI/Model/...]]`.
- Version hierarchy uses `/`: `[[OpenAI/Model/GPT/4/1]]` (GPT-4.1), `[[Anthropic/Model/Claude/3.5/Sonnet]]` (Claude 3.5 Sonnet).
- Always use the full namespace path, not bare display text ("Gemini 2.5 Pro").
- Stub page: frontmatter `alias:: [[model-name]]`, `tags:: [[AI/Model]]`; body `- # Model Name` + `- *Stub page - detailed documentation pending*`. Add it to the provider's model list page if one exists.
- Document specific model **versions**, not families.

## Detailed model page

When the model is a primary focus (capabilities, benchmarks, comparisons, full specs), author a full page — read [references/detail-page.md](./references/detail-page.md) for the section structure, research sources, examples, and best practices (canonical H1 link, model-code aliases, version status).

## Always

- Never modify existing `tags::` (protected). New model pages use `tags:: [[AI/Model]]`.
- Link existing model pages when available; use `logseq-link-hygiene` before inventing links.
