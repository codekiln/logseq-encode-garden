date-created:: [[2026-10-04 Sun]]

- # [[Person/codekiln/GitHub/logseq-encode-garden]]
	- ## [[Listen/ing]]
	  collapsed:: true
		- Max Cooper's 2026 album, "fabric presents Max Cooper," on my [[Campfire Audio/Solaris]]
			- TODO import this album and artist and link
	- ## [[Challenge]]s
	  collapsed:: true
		- ### [[Making/Music]]
		  collapsed:: true
			- I'm trying to make a bit of music a few times a week this fall, with the goal of some live performance. This week I don't think I really made any progress in terms of making music, but I did make some important progress towards being able to publish a podcast of my improvisations. It's actually live now.
			- #### Processing [[Microfreak/Preset]]s
			  collapsed:: true
				- I made a bit of progress on getting microfreak presets in and out of the synth in an automated way, as well as being able to automate the renaming of the presets. I'm still a bit hazy about what's possible as well as what I want.
				- I do sense that I need more memorable names than just having a preset named after the [[GitP]] episode. When I'm improvising, I need to be able to call up sounds from memory, and preset names named after dates aren't useful to me in that regard. The live performances I've done lately do require me to remember the names of presets. Presets are actually a starting point for me, not a destination.
					- I've thought about using them as a waypoint, e.g. making an improvisational system that has multiple presets that I'd sequence and go through as a way of organizing compositional structures. That said, I haven't actually performed this way yet, it's still an idea.
				- Now that my presets have [[Digital Twin]]s in this garden, I might think about them more in the context of [[Knowledge Gardening]]. For example, Maybe they would start out as a preset named for an episode, then over time, take on a life of their own and have their own name as they become more significant.
					- [[Person/Gergely Orosz/Pod/26/09 Design Engineering with Maggie Appleton]] had a section where [[Person/Maggie Appleton]] talked about her garden, and its principle of disclosing the level of growth of a page, from a seed through a seedling and eventually a fully grown tree. I'd like to model that in my gardens as well.
						- TODO model a [[Logseq/Entity]] extension about page maturity that would define [[Logseq/Frontmatter]] properties with levels and emojis to inspired by [[Person/Maggie Appleton]]'s knowledge garden to represent how established or mature that page or namespace in the garden is.
				- One of the last times I made music with the [[Launchpad]] and the [[Microfreak]], I used the [[Launchpad/UG/09 Sequencer]] along with [[Launchpad/UG/05 Session Mode]]. The result was confusing and complex. I need to review the Launchpad sequencer and think more about when I'd want to use it vs the [[Microfreak/UG/13 Sequencer]]. Having two sequencers around as well as the ability to loop anything in the session mode is rich in terms of a feature set, almost to a point of fault: there's too much flexibility and it's hard to know what to use for what. If only the Launchpad Sequencer was better synchronized with the [[Ableton/Live]] tempo.
		- ### [[Organization]] around challenges
		  collapsed:: true
			- Earlier this week I went into some investigation into [[Person/Cal Newport/Pod/26/08 Rethinking the Deep Life Stack (Again!)]] to try to figure out what he does each season around recording his plans. I thought I remembered some instructions related to printing out a season's plans, methods, techniques and laminating it. I think that was basically it; I just can't seem to find the source.
				- TODO do some [[Readwise/CLI]] searches related to this to see if I can find the source(s) of this.
			- The basic idea is that by identifying and clearly describing your techniques, goals, etc at the beginning of the season, you have your [[Algorithm]] for life worked out, and you can focus on execution throughout the season.
			- I think that's a good idea; there's something [[Discipline]]d about writing down one's plan and carrying it through.
			- My main issue with this has been that I have challenges at different tiers in terms of public and private. I think that ideally, I'd have a custom application for this, and I'm very interested in prototyping that, but I've held off, since it's usually a distraction to make a custom application for something. It tends to become a substitute for doing the hard thing: making a system to do the thing easier becomes its own thing and takes on its own momentum.
		- ### Technical Challenges
		  collapsed:: true
			- #### Breaking in [[1Password/Environment]]s and [[Sandbox/ing]]
			  collapsed:: true
				- I've already written a good bit about this in journal entries, but I'm not as enthusiastic about this as I was last weekend for [[Secrets Management]]. In particular, I need a way to enable my [[AI/Agent/Remote]] to make longer progress without me needing to be a [[Proxy/Meat]] to use [[Touch ID]] on my [[Mac]], and [[1Password]] just feels like it's getting in the way there. I think I'm headed more towards using [[fnox]] features that enable basic usage without [[Touch ID]] and then perhaps relying on [[1Password/Environment]]s for more sensitive workflows, e.g. deploying to prod.
				- What I really want is a remote, ephemeral, task-specific coding environment like [[Ona]] or [[DevPod]] or [[e2b]] that would integrate with [[iam]] and let me authorize a subset of my permissions to a task-specific agent.
			- #### [[Apple/AirPod/Pro/v2]] vs [[iPad]] Volume Issues
			  collapsed:: true
				- For the last ten-ish days I had a problem where my airpods were stuck on a very low volume only on my iPad, while the same airpods had normal behavior on all other devices. AI didn't provide that much useful help in debugging this; most of its suggestions were obvious things I tried before even asking AI. What ended up working was a hack I found by accident: if I swipe down from the upper right to display the screen with volume, brightness and other options, there's a nested option for "live mode." I'm not sure what it does, but I think that it's supposed to enable the outside world's sounds to pass through the airpods. When that mode is engaged, it forces the AirPods to renegotiate their max volume, so that when it's disabled, it again took on the conventional max volume.
			- #### [[ChatGPT/Enterprise]] usage is confusing and opaque
			  collapsed:: true
				- It feels like AI companies are headed in the direction of making it harder to find and predict usage. My organization is trying to switch from a relatively high-limit usage, limited number of seats plan on [[Claude]] to an org-wide ChatGPT plan that is supposed to be cheaper, but in practice, it seems to chew through a month's worth of "credits" (which are different from tokens?) in a few days, only to be reset a few days later. The result is that I don't actually feel confident in what I can tell others to rely on or even that the skills that I've made under Claude are going to be usable under ChatGPT. I'm stuck in between two worlds.
		- ### Health and Physical Challenges
		  collapsed:: true
			- #### [[Oura/Ring]] not recording data
			  collapsed:: true
				- My Oura Ring is less than a year old, and it's only recording my information on less than half of the nights I wear it. I used the in-app support chatbot to run a diagnostic, and apparently they are going to send me a new ring, but it hasn't been shipped yet, and that was five days ago or so; who knows how long it will take to get here. As a result, some of my health and wellness challenges related that I was recording in Oura are suffering in terms of continuity. For example, a key thing I'm working on is improving my [[HRV]], and until I find an alternative method of measuring that or receive my new Oura Ring, that challenge is pretty much on hold.
					- TODO create a [[Logseq/Entity/Diataxis/Explanation]], [[Logseq/Entity/Term/Acronym]] for Heart Rate Variability.
			- #### Reading and Adopting [[Person/Andrew Huberman/Book/26/Protocols]]
				- TODO import [[Person/Andrew Huberman/Book/26/Protocols]] book
				- I'm about two chapters into this book. It's good so far.
				- It's already affected my behavior a bit.
					- I'm getting outside and trying to get light in the morning. The sun rises so late these days, so it takes a bit of scheduling.
					- I'm also using a 10k lux lamp in the mornings when I get up, and [[Light/Blue/Blocker]]s in the evenings.
					- I've also been trying to get more physical workouts in before 2pm, which is supposed to be good for the circadian rhythm. This is a change for me as up until lately I have been going to gym classes after work.
					- I'd like to start strength training regularly again, but it takes a bit to make a routine that works for me without needing to stand in wait too much at the gym.
	- ## Thoughts
		- ### Layered, Cross-Sectional Thinking
		  collapsed:: true
			- The idea of [[Diagram/Cross-Section]] has been on my mind since last weekend, when I discovered the concept of [[Topology/Fiber/Bundle]]s. In my [[Knowledge Garden]]s I'm attempting to [[Prototype]] a method of [[Palimpsest]] or [[Layer]]s of writing. In fact, this week review is repeated in three different knowledge gardens, and each has similarly named headings at similar levels of indentation, and in my head, I'm thinking of the union of them, as though they were layered on top of each other.
			  collapsed:: true
				- TODO import [[Logseq/Entity/Concept]] pages
					- TODO for [[Diagram/Cross-Section]] with alias of `Cross-Section Diagram`
					- TODO for [[Topology]]
					- TODO for [[Topology/Fiber/Bundle]]. Try to explain it in a way that a person who has taken multivariate differential and integral calculus but not topology can understand.
			- #### [[Idea/My]] - [[App/Idea]] - [[Media/Layered]]
				- In early episodes of [[GitP]], I talked through my creation of a [[Microfreak/Preset]]. The ones I published this week were just music, which has a certain kind of simplicity and mystery to it. Imagine this: you are listening to a podcast, and at any moment, you can pause and make a comment with your voice, which records a new layer. Then when the next person  listens to that podcast, they hear a sound which indicates the presence of a media layer, an off-ramp. They can take some action (gestural with head / airpod, verbal, or with touch on the screen) to switch over to the layer, then perhaps they want to make a reply with their voice or with text, which becomes yet another layer. Perhaps some of these could be voted up like [[Reddit]] somehow, and perhaps some of these conversations would let a person bring in an [[AI/Agent/Personal]] to have a conversation with.
				- Some of these layers could be synchronously collaborative, like two or more musicians playing together.
				- Others could be asynchronously collaborative, like an idea that comes up in a podcast becoming a prototype.
				- The basic idea is that a good portion of the informational beauty of the web is its hyperlinks and its url hierarchies, but somehow that never made its way into video and audio, and outside the H1-H6 web standards, Logseq, or custom apps like Reddit, hierarchies or layers of narrative never really developed.
				- When I asked AI about this, they suggested a number of standards, such as the web annotations standard (I think it was from the w3c), which allows adding a comment to a particular segment of video or audio.
					- TODO import the web annotation standard as a [[Logseq/Entity/Standard]].
		- ### [[Book/Hackers]]
		  collapsed:: true
			- TODO import Hackers, Heroes of the Computer Revolution [[Logseq/Entity/Book]] by Levy under a [[Logseq/Entity/Person]] for him
			- I'm still reading and discussing this book with a friend. I'm through chapter 5; we are discussing chapter 4 today.
			- My main thought about it is that there are a lot of skills that are necessary to make today's [[AI/Agent]]s productive that, in time, are going to be more like being really good with at raw assembly / assembler: deeply learning things that are necessary will help you deeply understand what's coming next, but what's coming next is going to replace today's method of creating with machines. I'm seeking a more general purpose idea about when this type of experience is beneficial, when it's crucial, and when it's a waste.
				- TODO import a [[Logseq/Entity/Concept]] for assembly programming in a logical spot, probably under [[Programming Language]] somewhere