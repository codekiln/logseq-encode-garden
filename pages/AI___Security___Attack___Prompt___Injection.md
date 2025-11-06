tags:: [[AI/Security/Attack]]
alias:: [[Prompt Injection]]

- # Prompt Injection
	- A security vulnerability where malicious input is crafted to manipulate or override the intended behavior of an LLM application
	- Attackers inject malicious instructions into prompts to:
		- Bypass safety measures
		- Extract sensitive information
		- Manipulate the AI's behavior
		- Gain unauthorized access to systems
	- ## Types
		- **Direct Prompt Injection**: Malicious input is directly inserted into user prompts
		- **Indirect Prompt Injection**: Malicious content is embedded in data sources that the AI processes (e.g., web pages, documents, GitHub issues)
	- ## Detection and Testing
	- [[PromptFooAI]] - Testing framework for detecting prompt injection attacks
- ## Related Concepts
	- [[AI/Security/Attack/Toxic Agent Flow]] - Use of indirect prompt injection to trigger malicious tool use sequences

