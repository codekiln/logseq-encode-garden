tags:: [[Idea]], [[Software/Library]]

- # Cross-Platform #Diagramming #DSL #[[Markup Language]]
	- ## Problem
		- ### Diagramming is an afterthought in every programming language
			- When helping engineers with technical tasks, #LLM based [[AI Agents]] need to be able to communicate architectural ideas to both humans and other agents. Currently, LLMs can produce [[Mermaid Diagram]] in [[Mermaid]], but the only way to render that is to call [[Mermaid/mmdc]], a CLI tool which actually, according to [[Mermaid/DeepWiki]], uses [[Puppeteer]], a [[Browser/Headless]], to render the image.
		- ### Inspiration
			- As a result, [[ChatGPT/Code/Interpreter]] cannot compile to verify the syntax of the mermaid diagrams it generates, as it only has access to a python interpreter with mostly [[Native Implementation]] libraries.
		- ### Suggestion
			- Instead, we should create a language specification for a text to diagram markup language which is intended to produce [[Native Implementation]]s of the rendering behavior in each target language using [[AI Coding]].
		-
	-
-