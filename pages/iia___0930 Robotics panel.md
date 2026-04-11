# [Robotics at Scale Shipping autonomous systems that work outside the lab — the engineering, regulatory, and commercial hurdles of deploying robots and drones at scale.](https://imaginationinaction.co/2604mit/stages/atrium)
	- meta
	  collapsed:: true
		- [Panel]
		- [Sustaining Intelligence]
		- 9:30 AM
		- Panelists
			- [[Person/Navid Aghasadeghi]] moderator
				- AI & Robotics
				- Founder & CEO
			- [[Person/Alexander Wissner-Gross]]
				- Founder & Investor
				- last person to get 3 degrees, math, physics, CS, then phd from harvard, crazy
			- [[Person/Annika Thomas]] [[Robot/ics/Space]]
				- MIT Dept. Mechanical Engineering
				- PhD Candidate
			- [[Person/Hasan Khan]]
				- [[Formlabs]] making [[Print/er/3d]] which is a form of [[Robot/ics]]
					- Product & AI
					-
	- topics
		- 09:30 what's different this time? was there one experience or demo or product you saw which made you think, this time it's actually going to work?
			- [[Person/Alexander D. Wissner-Gross]]
				- computer vision got **solved**
				- willow robotics guys
				  collapsed:: true
					- asked them: what is the hardest? single number one problem
				- action models are on scaling law curve
				- [[AI/Model/Action]] are on [[Law/Scale/Curve]]
				- [[AI/Model/World]] are on [[Law/Scale/Curve]]
				- [[The Singularity]] is not one thing, it started with [[AlexNet]] and the curves are smooth from there
				- we're basically "there" for some definition of "there" at this moment
				- don't think [[AI/The Bitter Lesson]]
			- [[Person/Annika Thomas]]
				- [[Vision/Computer]] is solved in a sense, but we are working with limited compute [[IRL]]
				  collapsed:: true
					- we have multiple world robots
					- there are lots of limitations in the hardware in order to make these
					- embedded systems are harder
			- [[Person/Hasan Khan]]
				- [[Google/Glass]] -> [[Apple/Vision/Pro]] progression is amazing
			- [[Person/Annika Thomas]]
				- [[SLAM]] [[Acronym]] = simultaneous localization and mapping
				  collapsed:: true
					- they have to solve the estimation problem of where we are at in reference to the chair
					- she thinks slam is solved in small-scale indoor settings, but outdoors with dynamic settings
			- [[Person/Alexander D. Wissner-Gross]]
				- he just wrote [[Person/Alexander D. Wissner-Gross/Book/Solve Everything]]
				  collapsed:: true
					- he's talking about the idea that all that there is is to pour on more scale
					- "do you think asymptotic leaps are necessary?"
			- [[Person/Annika Thomas]]
				- difference between [[AI/LLM]]s and [[AI/Robot/ics]] is [[Data/Set/Availab/ility]]
				- she talks about a paper that came out years ago where everyone came together to combine data, but nobody uses it because it's too messy
	- [[Person/Navid Aghasadeghi]] let's go deeper into data. how do you think about how [[Robot/ics]] can deal with separate layers of intelligence stack?
		- [[Person/Alexander D. Wissner-Gross]]
			- elephant in room: what do you pre-train off of?
			- we are seeing pre-training off of [[YouTube]] and pre-recorded data
				- you can get really far on this
				- first-person, third-person doesn't make much of a difference
			- then you fine-tune on custom data
			- he thinks there's no data scarcity - frontier labs have better access to the compute to make use of the corpora that are already available
			- we are post-data scarcity from my standpoint [[Take/Hot]]
	- [[Person/Navid Aghasadeghi]] ok, so intelligence is about to be solved, but we don't see millions of robots around us. it's really hard to deploy robots at scale. [[Person/Hasan Khan]] has deployed lots of [[3d Printer]]s
		- [[Person/Hasan Khan]]
			- [[3d Printer]]s are autonomous goal-oriented systems
				- they are facing similar challenges to [[Robot/ics]]
				- people have [[Hesitation]] about [[AI]] because they tried, old, bad AI
			- a lot of people are worried about [[Job/Loss]] or [[Skill/Atrophy]]
	- [[Person/Annika Thomas]]
		- we've always had one part that works on perception, localization, navigation, and now we have people working on [[AI/Model/End/to/End]], and she's worried about that in terms of [[AI/Safe/ty]] and [[Repro/duc/ibility]]
			- when we put [[Swarm]]s of [[Robot]]s out there, I want to know why a [[Mistake]] happened
	- 09:50 [[Person/Alexander D. Wissner-Gross]]
		- the implied trade-off between safety and capability is a false dichotomy
			- we've seen that in [[Tesla/FSD]] with more recent iterations, they introduced modularity
			- it's very much possible to maintain modularity and [[Super/vision]] and and maintain [[End/to/End]] "Differentiable" solutions
	- 09:52 [[Person/Navid Aghasadeghi]] is safety a "feature" of the system Alex?
		- [[Person/Alexander D. Wissner-Gross]]
			- you get there by having rigorous [[AI Evals]]
		- 09:53 [[Person/Annika Thomas]]
			- with [[Diff/eren/tiabil/ity]] we will get there
			- I want to emphasize that you made a great point about [[AI Evals]]. Many of those systems in the past were based on [[Average]] [[Performance]], but we need [[Cert/if/iab/ility]], and [[Case/Edge]] matters.
	- 09:54 [[Person/Navid Aghasadeghi]] we think about replacing physical jobs with [[Robot/ics]], but where are the opportunities to expand the market, such as for applications in [[Space]]?
		- [[Person/Annika Thomas]]
			- this is what got me into robitcs - space
			- [[NASA]] administrator jared something said we will focus on settlements on the [[Moon]]
				- to do that we need [[Robot/ics/Space]] and autonomy
				- they just patented radiation shielding with bricks that are fully constructed on the moon autonomously [[Cool]]
				- [[AI/Response]]
					- You’re likely thinking of [[Person/Jared Isaacman]], not the NASA Administrator.
					- **NASA Administrator** is [[Person/Bill Nelson]]
					- Isaacman has been publicly discussing long-term human presence beyond Earth, including the Moon, in the context of private spaceflight and collaboration with NASA.
					  
					  For actual NASA policy language about Moon settlements, the authoritative framing comes from the **Artemis Program**, which explicitly states goals like:
					- “sustainable human presence on the Moon”
					- building infrastructure that enables longer-term habitation
					  
					  Primary sources you can use:
					- [https://www.nasa.gov/artemis/](https://www.nasa.gov/artemis/)
					- [https://www.nasa.gov/humans-in-space/artemis/](https://www.nasa.gov/humans-in-space/artemis/)
					  
					  If you want the exact quote you heard, it’s probably from:
					- a recent panel/interview featuring Isaacman discussing future human expansion
					- or a paraphrase of NASA’s “sustainable presence” language rather than a literal “settlements” quote from Nelson
					  
					  Key distinction:
					- NASA (Nelson): “sustainable presence”
					- Isaacman / private sector: more willing to say “settlements” explicitly
	- 09:59 [[Person/Alexander D. Wissner-Gross]]
		- he says "the economy is cooked"
			- even doctors
			- 'belmals cost disease'
		- next weekend - [[ProRL]] will focus first professional [[Robot/ics]] Marathon.
			- this is the first time in US history where we will have robots in the streets in the [[US/MA/Boston/Seaport]] [[Cool]]
				- [[Robot/Olympics]]
			- "come to the combine [[2026-04-19 Sun]]"
	- 10:04 comment from crowd - I just saw an [[OpenClaw]] bot to [[Blender]] designing [[3d/Model]]s, how will that impact things?
		- [[Person/Hasan Khan]]
			- when [[Robot]] can [[Hill Climb]], that's the new point.
	- 10:05 we talked about solved vs unsolved problems. What are unsolved problems in [[LLMs]] vs need for [[AI/Model/World]] [[Question]]
		- [[Person/Annika Thomas]]
			- [[LLM]]s are the bridge between the environment and the [[Robot/ics]] between perception and [[Plan/ing]].
			- something like [[LIDAR]] has uncertainty associated with it, *world models help with that?*
	-