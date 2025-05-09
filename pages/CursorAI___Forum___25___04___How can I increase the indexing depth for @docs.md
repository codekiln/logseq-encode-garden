created-by:: [[Person/codekiln]]
date-created:: [[2025-04-11 Fri]]

- # [How can I increase the indexing depth for @docs? - Discussion - Cursor - Community Forum](https://forum.cursor.com/t/how-can-i-increase-the-indexing-depth-for-docs/77949)
	- ## #[[Original Poster]]
		- I love the `@docs` feature, but I haven't yet figured out how to get it to index the parts of the docs I care about.
		- This morning I tried indexing https://mise.jdx.dev/ and it ended up only indexing the surface-level 10 pages, when the whole site has 50+ pages.
		- I tried a specific page, Getting Started | mise-en-place, and it indexed 16 pages.
		- The official Cursor documentation at Cursor – @Docs doesn't mention the indexing depth. Does it only go one level deep? Two levels deep? Does it traverse arbitrary depths but max out at a certain point? Is it using LLM preprocessing to try to infer the most interesting pages?
		- I've recently used GitHub - langchain-ai/mcpdoc: Expose llms-txt to IDEs for development to endow agent mode with the knowledge of the langgraph docs outside of the docs feature. langgraph LLMS-txt. If there was a way to turn an arbitrary docs site into a llms.txt file, I'd perhaps use that instead of cursor's @docs.
		- In addition, I have seen an instance where for a particular docs site it stated that it "Indexed 8 pages" but I counted much more than 8 entries in the list below that heading, but still much less than the full number of pages, so I'm not really sure what the number even corresponds to or how to think about this feature.
	- ## #[[Response]]
		- [[Person/Eric Zakariasson]]
			- > Yeah this is not in an ideal state and we want to make it better for sure!
	- ## #[[Related/Post]]
		- [Indexing https://llmstxt.org/ format to docs](https://forum.cursor.com/t/indexing-https-llmstxt-org-format-to-docs/62833)
		- [What does @docs document?](https://forum.cursor.com/t/what-does-docs-document/31888)
		- [More details on how the @docs work](https://forum.cursor.com/t/more-details-on-how-the-docs-work/17552)
		- [Documentation ingestion](https://forum.cursor.com/t/documentation-ingestion/44402)
		- [Need more information about how doc indexing works](https://forum.cursor.com/t/need-more-information-about-how-doc-indexing-works/42330)