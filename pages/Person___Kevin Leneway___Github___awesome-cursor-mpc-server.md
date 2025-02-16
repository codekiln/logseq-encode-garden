- [kleneway/awesome-cursor-mpc-server: Example of an MCP server with custom tools that can be called directly from cursor](https://github.com/kleneway/awesome-cursor-mpc-server)
	- ## [Tool Definitions](https://github.com/kleneway/awesome-cursor-mpc-server/blob/main/src/index.ts#L50-L111)
		- ```ts
		  server.setRequestHandler(ListToolsRequestSchema, async () => {
		    return {
		      tools: [
		        {
		          name: screenshotToolName,
		          description: screenshotToolDescription,
		          inputSchema: {
		            type: "object",
		            properties: {
		              url: {
		                type: "string",
		                description: "Full URL to screenshot",
		              },
		              relativePath: {
		                type: "string",
		                description: "Relative path appended to http://localhost:3000",
		              },
		              fullPathToScreenshot: {
		                type: "string",
		                description:
		                  "Path to where the screenshot file should be saved. This should be a cwd-style full path to the file (not relative to the current working directory) including the file name and extension.",
		              },
		            },
		            required: [],
		          },
		        },
		        {
		          name: architectToolName,
		          description: architectToolDescription,
		          inputSchema: {
		            type: "object",
		            properties: {
		              task: {
		                type: "string",
		                description: "Description of the task",
		              },
		              code: {
		                type: "string",
		                description: "Concatenated code from one or more files",
		              },
		            },
		            required: ["task", "code"],
		          },
		        },
		        {
		          name: codeReviewToolName,
		          description: codeReviewToolDescription,
		          inputSchema: {
		            type: "object",
		            properties: {
		              folderPath: {
		                type: "string",
		                description:
		                  "Path to the full root directory of the repository to diff against main",
		              },
		            },
		            required: ["folderPath"],
		          },
		        },
		      ],
		    };
		  });
		  ```