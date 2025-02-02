# DOING [Testing in Visual Studio Code](https://code.visualstudio.com/docs/editor/testing)
id:: 6773ad29-4fe7-4be1-b963-5bb434425cff
:LOGBOOK:
CLOCK: [2024-12-31 Tue 03:53:18]
:END:
- The [Test Explorer](https://code.visualstudio.com/docs/editor/testing#_automatic-test-discovery-in-test-explorer) provides a centralized place to manage and run your tests.
- you can also [run and debug tests](https://code.visualstudio.com/docs/editor/testing#_run-and-debug-tests) and set breakpoints in your test
- You can also [run tests with coverage](https://code.visualstudio.com/docs/editor/testing#_test-coverage) to see how much of your code is covered by your tests.
- you can [create tasks to run your tests](https://code.visualstudio.com/docs/editor/testing#_task-integration), and optionally run your tests in the background with every code change.
- ## [Testing extensions](https://code.visualstudio.com/docs/editor/testing#_testing-extensions)
	- They link to the [[VSCode/Extension/Python]]
		- ## Set up your environment
			- Configure tests by running the `Configure Tests` command
			- ![configure tests](https://raw.githubusercontent.com/microsoft/vscode-python/main/images/ConfigureTests.gif)
- ## [Automatic test discovery in Test Explorer](https://code.visualstudio.com/docs/editor/testing#_automatic-test-discovery-in-test-explorer) [[VSCode/Editor/Test Explorer]]
	- ### How do I access the #VSCode Test Explorer with a #Keyshort, and what is its icon?
		- You can access the Test Explorer view by selecting the **beaker icon** in the Activity Bar or by using the **Testing: Focus on Test Explorer View** command in the Command Palette (⇧⌘P).
		- ![image.png](../assets/image_1735634667166_0.png)
	- ### How can I quickly filter results for a particular test in the #VSCode Test Explorer #Keyshort or #Syntax?
		- use the **Filter** button to filter tests by status or only show tests for the current file.
		- use the **search box** to search for specific tests by name
		- use **@executed** to find executed tests
		- use **!subtraction** to filter out certain tests with the string subtraction in them
		- ![using @ symbol to search by executed](https://code.visualstudio.com/assets/docs/editor/testing/test-explorer-view-filtering.png)
	-
-