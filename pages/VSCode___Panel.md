- [Panel | Visual Studio Code Extension API](https://code.visualstudio.com/api/ux-guidelines/panel)
	- The **Panel** functions as another main area to display [View Containers](https://code.visualstudio.com/api/references/contribution-points#contributes.viewsContainers).
	- ![panel image](https://code.visualstudio.com/assets/api/ux-guidelines/examples/panel.png)
	- The **Panel Toolbar** [[VSCode/Panel/Toolbar]]
		- > The Panel Toolbar can expose options scoped to the currently selected View. For example the Terminal view exposes [View Actions](https://code.visualstudio.com/api/extension-guides/tree-view#view-actions) to add a new terminal, split the view layout, and more. Switching to the Problems view exposes a different set of actions. Similar to the [Sidebar Toolbar](https://code.visualstudio.com/api/ux-guidelines/sidebars#sidebar-toolbar), the toolbar will only render if there is just a single View. If more than one View is used, each View will render its own toolbar.
		- ![Panel Toolbar](https://code.visualstudio.com/assets/api/ux-guidelines/examples/panel-toolbar.png)
- ### [[VSCode/Command]] and #Keyshort to make the [[VSCode/Panel]] appear or disappear #card
  card-last-interval:: -1
  card-repeats:: 1
  card-ease-factor:: 2.5
  card-next-schedule:: 2026-04-13T04:00:00.000Z
  card-last-reviewed:: 2026-04-12T08:19:30.387Z
  card-last-score:: 1
	- [[VSCode/Command/View/Toggle Panel Visibility]]
		- **Command:** View: Toggle Panel Visibility
		- **Keyshort**: Cmd+J
		- [[VSCode/Keymap]]
			- ```json
			  {
			    "key": "cmd+j",
			    "command": "workbench.action.togglePanel"
			  }
			  ```