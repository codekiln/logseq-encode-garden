created-by:: [[Person/Brian Madison]]
date-created:: [[2025/02]]
tags:: [[CursorAI/Project Rules]]

- # [Ultimate Rule Generator - No more failure to generate and Private Rules! - Showcase - Cursor - Community Forum](https://forum.cursor.com/t/ultimate-rule-generator-no-more-failure-to-generate-and-private-rules/51782)
	- [[Original Poster]]
		- There have been a few attempts and shared rules that would generate other rules, but they all seems to have a few problems.
		  
		  After quite a bit of research, tweaking, and figuring out what the optimal format of rules might be (research in the readme linked below), I have created a template with a rule that will:
		- Always save or update a rule (does not fail to write or create a file occasionally
		- Optimize for auto rule selection through optimized front matter descriptions
		- Usage of mermaid diagrams in certain rules if it will aid LLM and reduce need for extra verbosity keeping context smaller
		- Auto Canonical classification
		- Ability to generate both public and private rules
		- Ability to request the LLM learn or never do something again and it will know to create or update a rule
		- A script that will add the rule and a few other nice things to a new or existing repo to quickly add the ability for auto rule generation.
		- If you have existing rules, once this rule is in place, it is great for updating all existing rules into granular well formatted optimized rules following this core rule 000
		  
		  Here is a [Video Demo and Walkthrough](https://youtu.be/jEhvwYkI-og) ([[Person/Brian Madison/YouTube/25/02/Unlock Cursor AI Automatic Rule Generation]]) of auto rule generation, theory of why this works so well, along with a demo of voice → rule generation and public vs private rule handling.
		  
		  Check it out here [[Person/Brian Madison/GitHub/cursor-custom-agents-rules-generator]]   - the readme has more info, or just take a look at the .cursor/rules rule 000.
	- ## #[[My Notes]]
		- comment from [[CursorAI/Forum/User/sanjiovani100]] [here](https://forum.cursor.com/t/ultimate-rule-generator-no-more-failure-to-generate-and-private-rules/51782/17?u=codekiln) mentions it might be possible to get the rules path to be somewhere else  ...
			- TODO *does this actually work??*
			- > Insert this JSON snippet into your global Cursor configuration file (e.g., settings.json). [[VSCode/settings.json]]
				- ```json
				  {
				    "rules.globalRulesPath": "~/.cursor/rules/enterprise-standards",
				    "rules.mergeStrategy": "override",
				    "rules.autoApplyPatterns": ["**/*.tsx", "**/api/*.ts"]
				  }
				  ```