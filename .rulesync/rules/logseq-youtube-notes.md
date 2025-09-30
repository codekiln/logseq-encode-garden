---
root: false
targets:
  - '*'
description: 'How to intake and format notes on a youtube video'
globs: []
---
# Logseq-Flavored Markdown (LFM) YouTube transcript headings

This rule applies to 'pages/*.md' that have a YouTube video with a transcript. It is an extension to Logseq Flavored Markdown (project rule in `logseq-flavored-markdown.mdc`).

Youtube video begins with a block like this:

```
	- ## [[Video]]
		- {{video https://www.youtube.com/watch?v=abcdefghijklmnop}}
			- NOTES SHOULD GO HERE UNDERNEATH THE VIDEO
```

## Basic Transcript Organization

The transcript should be organized with logical sections and proper hierarchical headings. Each major section should start with a timestamp-based heading. THE HEADINGS MUST BE NESTED UNDER THE VIDEO AND INCLUDE TIMESTAMPS for them to be clickable in logseq. Maintain proper logseq-flavored markdown throughout. Use quotes from the transcript and clean up the transcript, attempting to fix spelling or technology names where appropriate. The transcript of youtube videos is done by AI and may contain mistakes you should try to correct based on the context.

### Heading Structure
- Use `### {{youtube-timestamp X}}` for main sections
- Use `####` for subsections
- Use `#####` for detailed points within subsections
- Always maintain proper indentation using TABs

### Semantic Linking / Logseq Page Links
- Convert relevant terms into Logseq Page Links using `[[Topic]]` format if and onl if a given Logseq Page is known known to exist
- Do not invent link to Logseq Pages that do not already exist
    - if you invent a logseq page to link to it will just introduce a duplicate into the knowledge management system, so do not do that 
- Some common ones you CAN use
    - #Example
	- [[AI Coding]]
	- [[Py]] for python
	- see `pages/Index.md` for a list of pages you can link to

### Content Formatting
- Break long monologues into natural speech patterns
- Use bullet points for lists and sub-points
- Use **bold** for emphasis on key concepts
- Group related ideas under appropriate subheadings

### Example of Improved Formatting:

<BEFORE>
	- ## [[Video]]
		- {{video https://www.youtube.com/watch?v=FPTlP6Adefo}}
			- ... (many lines)
			- {{youtube-timestamp 364}} here Right so let's start with the classic the foundational AI coding tool You already know what I'm going to say Let's start with ADER Okay So we're going to use Ader like our control Right this is our kind of base level item Let's just walk through the variables
			- {{youtube-timestamp 378}} and let's give Ader a compute advantage Okay so compute scaling ADER is very bare metal It can use any single model but it doesn't have any super duper insane tricks to scale up the compute you're using right you're basically just calling the model You can use architect
			- {{youtube-timestamp 394}} mode So I'm going to drop this down to 25 And you can see there you know as I decrease this our compute advantage goes from 16 down to 8 Okay so comput scaling and autonomy have a massive impact on your compute advantage So autonomy ader
			- {{youtube-timestamp 411}} is not an autonomous tool at all right it's a bare metal um python application right it does have some nicities to it but in terms of AI running itself in terms of agentic loops and agentic capabilities ader has no true autonomy okay so we're going to drop that all the
			- {{youtube-timestamp 428}} way down to five for time effort and monetary costs these are all the variables that we don't want right so we want to decrease these as much as possible right in the perfect world Um this tool takes no time no effort and costs nothing Okay And so you can see
			- {{youtube-timestamp 443}} there our compute advantage went up So obviously no tool like this exists Um there are costs always associated with any tool you're using So let's be more realistic right um how much time does ADER take it doesn't take a ton of time Actually it is very helpful because it
			- {{youtube-timestamp 458}} prevents you from having to write code yourself So we're going to drop this down to 25 It's pretty good Effort on the other hand is going to be a little bit higher So we're just going to say 50 and monetary costs This is where Ader is a big big winner right this is open-
			- {{youtube-timestamp 472}} source technology Okay and the only costs you have are the costs of the model So we'll go ahead and just set this to 10 This is the first tool we're adding So I'm going to hit save tool here And so now you can see we have a personal compute advantage leaderboard
</BEFORE>

<AFTER>
	- ## [[Video]]
		- {{video https://www.youtube.com/watch?v=FPTlP6Adefo}}
			- ... (many lines)
			- ### {{youtube-timestamp 364}} Analysis of [[AI Coding]] Tools
				- #### Aider as the Baseline
					- Introduction as foundational tool:
						- "Let's start with the classic the foundational AI coding tool... Let's start with ADER"
						- "We're going to use Ader like our control Right this is our kind of base level item"
					- #### Compute Scaling Assessment
						- Bare metal characteristics:
							- "compute scaling ADER is very bare metal"
							- "can use any single model but it doesn't have any super duper insane tricks to scale up the compute"
							- "you're basically just calling the model"
						- Impact on compute advantage:
							- "as I decrease this our compute advantage goes from 16 down to 8"
					- #### Autonomy Evaluation
						- Limited autonomy:
							- "not an autonomous tool at all"
							- "bare metal python application"
							- "in terms of AI running itself in terms of agentic loops and agentic capabilities ader has no true autonomy"
					- #### Cost Analysis
						- Time and effort considerations:
							- "doesn't take a ton of time"
							- "very helpful because it prevents you from having to write code yourself"
							- "Effort on the other hand is going to be a little bit higher"
						- Monetary advantage:
							- "this is where Ader is a big big winner"
							- "this is open-source technology"
							- "the only costs you have are the costs of the model"
					- #### Unique Strengths
						- Programmability:
							- "Ader is a programmable AI assistant"
							- "You can take it and build out workflows that you cannot build with cursor"
						- Customization:
							- "With Ader you can of course select any single model you want"
							- "it's a lot more customizable"
</AFTER>

### Additional Guidelines
1. Keep timestamps at the most relevant points, but don't let them break the flow of ideas
2. Use semantic links to connect related concepts across notes
3. Break long monologues into digestible bullet points
4. Maintain hierarchy with proper indentation
5. Add structure with subsections when content is complex
6. Use emphasis (**bold**) for key concepts
7. Include `#Example` tags for practical examples
8. Add `[[Key Insight]]` markers for important takeaways
9. DO NOT CREATE ANY HEADING that lacks unordere list items UNDERNEATH it. Preferably each heading should last at least 90 seconds. Try not to make too many headings representing smaller sections. Ideally they should correspond to chapters in the youtube video

Remember: The goal is to make the transcript more readable and navigable while preserving the semantic connections between concepts.

If possible, visit the youtube URL and see what the chapters are, and name the headings after that. If that is not possible, use your best judgment or ask the user about how to group the sections of the transcript.
