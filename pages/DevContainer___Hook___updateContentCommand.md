tags:: [[DevContainer]], [[Diataxis/Explanation]]

- # updateContentCommand
	- ## Overview
		- `updateContentCommand` is a container-side hook for cases where workspace content changes during the creation flow.
		- It exists to reconcile environment setup with repository content that may not have been finalized at the earlier build stage.
	- ## When It Is Called
		- During creation workflows where content updates happen after the image build step, such as GitHub Codespaces prebuild-oriented flows.
		- It is not commonly the main hook in typical local VS Code usage.
	- ## Why You Would Use It
		- Use it when your environment setup depends on repository contents that may arrive or change after the image has already been prepared.
		- Typical cases include:
			- Refreshing generated artifacts after content sync
			- Re-running workspace-dependent setup in prebuild scenarios
			- Reconciling dependency state with post-build content changes
	- ## Mental Model
		- Treat `updateContentCommand` as the "content changed during creation" hook.
		- It is mainly about staged creation pipelines rather than ordinary local restarts.
	- ## Misconceptions
		- **It runs during every local create in a visible way** -> **False**. Many local workflows barely surface it.
		- **It is the same as `postCreateCommand`** -> **False**. It addresses a narrower content-change case during creation.
	- ## Related
		- [[DevContainer/Hook]]

