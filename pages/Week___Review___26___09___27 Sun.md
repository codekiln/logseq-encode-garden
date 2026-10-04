prev:: [[Week/Review/26/09/20 Sun]]

- # [[2026-09-27 Sun]] - [[Person/codekiln/GitHub/logseq-encode-garden]]
	- 09:40
		- ## Introit and Benediction
		  collapsed:: true
			- I've got my favorite [[Cinnamon Roll]] and my [[Coffee]] at my favorite seat at my favorite coffee shop for doing a weekly review. It's hopping in here. The same week review page open in each garden. I've got my [[Campfire Audio/Solaris]] earbuds in, and I'm listening to a playlist I just found out about on spotify that was created by the person behind Oneohtrix Point Never. I'm dedicated to not navigating from these pages. It's a concentration zone!
			  collapsed:: true
				- DONE import [[Logseq/Entity/Person]] entity for the person behind this musical artist Oneohtrix Point Never. I think it's ___ Lopatin.
					- DONE define [[Logseq/Entity/Person/Musician]] for when a person is a musician.
		- ## Garden Layers
		  collapsed:: true
			- Lately, I've been thinking about how I might make a system for a page in Logseq to function as a palimpsest.
			  collapsed:: true
				- DONE create [[Palimpsest]] [[Logseq/Entity/Concept]] page
			- If I'm not mistaken, a palimpsest is a document where multiple people have written over each other, possibly in a layered commentary like [[Judaism/Concept/Layered Interpretation]].
			- Was I thinking and writing about these concepts last week? I'm not willing to go do the research right now.
			- The idea here is that this page - this weekly review - has three levels of privacy, and I will record each idea at the most public layer that is appropriate for that item. In general, lately I've been working on "opening up." Didn't I articulate this in a principle last week or some time in the past? Yes; see [[My/Principle/Balance/Risk vs Reward/wrt Privacy - Make Things As Public As They Can Be]].
			  collapsed:: true
				- ### [[note/my/side]] clarifying heuristic on when to make things more private
				  collapsed:: true
					- this week I've been thinking of a Heuristic (see also [[Epistemics/Concept/Heuristic vs Axiom]]) that I should, by default, make information as public as I can, and make information more private when they are tied to specifically articulated perceived harms or [[Threat/Model]]s. Why? because of the reasons defined in the principle, but also because privacy is expensive and complex, and making things public often simplifies a system.
					- I wish there was a term like the opposite of Privacy. Something like Publicity, but without that term's current connotations of, say, a marketing campaign. Of course, we can speak about Openness, but in my opinion, that has a slightly different valence than Privacy. Privacy sounds like a right, an ideal, a quality. One could make a claim that Openness is a right, an ideal or a quality, but those aren't really connotations that drip off of that term, that the concept just naturally comes with or wicks off.
			- I intend to work towards a set of conventions, systems, and technologies that will enable me to create layered commentary in my [[Knowledge Gardens]].
				- [[Example]]
					- On the way over here, I was trying to figure out how I would implement Logseq, or maybe how I eventually will implement my own version of the Logseq idea, with respect to the layered commentary idea and how it integrates with the concept of a [[Logseq/Proxy]]. I was thinking that perhaps I could have a page name fragment or logseq namespace fragment affordance which would indicate layered commentary.
						- For example, let's say I have a page `1Password/Vault` in my public garden, and I want to merge that with `1Password/Vault` in [[Person/codekiln/GitHub/logseq-garden]], such that when I view `1Password/Vault` in `logseq-garden`, it contains my private notes merged with my public notes.
							- I believe that recently I was writing about how I could make a logseq plugin, nvim customization, or other on-disk, scripted affordance which would add a block reference to the upstream garden, then sync that block reference down. Maybe one way to do this would be to use abbreviations, like LG for logseq-garden and LEG for logseq-encode-garden, then have sub-namespaces like `1Password/Vault/Prxy/LEG` in `logseq-garden` to represent the contents of that page, then `1Password/Vault/Discussion` would contain my local commentary, even with block reference, then `1Password/Vault` would be a like a [[Math/Projection]] or a [[Database/View]], which let me "view the palimpsest" or view the original page with the layered commentary.
								- DONE create [[Logseq/Entity/Concept]] for [[Database/View]]
				- It's not really a fully formed idea, but I need to prototype and build something with this shape. I'd like to find a way to have a page in a knowledge garden represent an entity, then have that page in my various gardens explore those slices or layers of that entity. It would be a way of performing a sort of intellectual dissection of the universe.
			- ### [[Question/My/Side]] the contradictory hyperinflation of abundance
			  collapsed:: true
				- The people next to me in the coffeeshop are in California. They remarked on how cheap the avacado toast was. I replied that it's typically so expensive in the coffeeshops around here that I never get it. I wanted to ask them if they were in the "local inflation blast radius" of the AI companies. I've heard about the tremendous impact of the pending [[IPO]]s of the [[AI/Model/Lab]]s like [[OpenAI]] and [[Anthropic]] on the [[Real/Estate]] market in [[US/CA/San Francisco]], and I imagine it's possible that it could have an outsized impact on local [[Inflation]]. The strange thing here is that people at most AI labs believe that they will bring about [[Abundan/ce]]. So, is there a natural law similar to or reflecting [[Jevon's Paradox]] where the companies that produce abundance - which is [[Inflation/vs/Deflation]] -  may actually cause local hyperinflation?
					- DONE create [[Logseq/Entity/Concept]]s for common entities
						- with [[Logseq/Entity/Abbreviation]]
							- DONE create [[IPO]]
						- DONE create [[AI/Model/Lab]]
						- DONE create [[Real/Estate]]
						- DONE create [[Inflation]] and [[Inflation/vs/Deflation]] as [[Logseq/Entity/Trade-Off]].
						- DONE create [[Abundan/ce]] with alias of Abundance.
							- DONE import [[Person/Ezra Klein]] [[Logseq/Entity/Person]] and his [[Logseq/Entity/Book]] about abundance, linking it to the page above.
				-
		- ## Design, Anthropology and Cultural Appropriation
		  collapsed:: true
			- I need some good sources for becoming more educated about [[Anth/ro/polog/y/Cultural]] and [[Cultur/al/Appropriation]].
				- DONE create [[Logseq/Entity/Concept]]ual overviews
					- DONE create [[Anth/ro/polog/y/Cultural]] with alias of Cultural Anthropology
					- DONE create [[Cultur/al/Appropriation]] with alias of Cultural Appropriation and include a history of the idea
			- This week was the first time I ever saw [[Person/Madonna]]'s [[19/9/0]] performance of the song Vogue at the [[MTV/VMA]]s. This performance seemed pretty rad(ical) to me. Here are [[My Thoughts]].
			  collapsed:: true
				- todos
				  collapsed:: true
					- DONE import appropriate entities from above. Consider [[Logseq/Entity/Music/Performance]].
						- DONE define an extnsible entity for a piece of music that may be related to other pieces of music, for example, a track from an album or a movement from a sonata. Try to find an elegant way to differentiate it from [[Logseq/Entity/Music/Recording]] so that recorded media by other people, even though technically it may be true that it is recording. The entity should make it simple and obvious how to find the following things in the garden in appropriate logical proximity on disc with [[Lexicographic/Order]] to the things that should be considered "near" them, modeling the latent space in my mental representation of
							- the song Vogue by Madonna, in close proximity to other songs on the album that it was released on
							- the first movement of the Pathetique sonata by Beethoven, and of course its proximity or relationship to the other movements of that sonata
							- the piece of music 4'33" by John Cage
							- the 2nd movement of the 23rd piano concerto by Mozart and its relationship to the 3rd movement
							- the song "Landslide" by Stevie Nicks and its relationship to the covers by Smashing Pumpkins or other artists
				- I think this performance happened after the `Movie/YY/Paris is Burning`, which introduced the larger US to the culture of the Drag Queen.
				  collapsed:: true
					- DONE define a new logseq entity for Movie and fill in the movie entity above.
				- Madonna is dressed as Marie Antoinette and she's surrounded by dancing queer black men in short shorts. Not only is she a queer icon, but she's pretending to be their girl boss, moving them about, swatting them away, treating them with and from a position of power and authority. At the same time, she's singing about how important it is to feel beautiful and magical, and is thereby implying that their dancing is just such an expression. Then later in the piece, she names many famous people like Joe DiMaggio, Marlon Brando, James Dean, and thereby explicitly ties what they are doing - "voguing" - as the last in a long line of what icons do "on the cover of a magazine" when they "strike a pose." She's portraying them as beautiful from her bossy perspective.
				- Is this cultural appropriation? Yes. Is it exploitative? Yes. She's literally making money off of their unique culture, using their unique elements out of context to stick out in the marketplace and climb the charts. It's a fun little power and wealth game for her. It is ethically dubious or suspicious or wrong? I don't feel like it is from my position, and this is where I need to be more educated about the history of the idea of [[Cultur/al/Appropriation]] in order to answer this intelligently. She's "celebrating" or "appreciating" the culture, and she's lending her power as a white woman to these genderqueer black people.  It is partly to their benefit. But it's to their benefit in a way that's not above reproach.
				- I think Madonna was performing a kind of judo here: using her position of power and privilege to turn over the compost heap of culture and mix things up a bit. It's so funny to watch the performance now, because the camera follows her so closely across the stage. She's the protagonist, but my eyes want to see the truly startling performers on the stage - the queer dancers around her. The camera doesn't want to make them the subject, but *she* might have preferred them to be.
				- Here, Madonna was already the quintessential sex symbol. I think she posed for Playboy long before this. The camera is the capitalist market lens; and it's interested in turning her sexual position into eyeballs and attention to sell thing. But she's trying to take that attack and roll it over into something else, maybe even a discussion or a consideration of what it means to be more magical and beautiful by voguing. That's art, no doubt to me.
				- Then again, a part of me asks, how is this different than when an older man cat calls a woman on the street and then says that's "just appreciation? when this is questioned by others.
			- This week I have been making my way through [[Person/Maggie Appleton]]'s recent interview on The Pragmatic Engineering podcast. I think it's [[Person/Gergely Orosz/Podcast]].
			  collapsed:: true
				- todos
				  collapsed:: true
					- DONE import a [[Logseq/Entity/Podcast/Episode]] entity of this. Use [[Readwise]] to pull in the multiple sources (both [[Snipd]] from the podcast, as well as [[YouTube]]).
				- I don't think I knew this before, but it totally makes sense that Maggie Appleton studied [[Anth/ro/polog/y/Cultural]] as an undergrad. In her talk on [[Barefoot Developer]]s she mentioned the "Barefoot Doctors" of china that traveled from community to community.
				- ### [[Person/Gergely Orosz]] asked her to explain what, in her mind, [[Design]] was.
					- He prefixed this question be explaining his contact with designers at [[Uber]], who would create [[Wireframe]]s and [[Mock/Ups]], mostly visual resources. They would work in [[Figma]] or another visual system, and hand those assets with [[PRD]]s to the engineers to build. He acknowledged that he had an incomplete perspective of what design was, and she had worked in design at many firms, so that's why he asked her to define it.
					  collapsed:: true
						- DONE create [[Logseq/Entity/Concept]] overviews
							- DONE fill in [[Wireframe]]
							- DONE fill in [[Mock/Up]] with alias of [[Mock-Ups]]
							- DONE if [[Uber]] doesn't exist, import [[Logseq/Entity/Company]]
					- I really liked the way that she explained the full scope of the field of [[Design]] in that interview. She related [[Design/Product]] to [[Design/Software]] to [[Design/Architecture]]. They are all forms of the same fundamental skill: to make things simpler for a a group of people in a way that naturally emerges from them. This morning as I was writing about [[My/Entity/System]] and relating it to the foundational [[Design/Pattern]] system of [[Person/Christopher Alexander]], I realized that I am just as much a designer as I am an engineer.
				- ### Design Engineering, Engineering Design, and the Struggle of Osmotic Identity in [[My/History]]
				  collapsed:: true
					- I have always held a deep affinity for design.
					  collapsed:: true
						- DONE import [[Person/Frank Lloyd Wright]] as a [[Logseq/Entity/Person]]
					- #### Cool dad
						- When I was young, I gained my first sense of coolness from my dad. He was an professional architect that studied at a prominent school of design, in an era when that was first starting to mean something. When I was growing up, I was surrounded by weird, beautiful things he created and/or curated into our life: clarinet candelabras, a coffeetable made from an iron floor grate in an ancient gas heating system, a "personal pew" chair made from a church pew, a desktop bookshelf in the style of [[Person/Frank Lloyd Wright]], a model of a cup of coffee with a carton of milk forever pouring into it, etc. We had access to and read magazines like Wired, Architectural Digest and National Geographic because of him. When my parents were married they asked every married person in attendance wear the tuxedo or bridal dress *that they themselves originally wore to get married* to the wedding.
					- #### Artsy mom
						- While my mother was professionally an educator, she was also an artist, poet and a writer. Because of her, my earliest memory is being in a stroller at a big museum. My family went to the coffee shop on the weekends with our sketch books for drawing and journaling. I grew up surrounded by her many writing, reading, painting, sketching, poetry circles. We had private family holidays where we went to certain art galleries or sculpture gardens or outdoors concert series every year. We had a darkroom in her house. I started both taking photos with my own camera when I was four, and there has never been a point in my life since that I haven't been a photographer. In a very real way, being at this coffeeshop on the weekend and doing a week review is just an expression of that environment of evolutionary adaptedness in which my original personality was formed.
					- #### Architecture as Therapy
						- When I was growing up, I always had my own room, and for some reason, whenever I needed to work something out in my life, I did that by significantly re-arranging my room in some new configuration to try out a new configuration in life. For example, one time I turned my bunk bed upside down, using boxes on the bottom bunk to make an inner fort chamber illuminated with tiny lights. Another time I papered an entire wall with AOL CD-Roms. I suspended heavy speakers in quadrophonic arrangement from the corners of the room using copper wire, staples, and other shenanigans. Sometimes I'd do this kind of thing to the home as well, which my family reluctantly tolerated. In retrospect, this functioned as a form of therapy for me. By changing my physical surroundings, I felt like I could morph into a different identity in order to handle change.
					- After studying music, I became an engineer, and for a long time, being a maker and an engineer has been the cornerstone of my adult identity. But now I'm realizing that I actually might need to reconsider and newly approach my relationship with design. How is it that I didn't end up a designer? It's actually a weird thing that I ended up an engineer instead of a designer. Now that my professional life has become more involved with combining distributed technical systems architecture, product design, AI and pedagogy, I might be better served by approaching my Identity through the lens of Design.
					- Maybe it's time for the Return.
		- ## AI, Counterculture and Struggle
		  collapsed:: true
			- I went to a conference this week where there were many sessions that discussed the role of AI in teaching and learning.
				- It always inspires me to be around people who venerate great teaching.
				- I was really struck by the static electricity in the air produced by the [[Cognitive/Dissonance]] between the potential for AI to both help and hurt both teaching and learning. The conference was ostensibly themed around the topic of trying to figure out how to make a degree still mean something while acknowledging that in 2026, this is under question as AI transforms the landscape, and there's more to great education than just weeding out those can't do something traditionally challenging.
				  collapsed:: true
					- DONE add [[Logseq/Entity/Concept]]ual overview and history of the idea of [[Cognitive/Dissonance]].
				- One of the speakers opened a session with a live poll that asked, "What is an AI Native course?" I was [[Challenge]]d by that question. I couldn't answer it well in the 60-90 seconds I was given to answer it. I intend to have a better answer for that next time the question comes up.
				- Most who have passed from being a teen into being a young adult have some familiarity with a pattern of emergent counterculture, a certain type of infectious hipness or pedigree that is conveyed or expressed by "yucking" someone else's "yum."
					- I'm reminded of a [[Joke]] a relative of mine heard once:
						- Q: What did the wincing [[Hipster]] say as he took the hot pizza out of his mouth?
						- A: *I did that way before it was cool*
				- Many of the cooler attendees had this kind of cool kid's negation syndrome when it comes to AI.
					- I asked the other people at my table what they thought about what an AI Native course would be, and the fact that I repeated the question on the screen to them was very distasteful to them. They acted as though I had asked them if they wanted to dig through my garbage can with me.
				- Not all critiques of AI in education are about being cool or hip, though; some are just fair, necessary and practical.
					- ### Educational Deflation
						- For example, let's say you are a professor in a school that consistently grades on a curve so only 20% of your students can earn the highest mark, and another 20% can earn the next mark down, and the rest earn the next mark down. Then if every student starts asking ChatGPT to do their homework, then grade inflation isn't a problem, but educational deflation is! The top mark is literally just as exclusive as it was ten years before, but it means something entirely different.
					- ### varieties of difficult experiences
						- Terms that came up again and again:
							- Productive Struggle
							- Desirable Difficulty
							- Fighting with the material
								- "To Pushback On"
								- "To Grapple With"
								- "To Wrestle With"
						- How do we make it just as inevitable for students to still *work hard*?
					- ### Librarian - Chatbots Short Circuit Learning
						- I heard a compelling talk from a librarian that talked about the problem with chatbots. Our goal is for students to ==become original thinkers that understand how to express themselves in a powerful tradition of intellectual attribution==.
						- But if you ask a chatbot to explain XYZ to you, it does so in a way that bypasses or sidesteps your learning needs:
							- 1 - to formulate your own sense of what questions are important to ask
							- 2 - to find and evaluate reputable sources
							- 3 - to struggle with determining which terms and vocabulary are important for you to understand and which you merely need to be familiar with
							- etc.
		- ## Not Quite Broken, After The Fall
		  collapsed:: true
			- ### maybe, revenge of the the fish
			  collapsed:: true
				- Last week, for the first time in my life, I dropped my [[iPhone]] into a pool of water. It was submersed for probably 15-30 seconds. I took the iPhone out of its case and let it try in a bed of Sillica Gel packets overnight to dry out. Ever since then, things have been behaving poorly.
					- Not before then, my [[Oura/Ring]] has regularly been not recording over night and struggling to connect to my [[iPhone]]. It might be a coincidence, but I think it happened for the first time only after the submersion occurred. The ring didn't fall in, and I'm sure it would have been fine if it did.
					- I've regularly had trouble getting my [[iPhone/Port/Lightning]] to connect. Multiple times in the last week, I double and triple checked the connection before I fell asleep, only to wake up and find that the battery was very low.
					- Perhaps these are coincidences. Perhaps, though, something related to the bluetooth or the power have been affected.
			- ### crisp repetition
			  collapsed:: true
				- Every fall since I was a teen, when the air is just starting to feel cool and the leaves are starting to change, I pair my bike commute with Steve Reich's *Variations for Winds, Strings and Orchestra* and John Adams' *Shaker Loops* as played by Edo da Waart and the [[US/CA/San Francisco]] symphony orchestra. It's a trippy way of celebrating the arrival of the season. There's something about pairing the tessellated sonic shapes with the leaves on the ground that gets me to connect with the rhythm of life.
					- DONE import these pieces of music according to the entity definitions above.
		- ## Making Music
		  collapsed:: true
			- ### Goal: Decrease Friction to Making And Then Sharing Music
				- I've been trying to get a synth podcast up for quite a while. I made a bit of progress yesterday on [[GitP/A]], but I got bogged down with the [[Distractor]]s of [[Secrets Management]] and [[Knowledge Gardening]].
					- When I first started Ghost in the Patch, in each "episode" I narrated my creation of [[Microfreak/UG/04 Presets]] step by step, using [[Jargon]] and key vocabulary. Usually, by the end of the episode, I had longer periods without narration as I just played. It was a bit like falling asleep or into a trance. That was nice, in a way, but it was more than just a bit tangled in approach. I knew that I might be able to use [[AI/Voice/to/Text]] turn my narration into a transcription, then relate that to keywords in the [[Microfreak/Docs]] and use that to examine the [[MIDI]] captures to provide more informed commentary or linkages between various sounds of different episodes.
						- I kind of planned to eventually use some kind of [[Embedding]] model to find similar parts from similar episodes, then use that to drive some kind of a knowledge garden and composition system.
					- The problem with this is that it got me out of the groove and made it harder to practice and express what I was feeling. Consider the difference between practicing piano and discussing detailed finger and hand movements and you'll likely be able to understand what I'm talking about.
					- Lately, including the episode in [[Music/Composition/Log/26/09/25 Fri]], I didn't have any commentary at all. It's great, because I can get into the zone more, and focus on the practice of making music. That felt good, and it served my purpose of decreasing the friction of making and sharing music.
					- That's fine, but a raw audio recording of experimental live improv on a synth seems to be a pretty stark format for a podcast. So this morning I was thinking that I just need some custom software. Ideally, I'd record the synth. Then I'd go out listening with my earbuds in while walking around, and I'd comment on it in a way that would be recorded. I might do this multiple times. Then I'd have AI kind of stitch these layered commentaries together. That way it's as easy as possible to get a rich discussion podcast going while also honoring the sanctity of the space in which I make music.