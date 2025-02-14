- [GitHub CLI | Take GitHub to the command line](https://cli.github.com/manual/gh_api)
	- ```
	  gh api <endpoint> [flags]
	  ```
	- Makes an authenticated HTTP request to the GitHub API and prints the response.
	- The endpoint argument should either be a path of a GitHub API v3 endpoint, or `graphql` to access the GitHub API v4.
	- ## Notable Flags
		- ### [[GitHub/CLI/gh/api/-q]] aka [[GitHub/CLI/gh/api/--jq]]
	- ## Examples
		- ### list all repos for a user - works for me
		- ```
		  # list all repositories for a user
		  $ gh api graphql --paginate -f query='
		    query($endCursor: String) {
		      viewer {
		        repositories(first: 100, after: $endCursor) {
		          nodes { nameWithOwner }
		          pageInfo {
		            hasNextPage
		            endCursor
		          }
		        }
		      }
		    }
		  '
		  ```