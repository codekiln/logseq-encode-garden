type:: Project Milestone
status:: status/InProgress
created-by-template:: [[Logseq/Template/Project/Milestone/Page]]
up:: [[VSCode/Proj/24t3/LearnVSCode]]
tags:: [[VSCode/Language/Python]]
banner:: "../assets/Logseq/Plugins/logseq-banners-plugin/Land-of-the-Ancients-Overnighter_2.jpg"
icon:: 🎯

- # TODO Milestone - Basic VS Code Python Support
  :LOGBOOK:
  CLOCK: [2024-12-25 Wed 10:32:31]--[2025-01-15 Wed 03:29:30] =>  496:56:59
  :END:
	- ## Summary
		- ### Milestone #Goals
			- #Goal/Primary
				- **Job to be done:** To feel comfortable
					- writing larger python applications in VS Code
					- navigating python codebases not written by me
					- setting up VS Code for python
					- using keyboard shortcuts to navigate python code
			- #Goal/Secondary
				- make progress towards "level 2" python programming in [[VSCode]], where "level 5" is likely about where I'm at in #PyCharm - see also the other python milestones
				- To explore [[GitHub/CoPilot]] with python
		- ### Milestone #Scope
			- [[Scope/In]] - [[MoSCoW/Must-Have]]
				- Define a [[Poetry]] project interpreter with [[Pyenv]]
				- Set up basic run configurations for python, specifically poetry
				- Be able to use Intellisense to view and browse a python codebase
				- Be able to do basic #Debugging in python using poetry
				- Be able to navigate from stack trace to the the application
			- [[MoSCoW/Should-have]]
				- Configuring basic extensions for python development, including static analysis
			- [[MoSCoW/Could-have]]
			- [[Scope/Out]] - [[MoSCoW/Wont-have-right-now]]
				- out of scope - any item that should have its own milestone; see also create milestones in Project page
					- {{embed ((676c2977-8659-4e75-b3b3-2f46917382b0))}}
		- ## #Decisions
		  note:: place any decisions about the milestone underneath
		- ## #Reminders
		  Note:: reminders about the scope of the milestone or the actual objectives
	- ## #Todos
		- ### Best Next Actions
		  note:: nest items underneath that are references to other todos as a way to highlight them; then use block references to next actions to single out the important things
		  id:: 676dc72d-276f-4bfe-97fc-cb927a903f48
			- {{embed ((67877274-5d01-4a22-8e88-517fd286e8e9))}}
		- ### Practical Next Actions
			- done
			  note:: nest completed todos under
			  collapsed:: true
				- DONE do [[VSCode/Docs/Languages/Python/Tutorial]] [Get Started Tutorial for Python in Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial)
				  id:: 676d1726-f47d-453d-92a4-e2664e126776
				  :LOGBOOK:
				  CLOCK: [2024-12-25 Wed 11:05:29]--[2024-12-28 Sat 03:40:30] =>  64:35:01
				  :END:
				- DONE learn how to do **Python Static Analysis** for linting, mypy, etc
				  id:: 676c2f9c-c40c-4ca5-b632-4e3ec1d9423d
				  :LOGBOOK:
				  CLOCK: [2024-12-30 Mon 04:20:34]--[2024-12-30 Mon 04:34:27] =>  00:13:53
				  :END:
					- DONE Take notes on [[VSCode/Docs/Python/Linting]]
					  id:: 676fbb37-484e-4c18-9278-bb5e16488b91
					  :LOGBOOK:
					  CLOCK: [2024-12-30 Mon 04:21:41]--[2024-12-30 Mon 04:34:25] =>  00:12:44
					  :END:
					- DONE [[VSCode/Docs/Python/Formatting]] follow [Formatting Python in Visual Studio Code](https://code.visualstudio.com/docs/python/formatting#_choose-a-formatter) to install a formatter
					  id:: 676dc72d-dfae-48b6-a94a-d7eede7cd4aa
					  :LOGBOOK:
					  CLOCK: [2024-12-30 Mon 04:23:47]--[2024-12-30 Mon 04:34:26] =>  00:10:39
					  :END:
					- DONE install [[VSCode/Extension/charliermarsh.ruff]] for [[Ruff]]
					  id:: 677266b0-6ce4-4155-bca7-176f18bc786d
					  :LOGBOOK:
					  CLOCK: [2024-12-30 Mon 04:24:34]--[2024-12-30 Mon 04:34:14] =>  00:09:40
					  :END:
						- DONE configure [[Ruff]] extension [[VSCode/Extension/charliermarsh.ruff]]
						  :LOGBOOK:
						  CLOCK: [2024-12-30 Mon 04:26:14]--[2024-12-30 Mon 04:34:12] =>  00:07:58
						  :END:
							- DONE configure editor.formatOnSave
							  id:: 67726735-baf1-4d04-8e89-7bbb202e4aae
							  :LOGBOOK:
							  CLOCK: [2024-12-30 Mon 04:26:28]--[2024-12-30 Mon 04:34:06] =>  00:07:38
							  :END:
							- TODO skim [[Ruff/Settings]]
							  id:: 67726715-5130-4525-b8e5-7ca026b672d0
				- ((6777cb12-88af-4ac9-a143-2a0c4ef1f93c))
				  id:: 676fcf8f-f981-4726-a38c-0377baafddc5
				  :LOGBOOK:
				  CLOCK: [2024-12-31 Tue 03:33:26]
				  :END:
					- done
					  collapsed:: true
						- DONE ((6779110c-b7cc-42fa-b936-c4608e8d6837))
						- ((6777cb49-a088-457d-9854-2ff848db90c0))
						- ((677b9e94-0b27-4545-8822-13dad09d602a))
						- ((677cef29-5a77-4f88-ad9b-c17c21dcd84d))
						- ((677e4140-01f3-489c-9991-bb7ee91ac2fe))
						  id:: 677e4272-f038-4978-a4fb-cb6dfcb36b7f
					- ((677e41c5-3211-4b90-bc64-d0428a264e68))
					- ((677e4213-223f-4f80-827b-24b2838d3e67))
			- DOING backlog grooming on this milestone vs other milestones
			  id:: 67877274-5d01-4a22-8e88-517fd286e8e9
			  :LOGBOOK:
			  CLOCK: [2025-01-16 Thu 03:44:01]
			  :END:
				- TODO learn python refactoring
					- TODO find some plugins and research [Does VS Code have built-in code refactoring? : r/learnpython](https://www.reddit.com/r/learnpython/comments/1ar8z0g/does_vs_code_have_builtin_code_refactoring/) from 2024
					- TODO consider plugins and research from [Visual Studio Code is designed to fracture : r/vscode](https://www.reddit.com/r/vscode/comments/x221sl/visual_studio_code_is_designed_to_fracture/)
			- #Defer
				- TODO take notes on [[VSCode/Docs/Editor/Testing]]
				- TODO take notes on [Python profile template](https://code.visualstudio.com/docs/editor/profiles#_python-profile-template) [[VSCode/Docs/Editor/Profiles/Python Profile Template]] - Create a new [[VSCode/Docs/Editor/Profile/Python]]  [profile](https://code.visualstudio.com/docs/editor/profiles) with a curated set of extensions, settings, and snippets
				- TODO take notes on [[VSCode/Docs/Python/Debugging]] [Debugging](https://code.visualstudio.com/docs/python/debugging) - Learn to debug Python both locally and remotely.
					- TODO How do I create a [[VSCode/launch.json]] [[VSCode/Debugger/Configuration]] so that when it asks me for arguments, I can supply more than one and they will be supplied as more than one argument? #Question
					  id:: 676fd6c9-baa1-4402-ba53-1ca4a0dd8aaa
					- TODO is there any way to create a [[VSCode/launch.json]] [[VSCode/Debugger/Configuration]]
				- TODO take notes on [[VSCode/Extension/Python]] [Python - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
				- TODO take notes on [[VSCode/Docs/Python/Environments]] [Using Python Environments in Visual Studio Code](https://code.visualstudio.com/docs/python/environments)
				  id:: 676c30b5-0717-45b2-a906-e6d17f2242dd
				- TODO take notes on [[VSCode/Docs/Languages/Python]] [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
				- TODO find a good VSCode for Python course
		- ### Items to push to the parent project
			- TODO #to-file how can I format jinja files with [[Ruff]] in [[VSCode]]? #Question
			  id:: 677276bc-8175-4a8f-8e23-2e39eb5db802
		- ### Theoretical Next Actions
		- ### #Design todos
		- ### #Conceptual questions
		- ### [[Distraction/Side/Quest]] Todos - minimize these
		- ### Completion -
			- TODO  python is covered well enough for now; move on to another milestone
- # LearnVSCode_03_Python #Log
  Note:: reverse cron; use `/template` then `Today Link` (see [[Logseq/Template/Today/Link]]) for heading
	- **LearnVSCode_03_Python**
	  id:: 676e65d1-7fd6-4d37-8863-136b07ce7a9d
	- bna
	  collapsed:: true
		- {{embed ((676dc72d-276f-4bfe-97fc-cb927a903f48))}}
	- **LearnVSCode_03_Python** log [[2025/t1/w03/d7]] - [[2025/01/19]] - [[Sun, 2025/01/19]]
		- 07:14 - #Learned how to set [[Python/Environment/Variables/PYTHONDONTWRITEBYTECODE]] by default in [[VSCode]] - [[VSCode/Language/Python/Tips/Source Dotenv in Settings Json to Avoid Cache]]
		  id:: e40fa7f2-9b33-4445-a8ba-d520baa1af2c
			- put this in `.vscode/settings.json` in the repo:
				- ```json
				  {
				      "python.envFile": "${workspaceFolder}/.env"
				  }
				  ```
			- put this in `.env`
				- ```
				  # disable VSCode from creating __pycache__ folders
				  # works with .vscode/settings.json
				  PYTHONDONTWRITEBYTECODE=1
				  ```
	- **LearnVSCode_03_Python** log [[2025/t1/w03/d3]] - [[2025/01/15]] - [[Wed, 2025/01/15]]
	  id:: 67876f5b-b32e-4d3c-9447-1ed8ec2e54e6
	  collapsed:: true
		- bna
			- {{embed ((676dc72d-276f-4bfe-97fc-cb927a903f48))}}
		- ((677e4213-223f-4f80-827b-24b2838d3e67))
		- Next up - I think python is covered well enough; consider ((67877274-5d01-4a22-8e88-517fd286e8e9))
	- Archive
	  collapsed:: true
		- **LearnVSCode_03_Python** log [[2025/t1/w03/d2]] - [[2025/01/14]] - [[Tue, 2025/01/14]]
		  id:: 678623f2-3fcf-4f0a-a000-151f994870e1
		  collapsed:: true
			- 03:44 - finished ((677e41c5-3211-4b90-bc64-d0428a264e68))
			- next ((677e4213-223f-4f80-827b-24b2838d3e67))
		- **LearnVSCode_03_Python** log [[2025/t1/w03/d1]] - [[2025/01/13]] - [[Mon, 2025/01/13]]
			- 04:15 -  ((677e4140-01f3-489c-9991-bb7ee91ac2fe))
		- **LearnVSCode_03_Python** - log [[2025/t1/w02/d6]] - [[2025/01/11]] - [[Sat, 2025/01/11]]
		  id:: 678231a6-a751-4e93-a1ca-3bd6961e88e4
		  collapsed:: true
			- 03:54 - ((677e4140-01f3-489c-9991-bb7ee91ac2fe))
				- did a bit of maintenance on [[VSCode/Command/Test]] hierarchy; there are still more commands I want to add but I needed to clean things up in order to make room for them
			-
		- **LearnVSCode_03_Python** log [[2025/t1/w02/d5]] - [[2025/01/10]] - [[Fri, 2025/01/10]]
		  id:: 6780e0c0-33e2-40a7-9446-4d5d7fe970e6
		  collapsed:: true
			- 03:56 -  ((676fcf8f-f981-4726-a38c-0377baafddc5))
				- made progress here, there's still more to do tomorrow. lots of great commands to learn
		- **LearnVSCode_03_Python** log [[2025/t1/w02/d4]] - [[2025/01/09]] - [[Thu, 2025/01/09]]
		  id:: 677f87ea-b736-46f6-98c6-909f33c29965
		  collapsed:: true
			- 03:25 - ((676fcf8f-f981-4726-a38c-0377baafddc5))
				- ((677e4140-01f3-489c-9991-bb7ee91ac2fe))
					- #Learned that I can easily copy keyshorts from the [[VSCode/View/Keyboard Shortcuts]] view
					- ### [[VSCode/Keyshort]] for [[VSCode/Command/Go To/Problem/Next/In Files]] #card
					  id:: 677f8f5e-5523-453b-a6c9-634f3fa5b9d3
					  card-last-interval:: 84.1
					  card-repeats:: 5
					  card-ease-factor:: 2.76
					  card-next-schedule:: 2025-04-11T10:55:42.982Z
					  card-last-reviewed:: 2025-01-17T08:55:42.982Z
					  card-last-score:: 5
						- {
						    "key": "f8",
						    "command": "editor.action.marker.nextInFiles",
						    "when": "editorFocus"
						  }
						- see also ((677f9029-ca84-45f5-996f-a4b6ebf18b4a))
		- **LearnVSCode_03_Python** log [[2025/t1/w02/d3]] - [[2025/01/08]] - [[Wed, 2025/01/08]]
		  id:: 677e3d1c-9e83-497b-8aca-496109dcd7c4
		  collapsed:: true
			- 03:53 - ((677cef29-5a77-4f88-ad9b-c17c21dcd84d))
		- **LearnVSCode_03_Python** log [[2025/t1/w02/d2]] - [[2025/01/07]] - [[Tue, 2025/01/07]]
		  id:: 677cedf4-93ae-4ec6-baab-355815056429
		  collapsed:: true
			- 04:03 - ((677b9e94-0b27-4545-8822-13dad09d602a))
			- tomorrow: ((677cef29-5a77-4f88-ad9b-c17c21dcd84d))
			- DONE do [[VSCode/Flashcards]]
			  :LOGBOOK:
			  CLOCK: [2025-01-07 Tue 04:21:46]--[2025-01-07 Tue 04:30:37] =>  00:08:51
			  :END:
		- **LearnVSCode_03_Python** log [[2025/t1/w02/d1]] - [[2025/01/06]] - [[Mon, 2025/01/06]]
		  id:: 677b9d16-fb9b-45fb-91a5-faedcfbf3aff
		  collapsed:: true
			- 04:06 -
			- DOING update [[VSCode/Proj/24t3/LearnVSCode]]
			  :LOGBOOK:
			  CLOCK: [2025-01-06 Mon 04:05:22]
			  :END:
				- DONE set 2nd howler for 10min
				- DONE find next best todo or milestone
				  :LOGBOOK:
				  CLOCK: [2025-01-06 Mon 04:07:44]--[2025-01-06 Mon 04:25:41] =>  00:17:57
				  :END:
				- DONE create a log entry there and link here:
				- DONE open log in sidebar
				- DONE open milestone and create log entry and open in sidebar
			- DONE do [[VSCode/Keyshort]] flashcards
			  id:: dc91c02d-353b-4f5a-90f9-1156f73caad5
			- ((6777cb12-88af-4ac9-a143-2a0c4ef1f93c))
				- ((6779110c-b7cc-42fa-b936-c4608e8d6837))
					- [2025-01-06 04:24 - ab20760f - feat: update dependencies in poetry.lock and pyproject.toml; add pytest-](https://github.com/codekiln/gitpa/commit/ab20760f) #git/commit
				- tomorrow: ((677b9e94-0b27-4545-8822-13dad09d602a))
		- **LearnVSCode_03_Python** log [[2025/t1/w01/d4]] - [[2025/01/04]] - [[Sat, 2025/01/04]]
		  id:: 67790ecb-1279-4432-8bec-9941a294da90
		  collapsed:: true
			- bna
				- {{embed ((676dc72d-276f-4bfe-97fc-cb927a903f48))}}
			- 05:34 - ((fab544be-7716-477e-8ab5-0f2ab7e0d96d))
				- started using TODOs to track the headings in the page; I think that's going to work well. Got done with the section ((67790fe6-e552-4a05-a26f-f6ec149b1dd1))
		- **LearnVSCode_03_Python** - log [[2025/t1/w01/d3]] - [[2025/01/03]] - [[Fri, 2025/01/03]]
		  id:: 6777c29e-b433-4802-95cc-23e1abfec1a7
		  collapsed:: true
			- ((ca447fe7-a363-47ae-a5af-9db6f8ec6a07))
				- DONE start toggl with "Learning VSCode" under "[the great engineer](https://track.toggl.com/projects/256158/list/clients/66375519)" toggl client
				  :LOGBOOK:
				  CLOCK: [2025-01-03 Fri 05:56:11]--[2025-01-03 Fri 05:56:25] =>  00:00:14
				  :END:
				- DONE open [[Chrome/Tab/Group/VSCode]]
				- DOING update [[VSCode/Proj/24t3/LearnVSCode]]
				  :LOGBOOK:
				  CLOCK: [2025-01-03 Fri 05:57:17]
				  :END:
					- DONE set 2nd howler for 10min
					- DONE find next best todo or milestone
					  :LOGBOOK:
					  CLOCK: [2025-01-03 Fri 06:00:03]--[2025-01-03 Fri 06:01:03] =>  00:01:00
					  :END:
					- DONE create a log entry there and link here:
					- DONE open log in sidebar
					- DONE open milestone and create log entry and open in sidebar
					- ((676fcf8f-f981-4726-a38c-0377baafddc5))
						- :LOGBOOK:
						  CLOCK: [2024-12-31 Tue 03:36:56]--[2025-01-15 Wed 03:29:25] =>  359:52:29
						  :END:
						- Today, I worked on ((6777cb49-a088-457d-9854-2ff848db90c0))
				- TODO do [[VSCode/Keyshort]] flashcards
		- **LearnVSCode_03_Python** - log [[2024/Trimester/t3/w17/d9]] - [[Tue, 2024/12/31]]
		  id:: 6773ac7e-b13c-49af-883f-96871ef85b21
		  collapsed:: true
			- bna
				- {{embed ((676dc72d-276f-4bfe-97fc-cb927a903f48))}}
			- ((77e1948d-daed-43f8-8a62-59fcedb5ebd1))
				- :LOGBOOK:
				  CLOCK: [2024-12-31 Tue 03:36:56]--[2025-01-15 Wed 03:29:25] =>  359:52:29
				  :END:
					-
		- **LearnVSCode_03_Python** - log [[2024/Trimester/t3/w17/d8]] - [[Mon, 2024/12/30]]
		  id:: 67726583-8776-4776-bdf6-03d298d03deb
		  collapsed:: true
			- ((21d18a91-6019-4459-ac6a-401f5a49a752))
				- ((676c2f9c-c40c-4ca5-b632-4e3ec1d9423d))
				  collapsed:: true
					- ((676fbb37-484e-4c18-9278-bb5e16488b91))
					- ((676dc72d-dfae-48b6-a94a-d7eede7cd4aa))
					- ((677266b0-6ce4-4155-bca7-176f18bc786d))
						- ((67726735-baf1-4d04-8e89-7bbb202e4aae))
						- ((67726715-5130-4525-b8e5-7ca026b672d0))
					- [2024-12-30 04:33 - 2e1329b8 - style: ruff](https://github.com/codekiln/gitpa/commit/2e1329b8) #git/commit
					-
					-
		- **LearnVSCode_03_Python** log [[2024/Trimester/t3/w17/d6]] - [[Sat, 2024/12/28]]
		  id:: 676fb85f-b4f3-4b99-82da-1fcd916c175f
		  collapsed:: true
			- ((5b1f5e7e-4473-4d0a-8caf-dcc5c7415deb))
				- completed ((676d1726-f47d-453d-92a4-e2664e126776))
					- need to import these
					-
		- **LearnVSCode_03_Python** log [[2024/Trimester/t3/w17/d5]] - [[Fri, 2024/12/27]]
		  id:: 676e65d2-27ea-465b-924e-145f025e3cb5
		  collapsed:: true
			- ((a7ac112d-cfcf-4784-84f8-5f303d140398))
				- ((36b9625e-b11e-470c-81e9-1ff68ec4b73d))
					- ((676d1726-f47d-453d-92a4-e2664e126776))
						- #Filed
							- ((676e669d-4de0-43e9-831d-00e287115c4c))
							- ((676e67b7-70f1-4329-ac76-7653326f5548))
							- ((676e6807-8cc7-453d-81a7-0b0fbcb43420))
							- about five others as well
		- **LearnVSCode_03_Python** log [[2024/Trimester/t3/w17/d4]] - [[Thu, 2024/12/26]]
		  collapsed:: true
			- 04:03 - ((676d1726-f47d-453d-92a4-e2664e126776))
				- ((676d1726-828b-419f-a23d-033b79cb391b))
					- ((676d1cb7-8c2b-4108-89de-bb8129d3bf68))
					- TODO add taking notes on these to milestone todos #to-file
						- ((676d1d18-01df-4a93-8cc4-983f5a3d13c3))
						- ((676d1d2b-6ad5-4baa-9a2e-218ad2c419ce))
					- ((676d1d19-1ea4-42bd-b1b2-844f44aa63b3))
						- TODO #Question #to-file What is the #VSCode #Keyshort for the Run Python button
					- 04:19 #Filed ((676d1dfa-f9d4-4335-be68-fcd95e3fe89a))
				-
		- **LearnVSCode_03_Python** log [[2024/Trimester/t3/w17/d3]] - [[Wed, 2024/12/25]]
		  collapsed:: true
			- 10:35 - created milestone and filled out scope
			- 11:02 - ((2ca9c3c8-0810-4adc-ab6e-2a45fba87e46))
			  id:: 676c263c-2b13-40b2-8626-d83b0ac63c04
				- I'm just going to use [[GitP/acolyte]] since I already have that up
				- ((676a7d98-cc9a-40e8-a3ac-206723c03760))
				- 13:09 filed [[VSCode/Language/Python/How To/Use Poetry with Pyenv and VS Code]]
				- 13:11 filed [[VSCode/Language/Python/How To/Fix Stuck at Discovering Python Interpreters]]