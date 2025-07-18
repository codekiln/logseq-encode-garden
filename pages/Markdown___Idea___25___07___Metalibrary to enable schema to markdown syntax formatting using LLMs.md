tags:: [[Idea]], [[AI/Output/Post-Format]]

- # Library to facilitate spec-described, LLM-powered linting and formatting of Markdown documentation or any [[Programming/Language]], using [[Programming/Dynamic]]
	- ## Summary
		- Create a library which facilitates creating a spec that expresses expected formatting for a given structured language. The library should have an opinionated way to create a clear spec and include LLM-powered tools to create such a spec using a requirements elicitation process. The spec should format contain example artifacts which can aid in few-shot prompting. The library should enable compiling such a spec into an LLM-powered application which starts out just using the LLM to directly format the instructions in a prompted way. Over time, the prompted LLM-powered application should start to write code to automate the process and built up syntax parsing approaches, adding the approach to a memory bank that it can draw upon to make the conversion approach more consistent and tested.
	- ## [[see-also]]
		- [[ChatGPT/Deep Research/How To/Clean Up Markdown with Citations]]