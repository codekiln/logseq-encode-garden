tags:: [[DevContainer]], [[Diataxis/Explanation]]

- # postAttachCommand
	- ## Overview
		- `postAttachCommand` runs inside the container whenever a tool session attaches to it.
		- It is the most user-session-oriented hook in the standard lifecycle set.
	- ## When It Is Called
		- After the initial attach to a newly created or started dev container.
		- Again on later reattach events, such as window reloads or reconnects.
	- ## Why You Would Use It
		- Use it for tasks that only make sense when a developer-facing client has attached.
		- Typical cases include:
			- Session-oriented UX initialization
			- Printing banners or usage hints
			- Starting interactive processes tied to the attached session
			- Running commands that are useful on each editor attach
	- ## Practical Distinction
		- `postAttachCommand` is about the developer session becoming active.
		- If the task should happen even without a client attach, `[[DevContainer/Hook/postStartCommand]]` is the better hook.
	- ## Misconceptions
		- **It is just another startup hook** -> **False**. It is tied to attach events, not only container startup.
		- **It only runs once** -> **False**. It can run again on reattach or window reload.
	- ## Related
		- [[DevContainer/Hook]]
		- [[DevContainer/Hook/postStartCommand]]

