readwise-link:: https://read.readwise.io/new/read/01jfz94w9xygdp5gx50req7srh

- [Get Started Tutorial for Python in Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial)
- DONE install [[VSCode/Extension/Python]] [Python - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  id:: 676a7d98-cc9a-40e8-a3ac-206723c03760
  :LOGBOOK:
  CLOCK: [2024-12-25 Wed 11:13:07]--[2024-12-25 Wed 11:24:35] =>  00:11:28
  :END:
	- This automatically installs two other extensions
		- [[VSCode/Extension/Pylance]] - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) - to provide performant Python language support
		- [[VSCode/Extension/Python/Debugger]] - [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy) - to provide a seamless debug experience with [[Py/debugpy]]
- DONE get a python interpreter to work
- DONE prove [[IntelliSense]] works
  id:: 676d1cb7-8c2b-4108-89de-bb8129d3bf68
- DONE bookmark links to getting more advanced [[VSCode/Language/Python]] features
	- DONE import into #Readwise/Reader [Editing Python Code in Visual Studio Code](https://code.visualstudio.com/docs/python/editing)  [[VSCode/Docs/Python/Editing]]
	  id:: 676d1d18-01df-4a93-8cc4-983f5a3d13c3
	  :LOGBOOK:
	  CLOCK: [2024-12-26 Thu 04:10:14]--[2024-12-26 Thu 04:10:24] =>  00:00:10
	  :END:
	- DONE import into #Readwise/Reader [Linting Python in Visual Studio Code](https://code.visualstudio.com/docs/python/linting) [[VSCode/Docs/Python/Linting]]
	  id:: 676d1d2b-6ad5-4baa-9a2e-218ad2c419ce
