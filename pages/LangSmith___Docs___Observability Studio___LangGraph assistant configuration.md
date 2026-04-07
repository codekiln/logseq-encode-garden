# [Observability in Studio — full example configuration](https://docs.langchain.com/langsmith/observability-studio#full-example-configuration)
	- Popped out from [[2025-12-24]] (was under [[LangChain/Ecosystem]]) so the LangGraph assistant configuration recipe is one link away.
	- See also [[langgraph/Docs/Cloud/How To/Prompt Engineer in LangGraph Studio]] for `langgraph_nodes`, `langgraph_type`, and how Studio binds fields to nodes.
	- For some reason it's always so hard for me to find this page, which is, to the best of my knowledge, one of the only pieces of documentation that shows how to configure LangGraph assistants using `Annotated[Literal[...]]` and `json_schema_extra`.
	- ### Pydantic and dataclass examples
		- ```python
		  ## Using Pydantic
		  from pydantic import BaseModel, Field
		  from typing import Annotated, Literal
		  
		  class Configuration(BaseModel):
		      """The configuration for the agent."""
		  
		      system_prompt: str = Field(
		          default="You are a helpful AI assistant.",
		          description="The system prompt to use for the agent's interactions. "
		          "This prompt sets the context and behavior for the agent.",
		          json_schema_extra={
		              "langgraph_nodes": ["call_model"],
		              "langgraph_type": "prompt",
		          },
		      )
		  
		      model: Annotated[
		          Literal[
		              "anthropic/claude-sonnet-4-5-20250929",
		              "anthropic/claude-haiku-4-5-20251001",
		              "openai/o1",
		              "openai/gpt-4o-mini",
		              "openai/o1-mini",
		              "openai/o3-mini",
		          ],
		          {"__template_metadata__": {"kind": "llm"}},
		      ] = Field(
		          default="openai/gpt-4o-mini",
		          description="The name of the language model to use for the agent's main interactions. "
		          "Should be in the form: provider/model-name.",
		          json_schema_extra={"langgraph_nodes": ["call_model"]},
		      )
		  
		  ## Using Dataclasses
		  from dataclasses import dataclass, field
		  
		  @dataclass(kw_only=True)
		  class Configuration:
		      """The configuration for the agent."""
		  
		      system_prompt: str = field(
		          default="You are a helpful AI assistant.",
		          metadata={
		              "description": "The system prompt to use for the agent's interactions. "
		              "This prompt sets the context and behavior for the agent.",
		              "json_schema_extra": {"langgraph_nodes": ["call_model"]},
		          },
		      )
		  
		      model: Annotated[str, {"__template_metadata__": {"kind": "llm"}}] = field(
		          default="anthropic/claude-3-5-sonnet-20240620",
		          metadata={
		              "description": "The name of the language model to use for the agent's main interactions. "
		              "Should be in the form: provider/model-name.",
		              "json_schema_extra": {"langgraph_nodes": ["call_model"]},
		          },
		      )
		  ```
