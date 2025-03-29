# [How to configure a site to be completely ignored? | 1Password Community](https://www.1password.community/discussions/1password/how-to-configure-a-site-to-be-completely-ignored/105266)
	- ## [[My Notes]]
		- Can it be true that the only way to do this reliably is to disable "Offer to fill and save passwords" globally?
		- ((67e01553-67e4-42bc-b934-0e7837193376))
	- ## Response from 1Password Team
		- At the moment, there isn't a feature allowing you to blacklist specific websites in the 1Password extension. While I can't make any promises, I've created a feature request for our product team; we will go over your feedback and see if it's something we'll be able to add in a future version of 1Password.
		- Alternatively, there is an option that will prevent 1Password from offering to autofill on this web page for the duration of your browsing session. Once your browser is closed and reopened you will need to follow the steps again to prevent 1Password from offering to autofill on this web page again.
			- Right-click anywhere on the web page.
			- Select "1Password - Password Manager", then choose "Hide on this page".
		- You could also turn off the new Autosave feature in the 1Password extension; this applies to all websites:
			- Right-click the 1Password icon in your browser's toolbar and select "Settings".
			- In the **Autofill & save** section, turn off the "Save logins automatically" option.
		- > [[Original Poster]]: When I go to the special site, 1P is quiet, as expected, but when I click into the username field I, 1P still provides suggestions, which is irritating. (Some of them are even wrong.)
		- If the subdomain is different between the Login item and the specific website, I suggest using the "**Never fill on this exact domain**" Autofill behaviour rule on those Login items so they don't appear as suggestions.
			- DONE What is the **Never fill on this exact domain** Autofill behavior rule on login items? #Question **ANS: see [[1Password/Doc/Autofill Behavior]]**
			  id:: 67e01553-67e4-42bc-b934-0e7837193376
-