created-by:: [[People/Mahesh Murag]]
tags:: [[Anthropic/Model Context Protocol]]

- # [Building (Agents) with Model Context Protocol](https://www.ai.engineer/summit/2025/schedule/anthropic-mcp)
	- This workshop, from the creators of MCP, talks about the philosophy behind MCP, its impact on the broader ecosystem since launch, and how developers can use it to build context-rich AI apps and agentic experiences.
	- met
		- left
			- 1 - real estate
		- right hayden
			- headless agents hosting
			- headlessagents.ai
	- ## intro
		- what is MCP
			- APIs
				- web applications interact with backend
			- LSP - language server protocol
				- specifies how IDEs to interact with **language-specific tools**
			- MSP
				- standardize how Ai apps interact with external systems
		- without mcp - fragmented AI development
			- EACH AI app -> custom implementation custom prompt logic -> custom tool calls -> custom data access
			- if different teams in company are doing this
		- ### MCP - standardized AI development
			- ![image.png](../assets/image_1740238166470_0.png)
				- Any MCP Client:
				  •	Claude for Desktop
				  •	Cursor
				  •	Goose
				  •	Windsurf
				  •	Your Client
				- MCP Servers and Their Functions:
				- Database MCP server
				  •	Query and fetch data
				  •	Modify records
				  •	Handle data streams
				  → Databases
				- CRM MCP server
				  •	Create/update contacts
				  •	Manage opportunities
				  •	Track interactions
				  → CRM systems
				- Version Control MCP server
				  •	Commit changes
				  •	Resolve conflicts
				  •	Manage branches
				  → Version Control Software
		- #### with mcp - you build it once and get adoption everywhere
			- for AI app devs
				- connect your app to any mcp server with
			- for tool or API devs
				- build mcp server once, see adoption everywhere
			- for end users
				- more powerful and context-rich ai applications
			- for enterprises
				- clear separation of concerns between teams
					- #Insight
						- you can have **one team that owns the relationship to the vector database**
		- fast adoption
			- 1100 community built servers
			- [[Person/Jack Dorsey]] mentioned it yesterday
			- we think this is going to be industry-standard
		- ### MCP deep dive
			- ![image.png](../assets/image_1740238166470_0.png)
			- ### CGPT notes
				- #### MCP Client
				  •	Invokes Tools
				  •	Queries for Resources
				  •	Interpolates Prompts
				- #### MCP Server
				  •	Exposes Tools
				  •	Exposes Resources
				  •	Exposes Prompts
				- Components:
				- #### Tools (Model-controlled)
				  •	Functions invoked by the model:
				  •	Retrieve / search
				  •	Send a message
				  •	Update DB records
				- #### Resources (Application-controlled)
				  •	Data exposed to the application:
				  •	Files
				  •	Database Records
				  •	API Responses
				- #### Prompts (User-controlled)
					- Pre-defined templates for AI interactions:
					- Document Q&A
					- Transcript Summary
					- Output as JSON
			- #### my notes
				- MCP Client
					- invokes tools
					- queries for
				- server can interpolate
				- ### resources
					- manifest as attachments
					- attached to the chat
			- #### #Example [[IDE/Zed]] [[AI/Coding]] [[Slash Command]]
			- Q - why aren't resources modeled as tools
				- A - it's not about making model better but defining ways for application to interact with the server
				- we need separation between model-controlled and not model-controlled
				- contract for the client builder and server builder for what should be invoked where
			- [[langgraph]] just made adapters to connect to [[MCP]]
				- if it has this connection to mcp servers you can connect it to your agent
				- we don't think mcp is going to replace agent frameworks
			- a few questions are about "why isn't it a tool"
			- a few questions about "why do we need agent frameworks if we need this"
			- #### q - why do resources and prompts exist, because you can do it with tools
				- a - there are more capabilities with tools and resources
				- in reality, resources and prompts can be *dynamic* and interpolated with context from the user or the aplication and the server can return a customized resource or prompt for the task at hand
				- client can subscribe to resource, and server can notify the client and tell the client that you need to update the state of your system
				- you can do a lot with tools, but MCP isn't just about giving the model more context, it's about getting richer ways to give the application
		- ### MCP in Action
			- ![image.png](../assets/image_1740239495124_0.png)
				- ## MCP in Action
				- ### Screenshot 1:  **Claude AI Ticket Prioritization**
				- Lists various technical issues:
					- **Prompt Caching Support for Vertex/Bedrock (#774, #653)**
						- Multiple requests for prompt caching support
						- Parity gap between direct API and cloud provider integrations
						- Could improve performance and reduce costs
					- **PDF File Support Issues (#725)**
						- Problems with PDF document handling on Bedrock
						- Impacts users leveraging Claude's document understanding
					- **Testing Framework Updates (#647)**
						- Test suite failures with `pytest 8`
						- Maintaining test reliability is important for development
						  
						  **Prompt in UI:**
						  *"Can you triage the top 3 highest priority issues and add them to my Asana project for SDK Fixes?"*
				- ### Screenshot 2:  **GitHub Issues Page (Anthropic SDK)**
				- Open issues list:
					- **Some API error codes don’t appear to be supported in SDK (#853)**
					- **OpenAI Compatibility using Claude API Key (#851)**
					- **Feature request: `tool_choice="none"` to prevent unintended tool calls (#849)**
					- **Caching seems to be enabled by default (#837)**
					  
					  **Speaker:** Vibhu Sapra
					  **Presented by Anthropic**
				- [[Claude/Desktop]]
					- give url of github repository
					- the model, claude, does the invoke issues tool, and pulls those into context, summarizing them
					- it's personalizing to you based on your history with claude and what it knows you want
						- who you are,
						- what you are working on
						- how you like to interact with it
					- "can you triage the top 3 priority issues and add it to my asana project"
						- doesn't give name of asana
						- has installed asana server
							- 30 tools
						- finds the projects
							- starts adding these issues as tasks
					- callouts
						- I didn't build the github or asana server
						- each are a couple hundred lines of code
							- it's not a ton of additional work to build though
						- they are all playing together with claude for desktop
					- (video)
		- ### Here's [[IDE/Windsurf]]
			- they have their own ui inside of their agent
			- other applications don't call them tools (one calls them extensions)
				- -> which IDE is that? booz?
		- ### claim: MCP will be the foundational protocol for agents
			- the models are becoming better and they use the data that you bring to them in better ways.
		- ### blog post -> building effective agents
			- now, *with MCP*
			- the idea of an augmented LLM
			- takes inputs and outputs
			- LLM
				- query and results with retrieval systems
				- call and response with tools
				- read and write with memory
			- one of the key points of MCP is that the system can **discover new capabilities after the agent system is built**
			- agent is an "augmented LLM" running in a loop
				- working towards
			- you can let users of the agent system connect to their data and you as the developer can focus on **the core loop**
				- the agent can be focused with the interaction with the llm as it's core
			-
		- ## what does this look like in practice - [[MCP/mcp-agent]]
			- `mcp-agent` is a framework built by lastmile.ai
				- [[MCP/mcp-agent]]
					- perhaps - [lastmile-ai/mcp-agent: Build effective agents using Model Context Protocol and simple workflow patterns](https://github.com/lastmile-ai/mcp-agent)
			- case study -> research task -> quantum computing impact on cybersecurity
			- sub-agents
				- research agent
					- look up urls
				- fact checker agent
					- verify info coming in
						- brave, fetch, filesystem tools
							- each are mcp servers that it has access to
				- research writer
			- we get a `plan.md` and a `task.md`
				- ![image.png](../assets/image_1740239455247_0.png)
					- ### File:  `plan.md`
						- **Description:** Verify and validate collected information
							- **Tasks:**
								- Cross-reference technical claims about quantum computing capabilities and encryption threats
									- **Agent:** `fact_checker`
								- Verify timeline predictions and industry statistics for consistency across sources
									- **Agent:** `fact_checker`
								- Validate technical details of proposed quantum-resistant solutions
									- **Agent:** `fact_checker`
									  
									  **Editor:** VS Code
									  **Workspace:** `mcp-agent`
									  **Active Files:** `main.py`, `orchestrator.py`, `plan.md`, `task.md`
				- ### Screenshot 2:  **GitHub Issues Page (Anthropic SDK)**
					- Open issues list:
						- **Some API error codes don’t appear to be supported in SDK (#853)**
						- **OpenAI Compatibility using Claude API Key (#851)**
						- **Feature request: `tool_choice="none"` to prevent unintended tool calls (#849)**
						- **Caching seems to be enabled by default (#837)**
						-
			- to close out this part of **demo**
				- it starts doing some research
				- invoking the fact checking agent
			- [lastmile-ai/mcp-agent: Build effective agents using Model Context Protocol and simple workflow patterns](https://github.com/lastmile-ai)
				- someone asks about this and what's adapted
			- question - how do resources and prompts fit in in this case
				- resources and prompts come in when the user is in the loop
				- what if you had a nice loop in an extended chat interface
					- the chat interface application could take this plan and surface it to you
					- aplpication could have nice UI on top that shows the plan beautifully in the UI
				- prompts example
					- slash command - slash summarize (predefined prompt in server to give the user a summary)
			- questions - how does #MCP fit into evaluations
				- largely this is the same as it is right now
				- this could be a standard layer inside of evals themselves
				- there could be an MCP server that has the same 5 tools
			- question - I'm missing the infrastructure side of this
				- are these servers exposed globally, or only locally?
				- comment: line between client and server not clear to one person
					- how do you do authentication, retry logic, etc
				- q - what is the separation between the logic, retry logic, authentication
					- for retry logic, personal opinion is that it should happen on the server side
			- [[Q/My]] how do we do versioning well with MCP servers
			- #Q is there a best practice or a limit to the number of servers you can expose to an LLM?
				- today, they are good up to 50 or 100
					- [[Claude]] is good up to 100 in my opinion
				- but how do you avoid overloading context
				- "a tool to search tools" is exciting
					- RAG over tools
					- the entire library of tools that are
				- hierarchical systems of tools
				- #Observation *this reminds me of that [[LangChain/Blog/25/02/Benchmarking Single Agent Performance]]*
			- #Q - they have an entire page on how to make mcp server with claude or llms
				- he wrote all of those with claude
				- it's really easy to approach it
				- start with tool type
			- #Q - if these are simple, can lLms gerentate
				- if you've heard of cline, they have an mcp auto generator tool
					- if you want to start talking to gitlab
						- that works for simple servers
					- but if you want logging or data traan
			- #Q are you talking to the owners of the services and the data
				- a lot of th servers are public already
			- [[Q/My]] - how do you handle versioning of tool descriptions and tools available
				- typescript servers have semvar version
				- no best practice yet
			- #Q -
		- ## Building Effective Agents with MCP
			- ![image.png](../assets/image_1740240522201_0.png)
				- ## **Building Effective Agents with MCP**
				- ### **Sampling →**
				  
				  Allows a server to request completions from a client, giving the user application full control over security, privacy, and cost.
				- ### **Client-Server Interaction**
				  
				  ```
				  arduino
				  
				  CopyEdit
				  
				  Client  ←→  Server
				  (Request for inference)
				  ```
				- ### **Sampling Parameters:**
					- **Model Preferences & Hints**
					- **System Prompt**
					- **Temperature & Max Tokens**
			- notes
				- in typical applications, client invokes a server, but a class of server exists where the server will
				- server **asks the user** for **more information** so you **want the server to get intelligence**
				- federate these requests
				- client doesn't have to listen to it
					- has control over cost or privacy
					- limit certain # of requests
				- one of the design principles
			- ### Building effective Agents with MCP
				- ![image.png](../assets/image_1740240775949_0.png)
				- #### cgpt notes
					- ## **Building Effective Agents with MCP**
					- ### **Composability →**
						- [[Key Insight]] An [[MCP/Server]] can be a server and vice-versa.
					- ### **Client-Server Chain**
					  
					  ```
					  User & LLM  ←→  Client/Server  ←→  Client/Server  ←→  Client/Server
					  ```
					- The architecture allows for **recursive composition** where MCP clients can also act as servers.
					- Enables **modular AI workflows** by chaining multiple MCP instances.
				- #### my #notes
					- microservices and chaining
				- #### [[Q]] - how do you deal with compounding errors if the system itself is complex and multi-layered
					- same dynamic as with multi-layer agents
					- it's up to each successive layer to deal with controlling data as it's structured
					- the third node up there should collect data and fan in data from all the other ones and make sure it's
				- #### #Q - How do you do observability and how does the first client/server know about the results of the 3rd hop client/server?
					- it's you don't exactly know what's behind the hood
					- it's kind of a black box
				- #### #Q - how do you make #MCP able to be #Debuggable
					- it's up to the devs right now
				- #### #Q this is similar to [[Microservices]]
					- best practices from there should apply
				- #### #Q what if client wants control over the tool call
					- one suggestion is doing that via a prompt
					- they are thinking about something called [[MCP/Tool/Annotations]] to limit the number of tools to 5
				- #### #Q - what #Debugging patterns have you seen
					- they have something called [[MCP/Inspector]]
					- he's seen servers
				- #### #Q - how are you thinking about #Security #[[Good Question]]
					- we're going to bake in [[Auth]]
- ## what's coming next
	- ### Building effective agents with #MCP
		- ![image.png](../assets/image_1740241876883_0.png)
			- Notes from Hayden - *the tool specs are sent back, LLM is only called on client*
			-
		- cgpt notes
			- ## **Building Effective Agents with MCP**
			- ### **Sampling + Composability**
			  
			  Chain agents together while ensuring that the client application controls inference.
			- ### **Architecture**
			  
			  ```
			  arduino
			  
			  CopyEdit
			  
			  Application + LLM  →  Client/Server (Orchestrator Agent)
			                       ├── Client/Server (Analysis Agent)
			                       ├── Client/Server (Coding Agent)
			                       ├── Client/Server (Additional Agent)
			  ```
			- The **Orchestrator Agent** acts as the central hub, distributing tasks to specialized agents.
			- Each agent functions as both a **client and server**, supporting **modular and scalable AI workflows**.
			- Enables **controlled inference** with **hierarchical delegation**.
		- my #notes
			- orchestrator agent communicates with and fans out to analysis, coding, and research agents
		- we need guarantees about connectivity while we
		- [[MCP/Inspector]] with #Auth
			- ![image.png](../assets/image_1740242601017_0.png)
				- ## **MCP Inspector with Auth!**
					- ### **MCP Inspector v0.4.0**
					- **Transport Type:** SSE
					- **URL:** *(Redacted)*
					- **Connection Status:** ✅ Connected
					- ### **Resources Panel**
					- List of resources:
						- **general**
						- **random**
						- **justin-testing**
						- **test**
						- **slack-connect-testing**
						- **justin-testing-2**
					- **Resource Templates Panel** (Empty)
					- ### **Displayed JSON Response (Slack Message)**
					  
					  ```
					  json
					  
					  CopyEdit
					  
					  {
					  "contents": [
					    {
					      "uri": "slack://conversations/C04LN9C1SL/messages",
					      "mimeType": "application/json",
					      "text": "{\"channelId\":\"C04LN9C1SL\",\"messages\":[{\"text\":\"Unsubscribed from <https://github.com/modelcontextproto>\"}]}"
					    }
					  ]
					  }
					  ```
			- ![image.png](../assets/image_1740242590849_0.png)
				- ## **MCP Inspector with Slack OAuth Authentication**
				- ### **Slack OAuth Prompt**
				- **Slack MCP Server** is requesting permission to access the **Development Environment Slack workspace**
				- Requested Permissions:
					- **Content and info about you**
					- **Content and info about channels & conversations**
				- Options:
					- **[Cancel]**
					- **[Allow]**
		- [[SSE]] is the "best way" to do [[MCP/Server]]s that are remote
		- #Example
			- #Slack auth
				- the highlight here
				- num 1 thing -> remotely hosted servers
				- discoverable
				- you don't have to mess with stdio
				- you can
				- this is going to be a big explosion in the number of servers
					- you as a user don't need to know how to build it or host it
				- ## **MCP Inspector with Slack OAuth Authentication**
					- ### **Slack OAuth Prompt**
					- **Slack MCP Server** is requesting permission to access the **Development Environment Slack workspace**
					- Requested Permissions:
						- **Content and info about you**
						- **Content and info about channels & conversations**
					- Options:
						- **[Cancel]**
						- **[Allow]**
				- #### #Q what about elevating permissions
				- #### #Q the server then holds the token -> isn't that a bad thing?
					- if you think about the server being the one that's closest to slack
					- let's say slack builds that and then slack will want to control that
				- #### #Q does MCP replace [[REST]] in the long term?
					- LLMs need data in a different way than the server
					- RESTful is for stateless interactions
				- #### #Q - when we wrap our tools with MCP, how do we deal with evals, how do we think about when tools change and regressions happen
					- we are going to talk about the registry
					- this doesn't change too much about the eval system around tools
					- fixtures and diffs in the evals
				- #### #Q how far away in the spec is it
					- days away
	- ### [[MCP/Registry/API]] #API
		- ![image.png](../assets/image_1740242405280_0.png)
		- cgpt
			- ## **An Official MCP Registry API**
				- A **unified, hosted metadata service** enabling:
				- **Discovery**
				- **Centralization**
				- **Verification**
				- ### **Registry API Structure**
				  
				  ```
				  less
				  
				  CopyEdit
				  
				  Registry API
				  ├── registry: npm  (version: 1.2.0, type: stdio)
				  ├── registry: pypi (version: 1.0.0, type: sse)
				  ├── registry: npm  (version: 1.0.0, type: sse)
				  ```
				- Metadata includes **versions**, **protocol types** (`stdio`, `sse`), and **URLs**.
				- Supports **multiple package registries** (`npm`, `pypi`, etc.)
		- my #notes
			- this lets us have something like npm, pypi, [[Package Manager]]s for mcp
			- how do you determine whether it's sse or stdio
			- who built it, is it verified, did [[Shopify]] bless this server?
			- "this is coming, it's going to be great"
		- #### #Q can you give more examples of the server calling the client?
			- they don't yet have the ability to do server side "sampling" [[MCP/Sampling]]
				- [[Q/My]] what is sampling again here?
		- #### #Q does the model have to be in the loop with the LLM
			- someone
	- ## An official MCP registry API - why it's amazing?
		- cgpt
			- ## **An Official MCP Registry API**
			  
			  An MCP server registry helps make agents **self-evolving** by letting them discover and choose their own tools.
			- ### Workflow Example: Debugging with #Grafana
				- ```
				  pgsql
				  
				  CopyEdit
				  
				  User → "Fix the bug based on my Grafana logs"
				  ↓
				  Agent → Queries Grafana logs & suggests a fix
				  ↓
				  Agent → Searches for official Grafana server
				  ↓
				  Agent → Installs & invokes Grafana server
				  ↓
				  Registry API
				  ```
			- **Key Idea:** Agents can **autonomously** locate and use the necessary tools by querying the **MCP Registry API**.
			- Enables **adaptive AI workflows** where agents **evolve** based on available tools.
		- my #notes
			- agents can do their own discovery - agent will
	- ## Server discovery
		- ![image.png](../assets/image_1740243306243_0.png)
		- example - #Shopify
		- cgpt-notes
			- ## **Server Discovery with MCP**
			- ### **Workflow Example: Managing a Shopify Store**
			  
			  ```
			  pgsql
			  
			  CopyEdit
			  
			  User → "Help me manage my store on Shopify"
			  ↓
			  Agent → Checks if Shopify has a `.well-known/mcp.json`
			  ↓
			  Agent → Updates store on Shopify via Remote MCP server
			  ```
			- ### **Shopify MCP Server Metadata**
			  
			  ```
			  json
			  
			  CopyEdit
			  
			  {
			  "version": "1.0",
			  "servers": [
			    {
			      "id": "main-server",
			      "name": "Shopify Store Access",
			      "endpoint": "https://shopify.com/api/mcp",
			      "capabilities": ["resources", "tools"],
			      "authType": "oauth2"
			    },
			    {
			      "id": "admin-server",
			      "name": "Shopify Admin API",
			      "endpoint": "https://admin.shopify.com/api/mcp",
			      "capabilities": ["resources", "tools"],
			      "authType": "oauth2"
			    }
			  ],
			  "organization": {
			    "name": "Shopify"
			  },
			  "requirements": {
			    "minProtocolVersion": "0.5.0"
			  }
			  }
			  ```
			- ### **Key Features**
			- Uses **`.well-known/mcp.json`** for automatic **service discovery**.
			- Supports **OAuth2 authentication**.
			- Defines **multiple MCP endpoints** (`Store Access`, `Admin API`).
			- Ensures compatibility using **minProtocolVersion**.
		- registry is focused on discovery and ability to find tools from scratch
		- if you know you want to talk to shopify, it can check this [[MCP/.well-known]] - really nice complement to [[AI/Computer Use]].
		- what if you could have that PLUS MCP json (?)
			- didn't quite get this point
	- ## And a lot more
		- ![image.png](../assets/image_1740243402170_0.png)
		- cgpt notes
			- ## **And a lot more...**
			- **Long-lived vs short-lived connections**
			  Smooth upgrade from stateless to stateful capabilities
			- **Streaming**
			  Stream data from server to client
			- **Namespacing**
			  Prevent collisions between entities of multiple servers; create logical groups of servers or tools
			- **Elicitation**
			  Servers proactively request context from users
		- my #notes
			- in order of immediacy
			- they are using something like SSE
				- streaming -> stream data from server to client
			- elicitation -> "proctive" event behavior
				- better patterns for that.
- ## [[Q/My]]
	- how exactly do permission boundaries work with #MCP ? he mentions [[OAuth]] which has some concept of permission boundaries ...
		- cgpt
	-