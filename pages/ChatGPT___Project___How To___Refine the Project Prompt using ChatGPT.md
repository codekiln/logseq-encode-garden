tags:: [[ChatGPT/Project]], [[AI/Prompt/Engineering]], [[Diataxis/How To]]

- # How To Refine a ChatGPT Project #Prompt Using [[o3]]
	- ## [[My Notes]]
		- [[2025-05-16 Fri]]
		  id:: 68278fa8-7887-4aae-904d-4df99cbf4c82
			- I've had great luck using this template to iteratively improve the [[ChatGPT/Project/Instruction]]s to align with my expectations. These models are excellent prompt engineers, but, perhaps ironically, they need to be prompted a certain way in order to access their highest capabilities in this regard. For example, I used it to dramatically increase the alignment of [[ChatGPT/Project/Instruction/Diataxis Logseq]] quickly, using [[ChatGPT/Dictation]]
	- ## Goal
		- Produce a concise, well-structured prompt that meets project-specific length or formatting targets (e.g., 7 000 – 7 500 chars) by iterating with a reasoning model such as [[o3]], using [[ChatGPT/Code/Interpreter]] to measure length.
	- ## Preconditions
		- Access to ChatGPT with the **o3 reasoning model**.
		- **Code Interpreter** (python_user_visible) enabled.
		- A draft prompt that needs trimming or re-organization.
		- Knowledge of your project’s formatting rules (length limits, required sections, special markup, etc.).
	- ## Procedure
		- ### 1. Map Your Existing Prompt
			- Skim the draft and label logical parts (intro, bad example, critique, current rules, request).
			- Note all hard requirements (length cap, mandatory headings, prohibited markup, etc.).
		- ### 2. Build a Generic [[Prompt Template]] Skeleton
			- Ask ChatGPT to extract section headings and convert them into a reusable template.
			- Use the structure below; fill **[placeholders]** with topic-specific text:  
			  ~~~markdown
			  # Prompt Template: Refine Project Rules
			  
			  ## 1 Context  
			  > Currently in your project instructions: **[summary of situation]**
			  
			  ## 2 Anti-Pattern Example  
			  <EXAMPLE_OF_HOW_NOT_TO_DO_IT>  
			  **[paste flawed sample]**  
			  </EXAMPLE_OF_HOW_NOT_TO_DO_IT>
			  
			  ## 3 Problem Analysis  
			  The above example has problems:  
			  1. **[issue A]**  
			  2. **[issue B]**  
			  3. **[issue C]**
			  
			  ## 4 Current Project Rules  
			  <PROJECT_RULES>  
			  **[paste current rules]**  
			  </PROJECT_RULES>
			  
			  ## 5 Refinement Request  
			  Please rewrite the rules so that **[desired outcome]**.  
			  **Constraints:**  
			  - Keep length within 7000-7500 characters (it MUST be <8000 characters).  
			  - Follow all formatting guidelines in Section 4.  
			  ~~~
		- ### 3. Instruct the o3 Model to Rewrite
			- Send the filled-in template to ChatGPT (o3). You may need to select o3 from the model drop-down at the top.
			- Explicitly request: “Use Code Interpreter to count characters and iterate until the result fits the required range.”
		- ### 4. Measure with Code Interpreter
			- When ChatGPT returns a draft, have it run:  
			  ~~~python
			  rules = """...rewritten text..."""
			  print(len(rules))
			  ~~~
			- If the count is **outside** your target range, ask for automatic trimming or expansion and re-run the count.
		- ### 5. Validate Output
			- Confirm the rewrite matches **all** project formatting rules (headings, markup, fences, etc.).
			- Ensure no prohibited elements remain (e.g., unsupported tags or placeholders).
		- ### 6. Finalize
			- Save the approved prompt to your documentation repo or knowledge base.
			- Archive the template for future refinements across other projects.
	- ## Troubleshooting
		- *Output exceeds length requirement* → Ask o3 to “compress explanatory prose, keep tables.”
		- *Key formatting rule ignored* → Remind model: “Ensure compliance with project’s formatting checklist.”
		- *Prohibited markup persists* → Reinforce rule: “Strip all unsupported tags or symbols.”
		- *Code Interpreter unavailable* → Manually copy text into a local script (e.g., `wc -m`) to count characters.
	- ## References
		- [OpenAI Platform documentation](https://platform.openai.com/docs).
		- [Prompt Engineering best practices (OpenAI Cookbook)](https://github.com/openai/openai-cookbook/blob/main/techniques_to_improve_reliability.md).