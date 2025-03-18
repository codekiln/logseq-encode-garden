# How to publish a Logseq Graph with a `custom.css`
	- [[see-also]]
		- [[Logseq/Doc/Publish]] [Some features that aren't available do have workarounds](https://docs.logseq.com/#/page/67aa108b-a06f-4705-9433-0730af0846b8)
			- Put CSS import in [[Logseq/Logseq Dir/custom.css]]
				- ```css
				  // This uses the logseq-dev-theme but the url can be changed to any theme's github url
				  @import url("https://cdn.jsdelivr.net/gh/pengx17/logseq-dev-theme@main/custom.css");
				  ```