- ```
  openspec config profile
  
  Current profile settings
    Delivery: both
    Workflows: 11 selected (custom)
    Delivery = where workflows are installed (skills, commands, or both)
    Workflows = which actions are available (propose, explore, apply, etc.)
  
  ✔ What do you want to configure? Delivery only
  ? Delivery mode (how workflows are installed):
  ❯ Both (skills + commands) [current]
    Skills only
    Commands only
  
  Install workflows as both skills and slash commands
  ↑↓ navigate • ⏎ select
  
  ```
- There are three options:
	- 1 - Both
	- 2 - opsx installed in project as [[Agent/Skills]]
	- 3 - opsx installed in project as [[Slash Command]]
- Why might we want both?
	- {{embed [[Agent/Command/vs Agent Skills]]}}