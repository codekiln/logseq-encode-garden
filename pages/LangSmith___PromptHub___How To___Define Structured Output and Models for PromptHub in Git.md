# TODO find way to commit prompts locally and publish them to LangSmith PromptHub using Structured Output and model definitions
	- ## Query
		- What I want is something that facilitates defining prompts locally in my python codebase, defining the structured output definitions and models I want, then upload the prompt once for each model or structured output definition to the prompt hub in a private enterprise setting (I have langsmith enterprise).
		- The goal is to be able to push prompts with model parameters and schemas up to Prompt Hub, pull them back down, and keep them under version control in code.
	- ## [[ChatGPT/Response]]
		- Short answer: I couldn’t find a well-maintained, widely-used **community** Python library that sits *on top* of the LangSmith SDK and provides a full higher-level Prompt-Hub workflow (define prompts + structured outputs + multiple model variants locally, push one commit per model/schema, pull back and keep everything git-versioned) — most teams either use the official LangSmith SDK (or LangChain’s limited hub helpers), or they use general prompt-management tools (git-native or testing/eval tools) and glue code/CI to push to LangSmith. ([LangSmith Docs](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client))
		  
		  Below I list the concrete things I found (what exists, what’s missing), then a short, copy-pasteable Python helper you can use immediately to get the workflow you described (since the ecosystem currently lacks a polished community library that already does it).
		- # What I found (summary)
		- **Official LangSmith SDK is the canonical/official path.**
		  
		  `Client.push_prompt()` / `pull_prompt()` are the supported APIs for programmatic prompt management (you can push prompt templates and *RunnableSequence* (prompt|model)). That is the *recommended* route and what most projects call directly. ([LangSmith Docs](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client))
		- **Structured prompt (Pydantic schema) push is currently fragile / problematic.**
		  
		  There are active issues/threads in the LangSmith SDK repo showing pushing a `StructuredPrompt` that embeds a Pydantic model fails for many users (so programmatic commits of StructuredPrompt + Pydantic schema are not reliably supported at time of writing). That gap is one reason community wrappers that fully automate schema->PromptHub workflows are rare. ([GitHub](https://github.com/langchain-ai/langsmith-sdk/issues/1462?utm_source=chatgpt.com))
		- **Official helper tooling exists for migration / bulk operations, but it’s official not community abstraction.**
		  
		  LangChain org maintains a LangSmith migration tool that can migrate prompts and prompt versions between workspaces (useful for enterprise workflows), but again this is an official utility rather than a community “high-level PromptHub client library.” ([GitHub](https://github.com/langchain-ai/langsmith-data-migration-tool))
		- **There are many community prompt-management projects — but they are general purpose (git-native, testing, eval) rather than LangSmith-centered high-level wrappers.** Examples:
			- **PromptOps / promptops** — git-native prompt management frameworks (store prompts in repo, test, CI). Good for keeping prompts under version control; you’d still need a small integration to push to LangSmith. ([GitHub](https://github.com/llmhq-hub/promptops?utm_source=chatgpt.com))
			- **Promptfoo** — strong open-source tool for prompt tests/CI/evals (useful to gate prompt changes in PRs). Not a LangSmith prompt-hub wrapper, but pairs well with a small push tool to sync to LangSmith. ([GitHub](https://github.com/promptfoo/promptfoo?utm_source=chatgpt.com))
			- **PromptKnit / Knit / many hosted prompt GUIs** exist (commercial/hosted) but are not the Python “wrapper over LangSmith SDK” you asked about. ([promptknit.com](https://promptknit.com/?utm_source=chatgpt.com))
		- **Older hub code / langchainhub:** functionality historically lived in `langchainhub` which is deprecated; docs now point users to LangSmith SDK. That transition reduced the incentive for community packages to reimplement Prompt Hub sync. ([LangChain Docs](https://docs.langchain.com/langsmith/manage-prompts-programmatically?utm_source=chatgpt.com))
		- # Practical conclusion
		- **No polished community Python package** I could find that *specifically* provides the exact high-level abstraction you described (local definition of prompts + Pydantic structured outputs + per-model commits to Prompt Hub + pull & keep git versioned) as a drop-in library. Most orgs either:
			- use the **LangSmith SDK** directly and write a few helper scripts, or
			- use a **git-native prompt repo** (PromptOps style) + CI to run a small sync script that calls `client.push_prompt()` for each variant.
			  
			  (If you want, I can open a GitHub search log showing results I inspected; but the practical next step is to either pick one of the git-native prompt tools + write a small sync script, or use the sample helper below.)
		- # Ready-to-use Python helper (copy/paste)
		  
		  This is a small, practical helper you can drop in your repo. It:
		- lets you define a ChatPromptTemplate in code (or load from file),
		- converts a Pydantic model to JSON Schema and attaches it to the prompt (workaround for StructuredPrompt push),
		- pushes the bare prompt and then pushes model-tagged commits (prompt|model) so each model variant has its own commit in Prompt Hub,
		- writes local artifacts (yaml/json) so prompts+schemas are kept in your repo for version control.
		  
		  ```
		  # file: prompthub_sync.py
		  from typing import Any, Dict, List, Optional, Type
		  import json
		  import os
		  from pathlib import Path
		  
		  from langsmith import Client
		  from langchain_core.prompts import ChatPromptTemplate
		  # example model class provider import; optional:
		  # from langchain_openai import ChatOpenAI
		  
		  # if you use pydantic v1/v2 choose the right method to export schema:
		  try:
		    # pydantic v2
		    from pydantic import BaseModel as PydanticBase
		    def pydantic_to_json_schema(m: Type[PydanticBase]) -> Dict[str, Any]:
		        return m.model_json_schema()
		  except Exception:
		    # fallback for pydantic v1
		    from pydantic import BaseModel as PydanticBase
		    def pydantic_to_json_schema(m: Type[PydanticBase]) -> Dict[str, Any]:
		        return m.schema()
		  
		  class PromptHubSync:
		    def __init__(self, client: Optional[Client] = None, out_dir: str = "prompts"):
		        self.client = client or Client()
		        self.out_dir = Path(out_dir)
		        self.out_dir.mkdir(exist_ok=True, parents=True)
		  
		    def write_local_artifact(self, prompt_id: str, prompt_obj: Any, schema: Optional[Dict]=None):
		        # save prompt text and schema to repo for git/version control
		        base = self.out_dir / prompt_id
		        base.mkdir(exist_ok=True, parents=True)
		        if isinstance(prompt_obj, ChatPromptTemplate):
		            # get something serializable
		            with open(base / "prompt.txt", "w", encoding="utf8") as f:
		                try:
		                    # ChatPromptTemplate has from_messages/from_template; try to format sensibly
		                    f.write(str(prompt_obj))
		                except Exception:
		                    f.write(repr(prompt_obj))
		        else:
		            with open(base / "prompt.obj.json", "w", encoding="utf8") as f:
		                json.dump({"repr": repr(prompt_obj)}, f, indent=2)
		        if schema is not None:
		            with open(base / "schema.json", "w", encoding="utf8") as f:
		                json.dump(schema, f, indent=2)
		  
		    def push_prompt_with_models(
		        self,
		        prompt_id: str,
		        prompt_obj: ChatPromptTemplate,
		        pydantic_schema: Optional[Type[PydanticBase]] = None,
		        models: Optional[List[Dict[str, Any]]] = None,
		        tags: Optional[List[str]] = None,
		        description: Optional[str] = None,
		    ) -> Dict[str,str]:
		        """
		        - prompt_obj: ChatPromptTemplate (or other LangChain prompt object)
		        - pydantic_schema: Optional Pydantic BaseModel class (we attach its JSON Schema as readme)
		        - models: list of dicts each describing a model variant. Each dict can be:
		           {"name": "gpt-4o-mini", "model_obj": <langchain model instance>, "tags": ["g:gpt4o-mini"]}
		          OR: {"name": "gpt-4o-mini", "tags": ["g:gpt4o-mini"]} to only push prompt metadata for that model.
		        Returns mapping model_name -> url of pushed prompt commit.
		        """
		        # 1) save locally (git-managed)
		        schema_json = None
		        if pydantic_schema:
		            schema_json = pydantic_to_json_schema(pydantic_schema)
		        self.write_local_artifact(prompt_id, prompt_obj, schema_json)
		  
		        # 2) push a baseline prompt (content only). We'll put schema JSON in `readme` as a practical workaround.
		        readme_text = None
		        if schema_json:
		            readme_text = json.dumps({"schema": schema_json}, indent=2)
		        baseline_url = self.client.push_prompt(
		            prompt_id,
		            object=prompt_obj,
		            description=description or "",
		            readme=readme_text,
		            tags=tags or [],
		        )
		  
		        results = {"baseline": baseline_url}
		  
		        # 3) push model-specific commits (if model objects supplied, push prompt|model runnables)
		        if models:
		            for m in models:
		                name = m.get("name") or m.get("model") or "model"
		                model_obj = m.get("model_obj")
		                model_tags = (tags or []) + m.get("tags", [])
		                try:
		                    if model_obj is not None:
		                        # push prompt|model so the commit stores the model config LangSmith supports
		                        runnable = prompt_obj | model_obj
		                        url = self.client.push_prompt(f"{prompt_id}-{name}", object=runnable, tags=model_tags, description=(m.get("description") or ""))
		                    else:
		                        # fallback: just push the prompt but tag with the model name
		                        url = self.client.push_prompt(f"{prompt_id}-{name}", object=prompt_obj, tags=model_tags)
		                    results[name] = url
		                except Exception as e:
		                    results[name] = f"ERROR: {e}"
		        return results
		  
		  # Example usage:
		  if __name__ == "__main__":
		    from pydantic import BaseModel, Field
		    from langchain_core.prompts import ChatPromptTemplate
		  
		    class MySchema(BaseModel):
		        title: str = Field(..., title="Title")
		        score: int = Field(..., title="Score")
		  
		    messages = [("system", "You are a helpful assistant."), ("user", "{text}")]
		    prompt = ChatPromptTemplate.from_messages(messages)
		  
		    sync = PromptHubSync()
		    # If you use langchain_openai.ChatOpenAI as model, pass instance in models list (optional)
		    res = sync.push_prompt_with_models(
		        "my-enterprise-prompt",
		        prompt,
		        pydantic_schema=MySchema,
		        models=[{"name":"gpt-4o-mini", "tags":["prod","gpt-4o-mini"]}],
		        tags=["team:qa"],
		        description="My prompt with schema attached as readme"
		    )
		    print(res)
		  ```
		  
		  Notes on the helper and caveats
		- Because of the **StructuredPrompt / Pydantic** push issue, the helper attaches Pydantic JSON Schema into `readme` as a pragmatic workaround; when you `pull_prompt()` later you can `readme` and reconstruct the schema locally. This keeps your schema in the repo (versioned) and still usable in the UI for human editors. (See the SDK issue where pushing StructuredPrompt containing Pydantic fails.) ([GitHub](https://github.com/langchain-ai/langsmith-sdk/issues/1462?utm_source=chatgpt.com))
		- For model-attached commits, the code attempts to push `prompt | model` (a RunnableSequence). That is supported by the SDK and will create a commit that includes a model configuration for the prompt. ([LangSmith Docs](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client))
		- Keep the `prompts/` directory under git. Use PR checks (e.g., promptfoo) to run tests on changed prompts before the CI pipeline runs the sync script to push to LangSmith. This gives a clean PromptOps → CI → PromptHub workflow.
		- # Recommendations & next steps
		- If you want a **turnkey** community library, there isn’t a mature one yet — you can (a) adopt the small helper above, (b) pair it with a git-native prompt manager (PromptOps) and a prompt test suite (Promptfoo) and (c) add a CI job to sync changed prompts to LangSmith. ([GitHub](https://github.com/llmhq-hub/promptops?utm_source=chatgpt.com))
		- If **true StructuredPrompt** programmatic commits (Pydantic schemas embedded as structured output definitions) are critical, you can:
			- monitor/follow the LangSmith SDK issue(s) for fixes (issue #1462 shows the problem and ongoing discussion), or
			- implement a custom serialization path that converts your schema to the exact JSON format the API expects (more fragile and requires reverse-engineering/keeping up with API changes). ([GitHub](https://github.com/langchain-ai/langsmith-sdk/issues/1462?utm_source=chatgpt.com))
		- Short answer: I couldn’t find any public evidence that the LangSmith Python SDK reliably supports **programmatically pushing a `StructuredPrompt` that embeds a Pydantic schema** into Prompt Hub as of **September 19, 2025** — the GitHub issue reporting the problem remains open and there are related open issues about serialization/pulling structured outputs. I also didn’t find public community repos showing someone successfully pushing a StructuredPrompt (schema + template) programmatically to Prompt Hub. ([GitHub](https://github.com/langchain-ai/langsmith-sdk/issues/1462))
		  
		  What I checked (short, concrete list)
		- The original issue you cited, **“Programmatically update a StructuredPrompt … #1462”**, is still open and shows the same error when trying to push a `StructuredPrompt` defined in code (Pydantic used as schema). The issue was opened Jan 24, 2025 and has no resolution/comments that indicate it was fixed. ([GitHub](https://github.com/langchain-ai/langsmith-sdk/issues/1462))
		- There is a separate, closely related issue requesting the ability to **pull** a prompt and then chain `with_structured_output()` so code can invoke it — that feature request is also open (Issue #1690). That suggests the SDK’s structured-output prompt roundtrip is still being worked on. ([GitHub](https://github.com/langchain-ai/langsmith-sdk/issues/1690?utm_source=chatgpt.com))
		- The SDK repo contains prior bug/activity around **Pydantic serialization** / “failed to use model_dump” errors (e.g., Issue #1116), which matches the kind of serialization problem reported in #1462. That same serialization surface appears in other places (tracing, prompt commit manifest handling). ([GitHub](https://github.com/langchain-ai/langsmith-sdk/issues/1116?utm_source=chatgpt.com))
		- I searched for community examples (GitHub, PyPI, blog posts, gists) showing someone programmatically pushing a StructuredPrompt (Pydantic schema + prompt) into LangSmith’s Prompt Hub. I found prompt examples on the LangSmith Hub that include structured outputs (likely created in the UI), e.g. `efriis/my-structured-prompt-2`, but no public scripts/repos showing a reliable programmatic `push_prompt()` flow that includes a Pydantic class as the schema. That strongly suggests people are still either using the UI for schema entry or using workarounds. ([smith.langchain.com](https://smith.langchain.com/hub/efriis/my-structured-prompt-2?utm_source=chatgpt.com))
		  
		  Interpretation / conclusion
		- The *core blocker* is serialization of user-defined Python types (Pydantic model classes) into the JSON manifest the LangSmith API expects when creating a `PromptCommit`. The error in #1462 explicitly shows the API rejecting the serialized object because it contains a non-serializable class ref. Related issues show the SDK tries to use `model_dump`/`dict()` approaches but hit edge cases. ([GitHub](https://github.com/langchain-ai/langsmith-sdk/issues/1462))
		- Because the issue is open and there are multiple related open issues (push/pull/serialization), **I judge it unlikely that a public user has reliably pushed StructuredPrompt+Pydantic to Prompt Hub programmatically** by Sept 19, 2025.
		  
		  Practical workarounds I found / suggest
		- **Attach schema as JSON (or in `readme`) and push prompt content.** Push the prompt template and include your schema serialized to JSON Schema in the prompt `readme` or metadata. This is the pragmatic approach many teams use until the SDK supports direct class serialization. (Docs show `push_prompt()` and commit manifests but the SDK/API require serializable manifest pieces.) ([LangChain Docs](https://docs.langchain.com/langsmith/manage-prompts-programmatically?utm_source=chatgpt.com))
		- **Serialize the Pydantic model explicitly to a JSON Schema and push that JSON schema (not the class object).** Convert `MyModel.model_json_schema()` (pydantic v2) or `MyModel.schema()` (v1) and include that dict in the prompt manifest/readme or as separate artifact in your repo and in the prompt commit. That avoids sending a Python class object. (This is essentially the workaround in the helper I previously gave you.) ([Pydantic](https://docs.pydantic.dev/latest/concepts/serialization/?utm_source=chatgpt.com))
		- **Keep schemas in repo + CI sync:** Keep prompt templates and JSON schemas in git; run a small CI job that converts serialized JSON schemas into the prompt commit manifest and calls `client.push_prompt()` with only serializable JSON. This gives the git-versioned, reviewable flow you want without depending on SDK support for sending Python classes. (LangSmith docs show `push_prompt()` / commit usage.) ([LangChain Docs](https://docs.langchain.com/langsmith/manage-prompts-programmatically?utm_source=chatgpt.com))
		- Got it — here’s a **minimal test script** you can run in your environment to check if pushing a prompt with a JSON schema as the `StructuredPrompt.schema` works with the LangSmith SDK.
		  
		  It will try to push the prompt to your Prompt Hub; if serialization fails, you’ll see the same error reported in [issue #1462](https://github.com/langchain-ai/langsmith-sdk/issues/1462).
		  
		  ```
		  from langsmith import Client
		  from langchain_core.prompts import StructuredPrompt
		  
		  # 1. Define a JSON schema (this would normally come from a Pydantic model)
		  json_schema = {
		      "title": "MySchema",
		      "type": "object",
		      "properties": {
		          "title": {"type": "string"},
		          "score": {"type": "integer"}
		      },
		      "required": ["title", "score"]
		  }
		  
		  # 2. Define a StructuredPrompt with schema as JSON dict
		  structured_prompt = StructuredPrompt(
		      schema=json_schema,
		      template="Generate a {title} with a score of {score}."
		  )
		  
		  # 3. Push to LangSmith Prompt Hub
		  client = Client()
		  
		  try:
		      url = client.push_prompt(
		          "json-schema-test-prompt",
		          object=structured_prompt,
		          description="Test pushing StructuredPrompt with JSON schema"
		      )
		      print("✅ Success, pushed to:", url)
		  except Exception as e:
		      print("❌ Failed with error:", e)
		  ```
		- ### How to use it
		- Save as `test_structured_prompt_push.py`.
		- Run it with your LangSmith credentials configured (`LANGCHAIN_API_KEY` / `LANGCHAIN_ENDPOINT` / `LANGCHAIN_PROJECT` etc).
		- If it fails, you’ll know the SDK still doesn’t accept JSON schema–based `StructuredPrompt`. If it succeeds, check the Prompt Hub UI — does the schema show up as structured output metadata?
	-