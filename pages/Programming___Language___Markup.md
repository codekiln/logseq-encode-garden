alias:: [[Markup Language]]
tags:: [[Term]], [[Diataxis/Explanation]], [[Writing/Co-Written with AI]]
cgpt-link:: https://chatgpt.com/g/g-p-682deb17f048819181695404ef94a48a-diataxis-logseq/c/687ba400-a500-8329-9df1-d4eb0b459454?model=gpt-4o

- # Markup Language
	- ## Overview
		- A markup language is a notation system embedded within text to annotate its structure, formatting, or semantic meaning, without performing computation itself.
	- ## Context
		- Markup languages emerged to separate the structure and presentation of documents from their actual content, enabling consistency, interoperability, and readability across different systems.
	- ## Key Principles
		- **Declarative nature** – Markup languages describe *what* content is, not *how* computational tasks should be performed.
		- **Embedded annotation** – Markup instructions are directly included within the text.
		- **Human readability** – Designed to be easily written, understood, and modified by humans.
	- ## Mechanism
		- Markup languages employ symbols, tags, or special syntax embedded within plain text to define elements such as paragraphs, headings, or lists.
		- These annotations are then interpreted by a rendering engine or parser, which processes the markup to display, structure, or transport the document content.
		- Unlike programming languages, markup languages do not support logical operations or algorithmic execution.
	- ## Examples
		- HTML (HyperText Markup Language):
			- ~~~html
			  <h1>Welcome to Markup</h1>
			  <p>This is an example paragraph.</p>
			  ~~~
		- Markdown (Lightweight markup for formatting):
			- ~~~markdown
			  ## Welcome to Markup
			  This is an example paragraph with **bold text**.
			  ~~~
		- XML (eXtensible Markup Language):
			- ~~~xml
			  <note>
			    <to>User</to>
			    <from>Assistant</from>
			    <message>Hello!</message>
			  </note>
			  ~~~
		- LaTeX (Scientific and academic typesetting):
			- ~~~latex
			  \section{Introduction}
			  This document explains markup languages.
			  ~~~
		- AsciiDoc (Technical documentation):
			- ~~~asciidoc
			  == Introduction
			  This document explains markup languages.
			  ~~~
		- YAML (Configuration and data serialization):
			- ~~~yaml
			  title: Introduction
			  content: This document explains markup languages.
			  ~~~
		- reStructuredText (Used in Python documentation):
			- ~~~rst
			  Introduction
			  ============
			  This document explains markup languages.
			  ~~~
	- ## Misconceptions
		- **Markup languages as programming languages** → Markup languages do not execute logic, control flow, or algorithms; they simply describe structure or formatting.
		- **HTML as a purely presentational language** → Modern HTML (HTML5) emphasizes semantic structure, not just visual formatting.
		- **Markup languages always require angle brackets (`< >`)** → Some markup languages, like Markdown or YAML, use other syntactic approaches like indentation or plain symbols.
	- ## Related
		- [[Programming Language]] · [[HTML]] · [[XML]] · [[Markdown]]