tags:: [[DevContainer]], [[Diataxis/Explanation]]

- # postStartCommand
	- ## Overview
		- `postStartCommand` runs inside the container every time the container starts.
		- It is the runtime hook for re-establishing state that should exist whenever the container becomes live.
	- ## When It Is Called
		- On the initial container start after creation.
		- On every later restart of that container.
	- ## Why You Would Use It
		- Use it for repeatable runtime tasks that should happen each time the environment starts.
		- Typical cases include:
			- Starting background services
			- Recreating temporary runtime state
			- Running idempotent initialization checks
			- Preparing the live environment for normal use
	- ## Mental Model
		- Treat `postStartCommand` as the "container is live again" hook.
		- Because it runs repeatedly, commands here should be safe to rerun.
	- ## Misconceptions
		- **It is only for the first creation** -> **False**. It also runs on subsequent restarts.
		- **It is the same as `postAttachCommand`** -> **False**. Startup and client attachment are different events.
	- ## Related
		- [[DevContainer/Hook]]
		- [[DevContainer/Hook/postAttachCommand]]

