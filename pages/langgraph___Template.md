alias:: [[LangGraph Template]], [[LangGraph Templates]]

- # [LangGraph Templates](https://studio.langchain.com/?ref=blog.langchain.dev)
	- See also [LangChain - Changelog | 📐 LangGraph Templates: Build configurable](https://changelog.langchain.com/announcements/langgraph-templates-build-configurable-agentic-workflows)
	- ## [[My Notes]]
		- contains a bunch of different [[GitHub/Repo]]s showing how to do things like use configurable fields
			- Example
				- [rag-research-agent-template/src/retrieval_graph/configuration.py at main · langchain-ai/rag-research-agent-template](https://github.com/langchain-ai/rag-research-agent-template/blob/main/src/retrieval_graph/configuration.py)
				- [retrieval-agent-template/src/retrieval_graph/retrieval.py at main · langchain-ai/retrieval-agent-template](https://github.com/langchain-ai/retrieval-agent-template/blob/main/src/retrieval_graph/retrieval.py) has this pattern using [[Py/Context Manager]] and [[Py/Generator]]
					- ```python
					  @contextmanager
					  def make_retriever(
					      config: RunnableConfig,
					  ) -> Generator[VectorStoreRetriever, None, None]:
					      """Create a retriever for the agent, based on the current configuration."""
					      configuration = IndexConfiguration.from_runnable_config(config)
					      embedding_model = make_text_encoder(configuration.embedding_model)
					      user_id = configuration.user_id
					      if not user_id:
					          raise ValueError("Please provide a valid user_id in the configuration.")
					      match configuration.retriever_provider:
					          case "elastic" | "elastic-local":
					              with make_elastic_retriever(configuration, embedding_model) as retriever:
					                  yield retriever
					  
					          case "pinecone":
					              with make_pinecone_retriever(configuration, embedding_model) as retriever:
					                  yield retriever
					  
					          case "mongodb":
					              with make_mongodb_retriever(configuration, embedding_model) as retriever:
					                  yield retriever
					  
					          case _:
					              raise ValueError(
					                  "Unrecognized retriever_provider in configuration. "
					                  f"Expected one of: {', '.join(Configuration.__annotations__['retriever_provider'].__args__)}\n"
					                  f"Got: {configuration.retriever_provider}"
					              )
					  ```
					- note that a sample configuration is using [[Py/Dataclass]] - what exactly is this `__template_metadata__` - it's probably something specific to the templates, but is this how we make it show up in teh UI?
						- ```python
						  @dataclass(kw_only=True)
						  class IndexConfiguration:
						      """Configuration class for indexing and retrieval operations.
						  
						      This class defines the parameters needed for configuring the indexing and
						      retrieval processes, including user identification, embedding model selection,
						      retriever provider choice, and search parameters.
						      """
						  
						      user_id: str = field(metadata={"description": "Unique identifier for the user."})
						  
						      embedding_model: Annotated[
						          str,
						          {"__template_metadata__": {"kind": "embeddings"}},
						      ] = field(
						          default="openai/text-embedding-3-small",
						          metadata={
						              "description": "Name of the embedding model to use. Must be a valid embedding model name."
						          },
						      )
						  
						      retriever_provider: Annotated[
						          Literal["elastic", "elastic-local", "pinecone", "mongodb"],
						          {"__template_metadata__": {"kind": "retriever"}},
						      ] = field(
						          default="elastic",
						          metadata={
						              "description": "The vector store provider to use for retrieval. Options are 'elastic', 'pinecone', or 'mongodb'."
						          },
						      )
						  
						      search_kwargs: dict[str, Any] = field(
						          default_factory=dict,
						          metadata={
						              "description": "Additional keyword arguments to pass to the search function of the retriever."
						          },
						      )
						  
						      @classmethod
						      def from_runnable_config(
						          cls: Type[T], config: Optional[RunnableConfig] = None
						      ) -> T:
						          """Create an IndexConfiguration instance from a RunnableConfig object.
						  
						          Args:
						              cls (Type[T]): The class itself.
						              config (Optional[RunnableConfig]): The configuration object to use.
						  
						          Returns:
						              T: An instance of IndexConfiguration with the specified configuration.
						          """
						          config = ensure_config(config)
						          configurable = config.get("configurable") or {}
						          _fields = {f.name for f in fields(cls) if f.init}
						          return cls(**{k: v for k, v in configurable.items() if k in _fields})
						  ```
		- #Via [Launching LangGraph Templates](https://blog.langchain.dev/launching-langgraph-templates/)
	-