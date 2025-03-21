# [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research)
	- ## Official Summary
	  id:: 67ddbd2a-e19a-463e-9d98-0b536883ce59
		- Available search tools:
			- [Tavily API](https://tavily.com/) - General web search
			- [Perplexity API](https://www.perplexity.ai/hub/blog/introducing-the-sonar-pro-api) - General web search
			- [Exa API](https://exa.ai/) - Powerful neural search for web content
			- [ArXiv](https://arxiv.org/) - Academic papers in physics, mathematics, computer science, and more
			- [PubMed](https://pubmed.ncbi.nlm.nih.gov/) - Biomedical literature from MEDLINE, life science journals, and online books
			- [Linkup API](https://www.linkup.so/) - General web search
			- [DuckDuckGo API](https://duckduckgo.com/) - General web search
			- [Google Search API/Scrapper](https://google.com/) - Create custom search engine [here](https://programmablesearchengine.google.com/controlpanel/all) and get API key [here](https://developers.google.com/custom-search/v1/introduction)
		- Open Deep Research uses a planner LLM for report planning and a writer LLM for report writing:
		- You can select any model that is integrated [with the `init_chat_model()` API](https://python.langchain.com/docs/how_to/chat_models_universal_init/)
		- See full list of supported integrations [here](https://python.langchain.com/api_reference/langchain/chat_models/langchain.chat_models.base.init_chat_model.html)