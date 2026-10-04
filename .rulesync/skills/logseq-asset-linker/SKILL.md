---
name: logseq-asset-linker
description: >-
  Construct Logseq asset links: convert a macOS/absolute file path or a Logseq
  namespaced page name into a relative Markdown link (or file:/// link) into the
  graph's assets/ directory. Use when the user gives a file path or
  [[Namespace/Page]] and wants the asset/image/PDF link, an asset filename, or
  an asset folder path. Do not use for ordinary page wikilinks (logseq-core /
  logseq-link-hygiene).
targets: ["*"]
codexcli:
  short-description: Build relative Logseq asset links from paths or page names
---

# Logseq asset linker

Produce copy-pasteable asset links relative to a page in `pages/`.

## Quick rules

- Relative links into `assets/` are formed from a typical page location (`logseq/pages/somepage.md`), so they start `../assets/...`.
- Image link: `![name](../assets/path)`. File link: `[name](../assets/path)`. Folder link: `[name](../assets/folder)`.
- Use `file:/absolute/path` only when the user explicitly wants a direct file link.
- Read `[[Logseq/Entity/Asset]]` for page ownership and filename mapping; for B2 uploads also read `[[Logseq/Entity/Asset/B2]]`. New asset paths derive from the asset page namespace and final format segment. Preserve existing filenames and links; do not apply a competing separator or punctuation-sanitizing convention.
- Always return the result as a code snippet for easy copying.

Read [references/asset-link-construction.md](./references/asset-link-construction.md) for link construction and `file:///` handling. Its older filename examples describe existing files; the graph entity definition governs new names.
