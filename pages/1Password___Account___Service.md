alias:: [[1Password Service Account]], [[1Password Service Accounts]]

- # 1Password Service Accounts
	- See [[1Password/Dev/Doc/service-accounts/use-with-1password-cli]] for using with [[1Password/Dev/op]]
	- ## Important limitations
	  id:: 67dfdf7d-0d6b-4fef-afe6-16f2ed466dd1
		- While it sounds like a great idea, and 1P recommends Service Accounts over using [[1Password/Dev/op]], it's not available to all users or teams and has important use cases that aren't covered yet
		- ### Not a default feature of 1Password
			- According to [[1Password/Dev/Doc/service-accounts/Manage/creating service accounts]], only [[1Password/Business]] **admins** can enable a group to create and manage service accounts. So you can use service accounts if you are a [[1Password/Teams]] admin or if you in a 1Password Business setting in a Group that can create service accounts. [[1Password/Family]] doesn't have any ability to use service accounts.
				- {{embed ((67dfdd64-6d97-43dd-96f6-ff28165bafb8))}}
				- to fully embrace [[Security/Service Account]]s with fine-grained permissions, a team would need to create many service users, preferably with short-lived access credentials.
		- ### Can't programmatically delete short-lived service accounts
			- [[1Password/Slack/cli]] message [here](https://1password-devs.slack.com/archives/C037XTZ9RA6/p1740495354791039?thread_ts=1740495114.638429&cid=C037XTZ9RA6) from Vladyslav Ponoiko
				- > My issue mainly appears because I need to  use SA tokens, which I usually generate before run of a particular script and they're aimed onto liveness of max 1 day.
				  > Today I run into error when tried to create SA, so cleaned up couple of SA's and this worked, but I would love to get more consistent onto the 'cleaning up' part, as I have lots of SA's by now, and would really love to keep my way of doing things
				- response from 1Password jr software developer [[Person/Eddy Filip]] says that [[1Password/Dev/CLI]] doesn't enable deleting service accounts for the short-lived case
					- > currently the CLI doesn’t provide a programmatic way of deleting service accounts (either active or expired).
					  > The only way you can delete service accounts is through the browser. The expired service accounts will be grayed out and will also show with red that they are expired.
					  > In the meantime, I will file an issue internally with the request of adding support for deleting service accounts via the CLI.
				- the conversation also references [Service account management · Issue #115 · 1Password/onepassword-sdk-js](https://github.com/1Password/onepassword-sdk-js/issues/115)