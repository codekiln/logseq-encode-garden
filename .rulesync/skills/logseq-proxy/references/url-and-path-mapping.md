# logseq:// URLs and path mapping

## What the URL means (v1)

**Pattern:**

`logseq://graph/<graph_name>?page=<PageName>`

- **`graph_name`**: Must appear in `.rulesync/config/logseq-proxy.md` as `graph_name`; used to resolve `root` (see `references/graph-registry.md`).
- **`page`**: Logseq **logical page name** with `/` for namespaces (e.g. `rulesync`, `rulesync/Overview`).

**Out of scope for v1:** other query parameters (block id, anchor, day, etc.). If present, ignore them or warn the user; only `page=` is required.

## Protocol note

Logseq may register **`logseq://`** with the OS for app handoff. **Agents do not use that handler.** Parse the string locally and resolve via the registry.

## Page name → file under `pages/`

Same rule as command **`logseq-get-page-file`**: `/` in the page title becomes **`___`** in the filename.

Examples:

| `page=` value | Under `pages/` |
|---------------|----------------|
| `rulesync` | `rulesync.md` |
| `rulesync/Overview` | `rulesync___Overview.md` |
| `Proj/DistLogseq` | `Proj___DistLogseq.md` |

**Source path:**

`<root>/pages/<mapped_filename>.md`

## Journals

**Not supported in v1.** `page=` targets **`pages/`** only. Journal day pages live under `journals/` with different naming (`YYYY_MM_DD.md`). If the user needs a journal mirrored, treat it as a separate workflow.

## Edge cases

- **Missing file**: If `<root>/pages/...` does not exist, fuzzy-search `pages/*.md` for close matches (optional) and report failure with suggestions.
- **Percent-encoding**: If the URL contains `%2F` inside `page=`, decode before mapping.
- **Whitespace**: Trim `graph_name` and `page` values after parsing.

## Destination path

A proxy lives at the **exact same logical page name** as the source, in the destination garden's own `pages/` directory — same namespace, same `___` encoding, no added prefix. Proxying page `Apple` from graph `Agriculture` produces `[[Apple]]` in the destination garden, not a page under some `Logseq/Proxy/...` namespace. A proxy is identified only by its skill-managed properties (`logseq-url::`, `logseq-proxy-last-sync-date::` — see SKILL.md), never by where it lives.

Filesystem:

`pages/<PageName_with___>.md`

Example: `page=Logseq/Entity/Podcast` → `pages/Logseq___Entity___Podcast.md`.

## Name collisions

Before writing, check whether the destination file already exists:

- **Exists with `logseq-url::` set** — a previous proxy of this same page (or a page that reused the property manually). Proceed with the normal re-sync merge (proxy-workflow.md, Case B).
- **Exists without `logseq-url::`** — a real, unrelated page that happens to share the name. **Stop and ask the user** how to proceed before writing anything; do not silently overwrite or merge.
- **Does not exist** — create it (proxy-workflow.md, Case A).
