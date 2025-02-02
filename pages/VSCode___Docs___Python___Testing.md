# DONE [Testing Python in Visual Studio Code](https://code.visualstudio.com/docs/python/testing) - #Python #Pytest [[Software/Testing]]
id:: 6777cb12-88af-4ac9-a143-2a0c4ef1f93c
:LOGBOOK:
CLOCK: [2025-01-03 Fri 06:34:13]--[2025-01-15 Wed 03:26:46] =>  284:52:33
:END:
	- ## DONE [Run Tests](https://code.visualstudio.com/docs/python/testing#_run-tests)
	  id:: 67790fe6-e552-4a05-a26f-f6ec149b1dd1
		- ### #VSCode #Keyshort for running tests from [[VSCode/Command/Palette]] `Cmd Shift P`
			- #### What's the VSCode command and Keyshort to run all the discovered tests? #card
			  card-last-score:: 3
			  card-repeats:: 2
			  card-next-schedule:: 2025-01-21T12:00:08.417Z
			  card-last-interval:: 4.14
			  card-ease-factor:: 2.42
			  card-last-reviewed:: 2025-01-17T09:00:08.418Z
				- [[VSCode/Command/Test/Run/All Tests]]
					- Command: **Test: Run All Tests**
					- Keyshort: `⌘; A`
					- #VSCode/Keymap
						- ```json
						  {
						    "key": "cmd+; a",
						    "command": "testing.runAll"
						  }
						  ```
			- #### What's the VSCode Command and Keyshort to run the tests in open editor file? #card
			  card-last-score:: 5
			  card-repeats:: 5
			  card-next-schedule:: 2025-03-30T06:59:13.875Z
			  card-last-interval:: 71.94
			  card-ease-factor:: 2.62
			  card-last-reviewed:: 2025-01-17T08:59:13.876Z
				- **Command**: [[VSCode/Command/Test/Run/Tests in Current File]]
					- Command: **Test: Run Tests in Current File**
					- **Keyshort**: `⌘; f`
					- [[VSCode/Keymap]]
						- ```json
						  {
						    "key": "cmd+; f",
						    "command": "testing.runCurrentFile",
						    "when": "editorTextFocus"
						  }
						  ```
					- #Mnemonic
						- `⌘;` commonly used chord for making things happen in the UI
						- **F** - for **F**ile, as in current **F**ile
			- #### VSCode Command and Keyshort to run the test at the cursorpoint? #card
			  card-last-score:: 3
			  card-repeats:: 3
			  card-next-schedule:: 2025-01-24T22:39:35.470Z
			  card-last-interval:: 10.6
			  card-ease-factor:: 2.56
			  card-last-reviewed:: 2025-01-14T08:39:35.471Z
				- **Command**: [[VSCode/Command/Test/Run/Test at Cursor]]
					- Keyshort: `⌘; C`
					- [[VSCode/Keymap]]
						- ```json
						  {
						    "key": "cmd+; c",
						    "command": "testing.runAtCursor",
						    "when": "editorTextFocus"
						  }
						  ```
					- #Mnemonic - **C** for Test at **C**ursor
		- ### #VSCode #Keyshort for running tests from [[VSCode/View/Test Explorer]]
			- #### How can you run just a few specific tests from the test explorer? #card #Mouse
			  card-last-interval:: 11.2
			  card-repeats:: 3
			  card-ease-factor:: 2.8
			  card-next-schedule:: 2025-01-25T12:40:04.265Z
			  card-last-reviewed:: 2025-01-14T08:40:04.265Z
			  card-last-score:: 5
				- 1. [[VSCode/Command/Testing/Focus on Test Explorer]]
				- 2. `Cmd Click` on more than one
				- 3. click on the **Run Test** button on any of them
				- TODO #Question - is there any way to do this with focus management? Certainly there must for [[A11y]] reasons
	- ## DONE [Run Tests in Parallel](https://code.visualstudio.com/docs/python/testing#_run-tests-in-parallel)
	  id:: 6779110c-b7cc-42fa-b936-c4608e8d6837
	  :LOGBOOK:
	  CLOCK: [2025-01-06 Mon 04:09:48]--[2025-01-06 Mon 04:24:55] =>  00:15:07
	  :END:
		- add `pytest-xdist` to your project's python requirements - [[Python/Library/pytest-xdist]] [pytest-xdist · PyPI](https://pypi.org/project/pytest-xdist/)
	- ## DONE [Run tests with coverage](https://code.visualstudio.com/docs/python/testing#_run-tests-with-coverage)
	  id:: 677b9e94-0b27-4545-8822-13dad09d602a
	  :LOGBOOK:
	  CLOCK: [2025-01-07 Tue 04:05:12]--[2025-01-07 Tue 04:18:42] =>  00:13:30
	  :END:
		- See also [[VSCode/Docs/Editor/Testing/Test Coverage]]
		  id:: 677b9e74-b5eb-4cfd-90a4-b20130981d60
			- ### Where and what is the icon for the test coverage button in [[VSCode/View/Test Explorer]]?  #card
			  card-last-score:: 5
			  card-repeats:: 5
			  card-next-schedule:: 2025-05-05T09:00:11.846Z
			  card-last-interval:: 108
			  card-ease-factor:: 3
			  card-last-reviewed:: 2025-01-17T09:00:11.846Z
				- two places:
					- one on the top of the test explorer for getting **all** test coverage - **two triangles with check in circle**
					- one on **each test** - **one triangle with a check in circle**
				- ![run tests with coverage image](https://code.visualstudio.com/assets/docs/editor/testing/run-tests-with-coverage.png){:height 364, :width 397}
			- ### What is the 1.) #VSCode #Keyshort and 2.) icon for the Show Inline Coverage button? #card
			  card-last-score:: 3
			  card-repeats:: 2
			  card-next-schedule:: 2025-01-17T12:09:50.837Z
			  card-last-interval:: 4.14
			  card-ease-factor:: 2.46
			  card-last-reviewed:: 2025-01-13T09:09:50.837Z
				- keyshort: `⌘; ⇧⌘I`
				- icon: two circles with check
					- ![image.png](../assets/image_1736241312437_0.png){:height 98, :width 337}
				- #Mnemonic - `I` for `I`nline
				- This shows the test coverage in the active file
					- ![view coverage in editor](https://code.visualstudio.com/assets/docs/editor/testing/view-coverage-in-editor.png)
	- ## DONE [[VSCode/Docs/Python/Testing/Debug tests]] https://code.visualstudio.com/docs/python/testing#_debug-tests
	  id:: 677cef29-5a77-4f88-ad9b-c17c21dcd84d
	  :LOGBOOK:
	  CLOCK: [2025-01-08 Wed 03:56:07]--[2025-01-08 Wed 04:13:01] =>  00:16:54
	  :END:
		- see also
			- [Python debugging configurations](https://code.visualstudio.com/docs/python/debugging) [[VSCode/Docs/Python/Debugging]]
			- general VS Code [Debugging](https://code.visualstudio.com/docs/editor/debugging)  [[VSCode/Docs/Editor/Debugging]]
		- important note:
			- > **Note**: Running or debugging a test does not automatically save the test file. Always be sure to save changes to a test before running it, otherwise you'll likely be confused by the results because they still reflect the previous version of the file!
		- ### VSCode Test Debugging **Commands**
			- [[VSCode/Command/Test/Debug/All Tests]]
				- **Test: Debug All Tests** - Launches the debugger for all tests in your workspace.
			- [[VSCode/Command/Test/Debug/Tests in Current File]]
				- **Test: Debug Tests in Current File** - Launches the debugger for the tests you have defined in the file you have open in the editor.
			- [[VSCode/Command/Test/Debug/Test at Cursor]]
				- **Test: Debug Test at Cursor** - Launches the debugger only for the method where you have your cursor focused on the editor. You can also use the **Debug Test** icons in Test Explorer to launch the debugger for all tests in a selected scope and all discovered tests.
		- ### You can change default in the test explorer from run to debug
			- > by changing the `testing.defaultGutterClickAction` setting value to `debug` in your `settings.json` file
		- ### You can customize #VSCode global settings for #Debugging #Software/Testing and create a [[VSCode/launch.json]] for all [[VSCode/Command/Test/Debug]] commands by ... ? #card
		  card-last-interval:: -1
		  card-repeats:: 1
		  card-ease-factor:: 2.36
		  card-next-schedule:: 2025-01-18T05:00:00.000Z
		  card-last-reviewed:: 2025-01-17T08:56:02.107Z
		  card-last-score:: 1
		  id:: 677e3f6e-ccfa-4113-ac4d-54aae44ca3ea
			- See [[VSCode/Docs/Editor/Debugging/Launch configurations]] [here](https://code.visualstudio.com/Docs/editor/debugging#_launch-configurations)
				- updating `launch.json` to include a `"purpose": ["debug-test"]`
					- Why? because you might want to set environment variables, etc. I was actually wondering how to set [[Python/Environment/Variables/PYTHONDONTWRITEBYTECODE]] or [[Python/Environment/Variables/PYTHONUNBUFFERED]]
					- > This configuration will be used when you run **Test: Debug All Tests**, **Test: Debug Tests in Current File** and **Test: Debug Test at Cursor** commands.
					- ```
					  {
					    "name": "Python: Debug Tests",
					    "type": "debugpy",
					    "request": "launch",
					    "program": "${file}",
					    "purpose": ["debug-test"],
					    "console": "integratedTerminal",
					    "justMyCode": false
					  }
					  ```
				- see also [Debugging configurations for Python apps in Visual Studio Code](https://code.visualstudio.com/docs/python/debugging) [[VSCode/Docs/Python/Debugging]]
	- ## DONE [[VSCode/Docs/Python/Testing/Test Commands]] [Test commands](https://code.visualstudio.com/docs/python/testing#_test-commands)
	  id:: 677e4140-01f3-489c-9991-bb7ee91ac2fe
	  :LOGBOOK:
	  CLOCK: [2025-01-09 Thu 03:33:28]--[2025-01-13 Mon 04:24:04] =>  96:50:36
	  :END:
		- ### [[VSCode/Command]] and #Keyshort to Activate [[VSCode/Debugger]] on just the failed [[Test]](s) in the [[VSCode/Editor/Test Explorer]] #card
		  card-last-score:: 3
		  card-repeats:: 3
		  card-next-schedule:: 2025-01-25T19:58:03.225Z
		  card-last-interval:: 8.48
		  card-ease-factor:: 2.56
		  card-last-reviewed:: 2025-01-17T08:58:03.225Z
		  collapsed:: true
			- [[VSCode/Command/Test/Debug/Failed Tests]] with `⌘; ⌘E`
				- **Test:** Debug **Failed Tests**
				  Debug tests that failed in the most recent test run.
				- [[VSCode/Keymap]]
					- ```json
					  {
					    "key": "cmd+; cmd+e",
					    "command": "testing.debugFailTests"
					  }
					  ```
				- #Mnemonic
					- `⌘;` - commonly used chord prefix for shifting focus, making things appear, changing ui
					- `⌘E`
						- *the letter E kind of looks like a call stack*
						- T**E**st: Debug Fail**E**d T**E**sts
					- How to remember that this is debug failed tests, not debug tests?
						- Maybe think of pronouncing FailED tests in a shakespearean way
						-
		- ### [[VSCode/Command]] and #Keyshort to Activate [[VSCode/Debugger]] on the [[Test]]s that were run in the last run #card
		  card-last-interval:: 19.24
		  card-repeats:: 3
		  card-ease-factor:: 2.7
		  card-next-schedule:: 2025-02-05T13:57:13.761Z
		  card-last-reviewed:: 2025-01-17T08:57:13.761Z
		  card-last-score:: 5
		  collapsed:: true
			- Command: **Test:** Debug **Last Run** [[VSCode/Command/Test/Debug/Last Run]]
				- Debug tests that were executed in the most recent test run.
			- Keyshort: `⌘; ⌘L`
				- #Mnemonic
					- `⌘;` - commonly used chordr prefix for activating focus or other things that "change the UI"
					- `⌘L` - **L** for **L**ast Run
			- [[VSCode/Keymap]]
				- ```json
				  {
				    "key": "cmd+; cmd+l",
				    "command": "testing.debugLastRun"
				  }
				  ```
		- ### Commands if the [[VSCode/Editor/Peek/Error]] view is open
		  collapsed:: true
			- See also [[VSCode/Docs/User Guide/Code Navigation/Peek]] view [here](https://code.visualstudio.com/docs/editor/editingevolved#_peek)
			- #### [[VSCode/Command]] and #Keyshort to open and move [[VSCode/Editor/Peek/Error]] view of the previous or next  #Test in the [[VSCode/View/Test Explorer]] that failed #card
			  card-last-interval:: 4
			  card-repeats:: 2
			  card-ease-factor:: 2.22
			  card-next-schedule:: 2025-01-21T09:00:41.714Z
			  card-last-reviewed:: 2025-01-17T09:00:41.714Z
			  card-last-score:: 3
				- ##### [[VSCode/Command/Test/Go to/Previous/Test Failure]]
					- Test: Go to **Previous** Test Failure
					- > If the error peek view is open, open and move to the peek view of the previous test in the explorer that has failed.
					- Keyshort: **⇧⌥F8**
					- [[VSCode/Keymap]]
						- ```json
						  {
						    "key": "shift+alt+f8",
						    "command": "testing.goToPreviousMessage",
						    "when": "editorFocus && testing.isPeekVisible"
						  }
						  ```
					- #Mnemonic see **Go to Next Test Failure** below; this is a modifier of that one
				- ##### [[VSCode/Command/Test/Go to/Next/Test Failure]]
					- Test: Go to **Next** Test Failure
					- > If the error peek view is open, open and move to the peek view of the next test in the explorer that has failed.
					- Keyshort: **⌥F8**
					- [[VSCode/Keymap]]
						- ```json
						  {
						    "key": "alt+f8",
						    "command": "testing.goToNextMessage",
						    "when": "editorFocus && testing.isPeekVisible"
						  }
						  ```
					- **[[Mnemonic]]**:
						- This is a modifier of **F8**, which is **Go To Next Problem in Files**
							- {
							    "key": "f8",
							    "command": "editor.action.marker.nextInFiles",
							    "when": "editorFocus"
							  }
						- similar to the [[VSCode/Debugger]] keyshorts; F9 is set breakpoint, F10 is step over, F11 is step in ... so F8 is kind of like "before debugging".
			- ### [[VSCode/Command]] and #Keyshort to open [[VSCode/Editor/Peek/Error]] for a #Test particular Method that **failed** #card
			  card-last-score:: 1
			  card-repeats:: 1
			  card-next-schedule:: 2025-01-18T05:00:00.000Z
			  card-last-interval:: -1
			  card-ease-factor:: 2.36
			  card-last-reviewed:: 2025-01-17T08:59:54.486Z
				- > Command: **Test: Peek Output** - [[VSCode/Command/Test/Peek Output]] 
				  Opens the error peek view for a test method that has failed.
					- *note that the command name doesn't have anything to do with errors*
				- Keyshort `⌘; ⌘M`
					- ```json
					  {
					    "key": "cmd+; cmd+m",
					    "command": "testing.openOutputPeek"
					  }
					  ```
					- #Mnemonic
						- `⌘;` - commonly used chord for changing focus or making things appear
						- `⌘M` - **M** for **Method**
		- ### [[VSCode/Command]] and #Keyshort to refresh tests in [[VSCode/View/Test Explorer]] #card
		  card-last-score:: 5
		  card-repeats:: 6
		  card-next-schedule:: 2025-07-24T19:56:58.588Z
		  card-last-interval:: 188.48
		  card-ease-factor:: 2.62
		  card-last-reviewed:: 2025-01-17T08:56:58.588Z
		  collapsed:: true
			- [[VSCode/Command/Test/Refresh Tests]]: `⌘; ⌘R`
			- [[VSCode/Keymap]]
				- ```json
				  {
				    "key": "cmd+; cmd+r",
				    "command": "testing.refreshTests",
				    "when": "testing.canRefresh"
				  }
				  ```
			- [[Mnemonic]]: R for Refresh
		- ### Focus the [[VSCode/View/Test Explorer]] with a [[VSCode/Command]] and my User-Defined #Keyshort #card
		  card-last-score:: 5
		  card-repeats:: 3
		  card-next-schedule:: 2025-01-23T23:07:31.506Z
		  card-last-interval:: 10.6
		  card-ease-factor:: 2.56
		  card-last-reviewed:: 2025-01-13T09:07:31.506Z
		  collapsed:: true
			- [[VSCode/Command/Testing/Focus on Test Explorer]]: `⌘; ⌘T`
				- There is no default keyshort, I've made a [[VSCode/Keyshort/Chord/User]]
			- [[VSCode/Keymap]]
				- ```json
				  {
				    "key": "cmd+; cmd+t",
				    "command": "workbench.view.testing.focus"
				  }
				  ```
			- > Testing: Focus on Test Explorer View
			  Open the Test Explorer view. Similar to Testing: Focus on Python View on versions prior to 2021.9.
		- **note**: *there are about four more on the page I didn't import*
	- ## #Defer TODO [[VSCode/Docs/Python/Testing/Django unit tests]] [Django unit tests](https://code.visualstudio.com/docs/python/testing#_django-unit-tests)
	- ## DONE [[VSCode/Docs/Python/Testing/Intellisense for Pytest]] #Pytest [IntelliSense for pytest](https://code.visualstudio.com/docs/python/testing#_intellisense-for-pytest)
	  id:: 677e41c5-3211-4b90-bc64-d0428a264e68
	  :LOGBOOK:
	  CLOCK: [2025-01-14 Tue 03:46:27]--[2025-01-14 Tue 04:04:31] =>  00:18:04
	  :END:
		- This section is about [[VSCode/Extension/Pylance]]
			- works with [[Pytest/Fixture]]s and [[Pytest/Parameterization]]
				- [How to parametrize fixtures and test functions - pytest documentation](https://docs.pytest.org/en/stable/how-to/parametrize.html) [[Pytest/Docs/How To/Parameterize]]
				- Pylance will offer completions
					- from `@pytest.mark.parameterize` decorators
					- from `conftest.py`
				- Pylance also supports [[VSCode/Code Navigation]] actions for fixtures and parameterized tests
					- Go to Definition
					- Find All References
					- Rename Symbol Refactoring for these entities
						- [rename symbol refactoring](https://code.visualstudio.com/docs/editor/refactoring#_rename-symbol)
					- example of autocompleting housing_data from fixture
						- ![example of autocompleting housing_data from fixture](https://code.visualstudio.com/assets/docs/python/testing/pytest-fixture-autocomplete.png){:height 303, :width 570}
				- pylance will show the type of the fixture on hover
					- ![hover over test parameter](https://code.visualstudio.com/assets/docs/python/testing/pytest-inferred-parametrized-argument.png)
				- pylance support [[VSCode/Code Action]]s - see [[VSCode/Docs/Editor/Refactoring]]
					- [code actions](https://code.visualstudio.com/docs/editor/refactoring#_code-actions--quick-fixes-and-refactorings) can be used to add type annotations to test funcs with fixture parameters
					- example:
						- ![add type annotation to housing data inline hints](https://code.visualstudio.com/assets/docs/python/testing/pytest-annotation-code-action.png)
					- DONE what is an [[VSCode/Term/Inlay Hint]] and what Pylance Test configuration is available? #Question #card
					  card-last-interval:: -1
					  card-repeats:: 1
					  card-ease-factor:: 2.36
					  card-next-schedule:: 2025-01-18T05:00:00.000Z
					  card-last-reviewed:: 2025-01-17T08:55:33.771Z
					  card-last-score:: 1
						- > Inlay hints for inferred fixture parameter types can also be enabled by setting `python.analysis.inlayHints.pytestParameters` to `true` in your User settings.
						- via [[ChatGPT/Response]] [here](https://chatgpt.com/g/g-ZpZUQbCxM-vs-code-copilot/c/678627c9-1534-8000-84d2-f696bdc127ce)
							- > An **Inlay Hint** in Visual Studio Code is a small piece of contextual information that appears inline in your code, often as gray, non-intrusive text. It provides additional details such as inferred types, parameter names, or other annotations, without actually altering the source code itself. These hints help you better understand the code and improve your workflow.
							- > When you enable the setting `python.analysis.inlayHints.pytestParameters` by setting it to `true`, **Pylance** (the Python language server) will show inlay hints for **inferred types** of the parameters in pytest fixtures. This means you’ll see hints that indicate the expected data type of the fixture parameters in your test functions, helping you understand what type of data is being injected into the function.
							- > For example, if you have a pytest fixture called `housing_data` that returns a tuple of Pandas DataFrames, enabling this setting might show a hint like this:
								- ```python
								  def cost_manager(housing_data):  # (train_df: DataFrame, test_df: DataFrame, target_feature: str)
								      train_df, test_df, target_feature = housing_data
								  ```
							- > The hint (`# (train_df: DataFrame, test_df: DataFrame, target_feature: str)`) appears inline and tells you that the `housing_data` parameter is inferred to be of a specific type.
							-
	- ## DONE [[VSCode/Docs/Python/Testing/Test configuration settings]] [Test configuration settings](https://code.visualstudio.com/docs/python/testing#_test-configuration-settings)
	  id:: 677e4213-223f-4f80-827b-24b2838d3e67
	  :LOGBOOK:
	  CLOCK: [2025-01-15 Wed 03:19:37]--[2025-01-15 Wed 03:26:39] =>  00:07:02
	  :END:
		- ### What's the difference between the [[VSCode/Command]]s that begin with Testing and those that begin with Test #card
			- > **The settings that affect the UI of the testing features are provided by VS Code itself**, and can be found in the **[VS Code Settings editor](https://code.visualstudio.com/docs/getstarted/settings) [[VSCode/Docs/Getting Started/Settings]]  when you search for "Testing"**.
		- ### DONE [General Python settings](https://code.visualstudio.com/docs/python/testing#_general-python-settings)
			- `autoTestDiscoverOnSaveEnabled` - discover tests in each file on each save
			- `cwd` - working directory for tests
			- `debugPort` - port num used for debugging of unittest tests
			- `promptToConfigure` -
				- > Specifies whether VS Code prompts to configure a test framework if potential tests are discovered.
				- I imagine this is for disabling if the prompts get annoying
		- ### TODO [unittest configuration settings](https://code.visualstudio.com/docs/python/testing#_unittest-configuration-settings)
			- skipped
		- ### DONE [pytest configuration settings](https://code.visualstudio.com/docs/python/testing#_pytest-configuration-settings) #Pytest
		  :LOGBOOK:
		  CLOCK: [2025-01-15 Wed 03:24:42]--[2025-01-15 Wed 03:26:36] =>  00:01:54
		  :END:
			- `pytestEnabled` - t/f
			- `pytestPath` - the path to the pytest executable - unclear if it's python path or not, probably not
			- `pytestArgs` - array - args to pass to pytest, See [pytest command-line options](https://docs.pytest.org/en/latest/reference/reference.html#command-line-flags).
		- ### DONE [IntelliSense settings](https://code.visualstudio.com/docs/python/testing#_intellisense-settings)
			- `inlayHints.pytestParameters` - we already covered this farther up.
				- > Whether to display inlay hints for pytest fixture argument types. Accepted values are true or false.