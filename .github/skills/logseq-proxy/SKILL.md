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
---
# Logseq proxy

Copy `pages/*.md` from a **registered** on-disk graph into the **same-named** page in this garden, and answer **listing** questions about what is proxied.

**`[[Logseq/Entity/Proxy/Page]]` is the format authority.** It defines what a proxy page is, the `logseq://` URL, destination naming and the `___` filename mapping, the two skill-owned properties, the `tags::` and merge rules, the collision outcomes, asset handling, and the ripgrep recipes for listing. Read it before every sync or listing question and follow it end to end. This skill adds the repo-side mechanics the graph does not cover: the registry, path resolution, and reporting.

## Invariants

- **Never add, remove, or edit** a `tags::` line on an **existing** destination page (re-sync).
- **Skill-owned properties** — set or update `logseq-url::` and `logseq-proxy-last-sync-date::` on every successful sync; keep their key spellings.
- The **`logseq://` URL** is a portable intent string for agents; do not hand it to the OS or the Logseq app. Resolution uses **`.rulesync/config/logseq-proxy.md`** only.
- **Name collision** — a destination page that exists without `logseq-url::` is a real, unrelated page. Stop and ask before touching it.

## Procedure

1. Confirm cwd is the **destination** graph root (`pages/`, `logseq/` present).
2. Load **`[[Logseq/Entity/Proxy/Page]]`** and **`[[Logseq/Entity]]`**.
3. Parse the URL for `graph_name` and `page=` (URL-decode; reject if `page=` is missing).
4. Resolve `graph_name` to an on-disk `root` per **[references/graph-registry.md](./references/graph-registry.md)**.
5. Read the source file at `<root>/pages/<mapped filename>.md`. If it is missing, stop and report, with fuzzy filename suggestions when you have them.
6. Compute the destination path, check for a collision, and merge or create — all per the type page.
7. Copy referenced assets per the type page. A source asset missing on disk is a warning in the report, not a failed sync.
8. Record the change in `journals/YYYY_MM_DD.md` per **`[[Logseq/Journal]]`** (**`[[Filed]]`** for a new proxy, **`[[Updated]]`** for a re-sync).
9. Report per the section below.

## Report

- Source: resolved `root` (noting whether it came from `ghq-address` or an explicit `root`) plus the relative path.
- Destination: the relative path under this repo.
- The `logseq-url::` and `logseq-proxy-last-sync-date::` values written.
- Create vs re-sync.
- Assets copied, or none found.
