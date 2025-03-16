alias:: [[VSCode/Docs/Editor/EditingEvolved]]

- [Code Navigation in Visual Studio Code](https://code.visualstudio.com/docs/editor/editingevolved)
  readwise-link:: [Code Navigation | Readwise](https://read.readwise.io/new/read/01jfma7fzthzr3bz88fc99d3cs)
- # #Keyshort for #VSCode - [[VSCode/Code Navigation]]
	- ## Quick file navigation
		- ### view a list of all files open in an [[VSCode/Editor/Group]] and then open one #card
		  id:: 67692113-9416-4a9f-8a59-d6525b21bb6c
		  card-last-interval:: 36
		  card-repeats:: 4
		  card-ease-factor:: 2.9
		  card-next-schedule:: 2025-02-22T09:01:38.209Z
		  card-last-reviewed:: 2025-01-17T09:01:38.210Z
		  card-last-score:: 5
			- hold `Ctrl` and then press `Tab` to view a list of all files open in an editor group
				- ![editor group panel open](https://code.visualstudio.com/assets/docs/editor/editingevolved/quicknav.png)
			- While **still** holding `Ctrl`, press `Tab` to select the file below
			- Release `Ctrl` to open the file
			- **How to remember: ** it's very similar to `Ctrl+Tab` and `Ctrl+Shift+Tab` in old internet explorer
		- ### navigate forwards and backwards between files and edit locations like `Ctrl+]` in PyCharm and Vim #card
		  card-last-interval:: 36
		  card-repeats:: 4
		  card-ease-factor:: 2.9
		  card-next-schedule:: 2025-02-22T09:00:56.254Z
		  card-last-reviewed:: 2025-01-17T09:00:56.255Z
		  card-last-score:: 5
			- `Ctrl -` and `Ctrl Shift -`
			- > Alternatively, you can use ⌃- and ⌃⇧- to navigate between files and edit locations.
			- **note**: this will navigate **within a file** as well as **between files**
			- [[VSCode/Keymap]]
				- ```json
				  {
				    "key": "ctrl+-",
				    "command": "workbench.action.navigateBack",
				    "when": "canNavigateBack"
				  }
				  ```
	- ## Breadcrumbs
		- ### use the drop-down menu in the breadcrumbs to navigate to another folder higher up
			- ![Breadcrumbs example](https://code.visualstudio.com/assets/docs/editor/editingevolved/breadcrumb-folder-dropdown.png)
		- ### you can customize display of breadcrumbs
			- > If you have very long paths or are only interested in either file paths or symbols paths, you can use the `breadcrumbs.filePath` and `breadcrumbs.symbolPath` settings
				- These support `on`, `off`, `last`
				- The **symbols** here are the `TS` for typescript in the image above
		- ### Breadcrumb keyboard navigation
			- #### how to focus breadcrumbs and interact with them for navigation #card
			  card-last-score:: 5
			  card-repeats:: 3
			  card-next-schedule:: 2025-01-22T08:37:34.954Z
			  card-last-interval:: 11
			  card-ease-factor:: 2.66
			  card-last-reviewed:: 2025-01-11T08:37:34.954Z
				- `Cmd Shift Semicolon` to focus the breadcrumbs, then left and right arrows, then typing names
				- > use the Focus Breadcrumbs command or press `⇧⌘;`
				- > It will select that **last element** and **open a dropdown** that **allows you to navigate to a sibling file or symbol**.
				- > **Use the ← and → keyboard shortcuts to go to elements before or after AKA up the hierarchy or down the hierarchy of the current element**.
				- > Press **Down** to open the items in that dir. When the dropdown appears, **start typing** - all **matching elements will be highlighted** and the **best match will be selected** for quick navigation.
		- ### Go to definition - if a programming language is set up #card
		  card-last-score:: 1
		  card-repeats:: 1
		  card-next-schedule:: 2025-01-18T05:00:00.000Z
		  card-last-interval:: -1
		  card-ease-factor:: 2.8
		  card-last-reviewed:: 2025-01-17T09:01:16.499Z
			- id:: 676924b2-53eb-47c8-b29d-b765c3433ac2
			  > If a [programming language](https://code.visualstudio.com/docs/languages/overview) like [python](https://code.visualstudio.com/docs/languages/python) supports it [in VSCode], you can go to the definition of a symbol by pressing `F12`.
			- [[Mnemonic]]: the other related command, **Go to Implementation** is `Cmd F12`, which is a modifier of going to the **Definition** (rather than the concrete implementation)
			  id:: 676a798f-c5d0-427e-9a3f-ca77bc9e0d5d
		- ### Get a preview of the declaration #Mouse #card
		  id:: 676a7c8a-a832-4e47-9029-c855e0ef275b
		  card-last-interval:: 31.36
		  card-repeats:: 4
		  card-ease-factor:: 2.8
		  card-next-schedule:: 2025-02-17T17:04:29.439Z
		  card-last-reviewed:: 2025-01-17T09:04:29.439Z
		  card-last-score:: 5
			- `Cmd` and hover over symbol
			- ![ctrl hover](https://code.visualstudio.com/assets/docs/editor/editingevolved/ctrlhover.png)
			- see also ((676a7b3a-475a-4d9c-a42a-0df0c87d0b96))
			- Changelog:
				- [[Mon, 2024/12/30]] updated to `Cmd`; `Ctrl` is for Windows
		- ### Jump to definition or open definition to the side #Mouse #card
		  id:: 676a7d41-b46a-4d80-a225-f6cc2b373864
		  card-last-interval:: 225.58
		  card-repeats:: 7
		  card-ease-factor:: 2.24
		  card-next-schedule:: 2025-08-30T21:58:42.831Z
		  card-last-reviewed:: 2025-01-17T08:58:42.831Z
		  card-last-score:: 5
			- > You can **jump to the definition** with `Cmd+Click` or **open the definition to the side** with `Cmd+Opt+Click`.
			-
		- ### Go to Implementation #card
		  card-last-interval:: 9.28
		  card-repeats:: 3
		  card-ease-factor:: 2.32
		  card-next-schedule:: 2025-01-23T14:39:50.741Z
		  card-last-reviewed:: 2025-01-14T08:39:50.741Z
		  card-last-score:: 3
			- `Cmd F12`
			- Requires one a programming languages to be set up - see [[VSCode/Docs/Languages/Overview]]
			- **Note**: *this is different from Go to Definition because Go to Implementation is for finding how a method is implemented in specific subclasses vs Go to Definition which looks up where the current symbol is located* - according to [[ChatGPT/GPT/VS Code Copilot]] **here**
			- [[Mnemonic]]: `F12` is **Go to Definition**, and `Cmd F12` is a modifier to go to the **Concrete Implementations**
		- ### Navigate programming language symbols in a file, group by category #card
		  card-last-score:: 3
		  card-repeats:: 3
		  card-next-schedule:: 2025-01-21T22:37:57.925Z
		  card-last-interval:: 10.6
		  card-ease-factor:: 2.56
		  card-last-reviewed:: 2025-01-11T08:37:57.925Z
			- `Shift Cmd O` (that's capital **O** as in **Open**)
			- Typing `colon` will group them by category
			- Navigate `Up` or `Down` to navigate to place
			- ![navigate by symbol in vscode](https://code.visualstudio.com/assets/docs/editor/editingevolved/gotosymbol.png)
			- **How to Remember:** this is similar to PyCharm's open Object Cmd Shft O, and this could be used to browse objects in the current file.
		- ### [Open Symbol by Name](https://code.visualstudio.com/docs/editor/editingevolved#_open-symbol-by-name) #card
		  id:: 676bc54b-3fcb-4a9b-ad04-02f217c44fa8
		  card-last-interval:: 11.2
		  card-repeats:: 3
		  card-ease-factor:: 2.8
		  card-next-schedule:: 2025-01-22T12:38:35.361Z
		  card-last-reviewed:: 2025-01-11T08:38:35.361Z
		  card-last-score:: 5
			- `Cmd T`
			- ![autocomplete symbol](https://code.visualstudio.com/assets/docs/editor/editingevolved/symbol.png)
			- [[Mnemonic]] - the letter `T` is a picture of a road going up to a point where you have to pick whether to turn right or left, which is just like the situation you are in when you switch from browsing by file to browsing by symbol
		-