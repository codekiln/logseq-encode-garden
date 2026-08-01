logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Claude/Desktop/Connector]]

- # What can the Microsoft 365 connector for [[Claude/Code]] do when viewing [[o365]] Excel sheets?
	- ## [[AI Answer]]
		- **Short answer:** There is **no Excel-specific, cell-addressed tool**. The Microsoft 365 connector treats an Excel workbook as an ordinary file in OneDrive/SharePoint: Claude Code **finds** it via search and **opens and reads** its content (sheet data, tables, text) via `read_resource`. It can analyze what it reads. It **cannot** edit individual cells or formulas in place — writes are whole-file operations, and only when the optional write tools are enabled. Everything is scoped to your own Microsoft 365 permissions.
		- **What it can do with an Excel workbook (read, default):**
			- Locate the file with `sharepoint_search` / `sharepoint_folder_search` (covers SharePoint and OneDrive document libraries) — no manual upload needed.
			- Open and read the workbook contents via `read_resource`, then summarize, extract, compare, or reason over the data.
			- Claude can open any document it finds unless the file is encrypted/rights-protected.
			- The connector retrieves data **on-demand** during the query and does not cache file content.
		- **What it does *not* do:**
			- No dedicated spreadsheet API — no per-cell addressing (`A1`), no reading/writing individual formulas, no live worksheet-range operations. It reads the document as content, not through an Excel object model.
			- No in-place cell edits. To change a workbook, the write path is **whole-file**: `sharepoint_update_file` (replace) or `sharepoint_upload_file` (new file), plus item ops like `sharepoint_rename_item`, `sharepoint_move_item`, `sharepoint_copy_item`, `sharepoint_delete_item`, `sharepoint_create_folder`.
			- Write tools are **off by default** — the connector is read-only until you explicitly enable them.
		- **Permissions and surface:**
			- Backed by Microsoft Graph scopes such as `Files.Read.All` and `Sites.Read.All` (read), and `Files.ReadWrite.All` (write, when enabled).
			- Claude mirrors your existing Microsoft 365 permissions — nothing is reachable through Claude that you can't already see directly.
			- Available across Claude surfaces including **Claude Code**, web, desktop, mobile, and the API; rated **Read** by default.
		- Sources: [Microsoft 365 Connector — Claude](https://claude.com/connectors/microsoft-365), [Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector), [Microsoft 365 connector security guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)
