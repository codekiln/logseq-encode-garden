tags:: [[DevContainer]], [[Diataxis/Explanation]]

- # postCreateCommand
	- ## Overview
		- `postCreateCommand` runs inside the container after the environment has been created and the workspace is mounted.
		- In practice, this is the hook many teams use for their main project setup step.
	- ## When It Is Called
		- After first creation, once the workspace is ready inside the container.
		- It does not rerun on ordinary container restarts.
	- ## Why You Would Use It
		- Use it for project-level setup that depends on the actual checked-out workspace being present.
		- Typical cases include:
			- Running `npm install`, `pnpm install`, `pip install`, or similar dependency installation
			- Finalizing project configuration
			- Running setup scripts that need the workspace mount
			- Preparing local development tooling after the container exists
	- ## Practical Distinction
		- `postCreateCommand` is usually the best fit when the setup depends on repository files being mounted and available.
		- That is why it is often preferred over `[[DevContainer/Hook/onCreateCommand]]` for the main dependency-install step.
	- ## Misconceptions
		- **It runs every time the container starts** -> **False**. It is a creation-time hook, not a restart hook.
		- **It should replace image builds for everything** -> **False**. Stable base tooling often belongs in the image, not in a post-create step.
	- ## Related
		- [[DevContainer/Hook]]

