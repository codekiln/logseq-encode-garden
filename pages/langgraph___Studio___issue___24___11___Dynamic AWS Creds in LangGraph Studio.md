# [Dynamic AWS Credentials in Langgraph Studio Docker Container · Issue #203 · langchain-ai/langgraph-studio](https://github.com/langchain-ai/langgraph-studio/issues/203#issuecomment-2700707631)
	- Update from [[Person/David Duong]] [[2025/03]]
		- > Hello! For volume mounts, you can use the following docker-compose.yml to mount the volume if needed
			- ```yml
			  # docker-compose.yml
			  services:
			    langgraph-api:
			      volumes:
			       - .aws:/root/.aws:ro
			  ```