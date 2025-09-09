# [Designing for AI Agents MCP – Jessica Kerr](https://on24static.akamaized.net/event/49/94/94/2/rt/1/documents/resourceList1757091679028/mcpdesignfororeillybyjessitron1757091679028.pdf)
	- ## Overview
		- **Duration**: 15 minutes
		- **Time**: 13:55
		- **Speaker**: [[Person/Jessica Kerr]] from #Observability company [[Co/Honeycomb]]
		- **Event**: [[OReilly/Event/25/09/AI Codecon]]
		- **Resources**: [PDF](https://on24static.akamaized.net/event/49/94/94/2/rt/1/documents/resourceList1757091679028/mcpdesignfororeillybyjessitron1757091679028.pdf)
	- ## Description
		- Discussion of design principles for AI agents using Model Context Protocol (MCP)
		- Exploration of user experience considerations for AI agent interfaces
		- Focus on creating effective and intuitive AI agent interactions
	- ## Key Topics
		- Design principles for AI agents
		- Model Context Protocol (MCP) design considerations
		- User experience for AI agent interfaces
		- Creating intuitive AI agent interactions
		- Best practices for AI agent design
	- ## [[My Notes]] - GREAT TALK
		- [[Person/Tim O'Reilly]] talks about an architecture of participation in AI
			- he also has an "AI disclosures project"
				- many disclosures are "functional disclosures" (what does this mean?)
			- he mentions "fixing without understanding" blog post
		- Quotes Amanda Bernard, Director of Product Design, Honeycomb.io
			- > “AI is the most exciting innovation in design since I started doing it 25 years ago.”
			- > “MCP lets us bring people the experiences they need and want. That's why it's an MVP of AI IMO.”
		- [[Key Insight]], their product people WILL talk in Claude Desktop to ask questions
		- #Quote:
			- > [[MCP]] is its own living documentation
		- Checkout the screenshots in the slides which show how to use an [[Observability]] program using [[Anthropic/App/Claude Desktop]]
		- #LOL they respond with ASCII art because it's more efficient than sending back json - #Example
			- ```
			  HEATMAP(duration_ms)
			   3.0K ├
			   2.8K ├█
			   2.5K ├█
			   2.2K ├█
			   1.9K ├█
			   1.6K ├█
			   1.4K ├█
			   1.1K ├█
			   825  ├█
			   550  ├█
			   275  ├█
			   0    └█▁ ▁ ▁▁ ▁ ▁
			   └--------------------------------------------------
			   0.750 401 728
			  Buckets: 50, Step size: 16.0, Total points: 3034
			  Legend: ▁▂▃▄▅▆▇█ (0-3026 events)
			  ```
		- #Advice for #MCP
			- > “Give it quite a bit of guidance, in ways you wouldn’t like or find acceptable for people.”
				- BTW this is from someone who has the title "Austin Parker, Product Lead, MCP"
			- Give really great [[Error/Message]]s
				- [[Example/Bad]]
					- > Invalid parameters: query validation failed - check that calculations have required columns, time ranges are valid, and filters use supported operators
				- [[Example/Good]]
					- > This query uses the same column for 'group
					  by' and 'count distinct', which means the
					  query would group your data by column and
					  then also try to count distinct instances of
					  that column within each group. As a result,
					  'count distinct' would return 1 for every group.
					  Try re-running this query with a different
					  'group by' or 'count distinct' option
				- Errors in the process are not failures, they are part of the process #Quote from [[Person/Jessica Kerr]]
		- #Quote
			- > “If we had good enough
			  evaluation, AI could optimize
			  the software for us.”
			  Morgante Pell,
			  AI Engineering Lead
		-