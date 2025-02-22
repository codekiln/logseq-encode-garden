tags:: [[Neo4j]]
created-by:: [[Person/Alison Cossette]]

- # [Smarter AI with GraphRAG – Connecting Structured & Unstructured Data for Better Retrieval](https://www.ai.engineer/summit/2025/schedule/smarter-ai-with-graphrag-connecting-structured-and-unstructured-data-for-better-retrieval)
	- Summary
	  collapsed:: true
		- **Date**: February 22, 2025
		- **Time**: 12:30 PM
		- Generative AI is only as good as the data it retrieves—but traditional RAG (Retrieval-Augmented Generation) is limited by flat, disconnected search. AI models struggle to connect structured data (databases, APIs) with unstructured data (docs, PDFs, chat logs), leading to incomplete answers and hallucinations.
		- Enter GraphRAG—a next-generation retrieval approach powered by Neo4j. This workshop will show you how graphs unlock deeper context, better reasoning, and enterprise-ready AI applications. No graph experience needed!
		- You’ll learn how to:
		- Integrate structured and unstructured data into a unified retrieval system.
		  Use GraphRAG to improve accuracy, explainability, and trust in AI-generated answers.
		  Leverage graph-native retrieval, embeddings, and hybrid search for better responses.
		  Apply GraphRAG to real-world use cases, from enterprise AI copilots to knowledge-driven automation.
		  Whether you’re building AI-powered search, chatbots, or intelligent assistants—GraphRAG makes AI retrieval smarter. Join us to learn how Neo4j can take your Generative AI applications to the next level.
		- [[Person/Alison Cossette]]
			- Alison Cossette is a dynamic Data Science Strategist, Educator, and Podcast Host. As a Developer Advocate at Neo4j specializing in Graph Data Science, she brings a wealth of expertise to the field. With her strong technical background and exceptional communication skills, Alison bridges the gap between complex data science concepts and practical applications. Alison’s passion for responsible AI shines through in her work. She actively promotes ethical and transparent AI practices and believes in the transformative potential of responsible AI for industries and society. Through her engagements with industry professionals, policymakers, and the public, she advocates for the responsible development and deployment of AI technologies. She is currently a Volunteer Member of the US Department of Commerce - National Institute of Standards and Technology’s Generative AI Public Working Group Alison’s academic journey includes Masters of Science in Data Science studies, specializing in Artificial Intelligence, at Northwestern University and research with Stanford University Human-Computer Interaction Crowd Research Collective. Alison combines academic knowledge with real-world experience. She leverages this expertise to educate and empower individuals and organizations in the field of data science. Overall, Alison Cossette’s multifaceted background, commitment to responsible AI, and expertise in data science make her a respected figure in the field. Through her role as a Developer Advocate at Neo4j and her podcast, she continues to drive innovation, education, and responsible practices in the exciting realm of data science and AI.
		- Alison Cossette, Data Science Strategist, Advocate, Educator
		  LinkedIn
		  Twitter
	- form: https://docs.google.com/forms/d/e/1FAIpQLScKDk4bwnHLBKhTZXJ4XP-YBkGLgUh3B1C7-mc38jC7r0BAUQ/viewform
	- ## Intro
		- problems with #RAG
			- how do I handle
				- relative information
				- temporal information
			- you can ground chunks in relevant context
			- try to find ways that you can connect the types of storage you have
				- vector dbs
				- unstructured data, structured data
			- the info you need to get back is rarely just the chunk
			- we want chains of thought
			- we want to give insight into how we cnn connect the pieces of data into one thing
		- we are considering #MCP to feed *into* a knowledge graph
	- ## Graph db theory - Neo4j Graph Components
		- ![image.png](../assets/image_1740246298715_0.png)
			- This slide explains **Neo4j Graph Components**, breaking them down into:
			- **Nodes**: Represent entities in the graph (e.g., a person or a car).
			- **Relationships**: Represent associations or interactions between nodes (e.g., "KNOWS," "LIVES WITH," "OWNS").
			- **Properties**: Attributes of nodes or relationships, including metadata like names, birthdates, or embeddings.
			- ### Example from the slide:
				- **Person ("Andre")** knows **Person ("Mica")**.
				- **Andre lives with Mica** and has a Twitter handle `@dan`.
				- **Andre drives a Volvo V70**, which has properties like brand, model, and description embedding.
				- This structure highlights how **Neo4j stores interconnected data efficiently**—a key advantage of graph databases over relational models.
		- terms
			- nodes
				- the nouns
			- relationships
				- interactions
			- properties
				- of nodes or relationships
			- *the vector is a FEATURE of the relationship*
			- in the image above, notice the `DescEmbedding`
		- ### [[graphrag.com]] is their recommendation for learning
			- ### Terms
			- #### Domain Graph
				- it could be that domain structured knowledge is extracted from unstructured
			- #### Lexical Graph
				- unstructured data
		- ![image.png](../assets/image_1740246700998_0.png)
			- This slide illustrates how a **Knowledge Graph** can be structured, separating it into two main components:
			- ### **1. Domain Graph**
			- Represents **topics** in a structured way.
			- Shows how **topics are extracted** from documents.
			- ### **2. Lexical Graph**
			- Represents **documents** and their granular components.
			- Documents are broken into **chunks** (e.g., paragraphs, sections).
			- A relationship (`HAS_CHUNK`) connects a document to its respective chunks.
			- ### **Key Takeaways**
			- **Knowledge Graphs** integrate domain-specific relationships (topics) with textual content (documents and chunks).
			- This structure enables **contextual linking** between extracted knowledge and text sources, useful for **Retrieval-Augmented Generation (RAG)**.
		- ### knowledge graph -> memory graph
			- ![image.png](../assets/image_1740246723611_0.png)
		- ### knowledge graph with domain, lexical and memory graph
			- ![image.png](../assets/image_1740246865344_0.png)
				- cgpt-notes
					- This slide presents a **comprehensive Knowledge Graph structure**, integrating **Domain Graph, Lexical Graph, and Memory Graph**.
					- ### **1. Domain Graph (Structured Knowledge)**
					- Represents **entities and relationships**.
					- Example:
						- **Entity Type A** → relates to → **Entity Type B**.
						- **Entity Type B** → PRODUCES → **Document**.
						- **Entity Type C** → HAS_ENTITY → **Document**.
					- ### **2. Lexical Graph (Unstructured Knowledge)**
					- Links **documents** to their **chunks** (smaller text segments).
					- Example:
						- **Document** → HAS_CHUNK → **Chunk**.
					- ### **3. Memory Graph (Application-Level Interactions)**
					- Represents user interactions within a system.
					- Example:
						- **User** → OPENS → **Session**.
						- **Session** → CONTAIN → **Prompt**.
						- **Prompt** → NEXT → **Response**.
						- **Prompt** → RETRIEVES → **Chunk**.
						- **Response** → INCLUDES → **Chunk**.
					- ### **Key Takeaways**
					- This model **bridges structured and unstructured data**, making it ideal for **LLM-powered Retrieval-Augmented Generation (RAG)**.
					- **Memory Graph** ensures **context retention** by linking user prompts to relevant knowledge chunks.
					- **Lexical and Domain Graphs** provide structured and unstructured content retrieval for AI applications.
					  
					  This setup is well-suited for **AI-driven search, chatbots, or recommendation systems**.
			- #### example
				- which companies are susceptible to a lithium shortage
					- which *asset managers* are vulnerable to a lithium shortage
						- who are the managers that own those companies
				- getting the answer you need will cross the traversal from the lexical into the domain
				- *this is how humans answer questions*
				- what we haven't had an ability to do so far, and what we are challenged by is how do we provide that meta moment where we get the EXACT retrievals that we need
			- #### example
				- data science in rag apps
				- what are the subjects that people are communicating on
				- what are the areas of knowledge that they are interacting on
				- they came in asking about this and they left asking about that
				- having this understanding ... as a builder itmmight not be important to you, but to product owner, highly relevant
				-
			-
		-