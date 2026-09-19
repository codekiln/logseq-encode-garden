---
name: logseq-proxy
description: >-
  Proxy a page from another Logseq garden in the corresponding page location of
  the active garden, driven by logseq://graph/<name>?page=<Page> URLs and a
  local graph registry. Sets skill-managed page properties (logseq-url::,
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

Cross-garden **page proxy**: copy `pages/*.md` from a **registered** on-disk graph into the **same-named** page in this garden, record provenance in **skill-managed** properties, and answer **listing** questions via search.

A proxy mirrors the source page's exact name and namespace: a source page
`[[My/Page/Here]]` becomes `[[My/Page/Here]]` in the destination garden too —
same `___`-encoded filename, no added prefix or namespace. This is what lets
a whole namespace proxy cleanly: every page keeps its identity across
gardens. The proxy is identified **only** by its skill-managed properties;
its location never identifies it as a proxy.

## Invariants

- **Never add, remove, or edit** a `tags::` line on an **existing** destination page (re-sync). On first create, preserve the source file’s `tags::` as copied unless the user forbids it.
- **Skill-owned properties** (set or update on every successful sync): `logseq-url::`, `logseq-proxy-last-sync-date::`. Do not rename their keys.
- The **`logseq://` URL** is a **portable intent string** for agents; do not assume the OS or Logseq app will resolve it. Resolution uses **`.rulesync/config/logseq-proxy.md`** only, via `ghq-address` (preferred) or an explicit `root` (v1).
- **Name collision**: if the destination page already exists but has no `logseq-url::`, it is a real, unrelated page — stop and ask before touching it. Never silently overwrite a non-proxy page.

## Procedure

1. Open and follow **[references/proxy-workflow.md](./references/proxy-workflow.md)** end-to-end for sync.
2. For **registry format** and GitHub futures, see **[references/graph-registry.md](./references/graph-registry.md)**.
3. For **URL parsing** and `page=` → filename, see **[references/url-and-path-mapping.md](./references/url-and-path-mapping.md)**.
4. For **list / list-graphs** and ripgrep recipes, see **[references/listing-and-queries.md](./references/listing-and-queries.md)**.

## Progressive disclosure

- **This file** — scope, invariants, and pointers.
- **`references/proxy-workflow.md`** — numbered sync and merge steps, reporting.
- **Other `references/*.md`** — depth on demand.

## Entrypoints

- Slash command: **`/logseq-proxy`** → `.rulesync/commands/logseq-proxy.md` (thin wrapper around this skill).