- DONE Run [[Py]] code
  id:: 676d1d19-1ea4-42bd-b1b2-844f44aa63b3
  :LOGBOOK:
  CLOCK: [2024-12-26 Thu 04:11:58]--[2024-12-26 Thu 04:19:30] =>  00:07:32
  :END:
	-
	- it works for me, using my environment
		- ```
		  gitp-acolyte ✘ Me@Home  ~/dev/gitpa  ↱ cc/04-host-n-dist/03-ai-ep-yml  /Users/Me/.pyenv/versions/3.13.1/envs/gitp-acolyte/bin/python /Users/Me/dev/gitpa/gitp-acolyte/gitp_acolyte/hello.py
		  Roll a dice!
		  ```
	- ## four ways to run #Py in #VSCode
	  id:: 676d1dfa-f9d4-4335-be68-fcd95e3fe89a
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2024-12-28T05:00:00.000Z
	  card-last-reviewed:: 2024-12-27T09:01:44.627Z
	  card-last-score:: 1
		- #### How to run python file #Button #Mouse #card
		  card-last-score:: 5
		  card-repeats:: 3
		  card-next-schedule:: 2025-01-20T12:31:09.188Z
		  card-last-interval:: 11.2
		  card-ease-factor:: 2.8
		  card-last-reviewed:: 2025-01-09T08:31:09.189Z
			- hit the Run Python File button
			- ![run python in code editor](https://code.visualstudio.com/assets/docs/python/tutorial/run-python-file-in-terminal-button.png)
		- #### How to run python file in terminal - #Mouse #card
		  card-last-score:: 3
		  card-repeats:: 3
		  card-next-schedule:: 2025-01-17T15:28:37.718Z
		  card-last-interval:: 8.32
		  card-ease-factor:: 2.08
		  card-last-reviewed:: 2025-01-09T08:28:37.718Z
			- Right click in editor and select **Run Python > Run Python File in Terminal** (note, this **saves the file automatically** unlike some other VS Code commands like debug tests)
			- ![run python file in terminal](https://code.visualstudio.com/assets/docs/python/tutorial/run-python-file-in-terminal.png)
		- #### How to run selected lines #card #Keyshort and #Mouse methods, plus smart send
		  card-last-score:: 5
		  card-repeats:: 7
		  card-next-schedule:: 2025-11-18T18:56:19.553Z
		  card-last-interval:: 305.45
		  card-ease-factor:: 2.38
		  card-last-reviewed:: 2025-01-17T08:56:19.553Z
			- 3rd way to run python -
				- **select lines** and do one of the following
					- 1 - **Keyboard** - press `Shift Enter`
					- 2 - **Mouse** - right-click and select **Run Python > Run Selection/Line in Python Terminal**
				- 3 - **don't select lines**, but instead **place cursor** press `Shift Enter` - "smart send"
					- *use "smart send" by using `Shift+Enter` **without a selection**, which send the "smallest runnable block of code near where your cursor is placed"*
		- #### How to start python REPL #card #Keyshort
		  card-last-interval:: 9.28
		  card-repeats:: 3
		  card-ease-factor:: 2.32
		  card-next-schedule:: 2025-01-18T14:29:46.239Z
		  card-last-reviewed:: 2025-01-09T08:29:46.239Z
		  card-last-score:: 5
			- Way 4 to run python  - From Command Palette `Shift Cmd P` select **Python: Start Terminal REPL**
- ## [Configure and run the debugger](https://code.visualstudio.com/docs/python/python-tutorial#_configure-and-run-the-debugger)
	- ### What is the #VSCode #Keyshort to open the [[VSCode/Extension/View]] and search for an installed extension? #card
	  id:: 676e669d-4de0-43e9-831d-00e287115c4c
	  card-last-interval:: 10.24
	  card-repeats:: 3
	  card-ease-factor:: 2.56
	  card-next-schedule:: 2025-01-19T13:28:52.563Z
	  card-last-reviewed:: 2025-01-09T08:28:52.564Z
	  card-last-score:: 5
		- `Cmd+Shift+X` to open the view
		- search with `@installed <extension keyword query>`
	- ### #VSCode #Keyshort to set or unset a [[Debugger/Breakpoint]] on the current line in [[VSCode/Debugger]] #card
	  card-last-score:: 5
	  card-repeats:: 3
	  card-next-schedule:: 2025-01-22T12:38:04.957Z
	  card-last-interval:: 11.2
	  id:: 676e67b7-70f1-4329-ac76-7653326f5548
	  card-ease-factor:: 2.8
	  card-last-reviewed:: 2025-01-11T08:38:04.957Z
		- Toggle breakpoint with `F9`
		- Changelog
			- log [[2025/t1/w01/d4]] - [[2025/01/04]] - [[Sat, 2025/01/04]]
				- 05:57 - formerly, I had Shift F9 as unset breakpoint, but it's just F9 for both
	- ### #VSCode #Keyshort to initialize the [[VSCode/Debugger]] #card
	  id:: 676e6807-8cc7-453d-81a7-0b0fbcb43420
	  card-last-interval:: 11.2
	  card-repeats:: 3
	  card-ease-factor:: 2.8
	  card-next-schedule:: 2025-01-24T13:07:48.201Z
	  card-last-reviewed:: 2025-01-13T09:07:48.201Z
	  card-last-score:: 5
		- `F5`
		- ![initialize debugger](https://code.visualstudio.com/assets/docs/python/shared/debug-configurations.png)
	- ### The main #VSCode [[VSCode/Debugger]] #Keyshorts
		- #### What is the [[VSCode/Debugger]] #Keyshort **and logo** for [[Debugger/Action/Continue]] ? #card
		  card-last-interval:: 25.4
		  card-repeats:: 4
		  card-ease-factor:: 2.52
		  card-next-schedule:: 2025-02-11T17:56:23.702Z
		  card-last-reviewed:: 2025-01-17T08:56:23.702Z
		  card-last-score:: 5
			- `F5`
			- ![image.png](../assets/image_1735289188660_0.png) - continue (F5)
		- ####
		- #### What is the [[VSCode/Debugger]] #Keyshort and logo for [[Debugger/Action/Step/Over]]? #card
		  card-last-interval:: 31.36
		  card-repeats:: 4
		  card-ease-factor:: 2.8
		  card-next-schedule:: 2025-02-17T17:04:16.077Z
		  card-last-reviewed:: 2025-01-17T09:04:16.077Z
		  card-last-score:: 5
			- [[VSCode/Command/Debug/Step Over]] **Debug: Step Over**
				- Keyshort: **F10**
				- ![image.png](../assets/image_1735289288253_0.png) - step over (F10)
				- you can remember this because from left to right, F9-F12 are in the right order from left to right of when you need them. F10 is what you need after F9
				- [[VSCode/Keymap]]
					- ```json
					  {
					    "key": "f10",
					    "command": "workbench.action.debug.stepOver",
					    "when": "debugState == 'stopped'"
					  }
					  ```
		- #### What is the [[VSCode/Debugger]] #Keyshort and logo for [[Debugger/Action/Step/Into]]? #card
		  card-last-interval:: 11.2
		  card-repeats:: 3
		  card-ease-factor:: 2.8
		  card-next-schedule:: 2025-01-20T12:31:17.839Z
		  card-last-reviewed:: 2025-01-09T08:31:17.839Z
		  card-last-score:: 5
			- `F11`
			- ![image.png](../assets/image_1735289328581_0.png) - step into (F11)
		- #### What is the [[VSCode/Debugger]] #Keyshort and logo for [[Debugger/Action/Step/Out]]? #card
		  card-last-interval:: 10.24
		  card-repeats:: 3
		  card-ease-factor:: 2.56
		  card-next-schedule:: 2025-01-19T13:27:15.206Z
		  card-last-reviewed:: 2025-01-09T08:27:15.206Z
		  card-last-score:: 5
			- `Shift F11`
				- mnemonic: it's the opposite of [[Debugger/Action/Step/Into]]
			- ![image.png](../assets/image_1735289442750_0.png) - step out (⇧F11)
		- #### What is the [[VSCode/Debugger]] #Keyshort and logo for [[Debugger/Action/Restart]]? #card
		  card-last-interval:: 10.24
		  card-repeats:: 3
		  card-ease-factor:: 2.56
		  card-next-schedule:: 2025-01-19T13:27:29.240Z
		  card-last-reviewed:: 2025-01-09T08:27:29.240Z
		  card-last-score:: 5
			- `Shift Cmd F5`
			- ![image.png](../assets/image_1735289478443_0.png) - restart (⇧⌘F5)
		- #### What is the [[VSCode/Debugger]] #Keyshort and logo for [[Debugger/Action/Stop]]? #card
		  card-last-interval:: 10.6
		  card-repeats:: 3
		  card-ease-factor:: 2.56
		  card-next-schedule:: 2025-01-21T22:38:20.562Z
		  card-last-reviewed:: 2025-01-11T08:38:20.563Z
		  card-last-score:: 3
			- ![image.png](../assets/image_1735289587106_0.png) -  stop (⇧F5)
	- ## Links
	-
	-
-
-