tags:: [[Logseq]], [[Diataxis/How To]]

- # How To Collapse Linked References By Default in Logseq
	- ## [[tldr]]
	  id:: 6870cb73-4cd6-4646-ae45-2ed3a93e63d4
		- Change [[Logseq/config.edn/:ref/linked-references-collapsed-threshold]]
			- This setting determines the number of linked references that should trigger "collapsed by default" behavior. This feature was originally added because some pages had way too many references to render efficiently.
			- Change it from default: `:ref/linked-references-collapsed-threshold 50`
			- to `:ref/linked-references-collapsed-threshold 0` to collapse by default.
			- Then restart logseq.
	- ## Overview
		- This guide shows you how to configure Logseq to automatically collapse linked references when they exceed a certain threshold
		- Useful for pages with many linked references that can make navigation difficult
		- Helps maintain a cleaner interface by showing only the most recent or relevant references by default
	- ## Prerequisites
		- Logseq installed and running
		- Access to Logseq's configuration file (`config.edn`)
		- Basic familiarity with Logseq's settings interface
	- ## Steps
		- ### 1. Open Logseq Settings
			- Launch Logseq
			- Click on the **Settings** icon (gear/cog) in the top-right corner
			- Or use the keyboard shortcut: `Cmd/Ctrl + ,`
		- ### 2. Access Custom Configuration
			- In the Settings panel, navigate to **General**
			- Find and click on **Custom configuration**
			- Click **Edit config.edn** to open the configuration file
		- ### 3. Locate the Linked References Setting [[Logseq/config.edn/:ref/linked-references-collapsed-threshold]]
			- In the `config.edn` file, find the line containing `ref/linked-references-collapsed-threshold`
			- If the line doesn't exist, you can add it
			- The default value is likely set to a high number (e.g., 50)
		- ### 4. Set the Collapse Threshold
			- Change the value to your preferred threshold:
				- `0` - Always collapse linked references
				- `5` - Show only 5 most recent references
				- `10` - Show only 10 most recent references
			- Example configuration:
				- ~~~clojure
				  :ref/linked-references-collapsed-threshold 5
				  ~~~
		- ### 5. (Optional) Configure Block Expansion Level [[Logseq/config.edn/:ref/default-open-blocks-level]]
			- To also control how many levels of child blocks are expanded in linked references
			- Add or modify the `:ref/default-open-blocks-level` setting
			- Example configuration:
				- ~~~clojure
				  :ref/default-open-blocks-level 1
				  ~~~
		- ### 6. Save and Restart
			- Save the `config.edn` file
			- Restart Logseq for the changes to take effect
			- The linked references will now be collapsed by default when they exceed your threshold
	- ## Troubleshooting
		- **Setting not found**: If you can't find the `ref/linked-references-collapsed-threshold` line, add it manually to your `config.edn`
		- **No effect after restart**: Ensure the syntax is correct (no extra spaces, proper colons)
		- **Linked references still expanded**: Check that you saved the file and restarted Logseq completely
	- ## Related
		- [[Logseq/config.edn]]
		- [[Logseq/Settings]]
		- [How to set Logseq to collapse "Linked References" by default, similar to "Unlinked References"?](https://discuss.logseq.com/t/how-to-set-logseq-to-collapse-linked-references-by-default-similar-to-unlinked-references/16127/2)
		- [Collapse the Linked References](https://discuss.logseq.com/t/collapse-the-linked-references/11240)
		- [Way to collapse reference block for some pages?](https://www.reddit.com/r/logseq/comments/16qep6l/way_to_collapse_reference_block_for_some_pages/)