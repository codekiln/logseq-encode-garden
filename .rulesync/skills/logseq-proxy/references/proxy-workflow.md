# Proxy workflow (sync)

Read **[[Logseq/Entity/Proxy/Page]]** first — the frontmatter keys, the `tags::` invariant, the name-collision rule, and the page-name mapping are defined there, not here. This file is the sequence.

## Property block heuristic

For merge logic, treat a **leading property block** as consecutive lines from the start of the file that match:

`^\s*[^:\n]+::\s*.*$`

Stop at the first line that does **not** match (e.g. blank line, `- # Heading`, or plain text). This matches common Logseq export patterns; adjust if a file uses only block bullets with inline properties.

## Steps

### 0. Preconditions

- Confirm cwd is the **destination** Logseq graph root (`pages/`, `logseq/` present).
- Read `.rulesync/config/logseq-proxy.md` and locate `graph_name` → `ghq-address` and/or `root`.
- Resolve `root` per `graph-registry.md` (run `ghq list --full-path --exact <ghq-address>` when `ghq-address` is set; stop and ask before cloning if it isn't cloned locally).

### 1. Parse URL

From user input or command argument, extract:

- `graph_name` from `logseq://graph/<graph_name>`
- `page` from query `page=<value>`

Reject if `page` is missing. Trim both values. Decode percent-encoding (`%2F` inside `page=` is a namespace `/`). Other query parameters — block id, anchor, day — are out of scope: ignore them or warn. Journals are out of scope too; `page=` targets `pages/` only.

### 2. Resolve source file

Map `page` → `pages/<page_with___>.md` under the resolved `root`, and read it. If it is missing, stop with a clear error and optional fuzzy filename suggestions from `<root>/pages/*.md`.

### 3. Compute destination path and check for a collision

The destination mirrors the source name exactly: `pages/<page_with___>.md` in this garden.

- Destination doesn't exist → **create** (Case A, step 5).
- Destination exists **with** `logseq-url::` in its property block → **re-sync** (Case B, step 5).
- Destination exists **without** `logseq-url::` → **stop and ask** before writing anything.

### 4. Build the proxy properties

- `logseq-url::` — the URL as provided, normalized to consistent `?page=` encoding.
- `logseq-proxy-last-sync-date::` — today as `[[yyyy-MM-dd]]`, no weekday.

### 5. Merge or create

**Case A — destination does not exist**

- Start from **full source** text.
- Add or replace the two proxy property lines in the property block.
- Write to the destination path.

**Case B — destination exists (confirmed proxy per step 3)**

- Parse **destination** into `dest_props` + `dest_body`, and **source** into `source_props` + `source_body`, using the heuristic above.
- **Body** for the new file = **`source_body`**.
- **Properties** for the new file: start from `dest_props` minus the two proxy keys, then append them with the new values. Every other destination property — including every `tags::` line — carries over untouched, and no `tags::` comes from the source.
- **Edge case:** if the destination has no property block but has `tags::` only inside bullets, keep the whole destination structure and prepend a small property block with the two proxy lines, matching the style of other pages in `pages/`.

### 6. Assets

Copy any asset the source page references via a relative `../assets/...` link (images, PDFs, etc.):

- For each `../assets/<relpath>` found in the source, copy `<root>/assets/<relpath>` to `<destination-graph-root>/assets/<relpath>`, creating parent directories as needed.
- Overwrite the destination asset if it already exists — a re-sync refreshes assets the same way it refreshes the body.
- If the source reference is missing on disk under `<root>/assets/`, warn in the report rather than failing the whole sync.

### 7. Report

Summarize:

- Source: resolved `root` (note whether via `ghq-address` or explicit `root`) + relative path
- Destination: relative path under destination repo
- The `logseq-url::` and `logseq-proxy-last-sync-date::` written
- Whether this was create vs re-sync
- Assets copied, or none found
