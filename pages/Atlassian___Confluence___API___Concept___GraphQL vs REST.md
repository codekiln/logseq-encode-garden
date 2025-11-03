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
		- **Write Operations**: Both APIs support CRUD operations, but with different approaches. GraphQL provides mutations like `createPage`, `updatePage`, and `deletePage` for content management. REST provides comprehensive endpoints including dedicated operations like copying pages (`POST /wiki/rest/api/content/{id}/copy`) that don't have direct GraphQL equivalents
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
			- Single endpoint for all queries and mutations (typically `/graphql`)
			- Clients send queries specifying exact fields and relationships needed
			- Mutations available for creating, updating, and deleting content (e.g., `createPage`, `updatePage`, `deletePage`)
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
		- **GraphQL Mutation Example**: Creating a new page:
			~~~
			mutation {
			  confluence {
			    createPage(input: {
			      spaceId: "123"
			      title: "New Page"
			      body: {storage: {value: "Content here", representation: STORAGE}}
			    }) {
			      page {
			        id
			        title
			      }
			    }
			  }
			}
			~~~
			- Result: Single mutation request to create and return the new page
		- **Duplicating Pages**: While both APIs can duplicate pages, REST provides a dedicated copy endpoint (`POST /wiki/rest/api/content/{id}/copy`), while GraphQL requires fetching the original page content via query, then creating a new page via mutation
		- **Performance Trade-off**: While GraphQL can reduce request count, it may take longer for complex queries compared to optimized REST v2 endpoints in some scenarios
	- ## Official Guidance
		- **Atlassian has not provided explicit, comprehensive guidance** on when to choose GraphQL vs REST APIs for Confluence
		- Documentation focuses on describing capabilities rather than prescribing when to use each API
		- Developers must evaluate both APIs based on their specific use cases and requirements
		- **Considerations for Choosing**:
			- **Use REST API** when:
				- You need mature, stable, well-documented interfaces
				- Your use case requires specialized operations (e.g., direct page copying)
				- You prioritize maximum feature coverage and tooling support
				- You have existing REST integrations or team familiarity with REST
			- **Consider GraphQL API** when:
				- You need efficient data retrieval with related entities in single queries
				- You want to minimize over-fetching and reduce request count
				- You can work with evolving APIs (GraphQL was in beta as of March 2022)
				- Your use case benefits from schema introspection and strongly-typed queries
			- **Performance Note**: Community testing has shown REST v1 may outperform GraphQL and REST v2 in some scenarios, suggesting performance evaluation is use-case specific
		- **Beta Status**: GraphQL APIs were released in beta as of March 2022, emphasizing that they are still evolving and subject to change based on user feedback
		- **Deprecation Concerns**: Developer community discussions have raised concerns about REST v1 deprecation and the readiness of newer APIs to fully replace older versions
		- See also: [Confluence GraphQL API Documentation](https://developer.atlassian.com/cloud/confluence/graphql/), [Community Performance Discussion](https://community.developer.atlassian.com/t/performance-rest-vs-graphql/69254)
	- ## Misconceptions
		- GraphQL is always faster than REST → **False**. Performance depends on query complexity and server implementation. Some GraphQL queries may be slower than equivalent REST calls
		- GraphQL cannot create or modify content → **False**. GraphQL provides mutations like `createPage`, `updatePage`, and `deletePage` for content management operations. Both APIs support write operations, though REST may offer more specialized endpoints (like direct page copying)
		- GraphQL can do everything REST can do → **Partially false**. While GraphQL has mutations for CRUD operations, REST may have specialized endpoints that don't have direct GraphQL equivalents (e.g., dedicated copy endpoints). For duplicating pages, REST's copy endpoint is more straightforward than GraphQL's query-then-create approach
		- REST v2 is just an updated version of v1 → **False**. REST v2 was redesigned for performance and removed expansions, requiring a different approach to data retrieval
		- GraphQL eliminates the need for REST → **False**. Both APIs serve different purposes. REST may have specialized operations and better tooling for certain workflows, while GraphQL excels at complex nested data retrieval and provides a unified interface for queries and mutations
		- GraphQL beta fields are unstable and shouldn't be used → **Partially true**. Beta fields can change without notice and are intended for experimentation, but they provide access to newer features
	- ## Related
		- [[Atlassian/Confluence/API/GraphQL]]
		- [[Atlassian/Confluence/API/REST/v2]]
		- [[Atlassian/Confluence/API/REST/v1]]
		- [[Atlassian/Confluence/API]]

