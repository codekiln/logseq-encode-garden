# Block A — Agentic Futures - Internet of AI Agents
	- 13:45 [Block A — Agentic Futures - Internet of AI Agents](https://mitdecai.org/)
	- 10:30
		- Pioneer stage
			- The Future Internet of AI Agents and Why this is a New Frontier
				- [[Person/Ramesh Raskar]] [[MIT/Media Lab]] [Ramesh Raskar, MIT Media Lab, Camera Culture group, Cambridge MA, USA](https://web.media.mit.edu/~raskar/)
	- *1:45 – 2:45 PM – Bartos Theater(Toward the other side —look for signs)*
	- intro to [[NANDA]] https://nanda.media.mit.edu/
		- [[My Notes]]
			- how to create a nanda server
				- very similar to
				- they are using claude llm
				- they have a
			- [[NANDA/GitHub]]
				- https://github.com/aidecentralized
				- they have an [[SDK]]
				- it's a protocol layer
				- it's a registry (infrastructure layer)
					- reputation, rating, etc
				- it's a host
					- it's the only host that's out there works with mcp going forward
					- there will be many other hosts and many other search providers that will search for providers differently
					- or that can evaluate agents differently
					- they want to build an
		- main track -
			- 1 hour of deep dive presentations, then lightning talks. we have 30 posters, etc
			- • Chris Pease – AgentiCorp: Multi-Agent Systems (next 12 months)
			- 14:16 [[NANDA/Architecture]] Abhishek Singh – MIT Media Lab: Nanda Protocol, • Naman + Jon – NANDA Team: NANDA
			  collapsed:: true
				- [[My Notes]]
					- Tale of two species
					- what makes this possible is through things we have built
						- image -
					- 14:19 he talks about coupon protocol
					  collapsed:: true
						- taking inspiration from dns
						- there are practical challenges - we can't rely on existing structures
						- [[AI Notes]]
							-
							- ### **2:18 PM – Core Protocol Concepts**
							- **Unified client-server abstraction**:
								- In the agentic model, entities can act as **clients, servers, or both simultaneously**.
								- This enables fluid **agent-to-agent workflows** and simplifies interactions.
							- **Agent hyperlinking concept (“Google Protocol”)**:
								- Analogy: Hyperlinks connect fragmented web pages into the searchable web.
								- Proposal: Create a **hyperlink equivalent for agents**.
								- Solution: **Interaction coupons**.
									- **Coupons** are verifiable artifacts exchanged during agent interactions.
									- Serve as **traces** of communication and knowledge propagation.
									- Enable construction of **services**: search, reputation systems, transaction layers, etc.
							- **Agent registry system**:
								- Inspired by **DNS**, but with necessary extensions for agent use cases.
								- **Root zones**: Hosted by universities or major entities.
								- **Secondary/tertiary zones**: Open to any org; can be private/internal.
									- Example: A company can run a private registry for its agents.
									- These registries allow **localized queries and lookups**.
							- **Practical deployment tip**:
								- Reference to **Google’s 8.8.8 DNS**: fast and commonly used.
								- Similar model possible for agent registries — public or private layers.
								- Actionable takeaway: You can host your own registry now via GitHub with a **single Docker command**.
						-
					- 14:22 [[NANDA]] demo again
						- it's stored in your browser storage
						- bakery tool is a nanda node
							- it's a host, a client and a server
							- they are talking about
						- every company is not just going to create an [[MCP Server]] but they will include [[LLMs]] that know about their domain
						- in the future it's all going to be done by agents
						- this is the infrastructure for that
			- ### 14:26 Encryptech
			  collapsed:: true
				- bring private data insights
				- ZK proofs ... ?
				- Our offerings
					- what is privacy preserving compute and what's the compliance energy really?
			- ### 14:29 navigating the intersection of autonomy, ethics, and human-ai collaboration with [[Person/Peeyush Aggarwal]] from [[Deloitte]]
			  collapsed:: true
				- [[My Notes]]
					- I talked to this speaker earlier today before 8am - we had a good discussion
					- financial services industry
			- ###  14:36 from [[Microsoft]] [[Person/Aditya Challapally]] – Microsoft: Edge AI
			  collapsed:: true
				- he leads a research team in partnership with [[OpenAI]]
				- it's a
			- ### 14:45 [[Tata/Consultancy Services]] - [[Person/Anil Sharma]] - • Anil Sharma – TCS: Human Intelligence + Decentralized Intelligence
			  collapsed:: true
				- [[My Notes]]
					- consistency of expertise and wisdom
			- ### 14:51 [[Person/Anna Kazlauskas]] - [[VANA]]
				- [[Person/Anna Kazlauskas]] [Anna Kazlauskas - LinkedIn](https://www.linkedin.com/in/annakaz/)
				- [[My Notes]]
					- if you export your instagram data it has stuff like "stressed but not depressed
				- [[Transcript]]
					- 2:50 pm presentations, we're kind of running into this realization, which is like AI models are really only as good as their training data. This is the GPT-3 training data. You'll notice most of it is public information on the Internet. If you posted on Reddit, you might have already helped train some of these models. Something a lot of people don't realize is that most training data is private, not public. So the public Internet represents less than 0.1% of the overall Internet data. And that's because most Internet data requires permissions or sign-in to access. Right? If you think about your Google Drive, your email, your iMessage, your photos, none of that is really scrapable on the public Internet. That sits inside of these different platforms that aren't necessarily available, so they're not used to training AI today. There's kind of this idea of the data wall in training AI models, which is that we're actually running out of training data to train AI on. If you look at the training data of WAMA-3, it's around 15 trillion tokens or words, and that's actually the same amount of data as the whole public Internet. So people might be familiar with Common Crawl. FineWeb is the subset of Common Crawl, which is like high quality and deduplicated. That is 15 trillion words. Right? So one, it's impressive that we've trained AI on literally everything on the public Internet, but if we want to build better AI, we need someplace to actually get better data. Companies have realized that their data is really valuable in this AI age, and they've kind of locked down access to it. Right? So you have Reddit earning 200 million dollars from selling data just for AI training. Photobucket, one to two dollars an image. Apple's buying data for 50 million dollars. And we're kind of in this situation where the Internet is becoming less and less open. Maybe people remember Stack Overflow or Reddit. They made API changes to make it harder to get their data out, and that's because that allows them to kind of charge more money for the data. Something that a lot of people don't realize is that users still have access to their data. Right? So in the same way that when you park your car in a parking lot, the parking lot doesn't own your car. Right? They can't take your wheels. They can't do random things to your car. It's still legally yours. You go and get it back. That's actually the same thing as when you put your data in a platform. Right? And this is very counter to what most people think of as data. You might think, oh, it's Facebook's data, or oh, it's Twitter's data, but actually the default is it's yours, and then you can grant access. You do end up granting some permissive access when you check the kind of terms of service. So that's true for every data set from Tesla to Amazon to Instagram. Instagram is actually one I recommend you go explore your data. They give you not just the kind of posts and images that you posted, but they even include the like AI predictions that they've made about you, and it's a list of like 300 things. One of the things I found in the list they had predicted about me was stressed but not depressed. It's just like actually hilarious, so highly recommend you explore your Instagram data. So what VANA does is it really unlocks data from walled gardens and puts it in users control. Right? So you have these walled gardens which are kind of coming up around each platform, so VANA has each individual user export their data and put it into these different kind of data pools so that it's available and actually controlled by them. Some of the core concepts that make VANA possible are one, non-custodial data. What that means is in the same way that you use a crypto wallet to manage access to like your Bitcoin or your Ethereum, you're kind of acting as your own bank. With VANA, you are your own bank.
				- [[AI Notes]]
					-
					- ### **Anna Kazlauskas (Vana) – The Case for Data Sovereignty**
					- **Training data bottleneck**:
						- *“AI is only as good as its training data.”*
						- GPT-3 was trained on mostly **public** web data — Reddit, Common Crawl, etc.
						- But **public data = <0.1% of internet data** — the rest is behind logins, permissions, or paywalls (e.g., Google Drive, iMessages, photos).
						- AI is **hitting a wall**: models like WAMA-3 already trained on **all of public web** (~15T tokens).
					- **Market shift**:
						- Companies now realize the **monetary value of data**:
							- Reddit: $200M from licensing
							- Photobucket: $1–2 per image
							- Apple: $50M data deal
						- Platforms like Stack Overflow and Reddit have **restricted APIs** to increase pricing leverage.
					- **Legal & philosophical stance**:
						- *“Your data is like your car in a parking lot — it’s yours, not the platform’s.”*
						- Legally, **you own your data**, even when stored on Facebook, Twitter, etc.
						- Platforms **borrow usage rights**, but **you retain ownership**.
						- Example: Instagram lets users download their data — includes AI predictions (e.g., “stressed but not depressed”).
					- **What Vana enables**:
						- **User-driven data export** from platforms
						- **User-controlled data pools**
						- Empowers training on data that’s:
							- **Non-custodial** (like a crypto wallet — you hold the keys)
							- **Portable, sovereign, verifiable**
							  
							  > Vana proposes a world where AI is powered by **consensual, high-quality private data** instead of scraping the public web — with users at the center of value and control.
				- [[My Notes]]
					- 14:56 [[Data/DAO]]s
					- builder workshop at 4:30 pm
			- ### 14:59 [[Person/Marco Cello]] – [[Meshify]] : Agents for SME Operations
				- This is part of [[ScaleUpLabs]] https://www.scaleuplabs.vc/
			- ### 15:00 • Person/Gauri Gupta – Parallel Web Systems: AI Agents Future landscape
			  collapsed:: true
				- [[AI Notes]]
					- ### **Gauri Gupta (MIT Media Lab, Parallel Web Systems) – **
					- ### **Agentic AI: Hype, Current & Future**
					- **Role**: Researcher at MIT Media Lab, focusing on distributed systems and AI agents.
					- **Session focus**: A critical and forward-looking lens on the evolution of *Agentic AI*:
						- What’s **real** vs. **hype**
						- What’s **possible now**
						- What’s **coming next**
					- **Presentation tone**: Framing a grounded, research-driven perspective on the agent discourse that spans across:
						- Technical readiness
						- Human-AI collaboration models
						- Infrastructure and orchestration limits
						- Cultural and systemic adoption curves
						  
						  > Gauri’s perspective is positioned to blend deep technical insight with systems-level thinking—setting the stage for reflective discussion on where agentic AI is truly headed.
				- 3:03 [[Transcript]]
					- 3:03 pm Imagine one agent that's doing go-to-market research, another agent is writing code and building the product, the third agent might be writing some demo videos or demo code for you. All these agents now learn to collaborate in real-time, communicate and talk to each other, and solve these complex tasks. While we imagine this future, there are some key challenging problems that we need to solve. So I'll go over three important pillars that we are interested in solving and we have done some work around it. So the first one is protocol layer. How are these agents interacting with each other? Now we have seen multiple agent-to-agent protocols coming, we have seen MCB, A2A, and a brilliant work from our lab, a lambda protocol that you have all heard about today. But the other important protocol that we need to design is how are agents interacting with data? Can we define some agent-to-agent interaction protocols? Just like we had some robots.txt for each website, right? So we need to rethink on this protocol layer, how are we making these protocols that these agents are interacting with tools, data, and other agents that exist out there in the world. The second is intelligence attribution. Now the agents are becoming more and more intelligent as they are collaborating with other agents, resources, tools, etc. How do we ground the research that the agent has done so far? We have seen citations and excerpts are one way. But while agents are doing these complex research, how do we assign the...
				-
			- ### 15:06 • [[Person/Raghu Bala]] – [[SynergeticsAI]]: Agent Registries (AgentWorks Platform)
				- agentic maturity model
					- published on
			- ### 15:11 • [[Person/William Lindskog-Munzing]] – [[Flower Labs]]: Federated Learning
				- [[My Notes]]
					- data is naturally siloed and decentralized. AI can't use it
			- ### 15:17 • [[Person/Cameron Dennis]] – NEAR AI: Private Agent Cloud
				-
		- • Peeyush Aggarwal – Deloitte: Data Across Silos
		  • Vlad Larin – Fortytwo: Planetary-Scale Intelligence
		  • John Donaghy – Gensyn: Network Protocol
		  • Phil McMannis – Beacon Protocol: Private Data Networks
		  • Ayush Chopra – Camera Culture: Large Population Models
		  • Richard Blythman – Naptha: Framework for Multi-Agent Systems
		  • Gabriela Torres – Sundai: A2A Payments (Radius × Sundai)