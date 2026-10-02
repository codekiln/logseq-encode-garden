---
name: logseq-proxy
description: >-
  Proxy a page from another Logseq garden into the corresponding page location
  of the active garden, driven by logseq://graph/<name>?page=<Page> URLs and a
  local graph registry. Sets the proxy's page properties (logseq-url::,
  logseq-proxy-last-sync-date::). Use when the user proxies or syncs a remote
  graph page, pastes a logseq:// URL, asks what pages are proxied or from which
  graphs, or invokes /logseq-proxy. Do not use for entity filing, flashcards, or
  pages that must not be overwritten—confirm before re-syncing edited proxies.
allowed-tools:
  - Read
  - Write
  - Grep
  - Bash
---
# Logseq proxy

Cross-garden **page proxy**: copy `pages/*.md` from a **registered** on-disk graph into the **same-named** page in this garden, and answer **listing** questions via search.

## Read this first

**[[Logseq/Entity/Proxy/Page]]** (`pages/Logseq___Entity___Proxy___Page.md`) is the place of record for what a proxy page *is*: how one is recognized and named, its `logseq-url::` and `logseq-proxy-last-sync-date::` frontmatter, the `tags::` and name-collision invariants, and the ripgrep recipes that answer *what is proxied* and *from which gardens*. Read it before any sync or listing; this skill does not restate it.

What stays here is the **mechanics** — resolving a graph name to a path on disk, parsing the URL, and the create-versus-merge steps.

## Procedure

1. Open and follow **[references/proxy-workflow.md](./references/proxy-workflow.md)** end-to-end for sync.
2. For **registry format** and GitHub futures, see **[references/graph-registry.md](./references/graph-registry.md)**.

## Progressive disclosure

- **[[Logseq/Entity/Proxy/Page]]** — what a proxy is: naming, frontmatter, invariants, how to find them.
- **This file** — scope and pointers.
- **`references/proxy-workflow.md`** — numbered sync and merge steps, reporting.
- **`references/graph-registry.md`** — the registry at `.rulesync/config/logseq-proxy.md`.
