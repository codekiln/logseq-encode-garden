# Proxy workflow (sync)

## Skill-owned properties

These keys are **owned** by **logseq-proxy**. Set or update them on every successful sync:

- `logseq-url::` — full canonical URL, e.g. `logseq-url:: logseq://graph/logseq-encode-garden?page=rulesync`
- `logseq-proxy-last-sync-date::` — a plain ISO date **Logseq link** for the sync day, e.g. `logseq-proxy-last-sync-date:: [[2026-09-19]]` (`yyyy-MM-dd`, no weekday).

Optional later (not required in v1): `logseq-proxy-source-graph::` — only add if you want redundant filtering without parsing the URL.

**Do not** treat any other `*::` lines as owned by this skill.

## tags:: invariant

- **Re-sync** (destination file already exists): **never** add, remove, or edit `tags::`.
- **First-time** copy: copying the source file wholesale may include its `tags::`; that is acceptable. If the user wants no tags from the source, they should say so explicitly.

## Property block heuristic

For merge logic, treat a **leading property block** as consecutive lines from the start of the file that match:

`^\s*[^:\n]+::\s*.*$`

Stop at the first line that does **not** match (e.g. blank line, `- # Heading`, or plain text). This matches common Logseq export patterns; adjust if a file uses only block bullets with inline properties.

## Steps

### 0. Preconditions

- Confirm cwd is the **destination** Logseq graph root (`pages/`, `logseq/` present).
- Read `.rulesync/config/logseq-proxy.md` and locate `graph_name` → `ghq-address` and/or `root`.
- Resolve `root` per `references/graph-registry.md` (run `ghq list --full-path --exact <ghq-address>` when `ghq-address` is set; stop and ask before cloning if it isn't cloned locally).

### 1. Parse URL

From user input or command argument, extract:

- `graph_name` from `logseq://graph/<graph_name>`
- `page` from query `page=<value>` (URL-decode)

Reject if `page` is missing.

### 2. Resolve source file

Map `page` → `pages/<___>.md` under the resolved `root`. Read the file. If missing, stop with a clear error and optional fuzzy filename suggestions.

### 3. Compute destination path

Mirror the source page name exactly — see `references/url-and-path-mapping.md`:

`pages/<page_with___>.md`

### 4. Check for a name collision

- Destination file doesn't exist → **create** (Case A, step 7).
- Destination file exists **and** has `logseq-url::` in its property block → **re-sync** of the same proxy (Case B, step 7).
- Destination file exists **without** `logseq-url::` → **stop** and ask the user how to proceed before writing anything; do not overwrite or merge.

### 5. Build canonical `logseq-url`

Use the same string the user provided, normalized (consistent `?page=` encoding). Example:

`logseq-url:: logseq://graph/logseq-encode-garden?page=rulesync`

### 6. Sync date

Set `logseq-proxy-last-sync-date::` to today as a plain ISO date wiki link: `[[yyyy-MM-dd]]`, e.g. `[[2026-09-19]]`.

### 7. Merge or create

**Case A — destination does not exist**

- Start from **full source** text.
- Ensure skill-owned properties are present with correct values (add or replace those keys only in the property block).
- Write to the destination path.

**Case B — destination exists (confirmed proxy per step 4)**

- Parse **destination** into `dest_props` (property lines) + `dest_body` (rest of file).
- Parse **source** into `source_props` + `source_body` (same heuristic).
- **Body** for the new file = **`source_body`** (preserve LFM from source).
- **Properties** for the new file:
  - Start from **destination** property lines **excluding** any line whose key is skill-owned (`logseq-url`, `logseq-proxy-last-sync-date`).
  - Append or replace skill-owned lines with the new values.
  - **Never change** `tags::` lines from the destination (keep them exactly as they were, including multiple `tags::` if present).
- Do **not** copy `tags::` from source onto destination on re-sync (that would overwrite behavior—destination tags win).

**Case B — edge case:** If the destination has **no** property block but has `tags::` only inside bullets, keep the whole destination structure and **prepend** a small property block with only the two skill lines before the first line, **or** add the two lines as Logseq properties in the form this garden uses—prefer matching the style of other pages in `pages/`.

### 8. Assets

Copy any asset the source page references via a relative `../assets/...` link (images, PDFs, etc.):

- For each `../assets/<relpath>` found in `source_body` (or `source_props`), copy `<root>/assets/<relpath>` to `<destination-graph-root>/assets/<relpath>`, creating parent directories as needed.
- Overwrite the destination asset if it already exists — a re-sync refreshes assets the same way it refreshes the body.
- If the source reference is missing on disk under `<root>/assets/`, warn in the report rather than failing the whole sync.

### 9. Report

Summarize:

- Source: resolved `root` (note whether via `ghq-address` or explicit `root`) + relative path
- Destination: relative path under destination repo
- Canonical `logseq-url::` and `logseq-proxy-last-sync-date::` written
- Whether this was create vs re-sync
- Assets copied, or none found
