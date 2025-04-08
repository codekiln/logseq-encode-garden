# Are people using [[mise]] only in development, or are they using it in a deployment context as well?
	- ## Problem Context
		- it's easy for [[mise/Config/mise.toml]] to contain items that are related to python path configuration, and these items may get lost outside of the development context
	- ## Considerations
		- [[mise/Tasks]] are a bit like [[Makefile]]s and, like makefiles, may contain imperative setup commands that are meant to be used outside of the development context