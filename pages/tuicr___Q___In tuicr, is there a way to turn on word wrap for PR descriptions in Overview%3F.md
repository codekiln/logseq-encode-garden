logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tuicr/Q/Is there a way to copy text from the PR description and quote it in a comment?]]
- # In [[tuicr]], is there a way to turn on word wrap for PR descriptions in Overview?
	- ## [[AI Answer]]
		- **Short answer:** `:set wrap` exists, but it only controls the **diff view**. There is no separate command or config option for wrapping behavior in the PR description area.
		- [[Answer/Official]] from [tuicr keybindings](https://github.com/agavra/tuicr/blob/main/docs/KEYBINDINGS.md): `:set wrap` is documented as "Enable line wrap in diff view", and `:set wrap!` toggles it.
		- [[Answer/Official]] from [tuicr config docs](https://github.com/agavra/tuicr/blob/main/docs/CONFIG.md): `wrap = false` by default, and the option scope is also documented as diff view only.
		- In source, `:set wrap` dispatches to `app.set_diff_wrap(true)` ([handler.rs](https://github.com/agavra/tuicr/blob/main/src/handler.rs), [navigation.rs](https://github.com/agavra/tuicr/blob/main/src/app/navigation.rs)), reinforcing that the setting is diff-specific.
		- PR description rendering is handled in a separate path (`build_pr_info_lines` in [pr_info_panel.rs](https://github.com/agavra/tuicr/blob/main/src/ui/pr_info_panel.rs)) and does not expose a user-facing wrap toggle.
		- If the current PR-description behavior is not what you want, the practical next step is a feature request in [agavra/tuicr issues](https://github.com/agavra/tuicr/issues).
