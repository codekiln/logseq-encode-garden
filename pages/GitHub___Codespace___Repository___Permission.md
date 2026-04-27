- https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces#setting-additional-repository-permissions
	- ```json
	  {
	    "customizations": {
	      "codespaces": {
	        "repositories": {
	          "my_org/my_repo": {
	            "permissions": {
	              "issues": "write"
	            }
	          }
	        }
	      }
	    }
	  }
	  
	  ```
	- You can only reference repositories that belong to the same personal account or organization as the repository you are currently working in.
	- You can use the `*` wildcard to grant permissions to multiple repositories in an organization. For example, to grant permissions to all repositories in the `my_org` organization use `my_org/*`. This syntax is only valid for codespaces. In any `devcontainer.json` files that are used for prebuilds, you must define permissions for each repository separately. For more information, see [Allowing a prebuild to access other repositories](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/allowing-a-prebuild-to-access-other-repositories).
	- You can grant as many or as few of the following permissions for each repository listed:
		- `actions` - read / write
		- `checks` - read / write
		- `contents` - read / write
		- `deployments` - read / write
		- `discussions` - read / write
		- `issues` - read / write
		- `packages` - read
		- `pages` - read / write
		- `pull_requests` - read / write
		- `repository_projects` - read / write
		- `statuses` - read / write
		- `workflows` - write