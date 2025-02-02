type:: [[Diataxis/How To]]

- # How to use the keyboard to find replace across multiple files
	- In this how-to guide, we will replace the string "`Today Day Link`" with "`Today Page Link` (see [[Logseq/Template/Today/Link]])" across multiple files using VSCode keyboard shortcuts.
	- ### use the #VSCode #Keyshort to open the Find aka Search panel #card
	  card-last-interval:: 33.64
	  card-repeats:: 4
	  card-ease-factor:: 2.9
	  card-next-schedule:: 2025-02-09T00:33:18.841Z
	  card-last-reviewed:: 2025-01-06T09:33:18.842Z
	  card-last-score:: 5
		- Cmd Shift F
		- type in the item you wish to Search for
			- > `Today Day Link`
	- ### use the #VSCode #Keyshort to open the replace details in the Find dialog, #card
	  card-last-interval:: 33.64
	  card-repeats:: 4
	  card-ease-factor:: 2.9
	  card-next-schedule:: 2025-02-03T09:18:02.579Z
	  card-last-reviewed:: 2024-12-31T18:18:02.580Z
	  card-last-score:: 5
		- Cmd Shift H
		- enter in the term you wish to Replace the found items with
		- > `Today Page Link` (see [[Logseq/Template/Today/Link]])
	- tab to the "**Files to include**" text entry and enter a wildcard path that matches the files to include
		- `./pages/Logseq___*`
		- Note: you can use **up** and **down** to load prior values of field
	- tab to the "**Files to exclude**" text entry and enter a wildcard path that excludes files
		- (none in this example)
		- Note: you can use **up** and **down** to load prior values of field
	- **Tab** to the "Pages" disclosure in the panel so it's highlighted.
		- ![image.png](../assets/image_1734336383146_0.png){:height 360, :width 249}
	- Press **Down** to focus on the heading of the **pages** section containing the result
		- ![image.png](../assets/image_1734336430044_0.png){:height 341, :width 236}
	- Press **Down** again to select the first **page** that contains results (this is a whole **file** of results, even though the image below only contains a single result for each file)
		- ![image.png](../assets/image_1734336618891_0.png){:height 338, :width 351}
	- ## Apply changes to an entire File
		- ### *With a Page selected in the Pages section of the Find and Replace aka Search panel*, **Apply All Changes** in a File with #VSCode #Keyshort #card ![image.png](../assets/image_1734337247934_0.png){:height 258, :width 240}
		  card-last-interval:: 33.64
		  card-repeats:: 4
		  card-ease-factor:: 2.9
		  card-next-schedule:: 2025-02-03T09:18:25.974Z
		  card-last-reviewed:: 2024-12-31T18:18:25.975Z
		  card-last-score:: 5
			- **Cmd Shift 1**
			- Also, you can just tab to it
			- *Note: you won't see the change preview; if you need to see the change preview, use the method below using a Change Diff line below*
	- ## Apply particular changes in a File
		- At this point, no file will be open in the editor. If you press **Down** once to focus the **Change Diff** for the first Find and Replace Result for the File, the diff for the file will open in the editor. If there are multiple changes to make in the file, there will be one line for each change.
			- ![image.png](../assets/image_1734336727485_0.png)
		-
		- ### When focused on a particular Change Diff line in the Pages panel of the Find and Replace aka Search panel, what is the #VSCode #Keyshort to apply the selected Change? ![image.png](../assets/image_1734336877163_0.png) #card
		  card-last-interval:: 33.64
		  card-repeats:: 4
		  card-ease-factor:: 2.9
		  card-next-schedule:: 2025-02-03T09:18:12.559Z
		  card-last-reviewed:: 2024-12-31T18:18:12.559Z
		  card-last-score:: 5
			- Cmd Shift 1
			- Alternatively, if you press **Tab** while a particular **Change Diff** is selected, you can focus the **Replace** button
	-
	-