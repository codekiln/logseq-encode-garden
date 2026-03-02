tags:: [[DevContainer]], [[Diataxis/Explanation]]

- # initializeCommand
	- ## Overview
		- `initializeCommand` is the earliest standard DevContainer lifecycle hook.
		- It runs on the host machine before the container is created or built.
	- ## When It Is Called
		- During creation or rebuild flows, before Docker has finished building or starting the dev container.
		- Because it runs before the container exists, it cannot rely on tools that only live inside the container image.
	- ## Why You Would Use It
		- Use it when the environment needs host-side preparation before container creation can proceed.
		- Typical cases include:
			- Checking whether required local tools or files exist
			- Generating files that the Docker build or `devcontainer.json` depends on
			- Preparing host-side credentials or configuration inputs
			- Mutating `.devcontainer` inputs before the build starts
	- ## Mental Model
		- Treat `initializeCommand` as the "prepare the inputs" hook.
		- If the work must happen before the container build and startup sequence, this is the right place.
	- ## Misconceptions
		- **It runs inside the container** -> **False**. It runs on the host.
		- **It is a good place for package installation in the dev container** -> **False**. Container package installation belongs in the image build or a container-side hook.
	- ## Related
		- [[DevContainer/Hook]]

