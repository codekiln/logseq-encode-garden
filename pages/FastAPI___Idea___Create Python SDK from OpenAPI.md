tags:: [[Idea]], [[OpenAPI]], [[SDK]]

- [[FastAPI/Reddit]] [[2024/05]]
	- [How to generate python HTTP clients that consume OpenAPI / Pydantic / FastAPI specs : r/FastAPI](https://www.reddit.com/r/FastAPI/comments/1cx89hm/how_to_generate_python_http_clients_that_consume/)
		- [[Original Poster]]
			- I'm looking for a framework that will produce python libraries that can consume my pydantic-typed FastAPI endpoints in both sync and async contexts.
			  [Generate Clients - FastAPI](https://fastapi.tiangolo.com/advanced/generate-clients/) links to OpenAPI Generator, which apparently has a python generator: [Documentation for the python Generator | OpenAPI Generator](https://openapi-generator.tech/docs/generators/python/), but the documentation looks kind of sparse. Can someone link me to a tutorial about how to use it for FastAPI / Pydantic? Note, it also links to [Speakeasy](https://www.speakeasyapi.dev/pricing), which looks great if you work for a fortune 50 company or something; pricing is expensive.
			- I've also seen a few discussion threads in FastAPI about this, for example [Client with the same awesomeness? · Issue #85 · tiangolo/fastapi](https://github.com/tiangolo/fastapi/issues/85)
			- > Does anyone know a library that can consume a swagger file and provide nice interface for interacting with the API (something similar what [suds](https://github.com/cackharot/suds-py3) did for SOAP) ? I'm particularly after auto-generated Pydantic definitions of swagger request/response objects. I think [u/dmontagu](https://github.com/dmontagu) 's [fastapi_client](https://github.com/dmontagu/fastapi_client) and [@koxudaxi](https://github.com/koxudaxi) 's [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator) ...
			- It looks like `fastapi_client` is abandonware, and `datamodel-code-generator` looks cool but AFAICT it's not generating a python client but some client data models. Not sure what the use case is there, if you start out using pydantic with fastapi.
		- Comment
			- > We use openapi generator you liked. You're right, the docs are sparse but it does work. They have a generator which used pydantic which is a bit better, IMO, but both are fine
			-