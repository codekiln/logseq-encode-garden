# TODO How can I go to a Python class by name in #VSCode?
	- In VS Code, you can filter symbols to show only classes in the **Go to Symbol** (`Cmd + T` on macOS, `Ctrl + T` on Windows/Linux) by using a **prefix** `:class`.
	- ### [[VSCode/Keyshort]] for going to a class anywhere in the workspace #card
		- Press `Cmd + T` (or `Ctrl + T` on Windows/Linux) to open **Go to Symbol**.
		- Type `:class` (including the colon) before the class name.
			- Example: `:class MyClass`
			  
			  This will filter the list to show **only class symbols**.
	- ### [[VSCode/Keyshort]] for going to a class in the current file #card
		- Use `Cmd + Shift + O` (`Ctrl + Shift + O` on Windows/Linux) to open the symbol search for the **current file**.
		- Then type `:class` to filter only classes in the file.