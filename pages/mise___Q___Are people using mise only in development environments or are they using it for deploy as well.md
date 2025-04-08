# Are people using [[mise]] only in development, or are they using it in a deployment context as well?
	- ## Problem Context
		- It's easy for [[mise/Config/mise.toml]] to contain items that are related to python path configuration, and these items may get lost outside of the development context
		- [[mise/Tasks]] are a bit like [[Makefile]]s and may contain imperative setup commands that are meant to be used outside of the development context. In addition, they may be especially important in tasks that exist in the CICD space between development and deployment.
	- ## Examples
		- When working on [[Project - Conway's Game of Life in GitHub Bio]], I wanted to start using [[uv]], but then I encoded the extra steps to install an editable package and run tests in [[mise/Config/mise.toml]]. But then, when defining the [[GitHub/Action]] that would run these tests, I found myself needing to decide between separately describing how to set up the project with dev dependencies and run the tests or just using mise inside of [[Docker]].
	- ## Discussion
		-