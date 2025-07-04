tags:: [[AI Agents]]

- # [Project Vend: Can Claude run a small shop? (And why does that matter?) \ Anthropic](https://www.anthropic.com/research/project-vend-1)
	- ![project vend](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F4b10e3632598a2e9b8c2532f5947eab3042307ba-3225x4000.jpg&w=3840&q=75)
	- ## Quotes
		- The shopkeeping AI agent—nicknamed “**Claudius**” for no particular reason other than to distinguish it from more normal uses of Claude—was an instance of Claude Sonnet 3.7, running for a long period of time. It had the following tools and abilities:
			- A real web search tool for **researching products to sell**;
			- An email tool for **requesting physical labor help** (Andon Labs employees would periodically come to the Anthropic office to restock the shop) and contacting wholesalers (for the purposes of the experiment, Andon Labs served as the wholesaler, although this was not made apparent to the AI). Note that this tool couldn’t send real emails, and was created for the purposes of the experiment;
			- **Tools for keeping notes** and preserving important information to be checked later—for example, the **current balances and projected cash flow** of the shop (this was necessary because the full history of the running of the shop would overwhelm the “context window” that determines what information an LLM can process at any given time);
			- The ability to **interact with its customers** (in this case, Anthropic employees). This interaction **occurred over the team communication platform** [[Slack]]. It allowed people to inquire about items of interest and notify Claudius of delays or other issues;
			- The ability to change prices on the automated checkout system at the store.
		- Claudius **decided what to stock**, **how to price** its inventory, **when to restock** (or stop selling) items, and **how to reply to customers**
		- ![Basic Architecture of Project Vend](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0ee1d466f7d4bcb40c72ff20727ce6435bc10b5b-4096x2304.png&w=3840&q=75)