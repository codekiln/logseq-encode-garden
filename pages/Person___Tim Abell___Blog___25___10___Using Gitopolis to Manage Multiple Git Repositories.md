- [Using Gitopolis to Manage Multiple Git Repositories](https://0x5.uk/2025/10/25/using-gitopolis-to-manage-multiple-git-repositories/)
	- [[My Notes]]
		- Explains why, in a [[Microservices]] setup, companies need a standard way to structure where [[git/repo]]s are cloned on the hard drive
	- Quotes
		- The company’s onboarding process mentions “Install Gitopolis”.
		  Alice drops a copy of `.gitopolis.toml` into the shared Google Drive folder and links it in the new-starter docs.
		- When Dana joins the team, she runs:
		- ```
		  mkdir ~/work && cd ~/work
		  cp ~/GoogleDrive/dev-setup/.gitopolis.toml .
		  gitopolis clone
		  ```
		- All the right repos appear in the right places.
		- Alice shows her how to explore the setup:
		- ```
		  $ gitopolis tags --long
		  - backend
		        auth
		        billing
		        users
		        orders
		        payments
		        inventory
		        notifications
		        gateway
		        shipping
		  - frontend
		        web-ui
		        admin-ui
		        mobile
		        design-system
		        returns
		  - infra
		        infra
		        ci
		        monitoring
		        alerts
		  - shared
		        shared
		        devtools
		        scripts
		        docs
		  ```
		- Dana can instantly see which repos belong to which teams — `backend`, `frontend`, `infra`, `shared`.
		  She starts working without having to ask where anything lives.