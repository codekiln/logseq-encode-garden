- This is a bit like a [[UX/Pattern/Table of Contents]] that enables one to select whether subsequent steps of the `openspec config profile` will configure [[OpenSpec/Delivery]], [[OpenSpec/Workflow]]s, or both
	- ```
	  openspec config profile
	  
	  Current profile settings
	    Delivery: both
	    Workflows: 4 selected (core)
	    Delivery = where workflows are installed (skills, commands, or both)
	    Workflows = which actions are available (propose, explore, apply, etc.)
	  
	  ? What do you want to configure?
	  ❯ Delivery and workflows
	    Delivery only
	    Workflows only
	    Keep current settings (exit)
	  
	  Update install mode and available actions together
	  ↑↓ navigate • ⏎ select
	  Config profile cancelled.
	  
	  ```