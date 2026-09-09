tags:: [[Claude/Code]], [[Diataxis/How To]]
see-also:: [[Claude/Code/How To/Answer Permission Dialog To Record Wildcard Permissions in Local Settings]], [[Claude/Code/Q/How can I make auto mode the default permission mode?]], [[Claude/Code/Settings]], [[Claude/Code/--/enable-auto-mode]]
alias:: [[Anthropic/App/Claude Code/How To/Approve Actions Denied by the Auto Mode Classifier]]
title:: Claude/Code/How To/Approve Actions Denied by the Auto Mode Classifier

- # How To Approve Actions Denied by the Auto Mode Classifier
	- ## Overview
		- When [[Claude/Code]] runs in **auto mode**, a separate classifier model reviews tool calls and may block ones that escalate beyond the request, target unrecognized infrastructure, or look driven by hostile content. [^1]
		- Each blocked action shows a notification and lands under `/permissions` → **Recently denied**. From that list, approve the action for the rest of this session, then retry the failed tool call so Claude actually runs it again under the new approval. [^1] [^2]
		- Use this when a shell or other tool call was blocked as **Blocked by classifier** and you still want that work to proceed in the current session.
	- ## Prerequisites
		- [[Claude/Code]] in an interactive terminal session with auto mode available
		- Status bar shows `auto mode on` (cycle with `Shift+Tab` if needed) [^1]
		- At least one action already denied by the classifier in this session
	- ## Steps
		- ### 1. Open the permissions dialog
			- Run `/permissions`.
			- Tabs include **Recently denied**, **Allow**, **Ask**, **Deny**, **Auto mode**, and **Workspace**. [^3]
		- ### 2. Open Recently denied
			- Select the **Recently denied** tab.
			- Header text: "Commands recently denied by the auto mode classifier."
			- Each row shows the description Claude wrote for the tool call and the status **Blocked by classifier**. [^2]
			- Example list (anonymized — your labels will differ):
				- 1. Probe the remote build host over SSH
				- 2. Update known_hosts for the new address
				- 3. Verify passwordless sudo on the staging host
				- 4. First SSH to the staging host
		- ### 3. Approve the blocked action for this session
			- Use `↑` / `↓` to highlight a row.
			- Press **Enter** to approve — the action is added to this session's approval list so matching work can proceed without waiting on the classifier again for that approval.
			- Legend at the bottom of the tab: `Enter to approve · r to retry · ↑/↓ to navigate · Esc to cancel`.
		- ### 4. Retry the failed action now that it is allowed
			- With the same row still highlighted (or after approving several rows), press **`r`** to mark that denial for retry. [^1] [^2]
			- Exit the dialog (`Esc` or finish the approvals). Claude Code then tells the model it may retry that tool call and resumes the conversation — so the previously blocked command runs again under the session approval you just granted. [^2]
			- Approving alone does not re-run the failed call; **`r`** is what queues the retry after the allow is in place.
			- Press **Esc** without **`r`** if you only wanted the session allow and will ask Claude to continue in chat instead.
		- ### 5. Confirm on the Allow tab (optional)
			- Switch to the **Allow** tab and confirm the approved entry appears for this session.
			- Session approvals from this flow last for the current session; for a lasting rule, add an allow rule or trusted-infrastructure entry instead (next step).
		- ### 6. If the same destination keeps getting blocked
			- Add the host, domain, or registry to `autoMode.environment`, or run `/auto-mode-setup`, then confirm with `claude auto-mode config`. [^2]
			- Or add a narrow `permissions.allow` rule from the **Auto mode** / allow-rule UI when you want that command class without classifier review going forward. [^2] [^3]
	- ## Troubleshooting
		- **Action never appears under Recently denied** — if a safety check separate from auto mode refused the classifier's own request, or the classifier response did not parse, Claude Code denies without recording the entry; fix via settings or a normal permission prompt instead. [^1] [^2]
		- **Auto mode keeps pausing** — three consecutive classifier blocks, or twenty total in the session, fall back to prompting; approving the prompted action resumes auto mode. [^1]
		- **Need a wildcard that persists across sessions** — use the permission-dialog wildcard flow on [[Claude/Code/How To/Answer Permission Dialog To Record Wildcard Permissions in Local Settings]] rather than a one-session Recently denied approval.
	- ## Footnotes
		- [^1]: [Choose a permission mode — Eliminate prompts with auto mode](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) (blocked actions → `/permissions` → Recently denied; `r` retries with manual approval)
		- [^2]: [Configure auto mode — Review denials](https://code.claude.com/docs/en/auto-mode-config#review-denials)
		- [^3]: [Configure permissions](https://code.claude.com/docs/en/permissions) (`/permissions` dialog; Auto mode tab when auto mode is available)
