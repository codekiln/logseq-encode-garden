tags:: [[Diataxis/Explanation]]
- # GraphQL vs REST APIs Conceptual Overview
	- ## Overview
		- GraphQL and REST are two distinct API paradigms available in Atlassian Confluence Cloud, each offering different approaches to data retrieval and integration
		- GraphQL allows clients to request precisely the data they need in a single query, while REST uses traditional endpoint-based architecture with multiple resources
		- Understanding the differences helps developers choose the right API approach for their specific integration needs
	- ## Context
		- Confluence Cloud historically provided REST APIs (v1 and v2) for integration needs
		- GraphQL was introduced later as a modern alternative addressing limitations of REST in complex data retrieval scenarios
		- REST v2 was optimized for performance but removed expansions, creating a need for multiple requests to gather related data
		- GraphQL addresses the over-fetching and under-fetching problems common with REST by allowing clients to specify exact data requirements
		- Both APIs coexist to serve different use cases and developer preferences
	- ## Key Principles
		- **Query Efficiency**: GraphQL enables fetching multiple related resources in a single request, while REST typically requires multiple endpoint calls
		- **Data Control**: GraphQL clients specify exactly what fields they need, reducing over-fetching of unnecessary data
		- **Schema Evolution**: GraphQL uses continuous schema evolution with beta fields and deprecation periods, while REST relies on explicit versioning (v1, v2)
		- **Flexibility vs Stability**: REST provides stable, versioned endpoints with predictable behavior, while GraphQL offers flexibility but may change more frequently
		- **Tooling Maturity**: REST benefits from extensive tooling and community support, while GraphQL provides newer tools like GraphQL Explorer for query discovery
	- ## Mechanism
		- **REST API Approach**:
			- Uses HTTP methods (GET, POST, PUT, DELETE) on resource-based endpoints
			- Endpoints are organized by resource type (e.g., `/wiki/rest/api/content`, `/wiki/rest/api/space`)
			- Returns complete resource representations unless filtered server-side
			- Versioning handled through URL paths (`/api/v1/`, `/api/v2/`)
			- Authentication via OAuth 2.0 or Basic auth
		- **GraphQL API Approach**:
			- Single endpoint for all queries (typically `/graphql`)
			- Clients send queries specifying exact fields and relationships needed
			- Query language allows nested data fetching in one request
			- Schema introspection enables self-documenting APIs
			- Authentication via OAuth 2.0 or JWT for cloud apps
			- Beta fields marked for experimental features that may change
	- ## Examples
		- **REST API Example**: Fetching a page and its space requires multiple requests:
			- Request 1: `GET /wiki/rest/api/content/{id}` to get page details
			- Request 2: `GET /wiki/rest/api/space/{spaceKey}` to get space information
			- Result: Two separate HTTP requests with potential over-fetching
		- **GraphQL API Example**: Fetching the same data in a single query:
			~~~
			query {
			  content(id: "123") {
			    title
			    space {
			      key
			      name
			    }
			  }
			}
			~~~
			- Result: One request fetching only the specified fields
		- **Performance Trade-off**: While GraphQL can reduce request count, it may take longer for complex queries compared to optimized REST v2 endpoints in some scenarios
	- ## Misconceptions
		- GraphQL is always faster than REST → **False**. Performance depends on query complexity and server implementation. Some GraphQL queries may be slower than equivalent REST calls
		- REST v2 is just an updated version of v1 → **False**. REST v2 was redesigned for performance and removed expansions, requiring a different approach to data retrieval
		- GraphQL eliminates the need for REST → **False**. Both APIs serve different purposes. REST may be simpler for straightforward CRUD operations, while GraphQL excels at complex nested data retrieval
		- GraphQL beta fields are unstable and shouldn't be used → **Partially true**. Beta fields can change without notice and are intended for experimentation, but they provide access to newer features
	- ## Related
		- [[Atlassian/Confluence/API/GraphQL]]
		- [[Atlassian/Confluence/API/REST/v2]]
		- [[Atlassian/Confluence/API/REST/v1]]
		- [[Atlassian/Confluence/API]]

