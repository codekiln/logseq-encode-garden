logseq-entity:: [[Logseq/Entity/Podcast/Episode]], [[Logseq/Entity/YouTube]]
created-by:: [[Person/Jan-Niklas Wortmann]]
date-created:: [[2026-06-12 Fri]]

- # [Code Isn't Free - Mario Zechner on the Hard Truths of Coding With AI](https://www.wordman.dev/podcast/mario-zechner-pi-coding-agent/)
	- An episode of [[Person/Jan-Niklas Wortmann/Pod]], with guest [[Person/Mario Zechner]].
	- On Snipd and Apple Podcasts the episode is titled Faster Isn't Better — Mario Zechner on Everything AI Made Us Forget.
	- ## Overview
		- [[Person/Mario Zechner]] on building [[PiAI]] so it fits a workflow instead of the other way around, why [[Claude/Code]] stopped fitting his, local models on ordinary hardware, and why agent-written code still sends a bill.
	- ## Sources
		- [Episode page](https://www.wordman.dev/podcast/mario-zechner-pi-coding-agent/)
		- [YouTube recording](https://www.youtube.com/watch?v=GhjU-KvXtT0)
		- [Snipd episode](https://share.snipd.com/episode/7918cdcd-ce95-4875-8062-3861c5061c79)
		- Transcript excerpts are [[Snipd]]'s machine transcription, with a few misheard names corrected. Times are video seconds.
	- ## Video
		- {{video https://www.youtube.com/watch?v=GhjU-KvXtT0}}
			- ### {{youtube-timestamp 0}} Intro
			  collapsed:: true
			- ### {{youtube-timestamp 140}} Why Pi Fits Workflows
				- #### {{youtube-timestamp 211}} Agents Break When They Change Your Workflow
					- Snipd: https://share.snipd.com/snip/67d83a92-008e-4da2-b87a-437839b4d1de
					- Coding agents must fit developer workflows or they become unusable quickly.
					- Mario left Claude Code because frequent hidden harness changes broke his prompt templates and stability expectations.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- Agents.
						- [[Person/Jan-Niklas Wortmann]]
							- I've heard a little bit on the backstory that you basically tried a couple other coding agents and didn't really like any of them out there. So you felt like this developer itch of like, oh, I can do better.
						- [[Person/Mario Zechner]]
							- Would you admire that attitude obviously we we we all usually suffer from not invented here syndrome but honestly initially i was super happy with Claude Code it just over time didn't Fit my workflows anymore and i had no way to to change that um because Claude doesn't let me do the things I need to do for it to fit my workflows. That was basically the reason.
						- [[Person/Jan-Niklas Wortmann]]
							- That is actually the thing that I'm so much more interested in like benchmarks and those kind of things. I think we're now at this early stage of AI development where talking about workflows is like the interesting, at least for me interesting. So when you say it didn't fit your workflow, what do you mean with that?
						- [[Person/Mario Zechner]]
							- They have a very high frequency release cadence, which means you get one, two, three releases per day even sometimes. And with all of these releases come changes to things like the tool definitions, the system prompt and so on and so forth. So if I have a bunch of, say prompt templates or slash commands or whatever you say, or skills even, or I have workflow descriptions that the model is supposed to follow and the changes To the system prompt and tool definitions mess around with that, so my workflows don't work anymore, defined in prompt templates, then that is bad. If the model becomes dumber because they are injecting system reminders left and right behind your back that are not surfaced to the user interface and i am wondering why the fuck the Model doesn't behave anymore like it behaved yesterday even though it's the same model supposedly then that is bad so i i'm a developer i like my tools to be stable and Claude Code is not Something that is very stable, which doesn't mean it's bad. Obviously, it's not like millions of people use it productively. So more
				- #### {{youtube-timestamp 394}} Coding Agent Preferences Are Mostly Vibes
					- Snipd: https://share.snipd.com/snip/9e187410-fc91-4b18-9ffc-bf78a5b4e16a
					- Developers often justify tool preferences with concrete reasons, but coding-agent choices increasingly come down to how the interaction feels.
					- Mario compares this to preferring SolidJS over React because its abstractions fit his brain better, not because React is inferior.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- I think this is mind-blowing to me to be super honest because like usually developers have like very valid reasons of why they like tool y more than tool x most of the time i feel i can give You which is now completely obsolete but i don't think there's oh really no i could give you like exact reasons of why i like uh my ide more than vs code i could give you a reason why i preferred
						- [[Person/Mario Zechner]]
							- Angular over react why sure but you will always find people in the opposite camp that's that's my point so if it were objectively if it were objectively measurable if something is better
						- [[Person/Jan-Niklas Wortmann]]
							- Than something else then there wouldn't be camps right but that's true but usually they have like reasons whereas like i feel like this conversation between like what coding agents Is usually like it feels right or and like also when i look at models like it's it's so much vibe based based on like how i talk to the model and how i feel it responds to me but i think that's
						- [[Person/Mario Zechner]]
							- Kind of similar to when you prefer a specific abstraction over a different abstraction like if you have for example solid js versus react um kind of doing this a similar thing just entirely Different yeah i personally i'm a solid guy i i love solid it's it's
			- ### {{youtube-timestamp 533}} What Success Looks Like for Pi
			  collapsed:: true
			- ### {{youtube-timestamp 658}} Building Beyond the Coding Agent
			  collapsed:: true
			- ### {{youtube-timestamp 793}} Local AI Is Getting Real
				- #### {{youtube-timestamp 794}} Small Local Models Are Already Good Enough
					- Snipd: https://share.snipd.com/snip/cbeb5efc-1fd4-44d4-b76e-98977925d672
					- Small local models can handle real-world applications without expensive hardware.
					- Mario’s robot runs a chatbot with motors and a camera that is fast and effective for children.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- Would be curious to talk about that a little bit more because in the AI scene, even though everything kind of like... Feels like saying it like that um every conversation that i see is like everyone wants local ai but it's just not nowhere consumer ready and with consumer already i mean already like
						- [[Person/Mario Zechner]]
							- Developers who are like uh ready to uh crap like mess with it what is your experience yeah i mean that is definitely true um and i'm not even talking about the local model quality the setup Alone and the cost involved is still usually not worth it like if you actually buy a beefy i don't know dgx station workstation that costs you 100k that's a single b300 with i think 500 Or 700 gigabytes of vram that's beefy and you can run a really good model on that um but nobody has the money for that so um ultimately so i've been playing for this i've been for this robot I've been playing around with smaller months gamma 4 and quen 3.6 I think. Some mixture of experts model. And you, I didn't believe it, but for this application, a chatbot with motor and camera that is being talked to by a kid, they're more than perfectly fine. Like they're actually really, really good and really, really fast.
				- #### {{youtube-timestamp 824}} Local Models Are Practical For Many Uses
					- Snipd: https://share.snipd.com/snip/6cdafcec-670d-49ec-bb4e-b3a803a12075
					- Local inference on a regular Mac is nearer than people think for many real tasks.
					- Mario runs Qwen 3.6 and speech models on an M1 with ~14GB unified memory to power a local robot chatbot for kids.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- I mean that is definitely true um and i'm not even talking about the local model quality the setup alone and the cost involved is still usually not worth it like if you actually buy a beefy I don't know dgx station workstation that costs you 100k that's a single b300 with i think 500 or 700 gigabytes of vram that's beefy and you can run a really good model on that um but nobody Has the money for that so um ultimately so i've been playing for this i've been for this robot i've been playing around with smaller months gamma 4 and quen 3.6 I think. Some mixture of experts model. And you, I didn't believe it, but for this application, a chatbot with motor and camera that is being talked to by a kid, they're more than perfectly fine. Like they're actually really, really good and really, really fast. And I think there's a lot of applications out there that are not just toys, but also real world tasks that could be served by these models today and you do not need need hardware that's That's that's expensive like this thing runs on a run-of macbook m1 for example not even a beefed out one with 32 gigs and there's uh the speech to text with um parakeet um text-to with Qen3 uh tts those take about 10 gigabytes yeah and then i have qen3 whatever 3.6 which takes another 4 gigabytes so for 14 gigabytes of unified memory on macOS or an equivalent NVIDIA Setup on Windows, I could have a pretty good local inference machine. And that is affordable. Again, not for the entire world, obviously, but for a lot of people. And you also see a bunch of companies pushing in that direction. Like Google is really, really big on edge inference.
				- #### {{youtube-timestamp 887}} Small Models Make Local AI Affordable
					- Snipd: https://share.snipd.com/snip/a1c86678-b756-455a-bd77-3f4edc0b62ab
					- Smaller models can handle real-world tasks, not just toys, without expensive hardware.
					- A MacBook M1 with 14GB of unified memory can run speech, text, and vision models locally.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- And I think there's a lot of applications out there that are not just toys, but also real world tasks that could be served by these models today and you do not need need hardware that's That's that's expensive like this thing runs on a run-of macbook m1 for example not even a beefed out one with 32 gigs and there's uh the speech to text with um parakeet um text-to with Qen3 uh tts those take about 10 gigabytes yeah and then i have qen3 whatever 3.6 which takes another 4 gigabytes so for 14 gigabytes of unified memory on macOS or an equivalent NVIDIA Setup on Windows, I could have a pretty good local inference machine. And that is affordable. Again, not for the entire world, obviously, but for a lot of people. And you also see a bunch of companies pushing in that direction. Like Google is really, really big on edge inference.
						- [[Person/Jan-Niklas Wortmann]]
							- And I like that do you think we will see a rise in the smaller models um and in that so we at jet brains we have been doing the uh so basically we ship like tiny models that can literally just Do like css autocompletion it's completely offline and it doesn't work if you have like a big ass project. But for like completing tailwind classes, which I'm at least not capable of remembering all the fucking time, this is nice.
				- #### {{youtube-timestamp 975}} Smaller Models Can Preserve Frontier Quality
					- Snipd: https://share.snipd.com/snip/cc268f60-2b8a-4758-a3ac-e11aebac85d0
					- Mario expects today’s gigantic models can be distilled into much smaller systems without significant quality loss.
					- He cites DeepMind’s Denis Asaves and distinguishes training large models from deploying compact ones.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- So I'm wondering, do you think there will be, we will see a shift from these frontier models, which are like massively big? If we're being realistic, also for a lot of these things, like so I, with my microphone, I had a delay so i was trying to troubleshoot that with claude because i'm just too stupid for audio Video stuff you have clearly said uh seen before this recording that i failed because i'm my old microphone again so but like if we're being realistic for these kind of scenarios big Ass models like Claude are completely overkill. Do you think we will see a rise in small expert, very specially trained? And to some extent, we already see this with like examples, as you mentioned, like text to speech, where it's just like, this is just one thing that you're doing.
						- [[Person/Mario Zechner]]
							- I'm not involved in model training, so I can't speak from expertise, but what I'm hearing... Not here, man. Maybe, no. If you listen to people like Denis Asaves, for example, from DeepMind, his thoughts are that the current gigantic models actually don't need all these parameters they have, and that You can actually distill that down to much much much smaller models without losing a lot of output quality so my hope not my
				- #### {{youtube-timestamp 1032}} Distilling Giant Models Into Local Powerhouses
					- Snipd: https://share.snipd.com/snip/cd363eb4-6a63-4a0d-abe1-37d4f66500ff
					- Large models may be necessary for training, but distillation can preserve most capabilities in models an order of magnitude smaller.
					- Mario expects local models to match big-model performance, citing DeepSig V4 running on a 128-gigabyte laptop.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- If you listen to people like Denis Asaves, for example, from DeepMind, his thoughts are that the current gigantic models actually don't need all these parameters they have, and that You can actually distill that down to much much much smaller models without losing a lot of output quality so my hope not my my let's say uh knowledge is that um this is the future we try To take these we will always train no sorry not not speaking in absolute at least as i understand it we do have to train these big models for various reasons related to how training works And so on and so forth but once you have such a big model you can distill it rather easily down to something that's an order of magnitude or more smaller while still retaining most of the Capabilities and my hope is that we are heading to a future where we don't necessarily have specialized models. I don't think specialized models, I think they can be a band-aid for now if you want to kind of be sovereign and have some small tasks. But ultimately you want the same bang for the buck that you get for a big model locally. And I think we are very close to that, actually. Antiras from Redis, Salvatore, he started working on a very custom Influence engine just for DeepSig V4 called DS4C.
			- ### {{youtube-timestamp 1213}} How Mario Actually Works
				- #### {{youtube-timestamp 1222}} Use AI Agents As Rubber Ducks
					- Snipd: https://share.snipd.com/snip/875690d3-0733-4a60-9a93-1bb778e88962
					- Mario parallelizes issue analysis across sessions, then personally reviews code, tests hard cases, and iterates with the agent.
					- This back-and-forth creates guardrails around interfaces, modules, and tests before implementation.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- How do you work on features for Pi? How is your day structured in that sense?
						- [[Person/Mario Zechner]]
							- I'm an absolute caveman. There are two types of tasks I have. The first task is going through the issue tracker and picking off things that need to be fixed or implemented. These usually have an issue that is descriptive enough that I can give it to my agent with an additional prompt template that says, pull down all the information from this issue, including Any reference code, any reference pull requests, and so on and so forth. Ignore the analysis in the issue and do your own analysis based on the goals that we want to achieve here with this issue. Then i usually get a pretty good analysis of what this issue is about and options on how we could fix it either by pulling in a pull request that already exists or taking what's in there And modifying it or doing a from scratch implementation of fix and this analysis step usually per issue takes like five minutes for the llm for the agent to kind of go through so i queue One of these in one session. I open a second session, pull in the next issue. I open a third session, pull in the next issue and have kind of like a parallel pre-processing of all the issues I want to work on today. And then I just go to each session and check what the agent suggested, go into the code myself, ensure it makes sense, try to reproduce things manually if they're hard to test automatically And then it's just a classic back and forth until i agree with myself
				- #### {{youtube-timestamp 1229}} Preprocess Issues In Parallel Then Review Sequentially
					- Snipd: https://share.snipd.com/snip/1c8f7b6e-d8ba-4df0-af11-2e7015738583
					- Use one agent as a focused collaborator and pre-process multiple issues in parallel, then review sequentially.
					- Mario opens multiple sessions to queue analysis, inspects agent proposals, reproduces issues manually, then iterates like a human reviewer.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- I'm an absolute caveman. There are two types of tasks I have. The first task is going through the issue tracker and picking off things that need to be fixed or implemented. These usually have an issue that is descriptive enough that I can give it to my agent with an additional prompt template that says, pull down all the information from this issue, including Any reference code, any reference pull requests, and so on and so forth. Ignore the analysis in the issue and do your own analysis based on the goals that we want to achieve here with this issue. Then i usually get a pretty good analysis of what this issue is about and options on how we could fix it either by pulling in a pull request that already exists or taking what's in there And modifying it or doing a from scratch implementation of fix and this analysis step usually per issue takes like five minutes for the llm for the agent to kind of go through so i queue One of these in one session. I open a second session, pull in the next issue. I open a third session, pull in the next issue and have kind of like a parallel pre-processing of all the issues I want to work on today. And then I just go to each session and check what the agent suggested, go into the code myself, ensure it makes sense, try to reproduce things manually if they're hard to test automatically And then it's just a classic back and forth until i agree with myself using the agent as a rubber duck that this is the way i want to implement this and at that point the the context usually Already contains so much so many guardrails in terms of what will the interfaces look like, which specific modules will we modify, which tests will we write, and how should they work Exactly. Because just telling your agent to write tests is never a good idea. Yeah, at least, so at the end of this process of an analysis planning, I just say, go implement. And once it starts implementing which also takes another 10 to 30 minutes depending on what it is I do the same in the next session and once something pings and says I'm done I have a little Pie extension where I can basically pull up a diff of all the changes that were made and annotate individual lines inside that diff viewer with feedback. And then I click finish review. It gets fed back into the agent automatically. And that's how I iterate on the thing until I think the code is good.
				- #### {{youtube-timestamp 1346}} AI Coding Shifts From Review To Trust
					- Snipd: https://share.snipd.com/snip/0b170e34-dd66-4de2-8289-f4cf28c84a7d
					- Mario reviews core mechanics line by line but ignores generated code for simpler projects when he can specify the goal precisely.
					- He compensates with extensive manual testing, effectively trading code comprehension for speed.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- And once it starts implementing which also takes another 10 to 30 minutes depending on what it is I do the same in the next session and once something pings and says I'm done I have a little Pie extension where I can basically pull up a diff of all the changes that were made and annotate individual lines inside that diff viewer with feedback. And then I click finish review. It gets fed back into the agent automatically. And that's how I iterate on the thing until I think the code is good. For some pieces of code, I don't care. I just say fine. For other pieces, specifically core mechanics, I usually review every change that's being made like i would with a human and that that's the one thing that's that's like my day-to thing Fixing bugs and features and then there are other tasks like refactoring and building new things um for building new things i just slop camera Like this robot thing, the software for The robot thingy is not super complicated, but it has complexity already because the speech to speech pipeline has many services that need to get involved. I actually took the Python MLX implementations and converted them to Rust last night. Because I hate Python as a dependency and I want to have a single package people can download onto their Mac or onto their Windows machine with an NVIDIA card and just start it and have Everything running out of the box.
				- #### {{youtube-timestamp 1486}} Feel Out APIs Before Letting Agents Refactor
					- Snipd: https://share.snipd.com/snip/36022665-c99c-496a-839b-f9fad853fec7
					- Mario uses agents to explain code and propose module boundaries, but manually tests whether an interface and API actually feel right.
					- For the robot, he extracted 500 lines from a 3,000-line file only after validating the refactoring plan by hand.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- Fundamental so you can extend it more easily in the future you gotta go in and vibe refactor your vibe stop and there's two ways to do it you take what you learned and just build from scratch Or you start picking off individual refactoring tasks from this ball of vibe stop and that is what i did for the robot and the way i do this is i go in and read it myself or i let the agent explain To me how things work in specific parts of the code base for the robot it was basically two files one 3 000 lines of code file called server.ts and another 3 000 lines of code file called Client.ts that runs in the browser and yeah you can imagine that wasn't fun. But I basically just started like I would manually pulling things out into individual modules, defining interfaces, boundaries, and those I define by hand. I would, for example, I can ask the agent to propose a bunch of options for an interface or a module boundary. Then I take one or I let it write example apps or tiny little scripts where I can go in and manually feel how the interface, I still need to be kind of in the code to feel if an interface feels Good, if an API feels good. So I let the agent write the examples. I go in and play around with it. And if I like it, that becomes my plan basically. But yeah, that's the refactoring work. I use the agent to explain what exists. I use the agent to write options for how that could be refactored. Then I go in manually and kind of feel things out by typing up a little code or using the API myself by hand.
				- #### {{youtube-timestamp 1528}} Let Agents Propose Refactors But Validate By Hand
					- Snipd: https://share.snipd.com/snip/2ccae87a-6d13-4872-b904-541baf9bb799
					- Use agents to draft refactor options but validate interfaces by hand with small example apps.
					- Mario has agents propose module boundaries, then writes tiny scripts and manually 'feel' the API before accepting it.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- But I basically just started like I would manually pulling things out into individual modules, defining interfaces, boundaries, and those I define by hand. I would, for example, I can ask the agent to propose a bunch of options for an interface or a module boundary. Then I take one or I let it write example apps or tiny little scripts where I can go in and manually feel how the interface, I still need to be kind of in the code to feel if an interface feels Good, if an API feels good. So I let the agent write the examples. I go in and play around with it. And if I like it, that becomes my plan basically. But yeah, that's the refactoring work. I use the agent to explain what exists. I use the agent to write options for how that could be refactored. Then I go in manually and kind of feel things out by typing up a little code or using the API myself by hand.
			- ### {{youtube-timestamp 1598}} Discipline, Atrophy, and Juniors
				- #### {{youtube-timestamp 1606}} AI Coding Risks Atrophy And Lost Agency
					- Snipd: https://share.snipd.com/snip/5091cac1-7b5c-4345-a0b2-c6eeb557cd2f
					- Mario warns that delegating everything to agents can erode discipline, agency, and programming ability.
					- He repeatedly ends up in a corner crying when the machine’s output leaves everything falling apart.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- And I assume it's similar for you because i have 10 plus years of experience working in the nitty-gritty details of a code base having that manual experience um also learning by heart Learning the hard way what works and what doesn't work uh every developer i know has patterns that they would absolutely not do again because they tried it once thought it was great and It turned out to be horrible how do you think this will develop moving forward for people that are now just coming out of college i honestly don't know like if i were if i were a kid today
						- [[Person/Mario Zechner]]
							- I if I were an actual kid today, like I used to be in the 90s, right? When I started programming. I would probably not learn programming. I would probably just ask an agent to write me a program. I mean, we already see this at schools. Kids use GPT to do the homework. And I would have done that as well because i hate fucking homework fuck that um so i'm i'm not sure i don't know so for the young people um good luck my condolences for for old people like Us um they are definitely agents are definitely a force multiplier but there is a risk of atrophy and a risk of loss of discipline and agency that's something
				- #### {{youtube-timestamp 1628}} AI Coding Risks Atrophy and Loss of Agency
					- Snipd: https://share.snipd.com/snip/30d77239-9642-42fb-9ce8-97842d76c034
					- Mario warns that delegating everything to coding agents can erode discipline, agency, and understanding.
					- He repeatedly ends up “in a corner crying” when delegated work leaves him with brittle, unusable software.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- Patterns that they would absolutely not do again because they tried it once thought it was great and it turned out to be horrible how do you think this will develop moving forward for
						- [[Person/Mario Zechner]]
							- People that are now just coming out of college i honestly don't know like if i were if i were a kid today i if I were an actual kid today, like I used to be in the 90s, right? When I started programming. I would probably not learn programming. I would probably just ask an agent to write me a program. I mean, we already see this at schools. Kids use GPT to do the homework. And I would have done that as well because i hate fucking homework fuck that um so i'm i'm not sure i don't know so for the young people um good luck my condolences for for old people like Us um they are definitely agents are definitely a force multiplier but there is a risk of atrophy and a risk of loss of discipline and agency that's something i have struggled with as Well over the last year or two um just finding the discipline to not delegate all the things to the machine because inevitably every time i do this i end up in a corner crying because nothing Is good anymore and everything falls apart.
				- #### {{youtube-timestamp 1657}} Enterprise Vibe Coding Is Still Vibe Coding
					- Snipd: https://share.snipd.com/snip/0aba2f2e-5869-4a16-9453-21a87333e13b
					- Detailed specifications do not fundamentally change delegation-first coding.
					- Enterprise developers formalize the prompt, while vibe coders dictate the app directly.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- I would probably just ask an agent to write me a program. I mean, we already see this at schools. Kids use GPT to do the homework. And I would have done that as well because i hate fucking homework fuck that um so i'm i'm not sure i don't know so for the young people um good luck my condolences for for old people like Us um they are definitely agents are definitely a force multiplier but there is a risk of atrophy and a risk of loss of discipline and agency that's something i have struggled with as Well over the last year or two um just finding the discipline to not delegate all the things to the machine because inevitably every time i do this i end up in a corner crying because nothing Is good anymore and everything falls apart.
						- [[Person/Jan-Niklas Wortmann]]
							- That is also the biggest issue that I have with this narrative. I've seen this a couple times online where it's like, well, we have too much code now. We cannot review it anymore. Where I'm like, well, then how are you expecting to maintain it if you cannot read it? That doesn't make any sense what you're saying. That is just a little bit more sophisticated approach to vibe coding, but not much.
						- [[Person/Mario Zechner]]
							- Exactly. That's basically, it's like the vibe coder will just sit there with his voice dictation app and dictate what app they want at a very high level. And the enterprise vibe coder will first write a very detailed spec.
				- #### {{youtube-timestamp 1709}} AI Coding Revives Waterfall Development
					- Snipd: https://share.snipd.com/snip/a84d9837-12fb-4461-941b-3b67684284a7
					- Spec-driven AI coding can recreate waterfall development, replacing iterative understanding with a detailed prompt handed to an agent.
					- Software teams abandoned waterfall decades ago because it fails, yet AI hype is bringing back an even more rigid version.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- That is also the biggest issue that I have with this narrative. I've seen this a couple times online where it's like, well, we have too much code now. We cannot review it anymore. Where I'm like, well, then how are you expecting to maintain it if you cannot read it? That doesn't make any sense what you're saying. That is just a little bit more sophisticated approach to vibe coding, but not much.
						- [[Person/Mario Zechner]]
							- Exactly. That's basically, it's like the vibe coder will just sit there with his voice dictation app and dictate what app they want at a very high level. And the enterprise vibe coder will first write a very detailed spec. But essentially, it's the same fucking thing.
						- [[Person/Jan-Niklas Wortmann]]
							- I had a little bit of like a ram i think it was like two weeks ago where i was like i don't get why people are doing spec driven development i either it just doesn't click with with me or it's Like my way of working doesn't work but but like i i have struggled to get meaningful information from business people for ever what is now different like there's no reasonable way that I could write a complete prompt that that even like i could give this to another developer and they would develop it flawlessly neither a coding agent doesn't make any sense to me no yeah
						- [[Person/Mario Zechner]]
							- It's crazy it's like we forgot the lessons of the last 30 years.
						- [[Person/Jan-Niklas Wortmann]]
							- I mean, we literally introduced Scrum. Some people...
						- [[Person/Mario Zechner]]
							- Yeah, whatever, yeah. 30 years ago or 20, 25 years ago. No, actually, it's fucking 30 years ago. Holy shit.
			- ### {{youtube-timestamp 1748}} Spec-Driven Dev Is Just Hyper-Waterfall
				- #### {{youtube-timestamp 1788}} Spec Driven Agents Recreate Hyper Waterfall
					- Snipd: https://share.snipd.com/snip/151f4b55-f84e-4060-832f-f2ccee806744
					- Spec-driven agent development recreates hyper-waterfall: faster but hides the same design failures.
					- Mario warns that prompting an agent to write detailed specs hands off design and results in brittle code produced from internet garbage.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- Mean, we literally introduced Scrum. Some people...
						- [[Person/Mario Zechner]]
							- Yeah, whatever, yeah. 30 years ago or 20, 25 years ago. No, actually, it's fucking 30 years ago. Holy shit. People figured out that waterfall is bad. Waterfall doesn't work. And now we're back to hyper waterfall where you kind of... It's faster. And it's worse because now you're not even writing the spec anymore you just vibe prompt your agent to write a very detailed spec and that's like a tower of turtles yeah that's completely Ridiculous but i mean there's a counter argument to that and the counter argument is that since code is now essentially free and since iteration times are quicker, like previously, If you wrote a waterfall spec and had a team of engineers implement that, your turnaround time would have probably been months. Now it's maybe a day or even less, depending on the size of your spec. And then, so you just go in and manually test your way through this or whatever. And I can see the appeal of that. I have yet to find evidence that this actually works for production software. I have my reservations. But I'm not ruling out that there is some magician out there who can actually make that work and not wake up eventually and just try at night because everything is fucking broken now. I
				- #### {{youtube-timestamp 1891}} Agents Fill Spec Gaps With Internet Garbage
					- Snipd: https://share.snipd.com/snip/4329ecb2-0a28-4d49-ba75-a13416bc520f
					- Natural-language specs leave architectural gaps that agents must fill when translating prose into code.
					- Mario argues those gaps get filled with accumulated low-quality code patterns from the internet.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- And the reason for that is just that if you, if you, I've said this a million times now, I'm kind of sick of it, but if you're writing a spec, what is the most detailed spec you can actually Write? Like, what does that look like? The most detailed spec. It's basically your program, the program itself. Okay, so assuming you are not writing the program by hand because now you have agents, you're writing a human natural language prose-based spec. If you do that, the agent needs to translate that into architecture and code if you are not specifying any of that on the absolute highest detail level which is the program you are leaving Planks in your spec and the agent fills that out and the question is with what does the agent fill out the planks that you're leaving out in your spec with the garbage code that we put on The internet for the past 20 years so that is also exactly how a code base that's vibe coded or enterprise-wide coded with specs looks like it's very bad it's very bad so i i run an experiment
						- [[Person/Jan-Niklas Wortmann]]
							- So for full disclaimer i know nothing about cotton right everything in japanese runs from content I know nothing. I was probably more like a quota hire or something. I don't know. So when the Ralph loop was big, I was like, well, I should give this a try, right? Just to be like objective.
			- ### {{youtube-timestamp 2103}} Code Isn't Actually Free
				- #### {{youtube-timestamp 2109}} Quantity Of Code Delays The Cost
					- Snipd: https://share.snipd.com/snip/e500bbad-7581-4d1e-8c47-8a968346aaf3
					- Code is not actually free because quantity delays consequences that eventually arrive.
					- Mario saw teams generate ~500,000 lines with agents in a week and the resulting code created long-term pain, not savings.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- No. Because I don't.
						- [[Person/Mario Zechner]]
							- Okay. Because the consequences of your actions will eventually hit you. And if you think that any amount of code is good now, you just delayed the punishment. Because, like, I mean, I have seen people who shit out like 500,000 lines of code while a bunch of agents in a week. And guess what the outcome of that is? I have
				- #### {{youtube-timestamp 2250}} Agents Expand Exploration Not Replace Design
					- Snipd: https://share.snipd.com/snip/16adf380-dab5-4a9a-a70f-de9ad3e14006
					- Agents greatly speed up solution exploration but don't replace human design judgment.
					- Mario uses parallel agent experiments to see options fast, then chooses the best and iterates—thinking remains the bottleneck.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- You can actually explore things. And that is super valuable. Doesn't mean that the results of those explorations that are partially or fully written by agents are reusable, but you can get a feeling for the solution space and the solution you Want to have with agents way quicker, because you can tell a bunch of agents, go off and build it like this, build it like this, build it like this and then look at the results and that is
						- [[Person/Jan-Niklas Wortmann]]
							- What for me is the biggest productivity increase the thing that i also like is the asynchronous nature of this i can now give my agent a task to explore something evaluate something research, And go in a meeting because we still have meetings. We still need to talk to people and then come back. And at least if I have the mental capacity to like pick up on that, I can, I saved a little bit of like time in that space that I otherwise couldn't have used in any other way. But again, I don't see it realistically any near time soon that I'll spin up 10 agents and 10x my output in that sense.
						- [[Person/Mario Zechner]]
							- Well, I mean, the asynchronous nature is a benefit for some tasks. Like if you have a review agent or whatever, obviously you don't want to sit there and wait for the agent to finish its review. But if you do too much of that, at least for my old brain, it's like I probably need to start ketamine or something to get through having 20 agents running. It's the task switching. It's the context switching that's killing you. Previously, I could focus on two to three things a day at tops now on a good day i can go through 30 issues on pi fixing them and it is i couldn't do that before but i also only do this like once Or twice a month because after the day of doing that i'm so done with the world because my brain is just mush. The context switch is what kills you.
			- ### {{youtube-timestamp 2276}} Async Agents and Thinking Time
				- #### {{youtube-timestamp 2276}} Context Switching Is AI’s Hidden Productivity Cost
					- Snipd: https://share.snipd.com/snip/b554daa9-fd28-42f6-a3d0-23af315d45cd
					- Asynchronous agents can multiply output, but excessive parallel work makes task and context switching mentally exhausting.
					- Mario can fix 30 Pi issues in a day, yet does this only monthly because his brain feels like mush afterward.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- Thing that i also like is the asynchronous nature of this i can now give my agent a task to explore something evaluate something research, and go in a meeting because we still have meetings. We still need to talk to people and then come back. And at least if I have the mental capacity to like pick up on that, I can, I saved a little bit of like time in that space that I otherwise couldn't have used in any other way. But again, I don't see it realistically any near time soon that I'll spin up 10 agents and 10x my output in that sense.
						- [[Person/Mario Zechner]]
							- Well, I mean, the asynchronous nature is a benefit for some tasks. Like if you have a review agent or whatever, obviously you don't want to sit there and wait for the agent to finish its review. But if you do too much of that, at least for my old brain, it's like I probably need to start ketamine or something to get through having 20 agents running. It's the task switching. It's the context switching that's killing you. Previously, I could focus on two to three things a day at tops now on a good day i can go through 30 issues on pi fixing them and it is i couldn't do that before but i also only do this like once Or twice a month because after the day of doing that i'm so done with the world because my brain is just mush. The context switch is what kills you.
				- #### {{youtube-timestamp 2460}} AI Agents Cannot Quiet an Overactive Problem-Solving Brain
					- Snipd: https://share.snipd.com/snip/10b393cc-37dc-4ff0-bb7c-0250ea6de58e
					- Mario says agents have not changed his inability to stop thinking about an enticing problem, even after leaving work.
					- His brain can take an hour to let go after picking up his son from kindergarten, trapping him in a thinking loop.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- Otherwise i'm good to zone out like if i'm with my kids i i don't think necessarily about work or something or like a problem that faced me it when my mind is going idle like when i try to sleep Then i have that but like if i'm doing something and it can be as easy as like playing catch with the kids outside right how's that for you and now i'm wondering also do you think that will Change in such a workflow where you can like have someone like some kind of sparing partner in form of an ai so the the turning your brain off or or or stopping thinking about problems i've
						- [[Person/Mario Zechner]]
							- Never been good at that like i not good in the sense that you have been doing that all the time pre and post agents nothing changed for me with that in that regard because if i have something That is really enticing that is really capturing my attention um and say i work on that for four hours and then i i have to go because i need to pick up the boy from from kindergarten or something Like that it takes me about an hour for my brain to kind of let go of that of that problem and there's really nothing you can do about it it's super it sucks so i i would like to be able to just Step out and be like ah my brain is now uh all good but you know like the what's it called one of the superheroes in in the boys sage or so she would lobotomize herself just oh yeah yeah yeah Whenever she wants a little peace of mind and i i kind of wished i could do that because uh it sucks getting getting stuck in this thinking loop.
			- ### {{youtube-timestamp 2682}} Learning Without the Pain
				- #### {{youtube-timestamp 2784}} Use AI To Remove Friction That Does Not Teach You
					- Snipd: https://share.snipd.com/snip/fdd73c19-5630-4fd8-a65e-29ba3acf1cd9
					- AI agents can remove necessary friction from learning, but they are valuable when eliminating work that teaches you nothing.
					- Mario used Cursor to write MCU code while focusing on electronics, intervening only in performance-sensitive parts.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- And I would just have Cursor or later Claude Code write that code for me because I don't care. I only cared in performance sensitive parts where I would go in and just fix it up. So I used the agent to do stuff that is part of learning where I don't learn anything but that I still need to do to be able to learn the thing I actually want to learn. So there it's great because it removes a part of the friction that doesn't help me learn something. In terms of coding, it's hard because I'm so old and I have seen so many things and I don't learn a lot about coding anymore. I used to read a lot about software design and architecture and learn a lot of different APIs and build compilers and blah blah blah blah. I'm kind of tired. I don't think there's a lot in software that I still need to learn. At least I have no interest in learning any of the things. Like example TypeScript. There is now this big effect TS hype. I don't fucking care, man. Like, I understand the problem you're trying to solve. The way you're solving it is cute, but it doesn't matter. It's just fucking, it doesn't matter. So previously I would have slurped it up and kind of read all about it, tried it out. I don't't i'm just tired so i i don't have any i
			- ### {{youtube-timestamp 2953}} AI's Sloppy Software Wave
			  collapsed:: true
			- ### {{youtube-timestamp 3131}} GitHub Under Clanker Load
				- #### {{youtube-timestamp 3131}} GitHub’s Leadership Vacuum And Asia Move Hurt Reliability
					- Snipd: https://share.snipd.com/snip/a84a96b3-28a8-40b3-bc17-839b5fe92227
					- GitHub faces an AI-generated flood of issues, pull requests, and repositories, but its outages stem from deeper management and infrastructure problems.
					- Mario blames absent leadership and says reliability worsened after GitHub’s move to Asia.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- Tell me how you feel about GitHub.
						- [[Person/Mario Zechner]]
							- To be honest, GitHub is in a very strange situation. Like, Clankers are now submitting issues and pull requests en masse, creating repositories en masse without the human knowing, actually, that they're doing it. And GitHub gets the brunt of that and needs to just manage the info. It's really hard. So I don't think GitHub's outages are related to AI. Although I heard some things through the grapevine.
						- [[Person/Jan-Niklas Wortmann]]
							- I think, could Microsoft probably maintain GitHub a little bit better as a product? Probably, yes. Does it seem a little abandoned here and there? Also, yes.
						- [[Person/Mario Zechner]]
							- I mean, the guy who was the head of GitHub, he was just fucking off into the sunset and was like, I'm now head of, I don't know, Xbox, whatever. He didn't fucking care. He was like absent for months and shit was hitting the wall and he's like i exist i get a lot of money i don't know what the fuck i'm doing that's not good um but the kita people themselves Are actually very talented i think what's still killing them is the move to asia that since they started doing that move you can actually look at the outage history and you see once they Started going to asia or arsura whatever it's called, it's not been pretty.
						- [[Person/Jan-Niklas Wortmann]]
							- So one thing I would be curious to touch on with you, and you can tell me to go fuck myself,
			- ### {{youtube-timestamp 3211}} Family, Work, and Balance
			  collapsed:: true
			- ### {{youtube-timestamp 3425}} The Pi Team and Leadership
			  collapsed:: true
			- ### {{youtube-timestamp 3532}} Refactoring Pi's Core
			  collapsed:: true
			- ### {{youtube-timestamp 3812}} Security, YOLO, and Trust
				- #### {{youtube-timestamp 3813}} YOLO Mode Forces Security Awareness
					- Snipd: https://share.snipd.com/snip/a3936837-4d20-4332-b176-e747c6da167a
					- Mario makes Pi’s default YOLO mode intentionally uncomfortable so users think seriously about agent security.
					- Instead of built-in permissions, users must design safeguards suited to their own environment.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- I wanted to ask you why Pi is, as far as I'm aware, the only agent that runs YOLO mode by default.
						- [[Person/Mario Zechner]]
							- Do you think the tapping yes in the dialogue that asks you if the next operation...
						- [[Person/Jan-Niklas Wortmann]]
							- Oh, no, I think, I'm not saying you're wrong. I never said you're wrong.
						- [[Person/Mario Zechner]]
							- My thing is this. By telling people, this is YOLO mode, it's dangerous, you better think about this, I actually make people think about that. I actually hope to make people think about that. Because initially people come to Pi and are like, oh, this is garbage because it doesn't have permissions. And I'm like, yeah, think about why it doesn't have permissions and then think about how you fix that on your end.
				- #### {{youtube-timestamp 3831}} Make YOLO Explicit To Force Security Thinking
					- Snipd: https://share.snipd.com/snip/8689e086-36be-41bd-a1b4-af49fb5ed351
					- Expose YOLO mode and force users to think about security instead of pretending permissions solve it.
					- Mario makes YOLO explicit so users must design environment-level containment like containers rather than rely on incomplete built-in sandboxes.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- By telling people, this is YOLO mode, it's dangerous, you better think about this, I actually make people think about that. I actually hope to make people think about that. Because initially people come to Pi and are like, oh, this is garbage because it doesn't have permissions. And I'm like, yeah, think about why it doesn't have permissions and then think about how you fix that on your end. And the hope there is that people go inside themselves and look for this quiet, dark place that's called security awareness and think about real hard how within their environment, Which is different to my environment they would like to safeguard agentic work and the answer to that is usually if i don't want the computer that the agent is running on to be fucked i Containerize the agent or at least i containerize the tools the agent uses like read write files bash in a container that solves problem one but i cannot decide this for you i i could probably Install uh could probably bundle something like the sandbox thing that entropic has or bubble wrap or whatever but these are incomplete solutions and i do not want when it comes to security Provide you with an incomplete solution that you can fuck up configuring so ideally within the enterprise and then i had a bunch of enterprise people come up to me about that they actually Eventually understand it like yeah this makes total sense because you don't fucking know our environment at infra like if you use something like gondolin like you emu thing as the container Built in this wouldn't work in our infrastructure because we don't have hardware virtualization for blah blah blah so yeah that. That's why that's not in there. Because I think what exists in Codex and Claude Code is mostly security theater. It is now also, I mean, Claude Code now does what? It asks an LLM if a bash command is safe or not in auto mode. Is that good?
				- #### {{youtube-timestamp 3842}} Security Theater Is Not Real Sandboxing
					- Snipd: https://share.snipd.com/snip/c612f999-ee70-4446-baf1-c8850467b3a1
					- Mario leaves agent security decisions to users because bundled sandboxes are incomplete and easy to misconfigure.
					- He argues LLMs judging whether Bash commands are safe is security theater, not protection.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- Because initially people come to Pi and are like, oh, this is garbage because it doesn't have permissions. And I'm like, yeah, think about why it doesn't have permissions and then think about how you fix that on your end. And the hope there is that people go inside themselves and look for this quiet, dark place that's called security awareness and think about real hard how within their environment, Which is different to my environment they would like to safeguard agentic work and the answer to that is usually if i don't want the computer that the agent is running on to be fucked i Containerize the agent or at least i containerize the tools the agent uses like read write files bash in a container that solves problem one but i cannot decide this for you i i could probably Install uh could probably bundle something like the sandbox thing that entropic has or bubble wrap or whatever but these are incomplete solutions and i do not want when it comes to security Provide you with an incomplete solution that you can fuck up configuring so ideally within the enterprise and then i had a bunch of enterprise people come up to me about that they actually Eventually understand it like yeah this makes total sense because you don't fucking know our environment at infra like if you use something like gondolin like you emu thing as the container Built in this wouldn't work in our infrastructure because we don't have hardware virtualization for blah blah blah so yeah that. That's why that's not in there. Because I think what exists in Codex and Claude Code is mostly security theater. It is now also, I mean, Claude Code now does what? It asks an LLM if a bash command is safe or not in auto mode.
				- #### {{youtube-timestamp 3974}} Require Human Written Issues Before AI Pull Requests
					- Snipd: https://share.snipd.com/snip/0aea3407-87a2-4c2f-a8b0-1f6c99579479
					- AI agents turned one or two weekly pull requests into 50–60 daily submissions, most low-quality or based on user error.
					- Mario asks contributors to explain the problem and motivation in a brief human-written issue first.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- You kind of alluded to the fact that you're doing that to some extent manually, but you also online talked about the fact that you declare PR vacation every so often, which I thought was An interesting approach. So talk me through how open source process.
						- [[Person/Mario Zechner]]
							- So I've been in open source for 20 years and I had two other big projects in that space. So I know my way around. Previously, pre-agent, it would take people a lot of effort and time to create a pull request because they would have to understand everything with their human brain and write the code With their human hands nowadays people would just ask their clanker to send a pr to fix a thing they think is broken in pi usually the results of that are really shitty and not reusable And often they don't even identify something that's actually broken it's usually just user error so now what happens is instead of getting like one or two prs per week for a very successful Pre-agent open source project i get 50 to 60 prs per day by clankers and each pr has a description that is kind of like a full harry potter book and then usually has about 10 to 1,000 file Changes, depending on how the clanker felt. So what are you going to do with that?
			- ### {{youtube-timestamp 3987}} Taming the PR Flood
				- #### {{youtube-timestamp 4017}} Require Human Issues Before Accepting AI Pull Requests
					- Snipd: https://share.snipd.com/snip/5b470705-5cda-487f-8370-1fc0745821f7
					- AI-generated pull requests overwhelmed Pi with 50–60 submissions daily, often useless or caused by user error.
					- Mario requires a concise human-written issue first, proving contributors understand the problem before opening a PR.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- And not reusable and often they don't even identify something that's actually broken it's usually just user error so now what happens is instead of getting like one or two prs per week For a very successful pre-agent open source project i get 50 to 60 prs per day by clankers and each pr has a description that is kind of like a full harry potter book and then usually has About 10 to 1,000 file changes, depending on how the clanker felt. So what are you going to do with that? The default position is you now declare every pull request garbage and auto-close it. So how do I get meaningful pull requests? Well, you ask people to first write an issue in their human voice, no longer than a screen, and tell me exactly what it is you want to do and why you want to do it. And then I tell you, okay, that's good. Now you can send a PR. You have proven that you're human and you've proven that you understand the problem and you've proven that you understand the solution. Once I get that I type looks good to me and a little github workflow triggers that will put them in a file that says this account on github can now open PRs without them being auto close
				- #### {{youtube-timestamp 4038}} How Pi Filtered Out Thousands Of Clanker PRs
					- Snipd: https://share.snipd.com/snip/0234cb23-0d2b-4ee0-ac93-d280f5e6b6f9
					- Clanker agents flooded Pi with 50–60 PRs per day, each often huge and unreadable.
					- Mario enforces a human-first rule: require a short human-written issue before granting PR privileges, which restored PR quality.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- That is kind of like a full harry potter book and then usually has about 10 to 1,000 file changes, depending on how the clanker felt. So what are you going to do with that? The default position is you now declare every pull request garbage and auto-close it. So how do I get meaningful pull requests? Well, you ask people to first write an issue in their human voice, no longer than a screen, and tell me exactly what it is you want to do and why you want to do it. And then I tell you, okay, that's good. Now you can send a PR. You have proven that you're human and you've proven that you understand the problem and you've proven that you understand the solution. Once I get that I type looks good to me and a little github workflow triggers that will put them in a file that says this account on github can now open PRs without them being auto close and That's worked brilliantly because now I'm back to high quality PRs that I used to use that I used to get pre-clanker and I don't see the clanker PRs anymore what i do see though is the issues Because the issues i already auto close the issues but that's mostly just for visual reasons i still every day go to the issue tracker to the closed issues find the issue that's labeled Last read that's that's kind of like the marker up until which either me or armin have processed issues and then i painstakingly read through 30 to 60 issues that have been submitted In the last whatever 12 or 24 hours and identify is this clanker is this not clanker is it a good issue is it not a good issue and then i reopen the issues that are worth it and out of this like My last triage run was two days ago, because thankfully Armin is now doing that as well. I think I ran through 50 issues and two survived. Two issues got opened out of 50 closed issues.
				- #### {{youtube-timestamp 4063}} Require A Human Issue Before Accepting PRs
					- Snipd: https://share.snipd.com/snip/ecca40d5-0bb0-46ef-98f3-2f7c3128f83e
					- Prevent low-effort AI PRs by requiring a short human issue first and then whitelist accounts for PRs.
					- Mario auto-closes PRs until the contributor submits a concise human-written issue and gets a temporary PR whitelist.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- Well, you ask people to first write an issue in their human voice, no longer than a screen, and tell me exactly what it is you want to do and why you want to do it. And then I tell you, okay, that's good. Now you can send a PR. You have proven that you're human and you've proven that you understand the problem and you've proven that you understand the solution. Once I get that I type looks good to me and a little github workflow triggers that will put them in a file that says this account on github can now open PRs without them being auto close and That's worked brilliantly because now I'm back to high quality PRs that I used to use that I used to get pre-clanker and I don't see the clanker PRs anymore what i do see though is the issues Because the issues i already auto close the issues but that's mostly just for visual reasons i still every day go to the issue tracker to the closed issues find the issue that's labeled Last read that's that's kind of like the marker up until which either me or armin have processed issues and then i painstakingly read through 30 to 60 issues that have been submitted In the last whatever 12 or 24 hours and identify is this clanker is this not clanker is it a good issue is it not a good issue and then i reopen the issues that are worth it and out of this like My last triage run was two days ago, because thankfully Armin is now doing that as well. I think I ran through 50 issues and two survived.
				- #### {{youtube-timestamp 4100}} Human Issues Filter Out Clanker Pull Requests
					- Snipd: https://share.snipd.com/snip/b55e0f7d-632e-4f8f-a230-430c7a4a00d7
					- Mario requires contributors to explain an issue in their own words before earning permission to open pull requests.
					- This restored high-quality contributions, reducing 50 daily clanker PRs to roughly two worthwhile issues out of 50.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- That I used to get pre-clanker and I don't see the clanker PRs anymore what i do see though is the issues because the issues i already auto close the issues but that's mostly just for visual Reasons i still every day go to the issue tracker to the closed issues find the issue that's labeled last read that's that's kind of like the marker up until which either me or armin have Processed issues and then i painstakingly read through 30 to 60 issues that have been submitted in the last whatever 12 or 24 hours and identify is this clanker is this not clanker is It a good issue is it not a good issue and then i reopen the issues that are worth it and out of this like my last triage run was two days ago, because thankfully Armin is now doing that as well. I think I ran through 50 issues and two survived. Two issues got opened out of 50 closed issues. But it works. I mean, I spent about half an hour going through 50 issues, because most are very quickly to identify as garbage so that's not that's not hard it sucks that i have to do it but it's not that Bad for peter and open claw the scale is just orders of magnitude bigger and my version my my method would not work for that at all no chance
				- #### {{youtube-timestamp 4110}} AI-Generated Issues Overwhelm Human Triage
					- Snipd: https://share.snipd.com/snip/09cb8607-2496-4959-a181-6f5beb5216ad
					- AI agents flood projects with issues, forcing maintainers to manually separate useful reports from garbage.
					- Mario reviewed 50 closed issues and reopened only two, while OpenClaw’s scale made manual triage impossible.
					- Transcript
					  collapsed:: true
						- [[Person/Mario Zechner]]
							- I already auto close the issues but that's mostly just for visual reasons i still every day go to the issue tracker to the closed issues find the issue that's labeled last read that's That's kind of like the marker up until which either me or armin have processed issues and then i painstakingly read through 30 to 60 issues that have been submitted in the last whatever 12 or 24 hours and identify is this clanker is this not clanker is it a good issue is it not a good issue and then i reopen the issues that are worth it and out of this like my last triage run Was two days ago, because thankfully Armin is now doing that as well. I think I ran through 50 issues and two survived. Two issues got opened out of 50 closed issues. But it works. I mean, I spent about half an hour going through 50 issues, because most are very quickly to identify as garbage so that's not that's not hard it sucks that i have to do it but it's not that Bad for peter and open claw the scale is just orders of magnitude bigger and my version my my method would not work for that at all no chance So that is why he is trying to combat that with Automated tools. I actually, earlier in February, I wrote some things for the team, for the OpenClaw team, to visualize issues in a 3D space and be able to select clusters of issues that are very,
			- ### {{youtube-timestamp 4331}} Token Prices and Budgets
				- #### {{youtube-timestamp 4418}} Frontier Models Keep Raising Effective Prices
					- Snipd: https://share.snipd.com/snip/f2ed29fb-8b12-4e1b-b9b0-0c8871f795bb
					- Frontier models have repeatedly increased effective pricing despite promises of cheaper tokens.
					- Changing tokenizers can make identical input count 1.4 times more tokens at the same price.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- Companies when this is already the case yeah same um but at the same time then if there's also the conversation because right now it feels a little bit like an unlimited pot of gold that A lot of companies allocate to AI, which I think to some extent makes sense for people to experiment and get into the AI psychosis and pass it.
						- [[Person/Mario Zechner]]
							- Yeah.
						- [[Person/Jan-Niklas Wortmann]]
							- But with that, when we start the conversation of like, oh, do you really need to use Opus for centering that div now? Probably not. And I do that myself. I'm too lazy to switch models, so I usually pick one that works for me reliably. I usually use GPT 5.5 and call it a day. I also don't dramatically mess with different reasoning levels. So I think that might be biased, but I think that's the case for most developers, but I don't think that would be the case long-term just for price sensitivity. Thoughts?
						- [[Person/Mario Zechner]]
							- Yeah, I don't know. I mean, we were promised lower token pricing for the past two years, and I do not see that happening for the frontier models. Like the last couple of releases always increased pricing. Or they changed the tokenizer so that now for the same input text, they just count more tokens.
				- #### {{youtube-timestamp 4478}} Anthropic Won Developers Then Sold To Enterprises
					- Snipd: https://share.snipd.com/snip/a91065c5-ef45-4e35-aff4-fc8354e896a3
					- Mario argues Anthropic used developers to improve its models, then shifted toward enterprise buyers once companies demanded Claude at scale.
					- Free Claude Code coupons allegedly triggered a January office return where employees urged bosses to buy it.
					- Transcript
					  collapsed:: true
						- [[Person/Jan-Niklas Wortmann]]
							- Thoughts?
						- [[Person/Mario Zechner]]
							- Yeah, I don't know. I mean, we were promised lower token pricing for the past two years, and I do not see that happening for the frontier models. Like the last couple of releases always increased pricing. Or they changed the tokenizer so that now for the same input text, they just count more tokens. Which is too far, extra sneaky. Yeah, same token price, but it's just like 1.4 times more tokens for the same input. I mean, there's technical reasons why you want to switch out your tokenizer. But it's also kind of, I don't know, suspicious, but specifically pre-IPO.
						- [[Person/Jan-Niklas Wortmann]]
							- The thing that boggles my mind is you're you're marketing these things to developers right now because like oh they stopped marketing to developers they are now marketing to cios and
						- [[Person/Mario Zechner]]
							- Enterprises they don't care about developers anymore because you know what happened they marketed to developers for the past year 2020 25 basically from april to october they got All the training data for them in exchange for two paying anthropic 200 for that privilege then they improved the models with that data then over christmas they gave everybody ai psychosis In form of free coupons that you can share with your friends to try out Claude Code during christmas break and then in january every came everybody came back to the office and said boss We need to buy the clots all the clots and then all the companies started buying the cloths and this is what happened and at that point where the companies start requesting more cloths And tropic doesn't have to gather to the developers anymore and you can see it in all their actions since february um yeah i think the token prices will not decrease
