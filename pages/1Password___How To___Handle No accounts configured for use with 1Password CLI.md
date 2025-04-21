# How to handle `No accounts configured for use with 1Password CLI` when running [[1Password/Dev/op/run]] or other commands
	- ## Sample Error
		- ```
		  $ op vault list
		  No accounts configured for use with 1Password CLI.
		  
		  You can either:
		   - Turn on the 1Password desktop app integration to sign in with the accounts you've added to the app: https://developer.1password.com/docs/cli/app-integration/ for details.
		   - Add an account manually with 'op account add' and sign in by entering your password on the command line. See 'op account add --help' for details.
		   - Authenticate using a 1Password service account by setting the 'OP_SERVICE_ACCOUNT_TOKEN' environment variable to your service account token. Learn more: https://developer.1password.com/docs/service-accounts/ 
		   - Use 1Password CLI with a Connect server by setting the 'OP_CONNECT_HOST' and 'OP_CONNECT_TOKEN' environment variables to your Connect host and token, respectively. Learn more: https://developer.1password.com/docs/connect/
		  
		  Do you want to add an account manually now? [Y/n] 
		  ```
	- ## Why this might occur
		- You restarted [[iTerm2]] or [[CursorAI]] and didn't click **Allow** on [[MacOS App Popup Access Data from Other Apps]]
		- You didn't authorize in time when getting the [[1Password/Dev/CLI/1Password Access Requested PopUp]]