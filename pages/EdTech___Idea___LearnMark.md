# LearnMark - an [[LMS]]-neutral, [[Markdown]] with [[Markdown Yaml Frontmatter]]-based format for Modular Course Segments and Materials
	- Years ago I was into the [[Jamstack]], and spent some time thinking about how [[LMS/Courses]] could be represented using that setup.
	- Lately I've been considering an idea on how to formulate that idea into an open source, LMS-agnostic format for modular course materials. The "how" has many options, but one obvious option would be [[Markdown Yaml Frontmatter]] that adhered to a documented schema, which is the common format used by many Jamstack products.
	- The nice thing about [[Markdown]] with [[yaml]] frontmatter is that **both humans and LLMs can read or write them with ease**.
	- As a result of these properties, humans and AI could work together to **break courses down** into [[LMS Course Segments]], and **AI could help with re-authoring them** in a way that stitched them together.
	- If an LMS can write an exporter and an importer that translated from their format to LearnMark, it would enable courses to be exported to LearnMark, and then an AI system could be used on the LearnMark to identify the re-usable segments, where they could be re-uploaded up to the source platforms.
	- ## Metadata that could be a part of the YAML Frontmatter
		- Metadata that should travel along with the segments could include the following - see also [[IEEE/LOM]] or [[Dublin Core Metadata]]
			- content creation info
				- the duration of the segment or the average time a student would need for the segment
				- when the content was created or updated
				- copyright
				- authors
			- topics & prerequisites
				- the difficulty level
				- tagging
			- entity info
				- subjects
				- entities (companies, etc)
	- ## Prior Art - [[EdTech/Idea/LearnMark/Q/What precedents exist for LMS-agnostic format]]
		- see above for annotated deep research query