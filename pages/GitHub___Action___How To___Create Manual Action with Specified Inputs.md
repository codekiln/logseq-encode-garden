tags:: [[GitHub/Action/How To]], [[Diataxis/How To]]

- # How To Create Manual Action with Specified Inputs
	- ## Goal
		- Create a GitHub Action workflow that can be manually triggered via the GitHub UI with user-defined input parameters.
	- ## Preconditions
		- GitHub repository with Actions enabled.
		- Permissions to edit `.github/workflows/`.
	- ## Procedure
		- ### 1. Define Workflow File
			- Create a file like `.github/workflows/manual-action.yml`.
			- Start with this scaffold:
			  ~~~yaml
			  name: Slack Ops
			  
			  on:
			  workflow_dispatch:
			    inputs:
			      username:
			        description: 'Email or Slack username'
			        required: true
			        type: string
			      role:
			        description: 'Org role (e.g. marketing, eng)'
			        required: true
			        type: string
			      action:
			        description: 'onboard or offboard'
			        required: true
			        type: choice
			        options:
			          - onboard
			          - offboard
			  
			  jobs:
			  run-slack-ops:
			    runs-on: ubuntu-latest
			    steps:
			      - uses: actions/checkout@v4
			      - name: Run CLI command
			        run: |
			          pip install -e .
			          python scripts/slack_ops.py \
			            --action ${{ inputs.action }} \
			            --username ${{ inputs.username }} \
			            --role ${{ inputs.role }}
			        env:
			          SLACK_API_TOKEN: ${{ secrets.SLACK_API_TOKEN }}
			  ~~~
		- ### 2. Secure Secrets
			- Go to **Repo Settings → Secrets and variables → Actions**.
			- Add `SLACK_API_TOKEN` or any other secret needed by your CLI script.
		- ### 3. Create CLI Tool
			- Your `scripts/slack_ops.py` should accept arguments for `--username`, `--role`, and `--action`, and use those to process the appropriate YAML-defined channels.
		- ### 4. Run from GitHub UI
			- Go to the **Actions** tab in your repo.
			- Select the `Slack Ops` workflow → Click **Run workflow**.
			- Fill in the `username`, `role`, and `action` fields manually.
	- ## Troubleshooting
		- Action not appearing → Check that the YAML is valid and on the default branch.
		- Missing secrets → Set in repo or org-level Actions settings.
	- ## References
		- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
		- [Manual triggers with `workflow_dispatch`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch)