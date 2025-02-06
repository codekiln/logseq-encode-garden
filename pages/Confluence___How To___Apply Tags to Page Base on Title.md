- You can automate the addition of labels to Confluence pages based on their titles using Confluence's built-in automation features. Here's how you can set this up:
- ## **Access Automation Rules**:
	- Navigate to the space where you want to set up the automation.
	- Click on the space settings (usually a gear icon) and select "Automation" from the menu.
- **Create a New Rule**:
	- Click on "Create rule" to start setting up a new automation rule.
- **Set the Trigger**:
	- Choose the "Page published" trigger to apply the rule when a new page is created.
	- Optionally, add the "Page updated" trigger if you want the rule to apply when existing pages are updated.
- **Add a Condition**:
	- Use the "CQL condition" to specify which pages the rule should apply to.
	- For example, to target pages with titles containing the word "Project", set the CQL to:
	  
	  ```
	  nginx
	  
	  CopyEdit
	  
	  title ~ "Project"
	  ```
	  
	  This condition ensures that only pages with "Project" in their titles will have the label added.
- **Add the Action**:
	- Select the "Add labels" action.
	- Specify the label you want to add, such as "project-doc".
- **Save and Enable the Rule**:
	- Review your rule to ensure it’s set up correctly.
	- Save the rule and make sure it's enabled.
	  
	  With this automation in place, any new page with "Project" in its title will automatically receive the "project-doc" label upon creation or update. This method leverages Confluence's native automation capabilities to streamline content organization.
	  
	  For more advanced scenarios, such as adding labels based on specific templates or more complex conditions, you might consider using additional tools or apps like ScriptRunner or Smart Labels for Confluence. These tools offer enhanced functionalities for managing labels and automating content categorization. 
	  
	  [community.atlassian.com](https://community.atlassian.com/t5/Confluence-questions/Auto-Labeling-Solution-for-Confluence-Pages/qaq-p/2364865?utm_source=chatgpt.com)
	  
	  Remember to test your automation rule to ensure it works as expected and adjust the conditions or actions as needed to fit your specific requirements.